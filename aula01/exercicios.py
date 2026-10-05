"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""
    soma = 0
    for n in lista:
        soma = soma + n 
        return soma 


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""
    conta_pares = 0
    for n in lista: 
        if n % 2 == 0:
            conta_pares  + = 1
            return conta_pares


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""
    maior = lista [0]
    for n in lista:
        if maior < n:
            maior = n
            return maior 


def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""
    for n in lista: 
        if n == alvo:
            return true 
            return false


def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
            return -1


def segundo_maior(lista):
    """(Desafio) Devolve o segundo maior, percorrendo a lista uma unica vez."""
    maior = lista[0]
    segundo = none 
    for n in lista[1:]:
        if n > maior:
            segundo = maior
            maior = n
            elif n != maior and (segundo is None or n > segundo):
                segundo = n
                return segundo
