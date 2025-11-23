#1 exercicio
def comparador_de_numeros(numero1, numero2):

    if numero1 > numero2 :
     return (f'{numero1} é maior do que o segundo número.') 
    if numero2 > numero1 :
     return (f'{numero2} é maior do que o primeiro número.')
    if numero1 == numero2 : 
     return 'Os dois números são iguais.'

#2 exercicio

def comparador_de_letras(letra: str):

    if letra.lower() == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return 'Essa letra é uma vogal.'
    else:
        return 'Essa letra é uma consoante.'


#3 exercicio

def comparador_de_senhas(senha, senha2):

    if senha == senha2 :
        return 'Acesso permitido.'
    else:
        return 'As senhas não coincidem.'


#4 exercicio
def medias(nota1, nota2, nota3):

    soma = nota1 + nota2 + nota3
    media = soma/3
    if media >= 7 :
        return f'{media} foi sua média, você foi aprovado.'
    else:
        return f'{media} foi sua média, você foi reprovado.'
