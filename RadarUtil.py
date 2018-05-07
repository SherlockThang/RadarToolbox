import math
import numpy

speedOfLight = (2.9979246E8, 'm * s^-1')
boltzmannConstant = (1.38064852E-23, 'm^2 * kg * s^-2 K^-1')

def feetToMeters(x):
  return x * 0.3048

def wavelengthToFrequency(wavelength):
  return speedOfLight[0] / wavelength

def frequencyToWavelength(freq):
  return speedOfLight[0] / freq

def toLinear(dB):
  return 10.0 ** (dB / 10.0)

def todB(linear):
  return 10.0 * numpy.log10(linear)

def wrapToInterval(val, interval):
  extent = interval[-1] - interval[0]
  vPrime = val - interval[0]
  numWraps = math.floor(vPrime / extent)
  wrapped = val - numWraps * extent
  return wrapped


