rate_of_return = 0.075

def display_as_percentage(val):
  return 'My rate of reutrn is:{:>10.1f}%'.format(val * 100)

print(display_as_percentage(rate_of_return))