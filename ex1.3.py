def fib_memo(n,cache={}):
  #1
  if n == 0 or n == 1:
    return n
  
  elif n in cache:
    return cache[n]
  
  else:
    fibonacci_compute = fib_memo(n-1) + fib_memo(n-2)
    cache.update({n:fibonacci_compute})
    return fibonacci_compute
