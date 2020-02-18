
#!/usr/local/bin/python3

import tkinter as tk
import tkinter.messagebox

window=tk.Tk()
window.title('BMI计算器 | powered by skp')
window.geometry('500x400')
def c(bmi):
	who,nat="",""
	if bmi < 18.5:
		who,nat="偏瘦","便瘦"
	elif 18.5 <= bmi < 24:
		who,nat="正常","正常"
	elif 24 <= bmi <25:
		who,nat="正常","偏胖"
	elif 25 <= bmi <28:
		who,nat="偏胖","偏胖"
	elif 28 <= bmi <30:
		who,nat="偏胖","肥胖"
	else:
		who,nat="肥胖","肥胖"
	return "国内{0}，国际{1}".format(nat,who)


def calc():
	try:
		high=t1.get()
		weight=t2.get()
		bmi = eval(weight) / pow(eval(high) ,2)	
		r = "BMI:{:.2f},{:}".format(bmi,c(bmi))
		tkinter.messagebox.showinfo(title='结果为', message=r) 
	except:
		tkinter.messagebox.showerror(title='出错了', message="疑似没有正确输入数据")

t1=tk.Entry(window,show=None)
t1.pack()
t1.place(x=200,y=100)
t2=tk.Entry(window,show=None)
t2.pack()
t2.place(x=200,y=150)

l1 = tk.Label(window, text='身高:', font=('Arial', 16), width=10, height=2)
l1.pack()
l1.place(x=110,y=92)
l2 = tk.Label(window, text='体重:', font=('Arial', 16), width=10, height=2)
l2.pack()
l2.place(x=110,y=142)

calc = tk.Button(window, text='计算', font=('Arial', 16), width=20, height=1, command=calc)
calc.pack()
calc.place(x=180,y=200)

window.mainloop()

