import random
'''
Author: Mahad Osman
Date: Nov 12
Exercise: Python OOP Exercise.
'''
from wordfinder import WordFinder

class specialWordFinder(WordFinder):
    ''' A specialized subclass to take into account empty lines & comments
        Our wordFinder classes handles most of the work for us.
    '''
    
    def get_word(self, file):
        ''' Updating the get_word function to now filter out comments and empty words. '''
        newWord = []
        for word in file:
            if (word[0] != "#" and word.strip()):
                newWord.append(word.strip())
        
        return newWord




