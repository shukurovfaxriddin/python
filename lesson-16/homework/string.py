# 1
import numpy as np  

my_list = [12.23, 13.32, 100, 36.32]

array_1d = np.array(my_list)

print("Original List:", my_list)
print("One-dimensional NumPy array:", array_1d)
# 2
import numpy as np 

matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)
# 3
null_vector = np.zeros(10)

null_vector[6] = 11

print(null_vector)
# 4
a=np.arange(12,38)
print(a)
# 5
import numpy as np

original_array = np.array([1, 2, 3, 4])

float_array = original_array.astype(float)

print("Float array:", float_array)
# 6
import numpy as np

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

fahrenheit = (celsius * 9/5) + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
# 7
import numpy as np

# Asl array
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Qo‘shiladigan qiymatlar
values_to_append = [40, 50, 60, 70, 80, 90]

# Append qilish
new_array = np.append(original_array, values_to_append)

# Natijani chop etish
print("After append values to the end of the array:", new_array)
# 8
import numpy as np

arr = np.random.rand(10)      
mean_val = np.mean(arr)         
median_val = np.median(arr)     
std_val = np.std(arr)            

print("Array:", arr)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)
# 9
arr = np.random.rand(100).reshape(10, 10)
max=arr.max()
min=arr.min()
print(f'max:{max}')
print(f'max:{max}')
# 10
arr = np.random.rand(3, 3, 3)

print(arr)
