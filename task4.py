from flask import request
from flask_restplus import Namespace, Resource, fields
from tasks import Tasks4

task4 = Namespace("Problem 4", description="""Parenthesis valid combination""")


problem_4 = task4.model('Problem 4 input validator',
                        {
                          "num_of_pairs": fields.Integer(description="Number of pair of parenthesis",
                                                         required=True,
                                                         example=3)
                        })


@task4.route("/")
class ParaCombination(Resource):
    @task4.expect(problem_4, validate=True)
    def post(self):
        """

        :return:
        """
        data = request.json
        response = dict()
        n = data["num_of_pairs"]
        str_in = [" "] * 2 * n
        task = Tasks4()
        task.parenthesis(in_str=str_in,
                         n=n)
        response["pairs"] = task.out
        response["count"] = len(task.out)
        return response
