def fibonacci(n):
  fibs  = [0, 1]
  if n < 0:
    ValueError("Input must be 0 or greater!")
  if n <= len(fibs)-1 :
    return fibs[n]
  else:
    while n > len(fibs)-1:
      next_fibs = fibs[-1] + fibs[-2]
      fibs.append(next_fibs)
    return fibs[n]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)