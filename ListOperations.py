import random
import time
import matplotlib.pyplot as plt  # You must install a package called matplotlib
# To install matplotlib package goto menue file->settings->project->project interpreter -> + sing on the right -> search matplotlib and install

# These algorithms are explained in Chapter 9 of http://itlectures.ro/wp-content/uploads/2016/04/AdamDrozdek__DataStructures_and_Algorithms_in_C_4Ed.pdf
# Sorting algorithm implementations
# MAKE SURE YOU DO NOT MODIFY THE input_list in any of the functions
def bubble_sort(input_list):
    sorted_list = input_list[:]
    # copying the list, fastest way to copy is slicing
    # <implement the algo to sort the input list>
    for i in range(len(input_list)):  #outer loop to do the same thing repeatedly
        for i in range (len(input_list)-1,0,-1):   #inner loop to iterate the biggest element at the end
            for j in range(i):
                if sorted_list[j] > sorted_list [j+1]:
                    temp = sorted_list [j] # temp is being used as third variable to swap two integers
                    sorted_list [j] = sorted_list [j+1]
                    sorted_list[j+1] = temp   #  if the element before is greater than the element afterwards, then the elements swap places. After the first iteration, the biggest element is at the end of the list and it keeps going through iterations until it is completely sorted.
    # <return the sorted list>
    return sorted_list

def counting_sort(input_list):
    sorted_list = input_list[:]  # copying the list, fastest way to copy is slicing
    # <implement the algo to sort the input list>
    #First thing we need to do is find the largest element in the list
    max=input_list[0] #This makes the maximum the first element in the list
    for i in input_list: #this loop will compare the maximum to the element after it and if the max is smaller then that element becomes the new max (continues until the end of the list)
        if max < i:
            max=i
    counts= [0]*max #sets the range for the list
    for i in input_list:
        counts[i-1] = counts[i-1]+1  #counts numbers in the list (frequency)
    for i in range(1,len(counts)):
        counts[i]= counts[i-1]+counts[i]  #counts numbers ≤ i and adds them and stores them in counts[i]
        #puts numbers in order in input_list and transfers the numbers from input list to sorted_list
    for i in input_list:
        sorted_list[counts[i - 1] - 1] = i
        counts[i-1]=counts[i-1]-1  #count[i-1]-1 indicates the position of i in sorted_list
    # <return the sorted list>
    return sorted_list


# Searching algorithms implementations
def linear_search(input_list, key):
    # this function searched for the "key" and in the "input_list"
    # returns True if the "key" was found, False otherwise
    i=0
    while i < len(input_list):
        if input_list[i] == key:
            return True
        i = i + 1
    #this code goes through the list and checks if the element is equal to key, else: false is returned

    return False

def binary_search_iterative(input_list, key):

    pos=-1
    i=0 #start/lower bound
    n=len(input_list)-1  #end/upper bound
    while i<= n:
        mid= (i+n)//2
        if input_list[mid] == key: #checks if mid index value is equal to the element being looked for (key)
            pos=mid #position that's being looked for is mid
            return True
        else:
            if input_list[mid]< key:   #if key is greater than the mid then the mid is the new lower bound
                i= mid+1
            else:
                n= mid-1 #key is smaller than mid so the mid becomes new upper bound
    return False

    # The input_list must be sorted
    # this function searches for the "key" and in the "input_list"
    # returns True if the "key" was found, False otherwise
    # return True  # always found


def binary_search_recursive(input_list, key, start, end):
    pos = -1
    if start > end: #input_list has to be sorted, this checks for that
        return False
    if end > len(input_list)-1: #establishes the last index/max
        end = len(input_list)-1
    if start < 0:  #establishes the first index/min
        start = 0
    mid = (start + end) // 2
    if input_list[mid] == key:
        pos = mid #position that's being looked for is mid
        return True
    else:
        if input_list[mid] < key:
            return binary_search_recursive(input_list,key,mid+1,end) #calls the function with the mid as the new lower bound
        else:
            return binary_search_recursive(input_list,key,start,mid-1) #calls the function with the mid as the new upper bound

    # The input_list must be sorted
    # this function searches for the "key" and in the "input_list"
    # returns True if the "key" was found, False otherwise

# helper function
def is_sorted(input_list):
    sorted = False
    if not sorted:
        sorted = True
        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                sorted = False
                return False
        else:
            return True

 #compares the indexes and if any element before is greater than the element afterwards it returns False, similar algorithm to bubble sort is used

    # expects a list as input and returns True if the list is sorted, otherwise returns False
    # Make sure you are not sorting the list to check if it is sorted or not
    # do not use any built in algorithms, write your own logic


