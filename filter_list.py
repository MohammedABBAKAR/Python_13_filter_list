# Filter Strings from Array
# Create a function that takes a list of strings and integers,
# and filters out the list so that it returns a list of integers only.
# Examples

# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

# filter_list(["Nothing", "here"]) ➞ []


# def filter_list(l):
#     listin =[]
#     for i in l:
#         if i == int:
#            listin.append(i)
#         return   listin
# print(filter_list([1, 2, 3, "a", "b", 4]))

# This will correctly filter out non-integer values from the list. 
# The isinstance(i, int) check 
# ensures that only integers are appended to listin.


def filter_list(l):
    listin = []
    for i in l:
        if isinstance(i, int):
            listin.append(i)
    return listin

print(filter_list([1, 2, 3, "a", "b", 4]))

# The isinstance(x, int) function checks if x is an integer.

def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

# Test cases
print(filter_list([1, 2, 3, "a", "b", 4]))