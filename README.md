Spirograph Drawing with Turtle Module


This Python project utilizes the Turtle graphics module to create spirograph patterns. Spirographs are geometric drawings composed of curves, typically generated through a combination of circles and rotations.

Features


Draws a spirograph using the Turtle module.
Randomly selects colors from a predefined list.
Adjustable parameters for radius and angle to customize the spirograph.
Installation
To run this project, ensure you have Python installed on your system. The Turtle module is part of the standard library and does not require additional installation.

Usage


Clone the repository:

bash
Copy code
git clone <your-repo-url>
cd <your-repo-directory>
Run the Python script:

bash
Copy code
python spirograph.py
The script will open a Turtle graphics window and draw a spirograph pattern based on the specified parameters.

Code Explanation



python
Copy code
from turtle import Turtle, Screen
import random

halo = Turtle()
halo.speed("fast")
colours = ["green", "red", "blue", "purple", "brown"]

def draw_spirograph(radius, angle):
    for _ in range(int(360 / angle)):
        halo.color(random.choice(colours))
        halo.circle(radius)
        halo.left(angle)

draw_spirograph(100, 10)

screen = Screen()
screen.exitonclick()



Contributing


Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or pull request in the repository.