# A CUTOMIZE PRINT STATEMENT TO PRINT ANY DICT
# YOU DONT HAVE TO DO ANYTHING IN THIS FUNCTION
def print_dictionary(dict_in):
    for key in dict_in:
        print(key,': ', dict_in[key])


######## YOU DONT HAVE TO MODIFY ANYTHING IN THE FOLLOWING CODE, HOWEVER, YOU MUST UNDERSTAND WHAT IS GOING ON######
if __name__=="__main__":
    MAX = 100000
    # YOU CAN MODIFY THE FOLLOWING VARIABLE WHILE TESTING YOUR CODE
    # SET NUMBER OF LISTS TO 2 or 3, ONCE YOU ARE CONVINCED THAT YOUR CODE IS WORKING FINE
    # SET THE NUMBER_OF_LISTS BACK to 15 or more so you can get a good plot 
    NUMBER_OF_LISTS = 10
    # Creating a list of random numbers between 0 to Complexity.MAX
    # Setting the seed to make sure that the same random list is generated every time with the same parameters
    random.seed(123)  # If you comment this line, you will get different list every time for the same parameters
    Analysis = {}
    lengths_of_lists = [2 ** i for i in range(3, NUMBER_OF_LISTS + 1)]
    for list_length in lengths_of_lists: # Generating list length
        input_list = [int(random.random()*MAX) for i in range(list_length)] # Generating a list of given length with random numbers
        # Sorting a list using the built-in function of Python for list in order to test the correctness of your implememtation
        sys_sorted_list = sorted(input_list)  # Returns a sorted list without modifying the actual list

        ########## Testing bubble_sort
        start = time.time()  # noting the start time for bubble_sort
        sorted_list = bubble_sort(input_list)
        elapsed_time_lc = (time.time() - start) # computing the elapsed time in bubble_sorting
        if sorted_list == sys_sorted_list: # Checking is bubble_sort is working properly
            if 'Bubble' not in Analysis:
                Analysis['Bubble'] = [elapsed_time_lc] # noting time if bubble_sort is working properly
            else:
                Analysis['Bubble'].append(elapsed_time_lc) # noting time if bubble_sort is working properly
        else: # Adding failed instead of noting time
            if 'Bubble' not in Analysis:
                Analysis['Bubble'] = ['Failed']
            else:
                Analysis['Bubble'].append('Failed')

        ########## Testing counting_sort
        start = time.time()  # noting the start time for counting_sort
        sorted_list = counting_sort(input_list)
        elapsed_time_lc = (time.time() - start)  # computing the elapsed time in counting_sorting
        if sorted_list == sys_sorted_list:
            if 'Counting' not in Analysis:
                Analysis['Counting'] = [elapsed_time_lc]
            else:
                Analysis['Counting'].append(elapsed_time_lc)
        else:
            if 'Counting' not in Analysis: # Adding failed instead of noting time
                Analysis['Counting'] = ['Failed']
            else:
                Analysis['Counting'].append('Failed')

        ########## Testing linear_search
        sure_key =  random.sample(input_list, k=1)[0] # returns a list of one element, taking the first element
        unsure_key =  random.random() * MAX
        start = time.time()  # noting the start time for linear_search
        sure_found = linear_search(input_list, sure_key)
        unsure_found = linear_search(input_list, unsure_key)
        elapsed_time_lc = (time.time() - start)  # computing the elapsed time in linear_searching
        if sure_found == (sure_key in input_list) and unsure_found == (unsure_key in input_list):
            if 'Linear' not in Analysis:
                Analysis['Linear'] = [elapsed_time_lc]
            else:
                Analysis['Linear'].append(elapsed_time_lc)
        else: # Adding failed instead of noting time
            if 'Linear' not in Analysis:
                Analysis['Linear'] = ['Failed']
            else:
                Analysis['Linear'].append('Failed')

        ########## Testing binary_search_iterative
        sure_key =  random.sample(input_list, k=1)[0] # returns a list of one element, taking the first element
        unsure_key =  random.random() * MAX
        start = time.time()  # noting the start time for binary_search
        sure_found = binary_search_iterative(sys_sorted_list, sure_key)
        unsure_found = binary_search_iterative(sys_sorted_list, unsure_key)
        elapsed_time_lc = (time.time() - start)  # computing the elapsed time in binary_searching
        if sure_found == (sure_key in input_list) and unsure_found == (unsure_key in input_list):
            if 'BinaryItr' not in Analysis:
                Analysis['BinaryItr'] = [elapsed_time_lc]
            else:
                Analysis['BinaryItr'].append(elapsed_time_lc)
        else: # Adding failed instead of noting time
            if 'BinaryItr' not in Analysis:
                Analysis['BinaryItr'] = ['Failed']
            else:
                Analysis['BinaryItr'].append('Failed')

        ########## Testing binary_search_recursive
        sure_key = random.sample(input_list, k=1)[0]  # returns a list of one element, taking the first element
        unsure_key = random.random() * MAX
        start = time.time()  # noting the start time for binary_search
        sure_found = binary_search_recursive(sys_sorted_list, sure_key, 0, len(sys_sorted_list))
        unsure_found = binary_search_recursive(sys_sorted_list, unsure_key,0, len(sys_sorted_list))
        elapsed_time_lc = (time.time() - start)  # computing the elapsed time in binary_searching
        if sure_found == (sure_key in input_list) and unsure_found == (unsure_key in input_list):
            if 'BinaryRec' not in Analysis:
                Analysis['BinaryRec'] = [elapsed_time_lc]
            else:
                Analysis['BinaryRec'].append(elapsed_time_lc)
        else:  # Adding failed instead of noting time
            if 'BinaryRec' not in Analysis:
                Analysis['BinaryRec'] = ['Failed']
            else:
                Analysis['BinaryRec'].append('Failed')

