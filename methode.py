import numpy as np

array = [1,2,3,4,3,1,2]

def meine_methode(array):
    length = len(array)
    if length == 0:
        return "array empty!"
    if length % 2 == 0:
        return "array length even!"

    i=0
    while i < length:
        element = array[i]
        counter = 0
        j=i
        while j < length:
            if element == array[j]:
                counter+=1
            j+=1
        if counter == 1:
            return element
        i+=1

print(meine_methode(array))
print(type(array) == list)