from flask import Flask
from flask_restplus import Api
from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4

app = Flask(__name__)
api = Api(app, ui=False, doc="/")

api.add_namespace(task1, "/task1")
api.add_namespace(task2, "/task2")
api.add_namespace(task3, "/task3")
api.add_namespace(task4, "/task4")

if __name__ == "__main__":
    app.run(debug=True)
