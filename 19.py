import tkinter as tk
win =tk.Tk()

fr = open('preklopenie_obrazka.txt','r',encoding='utf-8')


x = fr.readline().strip().split(' ')
print(x)



lists = []
for i in fr.readlines():
    lists.append(i.strip().split(' '))
print(lists)

def matched():
    canvas = tk.Canvas(height=int(x[0]),width=int(x[1]),bg='white')
    canvas.pack()
    x_counter = 0
    y_counter = 0
    for i in lists:
        y_counter += 1
        for j in i:
            x_counter += 1
            if j == '1':
                canvas.create_rectangle(x_counter,y_counter,x_counter+1,y_counter+1,fill='black')
        x_counter = 0

def reversed():
    canvas = tk.Canvas(height=int(x[0]),width=int(x[1]),bg='white')
    canvas.pack()
    x_counter = 0
    y_counter = 0
    for i in lists:
        y_counter += 1
        for j in i[::-1]:
            x_counter += 1
            if j == '1':
                canvas.create_rectangle(x_counter,y_counter,x_counter+1,y_counter+1,fill='black')
        x_counter = 0

matched()
reversed()

win.mainloop()
