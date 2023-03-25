"""Tic Tac Toe
<<<<<<< HEAD
Exercises
=======

Exercises

>>>>>>> Modificacion
1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
  """Draw tic-tac-toe grid. TABLA"""
  line(-67, 200, -67, -200)
  line(67, 200, 67, -200)
  line(-200, -67, 200, -67)
  line(-200, 67, 200, 67)


def drawx(x, y):
  """Draw X player."""
  color('Blue')
  line(x + 40, y + 45, x + 100, y + 100)
  line(x + 40, y + 100, x + 100, y + 45)


def drawo(x, y):
  """Draw O player."""
  up()
  goto(x + 65, y + 45)
  down()
  color('Red')
  circle(25)


def floor(value):
  """Round value down to grid with square size 133."""
  return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
<<<<<<< HEAD
players = [drawo, drawx]
=======
players = [drawx, drawo]
>>>>>>> Modificacion


def tap(x, y):
  """Draw X or O in tapped square."""
  x = floor(x)
  y = floor(y)
  player = state['player']
<<<<<<< HEAD
  draw = players[player] 
  draw(x, y)
  update()
  if (x > 1):
    draw(x,y) 
    draw = players[player]
  else:
    state['player'] = not player
=======
  draw = players[player]
  draw(x, y)
  update()
  state['player'] = not player
>>>>>>> Modificacion


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
<<<<<<< HEAD
done()
=======
done()
>>>>>>> Modificacion
