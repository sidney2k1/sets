import array as arr
arraynum=arr.array("i",(1,3,5,7,9,5,3,3))
print("Original array:"+str(arraynum))
print("Number of occurences of 3 in the set:"+str(arraynum.count(3)))
arraynum.reverse()
print("The reverse of the list is:")
print(str(arraynum))