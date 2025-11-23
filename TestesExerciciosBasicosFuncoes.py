#1 teste
import unittest

from Anna-03.10 import *
class testeCompleto(unittest.TestCase):


def testar_comparador_de_numeros(self):
        self.assertEqual(comparador_de_numeros(3, 2), '3 é maior do que o segundo número.')
        self.assertEqual(comparador_de_numeros(10, 11), '11 é maior do que o primeiro número.')
        self.assertEqual(comparador_de_numeros(10, 10), 'Os dois números são iguais.')

if _name_=="__main__":
unittest.main()

#2 teste

import unittest

from trabalhoTeste import *
class testeCompleto(unittest.TestCase):

      def testar_comparador_de_letras(self):
        self.assertEqual(comparador_de_letras('a'), 'Essa letra é uma vogal.')
        self.assertEqual(comparador_de_letras('b'), 'Essa letra é uma consoante.')

if __name__ == "__main__" :
    unittest.main()


#3 teste

import unittest

from trabalhoTeste import *
class testeCompleto(unittest.TestCase):

      def testar_comparador_de_senhas(self):
        self.assertEqual(comparador_de_senhas (1,1), 'Acesso permitido.')
        self.assertEqual(comparador_de_senhas (2,1), 'As senhas não coincidem.')

if __name__ == "__main__" :
    unittest.main()


#4 teste

import unittest

from trabalhoTeste import *
class testeCompleto(unittest.TestCase):

      def test__manipular_medias(self):
        self.assertEqual(medias(9, 9, 9), f'9.0 foi sua média, você foi aprovado.')
        self.assertEqual(medias(2, 2, 2), f'2.0 foi sua média, você foi reprovado.')

if __name__ == "__main__" :
