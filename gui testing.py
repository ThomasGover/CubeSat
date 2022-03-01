# Python program to create a table

from tkinter import *

# take the data
xaxis = 12
yaxis = 13
zaxis = 14
dec = 15
head = 16



ROOT = Tk()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    
    class Table:
	
	    def __init__(self,root):
		
		# code for creating table
		    for i in range(total_rows):
			    for j in range(total_columns):
				
				    self.e = Entry(root, width=20, fg='black', bg= 'light blue', justify = 'center', bd = 12, relief = 'ridge',
							font=('Arial',16,'bold'))
				
				    self.e.grid(row=i, column=j)
				    self.e.insert(END, lst[i][j])

    # take the data
    lst = [('X-Axis',xaxis),
    	('Y-Axis',yaxis),
        ('Z-Axis',zaxis),
    	('Declination',dec),
    	('Heading',head)]

    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    xaxis+=1
    yaxis+=2
    zaxis+=3
    dec+=4
    head+=5


    t = Table(ROOT)
    # ROOT.configure(bg='red')
    ROOT.update()
    # USER_INPUT = raw_input("Give me your command! Just type \"exit\" to close: ")
    # if USER_INPUT == "exit":
    #     ROOT.quit()
    #     LOOP_ACTIVE = False
    # else:
    #     LABEL = Label(ROOT, text=USER_INPUT)
    #     LABEL.pack()
