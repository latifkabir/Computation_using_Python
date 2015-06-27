#!/usr/bin/env python

def r8_log_10 ( x ):

#*****************************************************************************80
#
## R8_LOG_10 returns the logarithm base 10 of |X|.
#
#  Discussion:
#
#    value = Log10 ( |X| )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    07 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, the number whose base 2 logarithm is desired.
#    X should not be 0.
#
#    Output, real VALUE, the logarithm base 10 of the absolute
#    value of X.  It should be true that |X| = 10**R8_LOG_10.
#
  from math import log

  value = log ( abs ( x ), 10.0 )

  return value

