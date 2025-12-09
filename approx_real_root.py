def approx_real_root(coeffs, interval):
   a, b = interval
    
   def p(x):
      return (coeffs[0] +
              coeffs[1]*x +
              coeffs[2]*x*x +
              coeffs[3]*x*x*x)
    
   while abs(b - a) > 1e-9:
        m = (a + b) / 2
        if p(a) * p(m) <= 0:
            b = m
        else:
            a = m

   return (a + b) / 2