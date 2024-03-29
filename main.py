from datetime import datetime
import time


# Part 1
def clock(n:int)->str:
  """
  show the time and update it once every second, for n number of seconds

  Parameters
  -----------
  n: int
    update clock once every second, for n number of seconds

  Returns
  ---------
  str
    clock updated once every second, for n number of seconds
  """
  timer = 0
  while timer < n:
    current_t = datetime.now()
    reformatted_t = current_t.strftime('%H:%M:%S')
    print(reformatted_t, end='\r')
    time.sleep(1)
    timer += 1

# clock(3)

# Part 2
def lcm(a, b):
  """
  calculating the lowest common multiple of integers a and b

  Paremeters
  ----------
  a, b: int
    used to calculate lcm

  Returns
  --------
  lcm: int
    lowest common multiple of integers a and b
  """
  a_original = a
  b_original = b
  while a != b:
    if a < b:
      a += a_original
    elif b < a:
      b += b_original
  if a == b:
    return a
# lcm(2,3)

# Part 3
def gcf(a, b):
  """
  calculating the greatest common factor GCD of integers a and b

  Paremeters
  ----------
  a, b: int
    used to calculate GCD

  Returns
  --------
  lcm: int
    greatest common factor GCD of integers a and b
  """
  while b != 0:
    r = a%b
    a = b
    b = r
  if b == 0:
    return a
    
# gcf(60,48)