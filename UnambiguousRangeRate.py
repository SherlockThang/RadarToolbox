import math
import PowerEquation

class UnambiguousRangeRate(PowerEquation.PowerEquation):

  def __init__(self):
    super(UnambiguousRangeRate, self).__init__(
        (0.25, ''),
        prf = (-1, 's^-1'),
        unambiguousRangeRate = (1, 'm * s^-1'),
        wavelength = (-1, 'm'))

if __name__ == '__main__':
  ur = UnambiguousRangeRate()
  ur.main()
