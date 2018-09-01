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
 # Uma exceção à regra “inteiros fazem inteiros” é quando dividimos um inteiro por outro
