import time
from directKeys import click
from PIL import ImageGrab
import keyboard
import numpy as np

middle = (1030, 615)
gray = (14, 16, 24)

next_counter = 0
prev_counter = 0

next_planet = [1204, 920]
prev_planet = [890, 920]

upgrade_box = [600, 400, 601, 990]
      
def main():
    
    start_loop = time.time()
    
    img = np.array(ImageGrab.grab(bbox=upgrade_box))

    global next_counter, prev_counter
    
    if prev_counter > 6:
        click(*prev_planet)
        click(*prev_planet)
        click(*prev_planet)
        prev_counter = 0
    elif next_counter > 10**6:
        click(*next_planet)
        next_counter = 0
        prev_counter += 1
    
    
    else:
        for y in range(0, len(img), 10):
            for x in range(len(img[y])):
                
                if img[y][x][0] == 14:
                    actual_x = x + upgrade_box[0]
                    actual_y = y + upgrade_box[1]
                    click(actual_x, actual_y)

                else:
                    click(*middle)
                    next_counter += 1
                             
    end_loop = time.time()
    
    print(f"loop time: {end_loop - start_loop}", end='||', flush=True)

while True:
    if keyboard.is_pressed('q'):
        break
    main()   
    print(next_counter, end= "\r", flush=True)