from flask import Flask, render_template, url_for, redirect, request
from sample import *
from markov_chain_one import *
from cleaner import file_cleaner
from autocomplete import *

app = Flask(__name__)

filename = './corpus.txt'
pure_text = file_cleaner(filename)
markov_chain = markov_chain_n_order(4, pure_text)


@app.route('/', methods=['POST', 'GET'])
def markov():
    vocabulary = get_lines('./corpus.txt')
    structure = autocomplete_setup(vocabulary)
    # getting user input = prefix
    if request.method == 'POST':
        prefix = request.form['prefix']
        # pasting prefix to autocomplete()
        words_to_choose = autocomplete(prefix, structure)
        print(words_to_choose)
    generated_sentence = generate_sentence(markov_chain, 20)
    return render_template('home.html', displayed=generated_sentence)



if __name__ == '__main__':
    app.run(debug=True)
