import pyautogui
import time
import random
import math

def get_mouse_position():
      print('Please move your mouse to the center of the HK coin and press enter')
      input()
      x, y = pyautogui.position()
      print(f'X => {x}, Y=>{y}')

      return x, y

def auto_click(x, y, radius = 300, wait_per_click_min=0.1, wait_per_click_max=0.2, click_number_min=100, click_number_max=1000, min_interval=10, max_interval=15):

      while True:
            click_number = random.randint(click_number_min, click_number_max)
            for i in range(click_number):
                  angle = random.uniform(0, 2*math.pi)
                  random_radius = radius * random.uniform(0, 1)
                  offset_x = random_radius * math.cos(angle)
                  offset_y = random_radius * math.sin(angle)
                  print(f"clicked for the {i+1} time")
                  pyautogui.click(x+offset_x, y+offset_y)

                  wait_per_click = random.uniform(wait_per_click_min, wait_per_click_max)
                  time.sleep(wait_per_click)

            interval = random.uniform(min_interval, max_interval)
            print(f'Wait for {interval} seconds before clicking again')
            time.sleep(interval)



if __name__ == "__main__":
      x, y = get_mouse_position()
      auto_click(x, y)