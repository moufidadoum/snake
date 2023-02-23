from turtle import *
import time
import random

#----------------INITIALISATION DES VARIABLES---------------------------------------------------------------#
score=0
execution_delay=0.1
#-----------------------------------------------------------------------------------------------------------#


#----------------CONFIGURATION FENETRE DE JEU---------------------------------------------------------------#
root=Screen()
root.title('Snake Game')
root.setup(width=600,height=600)
root.bgcolor('#FCBD72')
root.bgpic('border.gif')
root.tracer(False)
#-----------------------------------------------------------------------------------------------------------#


#---------------AJOUT DES DIFFERENTE PARTIES DU SERPENT + NOURRITURE----------------------------------------#
root.addshape('haut.gif')
root.addshape('food.gif')
root.addshape('bas.gif')
root.addshape('gauche.gif')
root.addshape('droite.gif')
root.addshape('corp.gif')
#-----------------------------------------------------------------------------------------------------------#


#---------------INITIALISATION TETE DU SERPENT--------------------------------------------------------------#
serpent=Turtle()
serpent.shape('haut.gif')
serpent.penup()
serpent.goto(0,0)
serpent.direction='stop'
#-----------------------------------------------------------------------------------------------------------#


#--------------INITIALISATION DE LA NOURRITURE--------------------------------------------------------------#
nourriture=Turtle()
nourriture.shape('food.gif')
nourriture.penup()
nourriture.goto(0,100)
#-----------------------------------------------------------------------------------------------------------#


#--------------INITIALISATION DU TEXT DE SCORE----------------------------------------------------------------#
text=Turtle()
text.penup()
text.goto(0,268)
text.hideturtle()
text.color('white')
text.write('Score:0',font=('courier',25,'bold'),align='center')
#-----------------------------------------------------------------------------------------------------------#


#--------------INITIALISATION DU MESSAGE DE GAME OVER--------------------------------------------------------#
lost=Turtle()
lost.color('white')
lost.penup()
lost.hideturtle()

#-----------------------------------------------------------------------------------------------------------#


#--------------FONCTION DE DEPLACEMENT DU SERPENT-----------------------------------------------------------#
def deplacements():
    if serpent.direction=='up':
        y=serpent.ycor()
        y=y+20
        serpent.sety(y)

    if serpent.direction=='down':
        y=serpent.ycor()
        y=y-20
        serpent.sety(y)

    if serpent.direction=='right':
        x=serpent.xcor()
        x=x+20
        serpent.setx(x)

    if serpent.direction=='left':
        x=serpent.xcor()
        x=x-20
        serpent.setx(x)

def aller_en_haut():
    if serpent.direction!='down':
        serpent.direction='up'
        serpent.shape('haut.gif')

def aller_en_bas():
    if serpent.direction!='up':
        serpent.direction='down'
        serpent.shape('bas.gif')


def aller_a_gauche():
    if serpent.direction!='right':
        serpent.direction='left'
        serpent.shape('gauche.gif')


def aller_a_droite():
    if serpent.direction!='left':
        serpent.direction='right'
        serpent.shape('droite.gif')

root.listen()

root.onkeypress(aller_en_haut,'Up')
root.onkeypress(aller_en_bas,'Down')
root.onkeypress(aller_a_gauche,'Left')
root.onkeypress(aller_a_droite,'Right')
segments=[]
#-----------------------------------------------------------------------------------------------------------#


while True:
    root.update()

    if serpent.xcor()>260 or serpent.xcor()<-260 or serpent.ycor()>260 or serpent.ycor()<-260:
        lost.goto(0,0)
        lost.write('Game Lost',align='center',font=('courier',34,'bold'))
        time.sleep(1)
        lost.clear()
        time.sleep(1)
        serpent.goto(0,0)
        serpent.direction='stop'
        for bodies in segments:
            bodies.goto(1000,1000)
        score=0
        execution_delay=0.1
        segments.clear()
        text.clear()
        text.write('Score:0',align='center',font=('courier',25,'bold'))




    if serpent.distance(nourriture)<20:
        x=random.randint(-255,255)
        y=random.randint(-255,255)
        nourriture.goto(x,y)
        execution_delay=execution_delay-0.003


        body=Turtle()
        body.penup()
        body.shape('corp.gif')
        segments.append(body)

        score=score+1
        text.clear()
        text.write(f'Score:{score}',font=('courier',25,'bold'),align='center')



    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x=serpent.xcor()
        y=serpent.ycor()
        segments[0].goto(x,y)







    deplacements()

    for bodies in segments:
        if bodies.distance(serpent)<20:
            time.sleep(1)
            serpent.goto(0,0)
            serpent.direction='stop'

            for bodies in segments:
                bodies.goto(1000,1000)

            segments.clear()
            score=0
            execution_delay=0.1
            lost.write('Game Lost', align='center', font=('courier', 34, 'bold'))
            time.sleep(1)
            lost.clear()

            text.clear()
            text.write('Score:0', align='center', font=('courier', 25, 'bold'))

    time.sleep(execution_delay)


