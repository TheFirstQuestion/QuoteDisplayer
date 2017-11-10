from random import randint
import flask
app = flask.Flask(__name__)

# The file to read quotes from
myFile = "quotes.txt"

# Availiable background colors
colors = ["#0E7C7B", "#17BEBB", "#D62246", "#4B1D3F", "#2F1847", "#624763", "#540804", "#C75146", "#C75146"]

# Get the file contents
textFile = open(myFile, "r")
lines = textFile.read().splitlines()
fileLength = len(lines)

# To not repeat
quoteTimes = [0] * fileLength
lowestCount = 0

def getQuote():
    global lowestCount
    myNumber = randint(0, fileLength - 1)

    i = 0
    # Search for a quote that's been displayed least often
    while quoteTimes[myNumber] is not lowestCount:
        myNumber = randint(0, fileLength - 1)
        i = i + 1
        # If all the quotes have been displayed equally often, display any of them
        if i == fileLength:
            lowestCount = lowestCount + 1
    # Keep track of how many times this quote has been displayed
    quoteTimes[myNumber] = quoteTimes[myNumber] + 1
    return lines[myNumber]



def getColor():
    myNumber = randint(0, len(colors) - 1)
    return colors[myNumber]




@app.route("/", methods=['POST', 'GET'])
def main():
    return flask.render_template('index.html', quote=getQuote(), color=getColor())



if __name__ == "__main__":
    app.run(host="0.0.0.0")
