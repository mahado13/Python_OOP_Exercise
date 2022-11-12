"""Word Finder: finds random words from a dictionary."""
'''
Author: Mahad Osman
Date: Nov 12
Exercise: Python OOP Exercise.
'''
import random

class WordFinder:
    """Used to generate random words from a file.
    Attributes:
    -----------------------
    path: is the file read in from.
    """
    def __init__(self, path):
        ''' Constructor that will open our file. Self.words is set using our function.'''
        file = open(path)
        self.words = self.get_word(file)
        print(f"{len(self.words)} words read")
        
    def get_word(self, file):
        ''' Method to parse out the words in the file and remove the spaces. Returns a list.'''
        newWord = []
        for word in file:
            newWord.append(word.strip())
        
        return newWord

    def rand_word(self):
        ''' Returns a random word of our list using random.choice form the random module.'''
        return (random.choice(self.words))
        
