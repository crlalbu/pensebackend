import sqlite3

class FraseModel:
    def __init__(self, frase, autor):
        self.frase = frase
        self.autor = autor

    def json(self):
        return {'frase': self.frase, 'autor': self.autor}

    # @classmethod
    # def find_by_autor(cls, autor):
