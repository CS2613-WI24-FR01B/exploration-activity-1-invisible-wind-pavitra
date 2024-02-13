# Exploratory Activity 1

## Section 1: Which package/library did you select?
   The package/library selected is Turtle within Python.
## Section 2:  What is the package/library?
   The Turtle package "provides a representation of a physics 'turtle' (a little robot with a pen) that draws on a sheet of paper on the floor[1]". The package "was originally created as an educational tool, to be used by teachers in the classroom [1]". Turtle package is an "effective[1]" and "well-proven way for learners to encounder programming concepts and interaction with software" because "it provides instant, visible feedback [1]". In turtle, the "onscreen pen that you use for drawing is called the turtle[2]". 
   
   To use turtle, it is crucial to use "version 3 of Python[2]". It is also significant to be "familiar with your programming environment[2]" and it depends on the user to "use applications like IDLE or Jupyter Notebook to program with turtle[2]" or probably use "REPL[2]". To use turtle, is is important to remember that turtle is a "built-in library, so you don't need to install any new packages[2]". The first step to use turtle would be to "import it into your Python environment[2]". To use Turtle, it is important to start by making a "separate window (called the screen) to carryout each drawing command[2]". This can be done using `s = turtle.getscreen()`[2]". It is worth noticing that "you now have your screen and your turtle[2]". This is where the "screen acts as a canvas, while the turtle acts like a pen[2]". Some important characteristics about turtle are that "the turtle has certain changeable characteristics, like size, color, and speed[2]". Moreover, the turtle "always points in a specific direction, and will move in that direction unless you tell it otherwise[2]".  Overall, there are "4 basic steps[3]" to use turtle [3]. The first step is to "import turtle module [3]", which can be done using `from turtle import *`[3] or `import turtle` [3]. The second step is to "create a screen and turtle object [3]", which can be done using `scr = turtle.Screen()` [3] and `tur = turtle.Turtle()` [3]. The third step to use turtle is to use the "commands to draw the required shape [3]", which can be done using `tur.forward(200)` [3]. The fourth step to use turtle is to "display", which can be done using `turtle.done()` [3].  

## Section 3: What are the functionalities of the package/library?
There are different functions that turtle offers some of which include `forward()`, `left()`, `home()`, `pos()`, `clearscreen()`, `color()`, `fillcolor()`, `begin_fill()`, `goto()`, `setheading()` and many more [1]. 
For example, the code below creates a square in the for loop and uses `goto()` to go to a different location on the screen and create a new square.
```
import turtle
turtle = turtle.Turtle()

for i in range(0, 4):
	turtle.right(90)
	turtle.forward(100)

turtle.penup()
turtle.goto(200, 200)

turtle.pendown()
for i in range(0, 4):
	turtle.right(90)
	turtle.forward(100)

a = input(" ")
```


<img width="500" alt="image" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-invisible-wind-pavitra/assets/113079611/5d14ee82-a369-4c03-8760-7073efa50105">


## Section 4: When was it created?

## Section 5: Why did you select this package/library?

## Section 6: How did learning the package/library influence your learning of the language?

## Section 7: How was your overall experience with the package/library?






References:

[1] https://docs.python.org/3/library/turtle.html 

[2] https://realpython.com/beginners-guide-python-turtle/ 

[3] https://www.boardinfinity.com/blog/turtle-in-python/





















   
