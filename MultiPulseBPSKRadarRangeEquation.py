import math
import MultiPulseRadarRangeEquation

class MultiPulseBPSKRadarRangeEquation(MultiPulseRadarRangeEquation.MultiPulseRadarRangeEquation):

  def __init__(self):
    super(MultiPulseBPSKRadarRangeEquation, self).__init__()
    self.addTerms(numChips = (1, ''))

if __name__ == '__main__':
  mprre = MultiPulseBPSKRadarRangeEquation()
  mprre.main()
