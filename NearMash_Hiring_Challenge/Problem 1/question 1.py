# Question 1

from os.path import abspath

# Set Input File Path
inputFile = abspath("input")

def count_unique_sets():
    # Read Input File
    fileName = open(inputFile, "r")

    # Iterate through every line in file
    for line in fileName:

        # Convert string into list
        number_list = line.split()

        # Remove Duplicate values from the list
        number_list = list(set(number_list))

        # Sort list and initialize count as 0
        number_list.sort()
        count = 0

        '''
        O(n^3) Algo-

        for i in range(len(number_list)-2):
            for j in range(i+1, len(number_list)-1):
                for k in range(j+1, len(number_list)):
                    if int(number_list[i]) + int(number_list[j]) > int(number_list[k]):
                        count+=1
        print(count)

        '''

        # Time Complexiy - O(n^2)

        # Fix the first element.  We need to run till n-3 as
        # the other two elements are selected from arr[i+1...n-1]
        for i in range(len(number_list)-2):

            # Initialize index of the rightmost third element
            k = i+2
            
            # Fix the second element
            for j in range(i+1, len(number_list)):
                while (k<len(number_list) and int(number_list[i]) + int(number_list[j]) > int(number_list[k])):
                    k+=1

                count += k-j-1

        print(count)

try:
    count_unique_sets()
except IOError:
    print("File Not Found.")
    pass















