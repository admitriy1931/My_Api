import requests
def printl():
    r = requests.get('http://127.0.0.1:5000/game')
    print(r.json())
    #requests.put("http://127.0.0.1:5000/game", json={"map": "1", "line": 1, "column": 1, "player1": 1, "player2": 2})
    # print(rr.json())

if __name__ == '__main__':
    printl()