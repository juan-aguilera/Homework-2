import sys
import execution_time_algorithm
import algorithms
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt

def plot_execution_time():
    size = []
    time_1 = []
    time_2 = []
    time_3 = []
    table = execution_time_algorithm.take_execution_time(10000,100000,10000,3)
    for row in table:
        size.append(row[0])
        time_1.append(row[1])
        time_2.append(row[1])
        time_3.append(row[2])
        #print(row)
  
    time_1_x = [x for x in size]
    fig, ax = plt.subplots()
    ax.plot(size, time_2, mfc = 'black', marker = '.', ms = 12, color= 'blue', label='Binary Algorithm',linestyle= '--')  
    ax.plot(size, time_3, mfc = 'black', marker = '.', ms = 12, color= 'orange', label='Ternary Algorithm',linestyle= '--')
    ax.plot(size, time_1, mfc = 'black', marker = '.', ms = 12, color= 'yellow', label='Linear Algorithm',linestyle= '--')
    #plt.show()

    return fig


"""     width = 600
    heigth = 600
    GREY = (230,230,230)
    BACKGROUND = (255,255,255)

    row_container_1 = pg.sprite.Group()
    row_container_2 = pg.sprite.Group()
    row_container_3 = pg.sprite.Group()

    screen = pg.display.set_mode([width,heigth])
    table = execution_time_algorithm.take_execution_time(10000,100000,10000,25)
    for row in table:
        row_container_1.add(row[1])
        row_container_2.add(row[2])
        row_container_3.add(row[3])
                

    pg.init()
    chart = pg.Surface((width//4, heigth//4))
    chart.fill(GREY)
    chart.set_alpha(230)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    screen.fill(BACKGROUND)

    chart_heigth = chart.get_height()
    chart_width = chart.get_width()



    pg.quit()
 """