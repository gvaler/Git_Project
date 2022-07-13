
"""
    Created by Valery Grey
    EX 1 Home work 2
    Version : 1.0
"""

# -----------Part A-----------
#Create variables and get string from user
s = input("Enter your string : ")
dict = {}

#Main logic
#take all chars and cheking if char in dictionary
#yes - add 1 to value
#no - add key with value 1
for ch in s:
    if ch not in dict.keys():
        dict[ch]=1
    else:
        dict[ch]+=1
#print the result
for k , v in dict.items():
    print(k," - ",v)

# -----------Part B-----------
reverseDict = {}
for k , v in dict.items():

    if v not in reverseDict:
        reverseDict[v]=[k]
    else:
        reverseDict[v].append(k)

print(reverseDict)






"""
    EX 2 Home work 2
"""
import collections

# function for checking common values
def checkRepeatDigits(lst):
    """
    Check if list have repeat values
    :param lst: list
    :return: True/False
    """
    count_repeat_digit = collections.Counter(lst)
    for k,v in count_repeat_digit.items():
        if v > 1 :
            return True
    return False

# function for returning common values with "and"
def repeated_values(lst):
    """
    Return repeated values from list
    :param lst: list
    :return: repeated values
    """
    dict = collections.Counter(lst)
    result = " "
    for k,v in dict.items():
        if v > 1:
            result+=str(k) +" and "
    return result


# main logic function
def mainFunction (d):
    """
    Search only those lists that have at least one repeating organ
    Find common values (found in all) from all the lists you found
    in section a. If one list remains - all its organs are common,
    if no list remains - the answer will be empty
    :param d: dictionary
    :return: print the results
    """
    #create variables
    dict  = collections.Counter(d) # create dictionary
    array ,true_arr= [] ,[]# create array for adding to it values
    str_result = "" # create string for print result
    true_counter = 0 # count arrays with common values

    # main loop
    for k,v in dict.items():
        # if value is repeat in array print appropriate message, and +1 to true counter
        if(checkRepeatDigits(v)==True):
            print(f"{k} includes the values",repeated_values(v)[:-5],"more then once")
            true_counter+=1
        else:
            array.append(v) # add values to array
            str_result+= k +" and " # creating string for printing results

    # checking main conditions (Part B)
    if (true_counter==len(dict)): # all arrays have common values the answer is "empty answer"
        print(" ")
    if(true_counter==2):
        # this case for case if have one list without common values
        # according to the requirements this values must be output
        # trim "[]"
        print(f"list {str_result[:-5]} doesn't have common values ",str(array)[2:-2])

    if (len(dict)-true_counter>1): # several arrays doesnt have common digits

        res = str(set.intersection(*map(set,array)))
        if res == 'set()':
            print(" ")
        else:
            print(f"the common values (of {str_result[:-5]}) are : ",res)

lst1 = [11,7,5,8,95,37,15,19]
lst2 = [22,10,1,11]
lst3 = [71,3,8,2,14,1]
dict = {"lst1":lst1,"lst2":lst2,"lst3":lst3}
mainFunction(dict)







"""
    EX 3 Home work 2
"""
import collections

def sortDigitsByAction(lst,action):
    """
    The function sorts list by user action
    :param lst: list of numbers
    :param action: action for execution
    :return: sorted lst desc/asc by action
    """
    new_list, res, temp = [],[],0        # create variables

    # dividing numbers to digits
    for v in lst:
        while (v > 0):
            new_list.append(v % 10)
            v = int(v / 10)

    d = collections.Counter(new_list)     # create dictionary from array with digits
    new_list.clear()                      # clean the list for continue

    # add all digits to array without duplicates
    for k, v in d.items():
        new_list.append(int(k))

    # sort by asc\desc have 2 cases only
    # action can be asc or desc
    if action=="asc":
        return sorted(new_list,reverse=False)
    else:
        return sorted(new_list,reverse=True)


# create variables
lst = [31, 99, 3, 1943]
action = ""
# ask for option until it is correct
if action!="asc" or action!="desc":
    while True:
        action = input("Enter your action (desc/asc) : ")
        if action == "asc" or "desc":
            break
# call to main function with main logic
print(sortDigitsByAction(lst,action))





