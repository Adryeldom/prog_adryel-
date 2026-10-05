"""Aula 03 - Construa e diga o custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

ATENCAO: quase todas as funcoes desta aula devolvem DUAS coisas,
o resultado e a contagem de operacoes:

    return soma, operacoes

Quem devolve so o resultado nao passa nos testes.
"""


def soma_contando(lista):

    soma_contando([1, 2, 3]) -> (6, 3)"""
    soma = 0
    operacoes = 0
    
    for num in lista:
        soma += num
        operacoes += 1
        
    return (soma, operacoes)

def busca_linear_contando(lista, alvo):
    comparacoes = 0
    
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return (i, comparacoes)
            
    return (-1, comparacoes)

def busca_binaria_contando(lista, alvo):
    """Recebe uma lista JA ORDENADA.
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == alvo:
            return (meio, comparacoes)
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return (-1, comparacoes)
def tem_repetido_contando(lista):
    comparacoes = 0
    n = len(lista)
    
    for i in range(n):
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] == lista[j]:
                return (True, comparacoes)
                
    return (False, comparacoes)


def quantas_divisoes(n):
    contador = 0
    
    while n > 1:
        n = n // 2
        contador += 1
        
    return contador

def mais_frequente_contando(lista):
    if not lista:
        return (None, 0)
        
    mais_frequente = lista[0]
    max_contagem = 0
    comparacoes = 0
    
    for i in range(len(lista)):
        contagem_atual = 0
        for j in range(len(lista)):
            comparacoes += 1
            if lista[i] == lista[j]:
                contagem_atual += 1
                
        if contagem_atual > max_contagem:
            max_contagem = contagem_atual
            mais_frequente = lista[i]
            
    return (mais_frequente, comparacoes)
