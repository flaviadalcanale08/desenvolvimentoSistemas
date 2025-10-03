
def comparador_de_numeros(numero1, numero2):

    if numero1 > numero2 :
     return (f'{numero1} é maior do que o segundo número.') 
    if numero2 > numero1 :
     return (f'{numero2} é maior do que o primeiro número.')
    if numero1 == numero2 : 
     return 'Os dois números são iguais.'


import unittest

from Flavia203Aula03_10 import *
class testeCompleto(unittest.TestCase):

    def testar_comparador_de_numeros(self):
        self.assertEqual(comparador_de_numeros(3, 2), '3 é maior do que o segundo número.')
        self.assertEqual(comparador_de_numeros(10, 11), '11 é maior do que o primeiro número.')
        self.assertEqual(comparador_de_numeros(10, 10), 'Os dois números são iguais.')


if __name__ == "__main__" :
    unittest.main()
