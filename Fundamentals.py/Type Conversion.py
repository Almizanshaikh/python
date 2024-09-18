
int_number = 23
float_number = 1.23

newnumber = int_number + float_number

print("value",(newnumber))
print("Data type",type(newnumber))

# In the above example, we have created two variables: integer_number and float_number of int and float type respectively.

# Then we added these two variables and stored the result in new_number.

# As we can see new_number has value 24.23 and is of the float data type.

# It is because Python always converts smaller data types to larger data types to avoid the loss of data.

num_string = "23"
num_integer = 12

print("Data type",type(num_string)) #Data type of num_string before Type Casting

num_string = int(num_string)

print("Data type",type(num_string)) #Data type of num_string after Type Casting

new_sum = num_string + num_integer

print("sum",new_sum)
print("Data type of new sum",type(new_sum))