from flask import Flask
from sample import *
from markov_chain_one import *
app = Flask(__name__)


@app.route('/')
def markov():    
    final = generate_sentence(20)
    return final


if __name__ == '__main__':
    app.run(debug=True)