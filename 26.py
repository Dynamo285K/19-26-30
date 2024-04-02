import tkinter as tk
import random
win = tk.Tk()

HEIGHT = 500
WIDTH = 500

canvas = tk.Canvas(height=HEIGHT,width=WIDTH,bg= 'skyblue')
canvas.pack()

def draw():
    colors = ['green','green1','green2','green3','green4']
    rand_color = random.choice(colors)
    udolie_ci_vrch = random.choice([1,2])
    random_x = random.randint(0,WIDTH)
    random_y = random.randint(0,HEIGHT)
    print(random_x,random_y)
    list_of_points = [[0,HEIGHT]]
    if udolie_ci_vrch == 1:
        temp = random.randint(200,400)
        for i in range(0,random_x,10):
            point_y = random.randint(temp-5,temp)
            list_of_points.append([i,point_y])
            temp = point_y
        peak = list_of_points[-1]
        temp1 = random.randint(peak[1],peak[1]+5)
        for i in range(random_x,WIDTH+1,10):
            point_y = random.randint(temp1,min(temp1 + 5, HEIGHT))
            list_of_points.append([i,point_y])
            temp1 = point_y
        list_of_points.append([WIDTH,point_y])
        list_of_points.append([WIDTH,HEIGHT])
        print(list_of_points)
        canvas.create_polygon(list_of_points, outline='black', fill=rand_color)
    else:
        temp = random.randint(200,300)
        for i in range(0,random_x,10):
            point_y = random.randint(temp,temp+5)
            list_of_points.append([i,point_y])
            temp = point_y
        peak = list_of_points[-1]
        temp1 = random.randint(peak[1] - 5,peak[1])
        for i in range(random_x,WIDTH+1,10):
            point_y = random.randint( temp1 - 5, temp1)
            list_of_points.append([i,point_y])
            temp1 = point_y
        list_of_points.append([WIDTH,point_y])
        list_of_points.append([WIDTH,HEIGHT])
        print(list_of_points)
        canvas.create_polygon(list_of_points, outline='black', fill=rand_color)

win.bind("<space>", lambda event: draw())  # Bind space key to generate a new landscape

draw()
win.mainloop()
