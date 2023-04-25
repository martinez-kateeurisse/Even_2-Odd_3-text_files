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
        num_input = input(f"{Fore.RED} Please enter an integer: " + Fore.RESET) 
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
      " And txt files (integer.txt, double.txt, triple.txt) will be created. "+Fore.RESET)
print("="*85)

#For output design
#Import modules
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

#Define the function for buttons
def button_click(button_number):
    #If button 1
    if button_number == 1:
        #Display output (even)
        output_text.set("Square of Even Integers: \n" + double_string)
    #If button 2
    elif button_number == 2:
        #Display output (Odd)
        output_text.set("Cube of Odd Integers  : \n" + triple_string)

#Create a new window
root = tk.Tk()
root.geometry("200x450")  # Size of the window 
root.title("File Handling - Even, Odd")  # Adding a title

#Add background image
canvas = tk.Canvas(root, width=1000, height=1500)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\Kate\\Desktop\\OOP\\program.git\\background_image(2).jpg"))
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()

#Add two buttons to the window (even, odd)
button1 = tk.Button(root, text="Even", command=lambda: button_click(1), fg="red")
button1.place(x=80, y=30)
button2 = tk.Button(root, text="Odd", command=lambda: button_click(2), fg="blue")
button2.place(x=80, y=60)

#Add a label to display output text
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text)
output_label.place(x=32, y=100)

#main loop method
root.mainloop()

#Output will also be displayed in the tkinter window.(Aside from the txt files)

#Displaying thank you message after the user closes the tkinter window
prog_design.program_footer()