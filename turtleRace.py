from turtle import Turtle, Screen
from random import randint

screen = Screen()

#Definição do tamanho da janela 
screen.screensize(500,400)
# Cria um novo input que armazena a cor da tartagura informada pelo usuário
user_aposta = screen.textinput(title="Preparem suas apostas", prompt="Qual tartaruga ganhará a corrida? Escolha a cor: ")
# Lista de cores da tartagura
cores = ["red", "yellow", "orange","green", "blue","purple"]
#Condição da corrida
raceON = False
# Lista para armazernar as tartaturas criadas
all_turtles = list()

def criar_turtles(px=-330, py=0, ncor=0):
    """Função cria um novo objeto tipo turtle.
    
    Retorno: Um objeto turtle atribuindo as seguintes características:
                cor: red
                posição x: -330
                posição y: 0
    """
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(cores[ncor])
    newTurtle.pu()
    newTurtle.goto(x = px, y = py)
    return newTurtle


# cria as tartarugas baseado pelo tamanho da lista de cores
# py = define a posição inicial da tartagura no eixo y. É dada pela expressão: py = i*50 -100
# 
for i in range(len(cores)):
    all_turtles.append(criar_turtles(py=i*50 - 100, ncor = i))
    
#Checa se o usuário realizou a aposta
if user_aposta:
    raceON = True
    
while raceON:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            raceON = False
            turtle_vencedora = turtle.pencolor()
            if turtle_vencedora == user_aposta:
                print(f"Você ganhou!!! Você apostou na tartaruga: {user_aposta}. Tartaruga vencedora: {turtle_vencedora}")
            else:
                print(f"Você Perdeu!!! Você apostou na tartaruga: {user_aposta}. Tartaruga vencedora: {turtle_vencedora}")
        random_distancia = randint(0,10)
        turtle.fd(random_distancia)
    

screen.exitonclick()
