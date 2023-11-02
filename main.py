import turtle
import random


s = turtle.Screen()
s.title("Space Attack")
s.setup(width=800, height=600)
s.tracer(0)
turtle.addshape("1 copy.gif")
turtle.addshape("enemy.gif")
turtle.addshape("player2.gif")
s.bgpic("main screen.gif")

#Text turtle
board = turtle.Turtle()
board.hideturtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.goto(0,240)
score = 0

def set_player2():
  def go_d():
    player2.setheading(0)
    player2.forward(25)
    global score
    score +=1
    board.clear()
    board.goto(0,240)
    board.write("Score:{}".format(score),align="center",font=("Courier",20,"normal"))
    
  def go_a():
    player2.setheading(180)
    player2.forward(25)
    global score
    score +=1
    board.clear()
    board.goto(0,240)
    board.write("Score:{}".format(score),align="center",font=("Courier",20,"normal"))
    
  def go_right():
    player.setheading(0)
    player.forward(25)
    global score
    score +=1
    board.clear()
    board.goto(0,240)
    board.write("Score:{}".format(score),align="center",font=("Courier",20,"normal"))
    
  def go_left():
    player.setheading(180)
    player.forward(25)
    global score
    score +=1
    board.clear()
    board.goto(0,240)
    board.write("Score:{}".format(score),align="center",font=("Courier",20,"normal"))
  
  #Add player
  player = turtle.Turtle()
  player.speed(0)
  player.shape("1 copy.gif")
  player.color("white")
  player.penup()
  player.goto(0,-250)
  player.direction = "stop"
  
  #Add player
  player2 = turtle.Turtle()
  player2.speed(0)
  player2.shape("player2.gif")
  player2.color("white")
  player2.penup()
  player2.goto(0,-150)
  player2.direction = "stop"
  
  #Create more enemy
  enemies = []

  #Add enemy
  
  for x in range(3):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("enemy.gif")
    enemy.color("white")
    enemy.penup()
    enemy.goto(100,250)
    enemy.speed = (random.randint(1,4))
    enemies.append(enemy)

  s.listen()
  s.onkeypress(go_a, "a")
  s.onkeypress(go_d, "d")
  s.onkeypress(go_left, "Left")
  s.onkeypress(go_right, "Right")

  #Main game
  game = True
  while True:
    s.update()
  #Moving Enemy
    for enemy in enemies:
      y = enemy.ycor()
      y -= enemy.speed
      enemy.sety(y)
    
  #Check if off the screen
      if y < -300:
        x = random.randint(-380,380)
        y = random.randint(300,400)
        enemy.goto(x,y)
      if score == 5 or score == 10 or score == 20 or score == 40 or score == 80:
        s.bgpic("level up.gif")
        s.update()
        s.bgpic("space.gif")  
      if score == 100:
        s.bgpic("win screen.gif")
        game = False
        break
    #Check for collision with player
      if enemy.distance(player2) < 80 or enemy.distance(player) < 80 :
        enemy.goto(x,y)
        s.clearscreen()
        s.bgpic("game over.gif")
        game = False
        break
    s.update()
    if game == False:
      # s.ontimer(s.bgpic("game over.gif"), 2000)
      break
    

def set_player():
  def go_right():
    player.setheading(0)
    player.forward(25)
    global score
    score +=1
    board.clear()
    board.goto(0,240)
    board.write("Score:{}".format(score),align="center",font=("Courier",20,"normal"))
    
  def go_left():
    player.setheading(180)
    player.forward(25)
    global score
    score +=1
    board.clear()
    board.goto(0,240)
    board.write("Score:{}".format(score),align="center",font=("Courier",20,"normal"))

  #Add player

  player = turtle.Turtle()
  player.speed(0)
  player.shape("1 copy.gif")
  player.color("white")
  player.penup()
  player.goto(0,-250)
  player.direction = "stop"
  
  #Create more enemy
  enemies = []

  #Add enemy
  
  for x in range(3):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("enemy.gif")
    enemy.color("white")
    enemy.penup()
    enemy.goto(100,250)
    enemy.speed = (random.randint(1,4))
    enemies.append(enemy)

  s.listen()
  s.onkeypress(go_left, "Left")
  s.onkeypress(go_right, "Right")

  #Main game
  game = True
  while True:
    s.update()
  #Moving Enemy
    for enemy in enemies:
      y = enemy.ycor()
      y -= enemy.speed
      enemy.sety(y)
    
  #Check if off the screen
      if y < -300:
        x = random.randint(-380,380)
        y = random.randint(300,400)
        enemy.goto(x,y)
      if score == 5 or score == 10 or score == 20 or score == 40 or score == 80:
        s.bgpic("level up.gif")
        s.update()
        s.bgpic("space.gif")
      if score == 100:
        s.bgpic("win screen.gif")
        game = False
        break  
    #Check for collision with player
      if enemy.distance(player) < 80:
        enemy.goto(x,y)
        s.clearscreen()
        s.bgpic("game over.gif")
        game = False
        break
    s.update()
    if game == False:
      # s.ontimer(s.bgpic("game over.gif"), 2000)
      break;
def start_game1():
  s.bgpic("space.gif")
  board.clear()
  set_player()

def start_game2():
  s.bgpic("space.gif")
  board.clear()
  set_player2()
def single_player():
  s.bgpic("single player.gif")
  board.goto(0,-240)
  board.write("Press x to continue ",align="center",font=("Courier",30,"normal"))
  s.listen()
  s.onkeypress(start_game1,"x")

def multi_player():
  s.bgpic("multiplayer.gif")
  board.goto(0,-240)
  board.write("Press x to continue ",align="center",font=("Courier",30,"normal"))
  s.listen()
  s.onkeypress(start_game2,"x")

#Set Screen


#Keyboard
  
s.listen()
s.onkeypress(single_player,"w") 
s.onkeypress(multi_player,"s")

s.mainloop