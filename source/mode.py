#Write a program that is given an array of integers and determines the mode, which is the number that appears most frequently in the array

array_of_integers = [1,2,1,2,3,4,5,6,1]

def find_the_mode(array):
    largest_amount = -1
    mode_index = [0]
    histogram = create_histogram(array)
    
    for key, value in histogram.items():
        if value > largest_amount:
            mode_index.append(key)
            mode_index.pop(0)
            largest_amount = value
        elif value == largest_amount:
            mode_index.append(key)
            
    if largest_amount == 1:
        return -1                       
    return mode_index


def create_histogram(array):
    histogram = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
    
    for i in array:
        histogram[i] += 1
    
    return histogram

array1 = [1,1,1,2,2,4,5]
find_the_mode(array1)
print(array1,"mode is:",find_the_mode(array1))

integer_array3= [0,9,0,0,0,0,9,9,9,9]
find_the_mode(integer_array3)
print(integer_array3,"mode is:",find_the_mode(integer_array3))