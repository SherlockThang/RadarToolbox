import math
import PowerEquation

class RangeResolution(PowerEquation.PowerEquation):

  def __init__(self):
    super(RangeResolution, self).__init__(
        (0.5 * PowerEquation.speedOfLight[0], PowerEquation.speedOfLight[1]),
        bandwidth = (1, 's^-1'),
        rangeResolution = (1, 'm'))

if __name__ == '__main__':
  rr = RangeResolution()
  rr.main()
