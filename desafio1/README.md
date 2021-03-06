
**Questão 1**. Desenvolver um programa em Ruby, Python ou Perl, sem auxílio de bibliotecas externas, para tentar encontrar a entrada e a saída de um labirinto. O programa deverá receber 4 argumentos na linha de comando, separados por espaços: # de linhas do labirinto, # de colunas do labirinto, uma string representando o labirinto e uma string representando o ponto de partida.
```
Ex.: `./programa 3 3 -1,0,-1,0,0,-1,-1,-1,-1 1,1`

    - # de linhas do labirinto será sempre um inteiro
    - # de colunas do labirinto será sempre um inteiro
    - a string representando o labirinto será sempre composta por inteiros, separados por vírgula, sem conter espaços
        - o inteiro -1 representa uma parede
        - o inteiro 0 representa um caminho
    - a string representando o ponto de partida será sempre composto por 2 inteiros, separados por vírgula, sem conter espaços

    Para o exemplo atual, a representação em uma matriz seria:

    -1  0 -1
     0  0 -1
    -1 -1 -1

    +--+   +--+
    |-1 | 0 |-1|
    +--+   +--+
     0    0 |-1|
    +--+---+--+
    |-1 |-1 |-1|
    +--+---+--+

    O programa deverá retornar como saída:
        - A representação do labirinto em string, com o caminho de uma entrada até uma saída marcado com o inteiro 1, se for possível;
        - 0 se não houver solução.

    Ex.: `./programa 3 3 -1,0,-1,0,0,-1,-1,-1,-1 1,1`
    -1,1,-1,1,1,-1,-1,-1,-1

    Ex.: `./programa 3 3 -1,-1,-1,0,0,-1,-1,-1,-1 1,1`
    0
    
    Vou dar um exemplo que espero que lhe ajude:

./programa 5 5 -1,0,-1,-1,-1,-1,0,0,0,-1,-1,0,-1,0,-1,-1,0,-1,0,-1,-1,0,-1,-1,-1 3,3

A representação do labirinto inicial:

-1   0   -1   -1   -1
-1   0    0    0   -1
-1   0   -1    0   -1
-1   0   -1    0   -1
-1   0   -1   -1   -1

A representação do labirinto, com o caminho marcado de um ponto de entrada até um ponto de saída:

-1   1   -1   -1   -1
-1   1    0    0   -1
-1   1   -1    0   -1
-1   1   -1    0   -1
-1   1   -1   -1   -1

A resposta correta seria: -1,1,-1,-1,-1,-1,1,0,0,-1,-1,1,-1,0,-1,-1,1,-1,0,-1,-1,1,-1,-1,-1
    
```

**Solução**
A modelagem do labirinto em um array é bem direta. Fiz uma rotina de parse da linha de comando, construí o array e fiz uma rotina de solve com backtrack. 
De acordo com o ultimo exemplo acima, nós podemos solenemente ignorar o ponto inicial para achar a solução. Primeiro eu vasculho possiveis pontos de entrada nas bordas e comeco o algoritimo de backtrack dali.
Para facilitar a leitura, mudei o formato de output da solução, conforme exemplo abaixo:

```
 ./programa.py   5 5 -1,-1,-1,-1,-1,-1,0,0,0,0,-1,0,0,0,-1,-1,0,-1,0,-1,-1,-1,-1,-1,-1 1,1
-1-1-1-1-1
-1 1 1 1 1
-1 1 1 0-1
-1 0-1 0-1
-1-1-1-1-1
```
Para executar o programa é necessário python>=2.6 (testei com 2.7 no ubuntu). 
Para instalar:
--------------

Baixe o programa `git clone git@github.com:aod7br/clavis2.git`.
Se não tiver o git instalado, baixe o zip e extraia: https://github.com/aod7br/clavis2/archive/master.zip

Entre no subdir `clavis2/desafio1`

Para rodar:
-----------

* No linux:

`./programa.py   5 5 -1,-1,-1,-1,-1,-1,0,0,0,0,-1,0,0,0,-1,-1,0,-1,0,-1,-1,-1,-1,-1,-1 1,1`

* No windows:

`python programa.py 5 5 -1,-1,-1,-1,-1,-1,0,0,0,0,-1,0,0,0,-1,-1,0,-1,0,-1,-1,-1,-1,-1,-1 1,1`
