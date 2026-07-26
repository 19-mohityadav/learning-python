import numpy as np

# TO check the installed numpy version
# print(np.__version__)

# Python List
my_list = [1, 2, 3, 4, 5]
my_list = my_list*2
print(my_list)   # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# NumPy Array
array = np.array([1,3,5])

array = array * 2
print(array)    #[ 2  6 10]
print(type(array))  # <class 'numpy.ndarray'> (n dimensional array)


# N dim (0 -> dot, 1 -> line, 2 -> square, 3 -> cube

array2 = np.array([1,3,5])

print(array2)   # [1 3 5]
print(array2.ndim)   # 1



array3 = np.array("Hello World")

print(array3)  # Hello World
print(array3.ndim)  # 0 -> no of dimension

array4 = np.array('A')
print(array4)    # A
print(array4.ndim) # 0


# Rows and column 2D
array5 = np.array([['A','B','C'],
                   ['D','E','F'],
                   ['G','H','I']]
                  )

# print(array5)
print(array5.ndim)  # 2

# (depth,each rows,each column) 3D
array6 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                   [['J','K','L'],['M','N','O'],['P','Q','R']],
                   [['S','T','U'],['V','W','X'],['Y','Z', '_']]]   #
                  )
# print(array6)
print(array6.ndim)  # 3
print(array6.shape)  # (3, 3, 3)
# Accessing the elements (Chain indexing)
print(array6[0][0][0])  # A

# multidimensional indexing
# (Faster than chain indexing -> because 1 internal .py fn call, no temp array obj in mem, D math)
print(array6[0,0,1])
print(array6[0,0,2])
print(array6[0,1,1]) # E row 1 & col 1 element

# Form your name using string concatenation

word = array6[1,1,0] + array6[1,1,2] + array6[0,2,1] + array6[0,2,2] + array6[2,0,1]
print(word) # MOHIT











