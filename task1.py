from flask import request
from flask_restplus import Namespace, Resource, fields
from tasks import Task1

task1 = Namespace("Problem 1", description="""Rotate Add task""")

problem_1 = task1.model('Problem 1 input validator',
                        {
                            "input_int": fields.Integer(description="Input string consists of number from 0 to 1",
                                                        example=12312322,
                                                        required=True),
                            "rotate": fields.Integer(description="Number of Rotations",
                                                     example=1,
                                                     required=True),
                            "add": fields.Integer(description="Number of Rotations",
                                                  example=1,
                                                  required=True)
                        })


@task1.route("/")
class StringRotateAdd(Resource):
    @task1.expect(problem_1)
    def post(self):
        """

        :return:
        """
        data = request.json
        response = dict()
        input_int = str(data["input_int"])
        num_arr = [int(x) for x in input_int]

        task = Task1(rotation=data["rotate"],
                     addition=data["add"],
                     num_arr=num_arr)
        """
        1. rotating number
        """
        task.rotate()
        """
        2. add to odd place
        """
        out = task.add_at_odd()
        response["output"] = ''.join(str(v) for v in out)

        return response
