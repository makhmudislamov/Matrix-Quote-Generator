from cleaner import file_cleaner

class Histogram(object):
    
    def __init__(self):
        pass

    def histogram(self, source_text):
        """
        Takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) 
        and return a histogram
        data structure that stores each unique word along with 
        the number of times the word appears in the source text.
        """
        file = "./sample_words.txt"
        cleaned_text = file_cleaner(file)
        

    def unique_words(self, histogram):
        """
        Takes a histogram argument and returns the total count of unique words in the histogram.
        """
        pass

    def frequency(self, word, histogram):
        """
        Takes a word and histogram argument and returns the number of times that word appears in a text
        """
        pass
