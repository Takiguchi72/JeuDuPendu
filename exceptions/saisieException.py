'''
Created on 26 déc. 2015

@author: takiguchi
'''
class SaisieException(Exception):
    '''
    Exception se levant lors d'une mauvaise saisie
    '''

    def __init__(self, pValue=""):
        '''
        Constructor
        '''
        self.value = pValue
        
    def __str__(self):
        '''
        Retourne le message de l'exception
        @return Le message de l'exception
        '''
        return repr(self.value)