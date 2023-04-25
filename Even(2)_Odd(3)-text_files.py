#Kate Eurisse Martinez_BSCPE 1-5

#A Python program that contains a method that will create two separate text files 
#after reading the source text file named integers.txt, which contains 20 integers. 
#The first output file will be named double.txt, containing the square of all even integers found in integers.txt, 
#and the second file will be named triple.txt, containing the cube of all odd numbers found in integers.txt.

#Import certain modules for the program's design and text formatting
from colorama import Back, Fore, Style 
import prog_design #own python file

#Print header art for the program
prog_design.double_triple_header()

#Ask the user's name and printing a greeting
print("//" * 20)
name = input(f"{Fore.RED} Enter your name: "+ Fore.RESET)
print("//"*20, "\n\n") 
print(Back.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, ("Hello " + name).center(84, "*") + Back.RESET, "\n")

#Display the program's instructions
print(f"{Fore.GREEN} This program will write the integers you'll enter into a text file named number.txt.","\n",
      "Then, all even integers will be doubled and written to even.txt,","\n"+" while odd integers will be tripled and written on odd.txt"+Fore.RESET)
print("="*85)

#Input 20 integers to the text file (user-input)

#Open the main text file named integers.txt
with open("integers.txt", "w") as num_file:
    #Initialize count
    number_count = 1    
    #Loop condition
    while number_count <= 20:    
        #Ask the user for input
        num_input = input(f"{Fore.RED}Please enter an integer: " + Fore.RESET) 
        #Write the input to the text file
        num_file.write(num_input+"\n")
        #Add one to the count
        number_count += 1

#Read and open the text files
with open("integers.txt", "r") as num_file, open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
    #Initialize lists
    double_int = []
    triple_int = []     
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
            #Append into a list
            double_int.append(integers.strip()) 
            #Join as string
            double_string = "\n".join(double_int)
        #if the integer is odd
        else:  
            #Cube the integer
            integers = integers**3
            #Convert integers to str
            integers = str(integers)
            #Write the result in new text file (triple.txt)
            triple_file.write(integers + "\n")
            #Append into a list
            triple_int.append(integers.strip())
            #Join as string
            triple_string = "\n".join(triple_int) 

#Outputs will be printed in new text files

#Displaying output instructions
print("="*85)
print(f"{Fore.LIGHTGREEN_EX} Note: The output of the program will be displayed in a new tkinter window.", "\n" 
      " And txt files (integer.txt, even.txt, odd.txt) will be created. "+Fore.RESET)
print("="*85)

#For output design
#Import modules
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#Define the function for buttons
#Define the function for button clicks
    #If button 1
        #Display output (even)
    #If button 2
        #Display output (Odd)

#Create a new window
#Size of the window 
#Add a title
#Add background image
#Add two buttons to the window (even, odd)
#Add a label to display output text

#main loop method

#Output will also be displayed in the tkinter window.(Aside from the txt files)