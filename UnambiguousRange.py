import math
import PowerEquation

class UnambiguousRange(PowerEquation.PowerEquation):

  def __init__(self):
    super(UnambiguousRange, self).__init__(
        (0.5 * PowerEquation.speedOfLight[0], PowerEquation.speedOfLight[1]),
        prf = (1, 's^-1'),
        unambiguousRange = (1, 'm'))

if __name__ == '__main__':
  ur = UnambiguousRange()
  ur.main()
