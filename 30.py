import tkinter, random
win = tkinter.Tk()


canvas = tkinter.Canvas(width=650, height=200)
canvas.pack()

zapalky = 15
counter = 0
text1 = canvas.create_text(325,20, text=f"taha hrac:{counter%3+1}")
text2 = canvas.create_text(325,40, text=f"pocet zapaliek:{zapalky}")

tags = []
def zapalka(x, y):
    tags.append(canvas.create_line(x, y, x, y+100, width=5, fill='yellow'))
    tags.append(canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown'))

for i in range(15):
    zapalka(i*20+10,100)
print(tags)


def delete1():
    global tags,counter,zapalky
    res = tags[-2:]
    print(res)
    del tags[-2:]
    for i in res:
        canvas.delete(i)
    zapalky -=1
    if zapalky == 0:
        canvas.delete("all")
        canvas.create_text(325,100,text=f'vyhral hrac cislo:{counter%3+1}')
    counter +=1
    canvas.itemconfigure(text1, text=f"taha hrac:{counter%3+1}")
    canvas.itemconfigure(text2, text=f"pocet zapaliek:{zapalky}")

def delete2():
    global tags,counter,zapalky
    res = tags[-4:]
    print(res)
    del tags[-4:]
    for i in res:
        canvas.delete(i)
    zapalky -=2
    if zapalky == 0:
        canvas.delete("all")
        canvas.create_text(325,100,text=f'vyhral hrac cislo:{counter%3+1}')
    counter +=1
    canvas.itemconfigure(text1, text=f"taha hrac:{counter%3+1}")
    canvas.itemconfigure(text2, text=f"pocet zapaliek:{zapalky}")


def delete3():
    global tags,counter,zapalky
    res = tags[-6:]
    print(res)
    del tags[-6:]
    for i in res:
        canvas.delete(i)
    zapalky -=3
    if zapalky == 0:
        canvas.delete("all")
        canvas.create_text(325,100,text=f'vyhral hrac cislo:{counter%3+1}')
    counter +=1
    canvas.itemconfigure(text1, text=f"taha hrac:{counter%3+1}")
    canvas.itemconfigure(text2, text=f"pocet zapaliek:{zapalky}")

win.bind("1", lambda event: delete1())
win.bind("2", lambda event: delete2())
win.bind("3", lambda event: delete3())

win.mainloop()
