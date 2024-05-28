from flask import Flask, redirect, render_template, request
from models.Car import Car

app = Flask("test")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cars")
def cars():
    return Car.get_available_cars()


app.run()
