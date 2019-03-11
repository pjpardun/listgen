# Python 3.6.4
import tkinter as tk
from tkinter import ttk
import os
import math

window = tk.Tk()
window.iconbitmap(os.path.abspath('./list.ico'))
window.title('ListGen 3.0')
window.resizable(0,0)


#functions
def start_value():
	textunitsplit.insert(tk.END, '0')
	textgroupsplit.insert(tk.END,'0')


def convert_delim():
	for i in textdict:
		i.delete('1.0',tk.END)

	getcombovar = combovar.get()
	getunitsplitvar = textunitsplit.get('1.0',tk.END)
	getgroupsplitvar = textgroupsplit.get('1.0',tk.END)

	if getcombovar == ',':
		rtext = ','
	elif getcombovar == ';':
		rtext = ';'
	elif getcombovar == '|':
		rtext = ';'

	input = textcolumn.get('1.0',tk.END)
	output = input.replace('\n',rtext)
	output = output[:-1]
	if output.endswith(rtext):
		output = output[:-1]
	else:
		output = output
	if int(float(getunitsplitvar)) == 0 and int(float(getgroupsplitvar)) == 0:
		textdelim = textdict[0]
		textdelim.delete('1.0',tk.END)
		textdelim.insert(tk.END,output)
	elif int(float(getunitsplitvar)) != 0 and int(float(getgroupsplitvar)) == 0:
		numofunits = len(output.split(rtext))
		splitnum = int(float(getunitsplitvar))
		numofgroups = math.ceil(numofunits/splitnum)
		unitarray = output.split(rtext)
		i=0 #text box array index start
		j=0 #unit array index start
		k=1 #group number start
		try:
			for group in range(1, numofgroups+1):
				textdict[i].insert(tk.END,rtext.join(unitarray[j:splitnum*k])) 
				i = i + 1
				j = j + splitnum
				k = k + 1
		except IndexError:
			return
	elif int(float(getunitsplitvar)) == 0 and int(float(getgroupsplitvar)) != 0:
		numofunits = len(output.split(rtext))
		numofgroups = int(float(getgroupsplitvar))
		splitnum = math.ceil(numofunits/numofgroups)
		unitarray = output.split(rtext)
		i=0
		j=0 
		k=1 
		try:
			for group in range(1, numofgroups+1):
				textdict[i].insert(tk.END,rtext.join(unitarray[j:splitnum*k])) 
				i = i + 1
				j = j + splitnum
				k = k + 1
		except IndexError:
			return


def convert_line():
	textcolumn.delete('1.0',tk.END)
	getcombovar = combovar.get()

	if getcombovar == ',':
		rtext = ','
	elif getcombovar == ';':
		rtext = ';'
	elif getcombovar == '|':
		rtext = ';'


	input = textdict[0].get('1.0',tk.END) 
	output = input.replace(rtext,'\n')
	output = output[:-1]
	if output.endswith('\n'):
		output = output[:-1]
	textcolumn.insert(tk.END,output)


def clearall():
	textcolumn.delete('1.0',tk.END)
	for i in textdict:
		i.delete('1.0',tk.END)


def copy_text(textObj):
	input = textObj.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


#GUI widgets
#icons
clip = tk.PhotoImage(file=os.path.abspath('./clipboard.png'))
right = tk.PhotoImage(file=os.path.abspath('./right.png'))
left = tk.PhotoImage(file=os.path.abspath('./left.png'))
clear = tk.PhotoImage(file=os.path.abspath('./clear.png'))

#for column data
tk.Label(text='Column Data:',font=('Arial',10)).grid(column=0,row=0,sticky='W',padx=10,pady=10)
textcolumn = tk.Text(window,height=23,width=20)
textcolumn.grid(column=0,row=1,rowspan=20,padx=10)
textcolumnscrollbar = tk.Scrollbar(window, orient='vertical')
textcolumnscrollbar.grid(column=0,row=1,rowspan=20,sticky='N'+'S'+'E')
textcolumnscrollbar.config( command = textcolumn.yview )
textcolumn.configure(yscrollcommand=textcolumnscrollbar.set)
tk.Button(window, image=clip, border=0, cursor='hand2',command=lambda:copy_text(textcolumn)).grid(column=1,row=18,sticky='W')

#for delimeter selection
combovar = tk.StringVar()
combovar.set(',')
comboval = [',', ';', '|']
ttk.Combobox(window,textvariable=combovar,values=comboval,state='readonly',font=('Arial','10'),justify='center',width=7).grid(column=1,row=2,sticky='W'+'E',padx=10)

#for conversions
tk.Button(window, image=right, border=0, cursor='hand2',command=convert_delim).grid(column=1,row=5,sticky='W'+'E')
tk.Button(window, image=left, border=0, cursor='hand2',command=convert_line).grid(column=1,row=8,sticky='W'+'E')
tk.Button(window, image=clear, border=0, cursor='hand2',command=clearall).grid(column=1,row=11,sticky='W'+'E')

#for output splitting
tk.Label(text='    Split Delimited Output:    ',font=('Arial',9)).grid(column=1,row=14,sticky='N'+'S'+'E'+'W')
tk.Label(text='Units:                  ',font=('Arial',9)).grid(column=1,row=16,sticky='E',padx=5,pady=10)
tk.Label(text='Groups:                  ',font=('Arial',9)).grid(column=1,row=18,sticky='E',padx=5,pady=10)
textunitsplit = tk.Text(window,height=1,width=7,font=('Arial',10))
textunitsplit.grid(column=1,row=16,sticky='E',padx=5)
textgroupsplit = tk.Text(window,height=1,width=7,font=('Arial',10))
textgroupsplit.grid(column=1,row=18,sticky='E',padx=5)
#tk.Label(text='   Default 0 for no splitting   ',font=('Arial',8)).grid(column=1,row=21,sticky='W'+'S')

#for delimited data
tk.Label(text='Delimited Data:',font=('Arial',10)).grid(column=2,row=0,sticky='W',padx=10,pady=10)

textdict = []
#create 5x5 grid of text boxes, scrollbars, and clipboard buttons
for thisrow in [1,4,7,10,13]:
	for thiscol in [2,4,6,8,10]:
		thistext = tk.Text(window,height=3,width=15)
		thistext.grid(column=thiscol,row=thisrow,rowspan=3)
		textdict.append(thistext) #reference to each textboxt added to cleardict
		thisscrollbar = tk.Scrollbar(window, orient='vertical')
		thisscrollbar.grid(column=thiscol,row=thisrow,rowspan=3,sticky='N'+'S'+'E',pady=3)
		thisscrollbar.config(command=thistext.yview)
		thistext.configure(yscrollcommand=thisscrollbar.set)
		thisbutton = tk.Button(window,image=clip,border=0,cursor='hand2',command=lambda lambdatext=thistext : copy_text(lambdatext)).grid(column=thiscol+1,row=thisrow+1,sticky='E')

tk.Label(text='© 2019 Parry Pardun',font=('Arial',8)).grid(column=0,row=24,sticky='W'+'S')

start_value()

window.update_idletasks()

window.deiconify()

window.mainloop()