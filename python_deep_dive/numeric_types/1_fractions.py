import fractions
import math


number = fractions.Fraction("22/7")
pi = fractions.Fraction(math.pi)
pi.limit_denominator(10)
