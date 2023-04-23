#Kate Eurisse Martinez_BSCPE 1-5

#A Python program that contains a method that will create two separate text files 
#after reading the source text file named integers.txt, which contains 20 integers. 
#The first output file will be named double.txt, containing the square of all even integers found in integers.txt, 
#and the second file will be named triple.txt, containing the cube of all odd numbers found in integers.txt.

#Create a source text file named integers.txt

#Read and open the text files
with open("numbers.txt") as num_file, open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    #For each line
    for line in num_file:
        #Convert line to int
        integers = int(line) 
        #If the interger is even
            #Square the integer
            #Convert integers to str
            #Write the result in new text file (double.txt)
        #if the integer is odd  
            #Cube the integer
            #Convert integers to str
            #Write the result in new text file (triple.txt)
#Outputs will be printed in new text files
