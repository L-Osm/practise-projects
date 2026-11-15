
print("----------------------")
print("Number Logger:")

# Function to check if the value entered is a number.
def validity_checknum(prompt, data_type=float):
  while True:
    try:
      return data_type(input(prompt))
    except ValueError:
         print("Incorrect input type, enter a number.")

# Initialising the final list displayed at the end of the program 
# (done here so the function below can recognise the variable)  
numlist = []

# Procedure to make numbers be repeatedly entered / or for exiting the program.
def repeat(numlist):
  repeat_val = validity_repeat()
  while repeat_val == "y":
    numlist.append(validity_checknum("Enter the next number you wish to record: ", float))
    repeat_val = validity_repeat()

# Function to find the median of the numbers entered. (I swear this took way too long)
def median(numlist):
  if not numlist:
   raise ValueError("Cannot find the median of an empty list.")
  
  listtemp = sorted(numlist)
  length = len(numlist)
  if length % 2 == 0:
    median_index1 = length // 2
    first_med = listtemp[median_index1 - 1]
    second_med = listtemp[median_index1]
    midpoint = (second_med - first_med) / 2
    return first_med + midpoint
  else: 
   median_index = length // 2
   return listtemp[median_index]


# Function to output list statistics when program is finished.
def exit_program(numlist):
  sorted_version = sorted(numlist)
  highest_num = max(numlist)
  lowest_num = min(numlist)
  avg = sum(numlist) / len(numlist)
  median_val = median(numlist)
  num_range = highest_num - lowest_num
  print("A list of numbers recorded: ", numlist)
  print("Sorted version:", sorted_version)
  print("Largest number: ", highest_num)
  print("Smallest number: ", lowest_num)
  print("Median of numbers:", median_val)
  print("Mean of numbers:", avg)
  print("Range of numbers:", num_range)
  print("Logging complete, exiting program.")

# Function to handle incorrect inputs by the user for the repeat variable.
def validity_repeat():
  while True:
    try:
      repeat = input("Would you like to enter another number? (y/n): ").strip().lower()
      if repeat == "y" or repeat == "n":
        return repeat
      else:
        raise ValueError("input must be either y or n.")
    except ValueError:
      print("Incorrect value entered, please enter either y or n.")

# The actual program.
input_num = validity_checknum("Enter the number you wish to record: ", float)
numlist.append(input_num)
repeat(numlist)
exit_program(numlist)

print("----------------------")
print("----------------------")
# The bars before and after the entire program don't actually do anything they just make everything look nice.