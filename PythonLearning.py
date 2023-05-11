
# pip install:
# python -m pip install PACKAGE_NAME

import numpy as np

# 
counter = 0
while counter < 10:
    print(counter)
    counter  = counter + 1
    if counter == 5:
        break

print(counter)

# for-loops
for i in range(6):
    print(i)

"hello"

list_x = [0,1,2,3]
list_x.append(4)

# Now the numpy presentations

# in R: array(rep(0,n), ...)
array_zeros = np.zeros(shape=(10,10))
print(array_zeros)

# dim() in R:
print(array_zeros.shape)

# Create an ID numpy array values 0 through 999
array_1d = np.arange(0,1000)

# Reshape our array to 100 rows x 10 columns:
array_2d = np.reshape(array_1d, (100,10))
print(array_2d)

# Multiply every value in our array by 2:
array_times_2 = array_2d * 2
array_times_2

# Inspect the first 5 elements of each of the first two rows
array_times_2[:5, :2] # first 5 rows and first two columns

# Remember: 0-indexed!

# Reassign value (row 0 and column 3)
array_times_2[0, 3] = 10000000

original = np.copy(array_times_2)

def change_zero_zero(x):
    """
    Changes the first entry in the array (0, 0) to 10000
    
    Parameters
    x : array_like
    
    Returns
    array
    """
    x[0, 0] = 10000
    return x

my_array = np.zeros((10, 10))
changed = change_zero_zero(my_array)


### Loading data

data = np.loadtxt("https://bit.ly/nds-python-pure")

print(data.shape)
# (506, 14)

print(data.dtype)
# float64

# mean of all our data
data.mean()
# 66.67816985036703

# mean over each row
data.mean(axis=0) # column: 1

# Slicing arrays: subsetting
# Calculate the SD
first_column = data[:, 0]
low = first_column.mean() - (first_column.std() * 2.5)
high = first_column.mean() + (first_column.std() * 2.5)
print(low, high)

# Create a mask for the outliers
mask = np.logical_or(first_column > high, first_column < low)
print(mask) # Output: boolean values if a value is an outlier


# Now get current directory:
import os
os.getcwd() # current directory

os.chdir("C:/Users/Roman/Desktop/BrainhackSchool/git/PublicTest")

# Check if directory has been changed
os.getcwd()

modified_data = data * 2
np.savetxt('modified_data.txt', modified_data)

# Now we upload our changes to github.


