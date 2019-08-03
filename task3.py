from flask import request
from flask_restplus import Namespace, Resource, fields
from tasks import Tasks3


task3 = Namespace("Problem 3", description="""11 left 00 right""")

problem_3 = task3.model('Problem 3 input validator',
                        {
                          "input_number": fields.String(description="String with 0 and 1",
                                                        required=True,
                                                        example="110101011")
                        })


@task3.route("/")
class OneOneZeroZero(Resource):
    @task3.expect(problem_3)
    def post(self):
        """

        :return:
        """
        data = request.json
        response = dict()

        number_list = [int(x) for x in data["input_number"]]
        task = Tasks3(num_array=number_list)
        response["sorting_0_1"] = task.count_0_1
        response["sorting_1_0"] = task.count_1_0
        return response
