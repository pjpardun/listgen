# Python 3.6.4
import tkinter as tk
from tkinter import ttk
import os
import math

window = tk.Tk()
window.iconbitmap(os.path.abspath('./list.ico'))
window.title('ListGen 2.0')
window.resizable(0,0)


#functions
def start_value():
	textsplit.insert(tk.END, '0')


def convert_delim():
	text2.delete('1.0',tk.END)
	varget1 = combovar1.get()

	vargetsplit = textsplit.get('1.0',tk.END)

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
	else:
		output = output
	if int(float(vargetsplit)) == 0:
		text2.insert(tk.END,output)
	else:
		numofunits = len(output.split(rtext))
		splitnum = int(float(vargetsplit))
		numofgroups = math.ceil(numofunits/splitnum)
		unitarray = output.split(rtext)
		text_list = [text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15,text16,text17,text18,text19,text20,text21,text22,text23,text24,text25,text26
	]
		i=0 #text box array index start
		j=0 #unit array index start
		k=1 #group number start
		try:
			for group in range(1, numofgroups+1):
				text_list[i].insert(tk.END,rtext.join(unitarray[j:splitnum*k])) 
				i = i + 1
				j = j + splitnum
				k = k + 1
		except IndexError:
			return


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
	text3.delete('1.0',tk.END)
	text4.delete('1.0',tk.END)
	text5.delete('1.0',tk.END)
	text6.delete('1.0',tk.END)
	text7.delete('1.0',tk.END)
	text8.delete('1.0',tk.END)
	text9.delete('1.0',tk.END)
	text10.delete('1.0',tk.END)
	text11.delete('1.0',tk.END)
	text12.delete('1.0',tk.END)
	text13.delete('1.0',tk.END)
	text14.delete('1.0',tk.END)
	text15.delete('1.0',tk.END)
	text16.delete('1.0',tk.END)
	text17.delete('1.0',tk.END)
	text18.delete('1.0',tk.END)
	text19.delete('1.0',tk.END)
	text20.delete('1.0',tk.END)
	text21.delete('1.0',tk.END)
	text22.delete('1.0',tk.END)
	text23.delete('1.0',tk.END)
	text24.delete('1.0',tk.END)
	text25.delete('1.0',tk.END)
	text26.delete('1.0',tk.END)
	textsplit.delete('1.0',tk.END)
	textsplit.insert(tk.END, '0')



def copy_text1():
	input = text1.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text2():
	input = text2.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text3():
	input = text3.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text4():
	input = text4.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text5():
	input = text5.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text6():
	input = text6.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text7():
	input = text7.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text8():
	input = text8.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text9():
	input = text9.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text10():
	input = text10.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text11():
	input = text11.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text12():
	input = text12.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text13():
	input = text13.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text14():
	input = text14.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text15():
	input = text15.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text16():
	input = text16.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text17():
	input = text17.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text18():
	input = text18.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text19():
	input = text19.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text20():
	input = text20.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text21():
	input = text21.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text22():
	input = text22.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text23():
	input = text23.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text24():
	input = text24.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text25():
	input = text25.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


def copy_text26():
	input = text26.get('1.0',tk.END)
	window.clipboard_clear()  
	window.clipboard_append(input)


# input dropdown and label
label1 = tk.Label(text='Column Data:',font=("Arial",10)).grid(column=0,row=0,sticky='W',padx=10,pady=10)
text1 = tk.Text(window,height=20,width=20)
text1.grid(column=0,row=1,rowspan=20,padx=10)
scrollbar1 = tk.Scrollbar(window, orient='vertical')
scrollbar1.grid(column=0,row=1,rowspan=20,sticky='N'+'S'+'E')
scrollbar1.config( command = text1.yview )
text1.configure(yscrollcommand=scrollbar1.set)

combovar1 = tk.StringVar()
combovar1.set(',')
comboval1 = [',', ';', '|']
combo1 = ttk.Combobox(window,textvariable=combovar1,values=comboval1,state='readonly',font=('Arial','10'), justify='center',width=7).grid(column=1,row=2,sticky='W'+'E',padx=10)

right = tk.PhotoImage(file=os.path.abspath('./right.png'))
button1 = tk.Button(window, image=right, border=0, cursor='hand2',command=convert_delim).grid(column=1,row=5,sticky='W'+'E')

left = tk.PhotoImage(file=os.path.abspath('./left.png'))
button2 = tk.Button(window, image=left, border=0, cursor='hand2',command=convert_line).grid(column=1,row=8,sticky='W'+'E')

clear = tk.PhotoImage(file=os.path.abspath('./clear.png'))
button3 = tk.Button(window, image=clear, border=0, cursor='hand2',command=clearall).grid(column=1,row=11,sticky='W'+'E')

labelsplit = tk.Label(text='Units per Group:*',font=("Arial",10)).grid(column=1,row=14,sticky='W',padx=10,pady=10)
textsplit = tk.Text(window,height=1,width=7)
textsplit.grid(column=1,row=17)



