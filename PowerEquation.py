import RadarUtil

import math
import optparse
import os

speedOfLight = RadarUtil.speedOfLight
boltzmannConstant = RadarUtil.boltzmannConstant

class PowerEquation(object):

  def __init__(self, lhs, **kwargs):
    """ Setup the equation as lhs = product of terms to powers """
    self.lhsVal = lhs[0]
    self.lhsUnits = lhs[1]
    self.eqn = {}
    self.units = {}
    self.hasNegativeExponent = False
    self.hasPositiveExponent = False
    for base, baseDetails in kwargs.items():
      if baseDetails.__class__.__name__ == 'tuple':
        exponent = float(baseDetails[0])
        units = baseDetails[1]
      else:
        exponent = float(baseDetails)
        units = ''
      self.eqn[base] = exponent
      self.units[base] = units
      if exponent < 0:
        self.hasNegativeExponent = True
      else:
        self.hasPositiveExponent = True

    #print(str(self))

  def addTerms(self, **kwargs):
    for base, baseDetails in kwargs.items():
      exponent = float(baseDetails[0])
      units = baseDetails[1]
      self.eqn[base] = exponent
      self.units[base] = units
      if exponent < 0:
        self.hasNegativeExponent = True
      else:
        self.hasPositiveExponent = True

  def removeTerms(self, keys):
    for key in keys:
      self.eqn.pop(key)
      self.units.pop(key)
    self.hasNegativeExponent = False
    self.hasPositiveExponent = False
    for exp in self.eqn.values():
      if exp < 0:
        self.hasNegativeExponent = True
      else:
        self.hasPositiveExponent = True

  def solve(self, dB, allowNonUnitNumberOfUnknowns, **kwargs):
    """ Solve for the unknown terms of the equation """
    #print kwargs
    unknowns = self.eqn.keys()
    rhs = 1.0
    for term, termVal in kwargs.items():
      # Figure out what term the user wants. This will give a ValueError
      # if the term is not in the equation
      try:
        unknowns.remove(term)
      except ValueError:
        print('Unknown term in equation:', term)
        print(self)
        return None
      if dB:
        rhs += self.eqn[term] * termVal
      else:
        rhs *= termVal ** self.eqn[term]

    if dB:
      lhs = 10.0 * math.log10(self.lhsVal)
    else:
      lhs = self.lhsVal
    units = ''
    if len(unknowns) == 1:
      unknown = unknowns[0]
      solnVars = unknown
      if dB:
        solution = (lhs - rhs) / self.eqn[unknown]
        solnUnits = 'dB ' + self.units[unknown]
      else:
        solnUnits = self.units[unknown]
        solution = (lhs / rhs) ** (1.0/self.eqn[unknown])
    elif allowNonUnitNumberOfUnknowns:
      if len(unknowns) == 0:
        solnVars = 'overdetermined equation'
        solution = (lhs == rhs)
        solnUnits = None
      else:
        print('WARNING: Multiple variables are being solved:' + str(unknowns))
        solnUnits = 'dB (' if dB else ''
        solnVars = ''
        for iu, unk in enumerate(unknowns):
          u = self.units[unk]
          e = self.eqn[unk]
          solnUnits += (u + '^' + str(e)) if u != '' else ''
          if dB:
            solnVars += str(e) + '*' + unk
          else:
            solnVars += unk + '^' + str(self.eqn[unk])
          if iu != len(unknowns)-1:
            if dB:
              solnVars += ' + '
            else:
              solnVars += ' * '
              if u != '':
                solnUnits += ' * '
        solnUnits = solnUnits.rstrip(' *+')
        if dB:
          solnUnits += ')'
          solution = (lhs - rhs)
        else:
          solution = (lhs / rhs)
    else:
      raise UserWarning, ' '.join(('Invalid number of unknowns when allowNonUnitNumberOfUnknowns is set to False', str(unknowns)))

    return solution, solnVars, solnUnits

  def interactiveSolve(self, dB):
    print('Insert a value for each term, blank to solve for that term.')
    myTerms= {}
    for base in self.eqn.keys():
      prompt = base + ' ('
      if dB:
        prompt += 'dB' + self.units[base]
      else:
        prompt += '' + self.units[base]
      prompt += '): '
      term = raw_input(prompt)
      try:
        valTerm = float(term)
      except:
        print('I will try to solve for ' + base)
      else:
        myTerms[base] = valTerm

    return self.solve(dB, True, **myTerms)

  def __str__(self):
    """ Get the good representation of the equation """
    s = ''
    lhsLen = len(str(self.lhsVal) + ' = ')
    # Write the exponents
    s += lhsLen * ' '
    if self.hasPositiveExponent:
      for base, exp in self.eqn.items():
        if exp >= 0:
          s += len(base)*' ' + str(exp) + ' '
    s += os.linesep
    # Write the left hand side, but only if no denominator
    if not self.hasNegativeExponent:
      s += str(self.lhsVal) + ' = '
    else:
      s += len(str(self.lhsVal) + ' = ') * ' '
    # Write the bases of numerator terms
    startNum = len(s)
    if self.hasPositiveExponent:
      for base, exp in self.eqn.items():
        if exp >= 0:
          s += base + (len(str(exp)) + 1) * ' '
    else:
      s += 5 * ' ' + str(1) + 5 * ' '
    numLength = len(s) - startNum
    s += os.linesep
    # Now write the denominator
    if self.hasNegativeExponent:
      # Write the left hand side and the division bar
      s += str(self.lhsVal) + ' = '
      s += numLength * '-' + os.linesep
      s += lhsLen * ' '
      # Exponents in the denominator
      for base, exp in self.eqn.items():
        if exp < 0:
          s += len(base)*' ' + str(-exp) + ' '
      s += os.linesep
      # Bases in the denominator
      s += lhsLen * ' '
      for base, exp in self.eqn.items():
        if exp < 0:
          s += base + (len(str(-exp)) + 1) * ' '
    s += os.linesep
    return s

  def main(self):
    optParser = optparse.OptionParser(
        description='Solve for ' + self.__class__.__name__ + ' terms. Unspecified terms will be solved for.')
    optParser.add_option('-i', '--interactive', action='store_true', dest='interactive',
        help='Get prompted for input values. If specified, other command line inputs are ignored.')
    optParser.add_option('--dB', action='store_true', dest='dB',
        help='Specifies whether inputs and outputs should be in dB')
    for base in self.eqn.keys():
      optParser.add_option('--'+base, type='float', dest=base, help='Specify the value for ' + base, default=None)
    (opts, args) = optParser.parse_args()
    if opts.interactive:
      print('Interactively solve for terms:')
      print(str(self))
      (val, var, units) = self.interactiveSolve(opts.dB)
      print('The solution to the ' + self.__class__.__name__ + ' is:')
    else:
      kwargs = {}
      optVars = vars(opts)
      print('The solution to the ' + self.__class__.__name__ + ' is:')
      for optField, optValue in optVars.items():
        if optField in self.eqn.keys():
          if optValue is not None:
            print(''.join(('   For user specified ', optField, ': ', str(optValue))))
            kwargs[optField] = optValue
      (val, var, units) = self.solve(opts.dB, True, **kwargs)
    print('   ' + var + ' = ' + str(val) + ' ' + units)
