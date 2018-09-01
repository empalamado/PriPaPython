import c     
>>> Y = 222

# Pergunta: O que acontece se eu atribuir um número inteiro a uma variável flutuante?
# Resposta: Podemos investigar esse comportamento criando uma nova variável.

>>> y = 1.0            # Esta declaração cria uma variável chamada y que contém o valor inteiro 1. 
                       # Mas y é uma variável inteira ou de ponto flutuante? Podemos descobrir vendo o conteúdo de y. 
                       #P ython imprimiu o valor com uma parte fracionária (que é zero).

>>> y      # Isso indica que o valor é um valor de ponto flutuante. 
1.0        # Em outras palavras, A PRESENÇA DE UM PONTO DECIMAL EM UM VALOR IMPRESSO NOS DIZ QUE O VALOR É UM FLOAT 
           # O valor é sempre ponto flutuante quando um decimal é incluído, mesmo se não houver casas decimais.

# Pergunta: E quanto aos cálculos de ponto flutuante e inteiro?
# Resposta: Podemos investigar os resultados dos cálculos digitando alguns e depois observando os resultados.

>>> 2 + 2
4        # quando adicionamos dois inteiros juntos, obtemos um resultado inteiro.

>>> 2.0 + 2 
4.0          # Este é o mesmo cálculo, mas desta vez o Python produz um resultado de ponto flutuante porque os operandos
             # (os números) sobre as quais o operador + está trabalhando são ambos valores de ponto flutuante.
 # Acontece que quando uma expressão contém um valor de ponto flutuante, o resultado do cálculo é automaticamente convertido 
 # em um valor de ponto flutuante. Geralmente, se a expressão contiver números inteiros, gerará um resultado inteiro. 
 # Se a expressão contiver um valor de ponto flutuante, a expressão gerará um resultado de ponto flutuante.
 # Uma exceção à regra “inteiros fazem inteiros” é quando dividimos um inteiro por outro.
  
>>> 1/2     #O valor de 1/2 é uma metade, que não pode ser retido em um inteiro, portanto, o resultado desse cálculo é zero
0.5         #no Python 2.7. Na verdade, qualquer número menor que 1 é truncado para zero nesse cálculo.
            #Isso significa que o resultado de 9/10, que deveria ser 0,9, também é zero. Isso pode resultar em somas muito 
#diferentes dos valores que podemos esperar.
#Isso levanta a terrível perspectiva de programas em Python que funcionam corretamente no Python 3.6, produzindo respostas 
#completamente erradas quando eles são executados em versões mais antigas do Python. 
#O melhor conselho que posso dar é sempre colocar um ponto decimal em um valor se você quiser gerar resultados de ponto flutuante
#quando usado em cálculos.
#Você pode fazer com que um programa do Python 2 se comporte da mesma maneira que o Python 3, dizendo-lhe para usar as rotinas 
#de divisão atualizadas: Colocando o código abaixo:

from __future__ import division

#Você deve dar este comando no início de um programa para fazer a divisão do Python 2 se comportar
#da mesma maneira que a divisão do Python 3.

#Acima, eu acabei de dizer que dividir um inteiro por um inteiro produz um resultado de ponto flutuante. 
#Isso é verdade na versão 3.6 do Python que estamos usando neste livro. 
#No entanto, no Python 2.7, o resultado da divisão de um inteiro por um inteiro é outro inteiro.

#A função float também pode ser usada para converter um valor inteiro em um valor de ponto flutuante. 
#Isso pode ser útil em programas Python mais antigos, como uma forma de forçar o comportamento correto do operador de divisão

z = float(1)      #Nessa declaração, a variável z será do tipo float, mesmo que o valor atribuído seja um inteiro.
                  #O comportamento do float pode parecer bastante familiar. 
#Isso ocorre porque ele se comporta de maneira semelhante à função int, exceto pelo fato de fornecer resultados de ponto flutuante.

z = float(234)
print(z)
234.0
#----------------------------------------------------------------------
2 + 3 * 4 -1 + 3 (2 + 3) * 4
'''
Essas expressões são avaliadas pelo Python trabalhando da esquerda para a direita, exatamente como você as lê. 
Assim como na matemática tradicional, multiplicação e divisão são realizadas primeiro, seguidas de adição e subtração.

O Python atinge essa ordem dando a cada operador uma prioridade. 
Quando funciona uma expressão, ele encontra todos os operadores com a prioridade mais alta e os aplica primeiro. 
Em seguida, ele procura os operadores próximos em prioridade e assim por diante, até que o resultado seja obtido. 

Se você quiser forçar a ordem na qual uma expressão é avaliada, você pode colocar parênteses em torno dos elementos 
da expressão que deseja avaliar primeiro, como no exemplo final acima. 
Você também pode colocar parênteses entre parênteses, se quiser - desde que tenha tantos parênteses de abertura quanto 
os de fechamento. '''

a = 1 
b = 2 
c = a + b   # total = 3
c = c * (a + b) #Primeiro somar a + b por estar entre colchetes e depois multiplica por c dando um total de 9
b = a + b + c #a = 1, b = 2, c = 9, dando um total de 12






