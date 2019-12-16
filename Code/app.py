from flask import Flask, render_template, url_for, redirect, request
from sample import *
from markov_chain_one import *
from cleaner import file_cleaner
from autocomplete import *

app = Flask(__name__)

vocabulary = get_lines('./corpus.txt')
structure = autocomplete_setup(vocabulary)

@app.route('/', methods=['POST', 'GET'])
def get_prefix():
    """
    should take prefix input
    then it should redirect to /words route
    """  
    return render_template('home.html')


@app.route('/words', methods=['POST', 'GET'])
def autocompleted_words():
    """
    Show all autocompleted words to choose from for loop should be here 
    also here we should have a form to POST chosen words then it should redirect to /quote
    """
    # getting user input = prefix
    if request.method == 'POST':
        prefix = request.form['prefix']
        # pasting prefix to autocomplete()
        words_to_choose = autocomplete(prefix, structure)
        print("generated words", words_to_choose)

    return render_template('retrieved.html', words=words_to_choose)

@app.route('/quote', methods=['POST', 'GET'])
def quote():
    """
    Show generated sentence
    """
    filename = './corpus.txt'
    pure_text = file_cleaner(filename)
    markov_chain = markov_chain_n_order(4, pure_text)
    if request.method == 'POST':
        word = request.form['chosen_word']
        generated_sentence = generate_sentence(markov_chain, 20, word)
    return render_template('sentence.html', displayed=generated_sentence)


if __name__ == '__main__':
    app.run(debug=True)
