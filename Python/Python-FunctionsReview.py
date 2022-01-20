# Write your code below:
def trip_planner_welcome(name):
  print('Welcome to tripplanner v1.0' + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print('Your trip starts off in ' + origin)
  print('And you are traveling to ' + destination)
  print('You will be traveling by' + mode_of_transport)
  print('It will take approximately ' + str(estimated_time) + ' hours')

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

rounded_time = estimated_time_rounded(13.3)

destination_setup('Italy', 'Israel', rounded_time, )

 
trip_planner_welcome(" <YOUR NAME HERE> ")
estimate = estimated_time_rounded(2.43)
destination_setup(" <PICK AN ORIGIN> ", "<PICK A DESTINATION > ", estimate, "Car")