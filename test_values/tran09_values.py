#!/usr/bin/env python
#
def tran09_values ( n_data ):

#*****************************************************************************80
#
## TRAN09_VALUES returns some values of the order 9 transportation function.
#
#  Discussion:
#
#    The function is defined by:
#
#      TRAN09(x) = Integral ( 0 <= t <= x ) t^9 exp(t) / ( exp(t) - 1 )^2 dt
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Milton Abramowitz and Irene Stegun,
#    Handbook of Mathematical Functions,
#    US Department of Commerce, 1964.
#
#    Allan McLeod,
#    Algorithm 757, MISCFUN: A software package to compute uncommon
#    special functions,
#    ACM Transactions on Mathematical Software,
#    Volume 22, Number 3, September 1996, pages 288-301.
#
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 20

  f_vec = np.array ( ( \
     0.26469772870084897671E-22, \
     0.11367943653594246210E-12, \
     0.74428246255329800255E-08, \
     0.48022728485415366194E-03, \
     0.11700243014358676725E+00, \
     0.27648973910899914391E+01, \
     0.24716631405829192997E+02, \
     0.12827119828849828583E+03, \
     0.46842894800662208986E+03, \
     0.31673967371627895718E+04, \
     0.46140886546630195390E+04, \
     0.11952718545392302185E+05, \
     0.20001612666477027728E+05, \
     0.31011073271851366554E+05, \
     0.10352949905541130133E+06, \
     0.19743173017140591390E+06, \
     0.33826030414658460679E+06, \
     0.36179607036750755227E+06, \
     0.36360622124777561525E+06, \
     0.36360880558827162725E+06 ))

  x_vec = np.array ( ( \
       0.0019531250E+00, \
       0.0312500000E+00, \
       0.1250000000E+00, \
       0.5000000000E+00, \
       1.0000000000E+00, \
       1.5000000000E+00, \
       2.0000000000E+00, \
       2.5000000000E+00, \
       3.0000000000E+00, \
       4.0000000000E+00, \
       4.2500000000E+00, \
       5.0000000000E+00, \
       5.5000000000E+00, \
       6.0000000000E+00, \
       8.0000000000E+00, \
      10.0000000000E+00, \
      15.0000000000E+00, \
      20.0000000000E+00, \
      30.0000000000E+00, \
      50.0000000000E+00 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    x = 0.0
    f = 0.0
  else:
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, x, f

def tran09_values_test ( ):

#*****************************************************************************80
#
## TRAN09_VALUES_TEST demonstrates the use of TRAN09_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'TRAN09_VALUES_TEST:'
  print '  TRAN09_VALUES stores values of the TRAN09 function.'
  print ''
  print '      X         TRAN09(X)'
  print ''

  n_data = 0

  while ( True ):

    n_data, x, f = tran09_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12g  %24.16g' % ( x, f )

  print ''
  print 'TRAN09_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  tran09_values_test ( )
  timestamp ( )

