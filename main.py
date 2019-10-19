from math import gcd

num = 1

for i in range(50):
  seat = i + 1
  
  if (seat == 127) or (seat == 128):
    continue
  
  #if num % seat != 0:
  #  num *= seat
  num = int(num * seat/gcd(num, seat))
  print(num)
  
for i in range(50):
  seat = i + 1
  
  #if (seat2 == 127) || (seat2 == 128):
  #  continue
  print(str(seat) + ": " + str(num % seat))