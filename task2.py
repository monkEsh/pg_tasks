from flask import request
from flask_restplus import Namespace, Resource, fields
from tasks import format_string


task2 = Namespace("Problem 2", description="""Line Justification""")

problem_2 = task2.model('Problem 2 input validator',
                        {
                            "size_of_line": fields.Integer(description="max number of characters in line",
                                                           required=True,
                                                           example=16),
                            "words": fields.String(description="string with n words",
                                                   required=True,
                                                   example="This is an example of text justification.",
                                                   max_length=1000)
                        })


@task2.route("/")
class StringCreator(Resource):
    @task2.expect(problem_2)
    def post(self):
        """

        :return:
        """
        data = request.json
        response = dict()
        out = format_string(line=data["words"].split(),
                            line_len=data["size_of_line"])
        response["formatted_string"] = out
        return response
