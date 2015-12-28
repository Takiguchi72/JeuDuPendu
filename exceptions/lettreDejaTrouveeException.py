'''
Created on 26 déc. 2015

@author: takiguchi
'''
class LettreDejaTrouveeException(Exception):
    '''
    Exception se levant lorsque le joueur a saisi une lettre qu'il a déjà saisi
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