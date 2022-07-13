"""
    Created by Valery Grey
    EX 1 Home work 1
    Version : 1.0
"""

lst = {3, 7, 2}
histo= ["*"*item for item in lst];



"""
    EX 2 Home work 1
"""

# Create variables
lst1 = ["a","b","c"]
lst2 = ["x",'y',"z"]
resultLst = []
# Variable for index of second array ,
# to fulfill the condition, must
# start from the end in the second array

#loop for feel result array with necessary chars
for i in range(len(lst1)):
    resultLst.append(lst1[i]+lst2[-1-i])

#print the result
print(resultLst)

