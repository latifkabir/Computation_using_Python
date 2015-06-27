#!/usr/bin/env python

def r8_pythag ( a, b ):

#*****************************************************************************80
#
## R8_PYTHAG computes sqrt ( A^2 + B^2 ), avoiding overflow and underflow.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    25 July 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    The SLATEC library
#
#  Parameters:
#
#    Input, real A, B, the values for which sqrt ( A**2 + B**2 )
#    is desired.
#
#    Output, real VALUE, the value of sqrt ( A**2 + B**2 ).
#
  from math import sqrt

  a = abs ( a )
  b = abs ( b )

  if ( b < a )
    value = a * sqrt ( 1.0 + ( b / a ) * ( b / a ) )
  elif ( b == 0.0 )
    value = 0.0
  elif ( a <= b )
    value = b * sqrt ( 1.0 + ( a / b ) * ( a / b ) )

  return value

