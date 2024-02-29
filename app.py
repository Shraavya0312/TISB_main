from flask import Flask, flash, redirect, render_template, request
from cs50 import SQL

app = Flask(__name__)

# db = SQL("sqlite:///asl.db")

@app.route("/")
def index():
    return render_template("index.html")