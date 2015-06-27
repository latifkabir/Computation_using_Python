#! /usr/bin/env python
#
def rhs_lucas ( nu, rho, n, x, y, t ):

#*****************************************************************************80
#
## RHS_LUCAS returns right hand sides of the Spiral Flow equations.
#
#  Location:
#
#    http://people.sc.fsu.edu/~jburkardt/py_src/navier_stokes_2d_exact/rhs_lucas.py
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, real NU, the kinematic viscosity.
#
#    Input, real RHO, the density.
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), the coordinates of the points.
#
#    Input, real T(N), the time coordinate or coordinates.
#
#    Output, real F(N), G(N), H(N), the right hand sides in the U, V and P equations.
#
  import numpy as np

  f = np.zeros ( n )
  g = np.zeros ( n )
  h = np.zeros ( n )

  u = - np.cos ( np.pi * x ) / np.pi
  dudt = np.zeros ( n )
  dudx = np.sin ( np.pi * x )
  dudxx = np.pi * np.cos ( np.pi * x )
  dudy = np.zeros ( n )
  dudyy = np.zeros ( n )

  v = - y * np.sin ( np.pi * x )
  dvdt = np.zeros ( n )
  dvdx = - np.pi * y * np.cos ( np.pi * x )
  dvdxx = + np.pi * np.pi * y * np.sin ( np.pi * x )
  dvdy = - np.sin ( np.pi * x )
  dvdyy = np.zeros ( n )

  p = np.zeros ( n )
  dpdx = np.zeros ( n )
  dpdy = np.zeros ( n )

  f = dudt - nu * ( dudxx + dudyy ) + u * dudx + v * dudy + dpdx / rho
  g = dvdt - nu * ( dvdxx + dvdyy ) + u * dvdx + v * dvdy + dpdy / rho
  h = dudx + dvdy

  return f, g, h

def rhs_lucas_test ( ):

#*****************************************************************************80
#
## RHS_LUCAS_TEST samples the right hand sides at the initial time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    07 March 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  from r8vec_uniform_ab import r8vec_uniform_ab

  nu = 1.0
  rho = 1.0

  print ''
  print 'RHS_LUCAS_TEST'
  print '  Lucas Bystricky Flow'
  print '  Sample the Navier-Stokes right hand sides'
  print '  at the initial time T = 0, over the unit square.'
  print '  Kinematic viscosity NU = %g' % ( nu )
  print '  Fluid density RHO = %g' % ( rho )

  n = 1000
  r8_lo = 0.0
  r8_hi = 1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  y, seed = r8vec_uniform_ab ( n, r8_lo, r8_hi, seed )
  t = 0.0

  f, g, h = rhs_lucas ( nu, rho, n, x, y, t )

  print ''
  print '           Minimum       Maximum'
  print ''
  print '  Ur:  %14.6g  %14.6g' % ( np.min ( f ), np.max ( f ) )
  print '  Vr:  %14.6g  %14.6g' % ( np.min ( g ), np.max ( g ) )
  print '  Pr:  %14.6g  %14.6g' % ( np.min ( h ), np.max ( h ) )

  print ''
  print 'RHS_LUCAS_TEST:'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rhs_lucas_test ( )
  timestamp ( )

