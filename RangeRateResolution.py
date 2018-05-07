import math
import PowerEquation

class RangeRateResolution(PowerEquation.PowerEquation):

  def __init__(self):
    super(RangeRateResolution, self).__init__(
        (0.5 , ''),
        wavelength = (-1, 'm'),
        rangeRateResolution = (1, 'm/s'),
        cpiTime = (1, 's'))

if __name__ == '__main__':
  rr = RangeRateResolution()
  rr.main()
