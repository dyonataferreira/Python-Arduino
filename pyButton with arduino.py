from pyfirmata import Arduino, util		# import lib to communicate with Arduino
import time								# import lib to works with time
from tkinter import *					# import lib to works a window	

board = Arduino('com13')				# change the COM to works fine in your project

# variable to switch
global aux1
aux1 = 0

global aux2
aux2 = 0

# Main Function
def Led(led):
    global aux1
    global aux2
    

    if(led == 1):
    	# switch led 1
        if (aux1==0):
            board.digital[2].write(1)		# write to digital 2 HIGH
            print("on led1")
            aux1=1
        else :
            board.digital[2].write(0)		# write to digital 2 LOW
            print("off led1")
            aux1=0
            
    if(led == 2):
    	# switch led 2
        if (aux2==0):
            board.digital[3].write(1)		# write to digital 3 HIGH
            print("on led2")
            aux2=1
        else :
            board.digital[3].write(0)		# write to digital 3 LOW
            print("off led2")
            aux2=0

# Create a Window
janel = Tk()
janel.title('testando viu')
janel.geometry('500x500')

# Put 2 buttons in scream
botao1 = Button(text = "led1", command = lambda: Led(1)).place(x = 50, y = 50)		# cria um botão
botao2 = Button(text = "led2", command = lambda: Led(2)).place(x = 150, y = 50)		# cria um botão

# Run our code
janel.mainloop()