label2 = tk.Label(text='Delimited Data:',font=('Arial',10)).grid(column=2,row=0,sticky='W',padx=10,pady=10)
text2 = tk.Text(window,height=3,width=15)
text2.grid(column=2,row=1,rowspan=3)
scrollbar2 = tk.Scrollbar(window, orient='vertical')
scrollbar2.grid(column=2,row=1,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar2.config( command = text2.yview )
text2.configure(yscrollcommand=scrollbar2.set)

#
text3 = tk.Text(window,height=3,width=15)
text3.grid(column=4,row=1,rowspan=3)
scrollbar3 = tk.Scrollbar(window, orient='vertical')
scrollbar3.grid(column=4,row=1,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar3.config( command = text3.yview )
text3.configure(yscrollcommand=scrollbar3.set)

text4 = tk.Text(window,height=3,width=15)
text4.grid(column=6,row=1,rowspan=3)
scrollbar4 = tk.Scrollbar(window, orient='vertical')
scrollbar4.grid(column=6,row=1,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar4.config( command = text4.yview )
text4.configure(yscrollcommand=scrollbar4.set)

text5 = tk.Text(window,height=3,width=15)
text5.grid(column=8,row=1,rowspan=3)
scrollbar5 = tk.Scrollbar(window, orient='vertical')
scrollbar5.grid(column=8,row=1,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar5.config( command = text5.yview )
text5.configure(yscrollcommand=scrollbar5.set)

text6 = tk.Text(window,height=3,width=15)
text6.grid(column=10,row=1,rowspan=3)
scrollbar6 = tk.Scrollbar(window, orient='vertical')
scrollbar6.grid(column=10,row=1,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar6.config( command = text6.yview )
text6.configure(yscrollcommand=scrollbar6.set)

text7 = tk.Text(window,height=3,width=15)
text7.grid(column=2,row=4,rowspan=3)
scrollbar7 = tk.Scrollbar(window, orient='vertical')
scrollbar7.grid(column=2,row=4,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar7.config( command = text7.yview )
text7.configure(yscrollcommand=scrollbar7.set)

text8 = tk.Text(window,height=3,width=15)
text8.grid(column=4,row=4,rowspan=3)
scrollbar8 = tk.Scrollbar(window, orient='vertical')
scrollbar8.grid(column=4,row=4,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar8.config( command = text8.yview )
text8.configure(yscrollcommand=scrollbar8.set)

text9 = tk.Text(window,height=3,width=15)
text9.grid(column=6,row=4,rowspan=3)
scrollbar9 = tk.Scrollbar(window, orient='vertical')
scrollbar9.grid(column=6,row=4,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar9.config( command = text9.yview )
text9.configure(yscrollcommand=scrollbar9.set)

text10 = tk.Text(window,height=3,width=15)
text10.grid(column=8,row=4,rowspan=3)
scrollbar10 = tk.Scrollbar(window, orient='vertical')
scrollbar10.grid(column=8,row=4,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar10.config( command = text10.yview )
text10.configure(yscrollcommand=scrollbar10.set)

text11 = tk.Text(window,height=3,width=15)
text11.grid(column=10,row=4,rowspan=3)
scrollbar11 = tk.Scrollbar(window, orient='vertical')
scrollbar11.grid(column=10,row=4,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar11.config( command = text11.yview )
text11.configure(yscrollcommand=scrollbar11.set)

text12 = tk.Text(window,height=3,width=15)
text12.grid(column=2,row=7,rowspan=3)
scrollbar12 = tk.Scrollbar(window, orient='vertical')
scrollbar12.grid(column=2,row=7,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar12.config( command = text12.yview )
text12.configure(yscrollcommand=scrollbar12.set)

text13 = tk.Text(window,height=3,width=15)
text13.grid(column=4,row=7,rowspan=3)
scrollbar13 = tk.Scrollbar(window, orient='vertical')
scrollbar13.grid(column=4,row=7,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar13.config( command = text13.yview )
text13.configure(yscrollcommand=scrollbar13.set)

text14 = tk.Text(window,height=3,width=15)
text14.grid(column=6,row=7,rowspan=3)
scrollbar14 = tk.Scrollbar(window, orient='vertical')
scrollbar14.grid(column=6,row=7,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar14.config( command = text14.yview )
text14.configure(yscrollcommand=scrollbar14.set)

text15 = tk.Text(window,height=3,width=15)
text15.grid(column=8,row=7,rowspan=3)
scrollbar15 = tk.Scrollbar(window, orient='vertical')
scrollbar15.grid(column=8,row=7,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar15.config( command = text15.yview )
text15.configure(yscrollcommand=scrollbar15.set)

text16 = tk.Text(window,height=3,width=15)
text16.grid(column=10,row=7,rowspan=3)
scrollbar16 = tk.Scrollbar(window, orient='vertical')
scrollbar16.grid(column=10,row=7,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar16.config( command = text16.yview )
text16.configure(yscrollcommand=scrollbar16.set)

text17 = tk.Text(window,height=3,width=15)
text17.grid(column=2,row=10,rowspan=3)
scrollbar17 = tk.Scrollbar(window, orient='vertical')
scrollbar17.grid(column=2,row=10,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar17.config( command = text17.yview )
text17.configure(yscrollcommand=scrollbar17.set)

text18 = tk.Text(window,height=3,width=15)
text18.grid(column=4,row=10,rowspan=3)
scrollbar18 = tk.Scrollbar(window, orient='vertical')
scrollbar18.grid(column=4,row=10,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar18.config( command = text18.yview )
text18.configure(yscrollcommand=scrollbar18.set)

text19 = tk.Text(window,height=3,width=15)
text19.grid(column=6,row=10,rowspan=3)
scrollbar19 = tk.Scrollbar(window, orient='vertical')
scrollbar19.grid(column=6,row=10,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar19.config( command = text19.yview )
text19.configure(yscrollcommand=scrollbar19.set)

text20 = tk.Text(window,height=3,width=15)
text20.grid(column=8,row=10,rowspan=3)
scrollbar20 = tk.Scrollbar(window, orient='vertical')
scrollbar20.grid(column=8,row=10,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar20.config( command = text20.yview )
text20.configure(yscrollcommand=scrollbar20.set)

text21 = tk.Text(window,height=3,width=15)
text21.grid(column=10,row=10,rowspan=3)
scrollbar21 = tk.Scrollbar(window, orient='vertical')
scrollbar21.grid(column=10,row=10,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar21.config( command = text21.yview )
text21.configure(yscrollcommand=scrollbar21.set)

text22 = tk.Text(window,height=3,width=15)
text22.grid(column=2,row=13,rowspan=3)
scrollbar22 = tk.Scrollbar(window, orient='vertical')
scrollbar22.grid(column=2,row=13,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar22.config( command = text22.yview )
text22.configure(yscrollcommand=scrollbar22.set)

text23 = tk.Text(window,height=3,width=15)
text23.grid(column=4,row=13,rowspan=3)
scrollbar23 = tk.Scrollbar(window, orient='vertical')
scrollbar23.grid(column=4,row=13,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar23.config( command = text23.yview )
text23.configure(yscrollcommand=scrollbar23.set)

text24 = tk.Text(window,height=3,width=15)
text24.grid(column=6,row=13,rowspan=3)
scrollbar24 = tk.Scrollbar(window, orient='vertical')
scrollbar24.grid(column=6,row=13,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar24.config( command = text24.yview )
text24.configure(yscrollcommand=scrollbar24.set)

text25 = tk.Text(window,height=3,width=15)
text25.grid(column=8,row=13,rowspan=3)
scrollbar25 = tk.Scrollbar(window, orient='vertical')
scrollbar25.grid(column=8,row=13,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar25.config( command = text25.yview )
text25.configure(yscrollcommand=scrollbar25.set)

text26 = tk.Text(window,height=3,width=15)
text26.grid(column=10,row=13,rowspan=3)
scrollbar26 = tk.Scrollbar(window, orient='vertical')
scrollbar26.grid(column=10,row=13,rowspan=3,sticky='N'+'S'+'E',pady=3)
scrollbar26.config( command = text26.yview )
text26.configure(yscrollcommand=scrollbar26.set)

#

clip = tk.PhotoImage(file=os.path.abspath('./clipboard.png'))
button4 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text1).grid(column=0,row=21,sticky='E')
button5 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text2).grid(column=3,row=2,sticky='E')
button6 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text3).grid(column=5,row=2,sticky='E')
button7 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text4).grid(column=7,row=2,sticky='E')
button8 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text5).grid(column=9,row=2,sticky='E')
button9 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text6).grid(column=11,row=2,sticky='E')
button10 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text7).grid(column=3,row=5,sticky='E')
button11 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text8).grid(column=5,row=5,sticky='E')
button12 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text9).grid(column=7,row=5,sticky='E')
button13 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text10).grid(column=9,row=5,sticky='E')
button14 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text11).grid(column=11,row=5,sticky='E')
button15 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text12).grid(column=3,row=8,sticky='E')
button16 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text13).grid(column=5,row=8,sticky='E')
button17 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text14).grid(column=7,row=8,sticky='E')
button18 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text15).grid(column=9,row=8,sticky='E')
button19 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text16).grid(column=11,row=8,sticky='E')
button20 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text17).grid(column=3,row=11,sticky='E')
button21 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text18).grid(column=5,row=11,sticky='E')
button22 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text19).grid(column=7,row=11,sticky='E')
button23 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text20).grid(column=9,row=11,sticky='E')
button24 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text21).grid(column=11,row=11,sticky='E')
button25 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text22).grid(column=3,row=14,sticky='E')
button26 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text23).grid(column=5,row=14,sticky='E')
button27 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text24).grid(column=7,row=14,sticky='E')
button28 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text25).grid(column=9,row=14,sticky='E')
button29 = tk.Button(window, image=clip, border=0, cursor='hand2',command=copy_text26).grid(column=11,row=14,sticky='E')

label8 = tk.Label(text="© 2019 Parry Pardun",font=("Arial",8)).grid(column=0,row=22,sticky='W'+'S')

label9 = tk.Label(text="*Default 0 for no grouping",font=("Arial",8)).grid(column=1,row=22,sticky='W'+'S')

start_value()
window.update_idletasks()
window.deiconify()
window.mainloop()


