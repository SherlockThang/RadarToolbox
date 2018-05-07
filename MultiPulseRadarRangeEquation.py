import math
import RadarRangeEquation

class MultiPulseRadarRangeEquation(RadarRangeEquation.RadarRangeEquation):

  def __init__(self):
    super(MultiPulseRadarRangeEquation, self).__init__()
    self.addTerms(numPulses = (1, ''))

if __name__ == '__main__':
  mprre = MultiPulseRadarRangeEquation()
  mprre.main()
