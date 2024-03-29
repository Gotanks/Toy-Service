# DONE Make a simple server application using Python. Use the socket library or flask. All the server has is a dictionary which contains a toy and the quantity of that toy. The client should be able to use a GET request to the server to see how many characters it has.
# DONE Make get request for client to query through ex: if user types in value in the url, the server returns key
# DONE Read up on JSON for more information on how the JSON, ONLY TWO LINES NEED TO BE MODIFIED
from ast import Or
from flask import *
app = Flask(__name__)
charlist = {
    "Bowser": 64,
    "Ganondorf": 3,
    "Falco": 10,
    "Lucario": 3,
    "Ike": 1,
    "Cloud": 1,
    "Ridley": 5,
    "Kazuya": 2
}
#TODO return a json of characters when returning name and quantity as the fields, if the key does not exist, then return saying item doesn't exist
@app.route('/character/<char>', methods = ['GET'])
def checkseries(char):
    for key, value in charlist.items():
        if key.lower() == char.lower():
            return json.dumps({
                "name" : key,
                "quantity" : value
            })
    return json.dumps({
        "error" : "character not found"
    })
@app.route('/order', methods = ['POST'])
def makeorder():
    user_order = request.form.get("character")
    order_quantity = request.form.get("quantity")
    for key, values in charlist.items():
        if  user_order.lower() == key.lower():
            if charlist[key] - int(order_quantity) >= 0:
                final_order = charlist[key] - int(order_quantity)
                charlist[key] = final_order
                break
            elif charlist[key] - int(order_quantity) < 0:
                return "Order cannot be made, not enough "
    return "Thank you for ordering " + user_order.title() + ". There's now only " + str(final_order) + " Stock remaining!"
    #  return "How did you get here?"
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')