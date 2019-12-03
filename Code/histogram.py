from cleaner import file_cleaner

class Histogram(object):
    
    def __init__(self):
        
        self.histogram = {}

    def build(self, file):
        """
        Takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) 
        and return a histogram
        data structure that stores each unique word along with 
        the number of times the word appears in the source text.
        """
        # cleaning the file and working with pure text 
        cleaned_text = file_cleaner(file)
        print(cleaned_text)
        for word in cleaned_text:
            # checking if the word is not in the dict
            if word not in self.histogram.keys():
                self.histogram[word] = 1
            else:
                self.histogram[word] += 1
        # print(self.histogram)
        return self.histogram



    def unique_words(self, histogram):
        """
        Takes a histogram argument and returns the total count of unique words in the histogram.
        """
        unique_word_count = 0

        for word, _ in histogram.items():
            unique_word_count += 1
        
        return unique_word_count

    def frequency(self, word):
        """
        Takes a word and histogram argument and returns the number of times that word appears in a text
        """
        return self.histogram.get(word)
        

            


if __name__ == '__main__':
    file = "./sample_words.txt"
    histogram = Histogram()
    histogram.build(file)
    print(histogram.frequency('fiLOLO'))
