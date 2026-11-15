#Speed, Distance & Time Calculator - www.101computing.net/python-challenge-speed-distance-time-calculator

print("Speed, Distance and Time Calculator")
print("------------------------------------")

def speed_calc(t, d):
           speed = float(d / t)
           return round(speed, 3)
           
def time_calc(s, d):
           time = float(d / s)
           return round(time, 3)

def distance_calc(t, s):    
           distance = float(t*s)
           return round(distance, 3)

print ("s - Speed, d - Distance, t - Time")

while True: 
 user_result = input("What would you like to calculate? - ")

 while user_result not in ["s", "t", "d"]:
  if (user_result != "s" and user_result != "t" and user_result != "d") :
   user_result = str(input("Incorrect input, choose between s, d, and t: "))
 
 if user_result == "s":
   t = float(input("Enter a time -"))
   t_unit = str(input("What unit is your time in -"))
   d = float(input("Enter a distance -"))
   d_unit = str(input("What unit is your distance in -"))
   print ("speed =", speed_calc(t , d), d_unit, "/", t_unit)

 if user_result == "t":
   s = float(input("Enter a speed -"))
   s_unit = str(input("What unit is your speed in -"))
   d = float(input("Enter a distance -"))
   d_unit = str(input("What unit is your distance in -"))
   print ("time =", time_calc(s , d), d_unit, "/", s_unit)
           
 if user_result == "d":
   t = float(input("Enter a time -"))
   t_unit = str(input("What unit is your time in -"))
   s = float(input("Enter a speed -"))
   s_unit = str(input("What unit is your speed in -"))
   print ("distance =", distance_calc(t, s), s_unit, t_unit)
 
 repeat = input("Would you like to calculate another value? (y/n): ")
 
 while repeat not in ["y", "n"]:
      repeat = input("Input was incorrect, would you still like to calculate another value?")

 if repeat == "n":
      print("Calculations complete.")
      break 
     

