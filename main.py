import os

# read value from environment variable
# and print it out
secret = os.getenv('SECRET', 'default_secret')
print(secret)

variable = os.getenv('VARIABLE', 'default_variable')
print(variable)

not_set = os.getenv('NOT_SET', 'default_not_set')
print(not_set)
