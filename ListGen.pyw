# Python 3.6.4
import tkinter as tk
from tkinter import ttk
import os


window = tk.Tk()
window.iconbitmap(os.path.abspath('./list.ico'))
window.title('ListGen 1.0')
window.resizable(0,0)


#functions
def convert_delim():
	text2.delete('1.0',tk.END)
	varget1 = combovar1.get()

	if varget1 == ',':
		rtext = ','
	elif varget1 == ';':
		rtext = ';'
	elif varget1 == '|':
		rtext = ';'

	input = text1.get('1.0',tk.END)
	output = input.replace('\n',rtext)
	output = output[:-1]
	if output.endswith(rtext):
		output = output[:-1]
	text2.insert(tk.END,output)


def convert_line():
	text1.delete('1.0',tk.END)
	varget1 = combovar1.get()

	if varget1 == ',':
		rtext = ','
	elif varget1 == ';':
		rtext = ';'
	elif varget1 == '|':
		rtext = ';'


	input = text2.get('1.0',tk.END) 
	output = input.replace(rtext,'\n')
	output = output[:-1]
	if output.endswith('\n'):
		output = output[:-1]
	text1.insert(tk.END,output)


def clearall():
	text1.delete('1.0',tk.END)
	text2.delete('1.0',tk.END)


def copy_text1():
	input = text1.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text2():
	input = text2.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)

# input dropdown and label
label1 = tk.Label(text='Column Data:',font=("Arial",10)).grid(column=0,row=0,sticky='W',padx=10,pady=10)
text1 = tk.Text(window,height=20,width=20)
text1.grid(column=0,row=1,rowspan=20,padx=10,pady=10)
scrollbar1 = tk.Scrollbar(window, orient='vertical')
scrollbar1.grid(column=0,row=1,rowspan=20,sticky='N'+'S'+'E',padx=10,pady=10)
scrollbar1.config( command = text1.yview )
text1.configure(yscrollcommand=scrollbar1.set)

combovar1 = tk.StringVar()
combovar1.set(',')
comboval1 = [',', ';', '|']
combo1 = ttk.Combobox(window,textvariable=combovar1,values=comboval1,state='readonly',font=('Arial','10'), justify='center',width=7).grid(column=1,row=9,padx=10,pady=10,sticky='W'+'E')

right = tk.PhotoImage(file=os.path.abspath('./right.png'))
button1 = tk.Button(window, image=right, border=0, cursor='hand2',command=convert_delim).grid(column=1,row=10,sticky='W'+'E',pady=10,padx=10)

left = tk.PhotoImage(file=os.path.abspath('./left.png'))
button2 = tk.Button(window, image=left, border=0, cursor='hand2',command=convert_line).grid(column=1,row=11,sticky='W'+'E',pady=10,padx=10)

clear = tk.PhotoImage(file=os.path.abspath('./clear.png'))
button3 = tk.Button(window, image=clear, border=0, cursor='hand2',command=clearall).grid(column=1,row=12,sticky='W'+'E',pady=10,padx=10)



label2 = tk.Label(text='Delimited Data:',font=('Arial',10)).grid(column=2,row=0,sticky='W',padx=10,pady=10)
text2 = tk.Text(window,height=20)
text2.grid(column=2,row=1,rowspan=20,padx=10,pady=10)
scrollbar2 = tk.Scrollbar(window, orient='vertical')
scrollbar2.grid(column=2,row=1,rowspan=20,sticky='N'+'S'+'E',padx=10,pady=10)
scrollbar2.config( command = text2.yview )
text2.configure(yscrollcommand=scrollbar2.set)


clip = tk.PhotoImage(file=os.path.abspath('./clipboard.png'))
button4 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text1).grid(column=0,row=21,sticky='E',padx=10)
button5 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text2).grid(column=2,row=21,sticky='E',padx=10)



label8 = tk.Label(text="© 2018 Parry Pardun",font=("Arial",8)).grid(column=0,row=22,sticky='W'+'S')

window.update_idletasks()
window.deiconify()
window.mainloop()


