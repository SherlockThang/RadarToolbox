import math
import PowerEquation

class DutyFactorCpiRadarRangeEquation(PowerEquation.PowerEquation):

  def __init__(self, useCpiTimes=True):
    super(DutyFactorCpiRadarRangeEquation, self).__init__(
        ((4.0 * math.pi) ** 3.0 * PowerEquation.boltzmannConstant[0], PowerEquation.boltzmannConstant[1]),
        transmitPower = (1, 'W'),
        transmitGain = (1, ''),
        receiveGain = (1, ''),
        crossSection = (1, 'm^2'),
        wavelength = (2, 'm'),
        snr = (-1, ''),
        rangeDist = (-4, 'm'),
        temperature = (-1, 'K'),
        loss = (-1, ''),
        noiseFigure = (-1, ''),
        cpiTime = (1, 's'),
        dutyFactor = (1, ''))
    if not useCpiTimes:
      self.removeTerms(['cpiTime'])
      self.addTerms(numPulses = (1, ''), pri = (1, 's'))

if __name__ == '__main__':
  rre = DutyFactorCpiRadarRangeEquation()
  rre.main()
