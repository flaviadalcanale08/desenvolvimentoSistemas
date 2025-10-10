1. 
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


2. 
def comparador_de_letras(letra: str):

    if letra.lower() == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return 'Essa letra é uma vogal.'
    else:
        return 'Essa letra é uma consoante.'

import unittest

from trabalhoTeste import *
class testeCompleto(unittest.TestCase):

      def testar_comparador_de_letras(self):
        self.assertEqual(comparador_de_letras('a'), 'Essa letra é uma vogal.')
        self.assertEqual(comparador_de_letras('b'), 'Essa letra é uma consoante.')

if __name__ == "__main__" :
    unittest.main()


3. 
def comparador_de_senhas(senha, senha2):

    if senha == senha2 :
        return 'Acesso permitido.'
    else:
        return 'As senhas não coincidem.'

import unittest

from trabalhoTeste import *
class testeCompleto(unittest.TestCase):

      def testar_comparador_de_senhas(self):
        self.assertEqual(comparador_de_senhas (1,1), 'Acesso permitido.')
        self.assertEqual(comparador_de_senhas (2,1), 'As senhas não coincidem.')

if __name__ == "__main__" :
    unittest.main()


4. 
def medias(nota1, nota2, nota3):

    soma = nota1 + nota2 + nota3
    media = soma/3
    if media >= 7 :
        return f'{media} foi sua média, você foi aprovado.'
    else:
        return f'{media} foi sua média, você foi reprovado.'

import unittest

from trabalhoTeste import *
class testeCompleto(unittest.TestCase):

      def test__manipular_medias(self):
        self.assertEqual(medias(9, 9, 9), f'9.0 foi sua média, você foi aprovado.')
        self.assertEqual(medias(2, 2, 2), f'2.0 foi sua média, você foi reprovado.')

if __name__ == "__main__" :
    unittest.main()
