#Make a simple server application using Python. Use the socket library or flask. All the server has is a dictionary which contains a toy and the quantity of that toy. The client should be able to use a GET request to the server to see how many characters it has.
from flask import *
app = Flask(__name__)
#sample server client name 
@app.route('/', methods = ['POST', 'GET'])
def data():
    while True:
        charlist = {'Ganondorf': 1, 'Falco': 2, 'Bowser': 3}
        for i in range(len(charlist)):
            charlist[i] = charlist[i].lower()
        charname = charlist.get('name')
        charnumber = charlist.get('number')
        if request.method == 'GET':
            return print("These are the characters"), charlist
        if request.method == 'POST':
            # input = d.receive()
            # input = input.lower()
            if charlist in charlist(charname, charnumber):
                result = {key: value for key, value in charlist.items}
        print(result + "is in the list")
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')