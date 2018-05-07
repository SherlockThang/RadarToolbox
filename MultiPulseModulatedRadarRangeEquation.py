import math
import MultiPulseRadarRangeEquation

class MultiPulseModulatedRadarRangeEquation(MultiPulseRadarRangeEquation.MultiPulseRadarRangeEquation):

  def __init__(self):
    super(MultiPulseModulatedRadarRangeEquation, self).__init__()
    self.addTerms(cpiLength = (1, 's'), processingBandwidth = (1, 's'))

if __name__ == '__main__':
  mprre = MultiPulseModulatedRadarRangeEquation()
  mprre.main()
