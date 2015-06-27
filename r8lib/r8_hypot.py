#!/usr/bin/env python

def r8_hypot ( x, y );

#*****************************************************************************80
#
## R8_HYPOT returns the value of sqrt ( X^2 + Y^2 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    01 June 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real X, Y, the arguments.
#
#    Output, real VALUE, the value of sqrt ( X^2 + Y^2 ).
#
  from math import sqrt

  if ( abs ( x ) < abs ( y ) ):
    a = abs ( y )
    b = abs ( x )
  else:
    a = abs ( x )
    b = abs ( y )
#
#  A contains the larger value.
#
  if ( a == 0.0 ):
    value = 0.0
  else:
    value = a * sqrt ( 1.0 + ( b / a ) ** 2 )

  return
end
