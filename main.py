import json
import parser
from random import randint

from flask import Flask
from flask_restful import Api, Resource, reqparse


def making_json_map():
    a = randint(8, 12)
    arr = [[randint(0, 9) for j in range(a)] for i in range(a)]
    j = json.dumps(arr)
    return j

def map_checking(map, line, col):
    for i in range(len(map)):
        if map[0][i] == -1 or map[len(map)-1][i] == -1\
                or map[i][0] == -1 or map[i][len(map)-1] ==-1:
            return False
    neighbours = [(line + a[0], col + a[1]) for a in [(-1, 0), (1, 0), (0, -1), (0, 1)] if (0 <= line + a[0] <= len(map)-1) and (0 <= col + a[1] <= len(map)-1)]
    for e in neighbours:
        if map[e[0]][e[1]] == -1:
            return False
    return True

my_list = [
    {
        "map": making_json_map(),
        "line": 0,
        "column": 0,
        "player1": 0,
        "player2": 0
    }
]

class Resource(Resource):
    def get(self):
        if (map_checking(json.loads(my_list[0]["map"]),my_list[0]["line"], my_list[0]["column"])):
            return my_list[0]
        else:
            pl1 = my_list[0]["player1"]
            pl2 = my_list[0]["player2"]
            if pl1 > pl2:
                return f"Игра окончена! Игрок 1 победил. Итоговый счет: {pl1}, {pl2}."
            elif pl1<pl2:
                return f"Игра окончена! Игрок 2 победил. Итоговый счет: {pl1}, {pl2}."
            else:
                return f"Игра окончена! Ничья."

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("map")
        parser.add_argument("line")
        parser.add_argument("column")
        parser.add_argument("player1")
        parser.add_argument("player2")
        params = parser.parse_args()
        my_list[0]["map"] = params["map"]
        my_list[0]["line"] = params["line"]
        my_list[0]["column"] = params["column"]
        my_list[0]["player1"] = my_list[0]["player1"] + int(params["player1"])
        my_list[0]["player2"] = my_list[0]["player2"] + int(params["player2"])

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Resource, "/game")
    app.run(debug=True)