import turtle
import time
from datetime import datetime
import random

def display_text(text1, color1, text2, color2):
    turtle.clear()
    
    turtle.penup()
    turtle.goto(0, 50)
    
    turtle.color(color1)
    turtle.write(text1, align="center", font=("Times New Roman", 24, "bold"))
    
    turtle.color(color2)
    turtle.goto(0, -50)
    turtle.write(text2, align="center", font=("Times New Roman", 24, "bold"))
    
    turtle.update()

def window():
    # Set up the turtle screen
    turtle.bgcolor("lightblue")
    turtle.tracer(0)  # Turn off automatic screen updates
    turtle.hideturtle()

    # Set a shorter delay for faster updates
    turtle.delay(0)

def main():
    while True:
        current_datetime = datetime.now()

        date = str(current_datetime.date())
        time_str = current_datetime.strftime("%H:%M:%S")
        
        text_1 = f"{{Current Date and Time}}:"
        text_2 = f"({date})<>({time_str})"
        
        display_text(text_1, 'black', text_2, 'purple')
        
        if turtle.window_width() // 2 <= 0 or turtle.window_height() // 2 <= 0:
            break  # Exit the loop if the turtle window is closed

        time.sleep(1)  # Add a small delay to control the speed of the animation

    turtle.done()

if __name__ == "__main__":
    window()
    main()
