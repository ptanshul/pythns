def factors(n):
  for val in range(1, n+1):
      if n % val == 0:
          yield val
          yield val
print(next(factors(20)))