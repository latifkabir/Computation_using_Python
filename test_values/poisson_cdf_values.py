#!/usr/bin/env python
#
def poisson_cdf_values ( n_data ):

#*****************************************************************************80
#
## POISSON_CDF_VALUES returns some values of the Poisson CDF.
#
#  Discussion:
#
#    CDF(X)(A) is the probability of at most X successes in unit time,
#    given that the expected mean number of successes is A.
#
#    In Mathematica, the function can be evaluated by:
#
#      Needs["Statistics`DiscreteDistributions`]
#      dist = PoissonDistribution [ a ]
#      CDF [ dist, x ]
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
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
#    Stephen Wolfram,
#    The Mathematica Book,
#    Fourth Edition,
#    Wolfram Media / Cambridge University Press, 1999.
#
#    Daniel Zwillinger,
#    CRC Standard Mathematical Tables and Formulae,
#    30th Edition, CRC Press, 1996, pages 653-658.
#
#  Parameters:
#
#    Input/output, integer N_DATA.  The user sets N_DATA to 0 before the
#    first call.  On each call, the routine increments N_DATA by 1, and
#    returns the corresponding data; when there is no more data, the
#    output value of N_DATA will be 0 again.
#
#    Output, real A, the parameter of the function.
#
#    Output, integer X, the argument of the function.
#
#    Output, real F, the value of the function.
#
  import numpy as np

  n_max = 21

  a_vec = np.array ( ( \
     0.02E+00, \
     0.10E+00, \
     0.10E+00, \
     0.50E+00, \
     0.50E+00, \
     0.50E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     1.00E+00, \
     2.00E+00, \
     2.00E+00, \
     2.00E+00, \
     2.00E+00, \
     5.00E+00, \
     5.00E+00, \
     5.00E+00, \
     5.00E+00, \
     5.00E+00, \
     5.00E+00, \
     5.00E+00 ))

  f_vec = np.array ( ( \
     0.9801986733067553E+00, \
     0.9048374180359596E+00, \
     0.9953211598395555E+00, \
     0.6065306597126334E+00, \
     0.9097959895689501E+00, \
     0.9856123220330293E+00, \
     0.3678794411714423E+00, \
     0.7357588823428846E+00, \
     0.9196986029286058E+00, \
     0.9810118431238462E+00, \
     0.1353352832366127E+00, \
     0.4060058497098381E+00, \
     0.6766764161830635E+00, \
     0.8571234604985470E+00, \
     0.6737946999085467E-02, \
     0.4042768199451280E-01, \
     0.1246520194830811E+00, \
     0.2650259152973617E+00, \
     0.4404932850652124E+00, \
     0.6159606548330631E+00, \
     0.7621834629729387E+00 ))

  x_vec = np.array ( ( \
     0, 0, 1, 0, \
     1, 2, 0, 1, \
     2, 3, 0, 1, \
     2, 3, 0, 1, \
     2, 3, 4, 5, \
     6 ))

  if ( n_data < 0 ):
    n_data = 0

  if ( n_max <= n_data ):
    n_data = 0
    a = 0.0
    x = 0.0
    f = 0.0
  else:
    a = a_vec[n_data]
    x = x_vec[n_data]
    f = f_vec[n_data]
    n_data = n_data + 1

  return n_data, a, x, f

def poisson_cdf_values_test ( ):

#*****************************************************************************80
#
## POISSON_CDF_VALUES_TEST demonstrates the use of POISSON_CDF_VALUES.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  print ''
  print 'POISSON_CDF_VALUES_TEST:'
  print '  POISSON_CDF_VALUES stores values of the Gegenbauer polynomials.'
  print ''
  print '      A         X            FX'
  print ''

  n_data = 0

  while ( True ):

    n_data, a, x, fx = poisson_cdf_values ( n_data )

    if ( n_data == 0 ):
      break

    print '  %12f  %12f  %24.16g' % ( a, x, fx )

  print ''
  print 'POISSON_CDF_VALUES_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poisson_cdf_values_test ( )
  timestamp ( )

