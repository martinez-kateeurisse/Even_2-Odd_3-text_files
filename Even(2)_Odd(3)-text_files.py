#Kate Eurisse Martinez_BSCPE 1-5

#A Python program that contains a method that will create two separate text files 
#after reading the source text file named integers.txt, which contains 20 integers. 
#The first output file will be named double.txt, containing the square of all even integers found in integers.txt, 
#and the second file will be named triple.txt, containing the cube of all odd numbers found in integers.txt.

#Input 20 integers to the text file (user-input)

#Open the main text file named integers.txt
with open("integers.txt", "w") as num_file:
    #Initialize count
    #Loop condition
        #Ask the user for input
        #Write the input to the text file
        #Add one to the count

#Read and open the text files
with open("integers.txt", "r") as num_file, open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    #For each line
    for line in num_file:
        #Convert line to int
        integers = int(line) 
        #If the interger is even
        if (integers % 2) == 0:
            #Square the integer
            integers = integers**2
            #Convert integers to str
            integers = str(integers)
            #Write the result in new text file (double.txt)
            double_file.write(integers + "\n")
        #if the integer is odd
        else:  
            #Cube the integer
            integers = integers**3
            #Convert integers to str
            integers = str(integers)
            #Write the result in new text file (triple.txt)
            triple_file.write(integers + "\n")
#Outputs will be printed in new text files
