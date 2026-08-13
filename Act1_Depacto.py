import math
def main ():
  x1 = float(input("Enter x1: "))
  y1 = float(input("Enter y1: "))
  x2 = float(input("Enter x2: "))
  y2 = float(input("Enter y2: "))
  distance (x1, y1, x2, y2)
def distance (x1, y1, x2, y2):
  distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

  print("The distance between the two points is:", round(distance, 2))

main ()
          
# Reflection:
# Using a math library makes the program easier because I can use
# sqrt() and pow() instead of writing those calculations from scratch.
# Without the library, calculating the square root and powers would
# make the program longer and more difficult to understand.
