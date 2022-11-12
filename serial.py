"""Python serial number generator."""
'''
Author: Mahad Osman
Date: Nov 12
Exercise: Python OOP Exercise.
'''

from numpy import number


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        '''Creating two variables, one to hold the start and one to hold the incrementing values'''
        self.start = start
        self.nextNumber = start
    
    def __repr__(self):
        return f"<SerialGenerator start = {self.start} next = {self.nextNumber}>"
        

    def generate(self):
        ''' Increments our next number than returns it subtracted to match the test cases'''
        self.nextNumber = self.nextNumber + 1
        return self.nextNumber - 1
    
    def reset(self):
        '''To reset our nextNumber we set it to our untouched start number than return it '''
        self.nextNumber = self.start
        #return self.nextNumber # does not return it as the last test expects nothing
    