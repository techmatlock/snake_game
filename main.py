from turtle import Screen, Turtle
import turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

turtle_object = Turtle()
turtle_object.shape("square")
turtle_object.fillcolor("white")

screen.exitonclick()