import numpy
import matplotlib.pyplot as plt

def setPlotDefaults():
  plt.rc('lines',\
      linewidth=3, \
      markersize=6, \
      color='b')

  plt.rc('font', size=12, weight='bold')

  plt.rc('legend', numpoints=1, loc='best', markerscale=1.5, fontsize=10)
  plt.rc('axes', labelsize=14, labelweight='heavy', linewidth=2, titlesize=16, facecolor=[0.5, 0.5, 0.5])
  plt.rc('axes', color_cycle=([0.8, 0., 0.], [0., 0.8, 0.], [0., 0., 0.8], [0., 0.7, 0.7], [0.7, 0.7, 0.], [0.7, 0., 0.7]))
  plt.rc('xtick', labelsize=13)
  plt.rc('ytick', labelsize=13)
  plt.rc('figure', facecolor='w', figsize=[8, 6])

def resetPlotDefaults():
  plt.rcdefaults()

def _colorGenerator():
  isc = 0
  colors=([0.8, 0., 0.], [0., 0.8, 0.], [0., 0., 0.8], [0., 0.7, 0.7], [0.7, 0.7, 0.], [0.7, 0., 0.7])
  while True:
    ic = isc % len(colors)
    yield colors[ic]
    isc += 1

def _symbolGenerator():
  isc = 0
  symbols = 'os^dv'
  while True:
    isym = isc / len(symbols)
    yield symbols[isym]
    isc += 1

_symbolGenerator = _symbolGenerator()
_colorGenerator = _colorGenerator()
def nextSymbol():
  global _symbolGenerator
  return _symbolGenerator.next()
def nextColor():
  global _colorGenerator
  return _colorGenerator.next()
