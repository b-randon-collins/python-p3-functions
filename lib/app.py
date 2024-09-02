def my_function(param):
    print("Running my_function")
    return param + 1


my_function_return_value = my_function(1)
# => Running my_function
# => 2
print(my_function_return_value)
# => 2

def  sayHi(name = "Engineer"):
  print(f'Hi there, {name}!')


sayHi()