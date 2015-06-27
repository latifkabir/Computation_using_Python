#!/usr/bin/env python

def f2 ( i ) :

#*****************************************************************************80
#
## F2 is the iteration function for example 2.
#
#  Discussion:
#
#    This function has a cycle
#
#    3, 67, 35, 51, 43, 11, 27, 19, 59, of length 9
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    13 May 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer I, the argument of the function.
#
#    Output, integer VALUE, the value of the function.
#
  value = ( ( 22 * i + 1 ) % 72 )

  return value

