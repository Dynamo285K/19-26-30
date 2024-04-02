import tkinter as tk
import random
win = tk.Tk()

HEIGHT = 250
WIDTH = 250

canvas = tk.Canvas(height=HEIGHT,width=WIDTH,bg= 'skyblue')
canvas.pack()

def draw():
    colors = ['green','green1','green2','green3','green4']
    rand_color = random.choice(colors)
    udolie_ci_vrch = random.choice([1,2])
    random_x = random.randint(0,WIDTH)
    random_y = random.randint(0,HEIGHT)
    print(random_x,random_y)
    if udolie_ci_vrch == 1:
        temp = random.randint(random_y,HEIGHT)
        list_of_points = [[0,HEIGHT]]
        for i in range(0,random_x,10):
            point_y = random.randint(temp-10,temp)
            list_of_points.append([i,point_y])
            temp = point_y
        print(list_of_points)
        temp1 = random_y
        list_of_points.append([random_x,random_y])
        for i in range(random_x,WIDTH+1,10):
            point_y = random.randint(temp1, min(temp1 + 10, HEIGHT))
            list_of_points.append([i,point_y])
            temp1 = point_y
        list_of_points.append([WIDTH,point_y])
        list_of_points.append([WIDTH,HEIGHT])
        print(list_of_points)
        canvas.create_polygon(list_of_points,outline='black', fill=rand_color)
    else:
        list_of_points = [[0,HEIGHT]]
        temp = random.randint(0,random_y)
        for i in range(0,random_x,10):
            point_y = random.randint(temp, min(temp + 10, random_y))
            list_of_points.append([i,point_y])
            temp = point_y
        print(list_of_points)
        temp1 = random_y
        list_of_points.append([random_x,random_y])
        for i in range(random_x,WIDTH+1,10):
            point_y = random.randint(max(temp1 - 10, 0),temp1)
            list_of_points.append([i,point_y])
            temp1 = point_y
        list_of_points.append([WIDTH,point_y])
        list_of_points.append([WIDTH,HEIGHT])
        print(list_of_points)
        canvas.create_polygon(list_of_points, outline='black', fill=rand_color)


win.bind("<space>", lambda event: draw())  # Bind space key to generate a new landscape


draw()

win.mainloop()