############FOLLOWING IS THE BONUS PART ######################
############IF YOU OPT TO ATTEMPT, PLEASE UNCOMMENT THE FOLLOWING BLOCK ########### 
        ########## Testing is_sorted
        sure_key =  random.sample(input_list, k=1)[0]
        unsure_key =  random.random() * MAX
        start = time.time()  # noting the start time for is_sorted
        input_sorted = is_sorted(input_list)
        system_sorted = is_sorted(sys_sorted_list)
        elapsed_time_lc = (time.time() - start)  # computing the elapsed time in is_sorting
        if input_sorted == False and system_sorted == True:
            if 'IsSOrted' not in Analysis:
                Analysis['IsSOrted'] = [elapsed_time_lc]
            else:
                Analysis['IsSOrted'].append(elapsed_time_lc)
        else: # Adding failed instead of noting time
            if 'IsSOrted' not in Analysis:
                Analysis['IsSOrted'] = ['Failed']
            else:
                Analysis['IsSOrted'].append('Failed')

# printing the analysis dictionary
# ****************IMPORTANT*******************************************************
# If everything worked fine, you wont see a "Failed" keyword anywhere in the output
print_dictionary(Analysis)

# plotting the time taken by each algorithm
# Initially almost everything would be Failed
# In the end, there will be 5 different lines on the plot
# Sometimes the plot lines may not be visible because they may be on top of each other
# plotting the time taken by each algorithm
# Initially almost everything would be Failed
# In the end, there will be 5 different lines on the plot
# Sometimes the plot lines may not be visible because they may be on top of each other
sorting_functions = ["Bubble","Counting"]
searching_functions = ["Linear","BinaryItr", "BinaryRec"]
aux_functions = ["IsSOrted"]


### Plotting for sorting_functions
plt.figure("Sorting")
for key in sorting_functions:
    plt.plot(Analysis[key], '-o')
plt.title('Complexity of Sorting Functions')
plt.legend(sorting_functions)
plt.ylabel('Running time')
plt.xlabel('Number of elements')
plt.xticks(range(NUMBER_OF_LISTS), lengths_of_lists)



### Plotting for sorting_functions
plt.figure("Searching")
for key in searching_functions:
    plt.plot(Analysis[key], '-o')
plt.title('Complexity of Searching Functions')
plt.legend(searching_functions)
plt.ylabel('Running time')
plt.xlabel('Number of elements')
plt.xticks(range(NUMBER_OF_LISTS), lengths_of_lists)


# ## Plotting for aux_functions
plt.figure("IsSOrted")
for key in aux_functions:
    plt.plot(Analysis[key], '-o')
plt.title('Complexity of IsSOrted Functions')
plt.legend(aux_functions)
plt.ylabel('Running time')
plt.xlabel('Number of elements')
plt.xticks(range(NUMBER_OF_LISTS), lengths_of_lists)

plt.show()
