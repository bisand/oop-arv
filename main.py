from crypt import methods
from flask import Flask, redirect, render_template, request
from models.Car import Car
from models.Vehicle import Vehicle

app = Flask("test")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cars", methods=["GET"])
def cars():
    result = []
    for v in Vehicle.vehicles:
        result.append(v.__dict__)
    return result


@app.route("/cars", methods=["POST"])
def new_car():
    make = request.form["make"]
    model = request.form["model"]
    doors = request.form["doors"]

    car = Car(make, model, doors)
    print(car.__dict__)
    return redirect("/cars")


app.run()
