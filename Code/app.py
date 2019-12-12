from flask import Flask, render_template
from sample import *
from markov_chain_one import *
from cleaner import file_cleaner
app = Flask(__name__)

filename = './corpus.txt'
pure_text = file_cleaner(filename)
markov_chain = markov_chain_n_order(4, pure_text)


@app.route('/')
def markov():
    generated_sentence = generate_sentence(markov_chain, 20)
    return render_template('home.html', displayed=generated_sentence)
    # displayed = generated_sentence


if __name__ == '__main__':
    app.run(debug=True)
