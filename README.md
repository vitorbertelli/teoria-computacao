# TRABALHO TEORIA DA COMPUTAÇÃO - MÁQUINA NORMA
Este repositório contém a resolução do trabalho do 2º bimestre da disciplina de Teoria da Computação ministrada pelo professor Saulo Ribeiro.

O trabalho consiste na criação de uma Máquina Normal escrita em *Python*. A aplicação deve ler programas monolíticos escritos em forma de instruções rotuladas e executá-las, imprimindo o resultado de cada instrução e mostrando os registradores e seus valores durante a execução do programa.

Para a resolução desse trabalho, foi escolhido criar uma classe `Machine` que contém os 8 registradores e encapsula suas funções básicas como `ADD` e `SUB`, além do teste `ZER`. Além disso, foi criada uma função para executar qualquer programa monolítico que siga a lógica do projeto.

Este programa está disponível para uma melhor visualização e execução online no Google Colab através deste [link](https://colab.research.google.com/drive/1ufcEeHZ5wYe9RWxuMHL8JYRqpderjHJ_#scrollTo=tZaGumUTW5J7).

A seguir estão as instruções usadas como base para cada problema proposto e seus detalhes e explicações.

## SOMA
Esse programa é resolução do seguinte problema:

**A := A + B usando C, onde o registrador C armazena a soma, A e B ficam zerados.**

#### Programa monolítico
```
1: se ZERO_A então vá_para 4 senão vá_para 2
2: faça SUB_A vá_para 3
3: faça ADD_C vá_para 1
4: se ZERO_B então vá_para 8 senão vá_para 5
5: faça SUB_B vá_para 6
6: faça ADD_C vá_para 4
```
#### Arquivo tipo texto lido pelo *Python*
```
A=5, B=3, C=0
1: ZER A 4 2
2: SUB A 3
3: ADD C 1
4: ZER B 8 5
5: SUB B 6
6: ADD C 4
```

## MULTIPLICAÇÃO
Esse programa é resolução do seguinte problema:

**A := A * B usando C , D, onde o registrador A armazena o produto, B tem seu valor restaurado, C e D ficam zerados.**

#### Programa monolítico
```
1: se ZERO_A então vá_para 4 senão vá_para 2
2: faça ADD_C vá_para 3
3: faça SUB_A vá_para 1
4: se ZERO_C então vá_para 13 senão vá_para 5
5: se ZERO_B então vá_para 9 senão vá_para 6
6: faça ADD_A vá_para 7
7: faça SUB_B vá_para 8
8: faça ADD_D vá_para 5
9: se ZERO_D então vá_para 12 senão vá_para 10
10: faça ADD_B vá_para 11
11: faça SUB_D vá_para 9
12: faça SUB_C vá_para 4
```
#### Arquivo tipo texto lido pelo *Python*
```
A=5, B=3, C=0, D=0
1: ZER A 4 2
2: ADD C 3
3: SUB A 1
4: ZER C 13 5
5: ZER B 9 6
6: ADD A 7
7: SUB B 8
8: ADD D 5
9: ZER D 12 10
10: ADD B 11
11: SUB D 9
12: SUB C 4
```

## FATORIAL
Esse programa é resolução do seguinte problema:

**Computar o fatorial de um número que está no registrador A. Usar os registradores B,C e D como auxiliares. Pode escolher em qual registrador ficará o resultado do fatorial.**

#### Programa monolítico
```
1: faça ADD_B vá_para 2
2: se ZERO_A então vá_para 16 senão vá_para 3
3: se ZERO_B então vá_para 6 senão vá_para 4
4: faça ADD_C vá_para 5
5: faça SUB_B vá_para 3
6: se ZERO_C então vá_para 15 senão vá_para 7
7: se ZERO_A então vá_para 11 senão vá_para 8
8: faça ADD_B vá_para 9
9: faça ADD_D vá_para 10
10: faça SUB_A vá_para 7
11: se ZERO_D então vá_para 14 senão vá_para 12
12: faça ADD_A vá_para 13
13: faça SUB_D vá_para 11
14: faça SUB_C vá_para 6
15: faça SUB_A vá_para 2
16: se ZERO_B então vá_para 19 senão vá_para 17
17: faça ADD_A vá_para 18
18: faça SUB_B vá_para 16
```
#### Arquivo tipo texto lido pelo *Python*
```
A=2, B=0, C=0, D=0
1: ADD B 2
2: ZER A 16 3
3: ZER B 6 4
4: ADD C 5
5: SUB B 3
6: ZER C 15 7
7: ZER A 11 8
8: ADD B 9
9: ADD D 10
10: SUB A 7
11: ZER D 14 12
12: ADD A 13
13: SUB D 11
14: SUB C 6
15: SUB A 2
16: ZER B 19 17
17: ADD A 18
18: SUB B 16
```

## TESTES
Para resolver os problemas de teste binário, foi escolhido armazenar o valor 1 no caso de o teste ser verdadeiro em um registrador específico de cada função, ou 0 caso o teste seja falso. Além disso, para evitar repetição de instruções e lógica, foram criadas duas funções que auxiliam os outros testes. Elas estão detalhadas e explicadas em suas respectivas seções.

### MENOR
Nesse teste, resolvemos o seguinte problema proposto: 

**Teste se o valor de um registrador é menor que outro registrador.**
</br>
A < B usando C, D, E

Como resolução do problema, caso o teste seja verdadeiro, é armazenado o valor de 1 para o registrador `E`, caso contrário, é armazenado 0.

#### Programa monolítico
```
1: se ZERO_A então vá_para 5 senão vá_para 2
2: faça ADD_C vá_para 3
3: faça ADD_E vá_para 4
4: faça SUB_A para 1
5: se ZERO_E então vá_para 8 senão vá_para 6
6: faça ADD_A vá_para 7
7: faça SUB_E vá_para 5
8: se ZERO_B então vá_para 12 senão vá_para 9
9: faça ADD_ADD D vá_para 10
10: faça ADD_E vá_para 11
11: faça SUB_B vá_para 8
12: se ZERO_E então vá_para 15 senão vá_para 13
13: faça ADD_B vá_para 14
14: faça SUB_E vá_para 12
15: se ZERO_C então vá_para 19 senão vá_para 16
16: se ZERO_D então vá_para 21 senão vá_para 17
17: faça SUB_C vá_para 18
18: faça SUB_D vá_para 15
19: se ZERO_D então vá_para 21 senão vá_para 20
20: faça ADD_E vá_para 21
```
As linhas de 1 a 14 realizam as instruções de copiar os valores de A e B e atribuí-los a C e D, respectivamente.
#### Arquivo tipo texto lido pelo *Python*
```
A=1, B=2, C=0, D=0, E=0
1: ZER A 5 2
2: ADD C 3
3: ADD E 4
4: SUB A 1
5: ZER E 8 6
6: ADD A 7
7: SUB E 5
8: ZER B 12 9
9: ADD D 10
10: ADD E 11
11: SUB B 8
12: ZER E 15 13
13: ADD B 14
14: SUB E 12
15: ZER C 19 16
16: ZER D 21 17
17: SUB C 18
18: SUB D 15
19: ZER D 21 20
20: ADD E 21
```

### MOD
Nesse teste, resolvemos o seguinte problema proposto: 

**Teste se o valor da divisão inteira é zero.**
</br>
Teste_mod(A, B) usando C, D, E, C’, D’, E’

No programa monolítico abaixo, o teste anterior ([MENOR](#menor)) foi usado na linha 10.

#### Programa monolítico
```
1: se ZERO_A então vá_para 5 senão vá_para 2
2: faça SUB_A vá_para 3
3: faça ADD_E vá_para 4
4: faça ADD_C vá_para 1
5: se ZERO_E então vá_para 8 senão vá_para 6
6: faça ADD_A vá_para 7
7: faça SUB_E vá_para 5
8: se ZERO_B então vá_para 20 senão vá_para 9
9: se ZERO_A então vá_para 19 senão vá_para 10
10: se C < B então vá_para 18 senão vá_para 11
11: se ZERO_B então vá_para 15 senão vá_para 12
12: faça ADD_E vá_para 13
13: faça SUB_B vá_para 14
14: faça SUB_C vá_para 11
15: se ZERO_E então vá_para 10 senão vá_para 16
16: faça ADD_B vá_para 17
17: faça SUB_E vá_para 15
18: se ZERO_C então vá_para 19 senão vá_para 20
19: faça ADD_D vá_para 20
```
O registrador `C` guarda o resto da divisão, caso seja zero, o valor 1 é armazenado no registrador `D`, indicando que o teste é verdadeiro.
#### Arquivo tipo texto lido pelo *Python*
```
A=16, B=4, C=0, D=0
1: ZER A 5 2
2: SUB A 3
3: ADD E 4
4: ADD C 1
5: ZER E 8 6
6: ADD A 7
7: SUB E 5
8: ZER B 20 9
9: ZER A 19 10
10: LESS C B 18 11
11: ZER B 15 12
12: ADD E 13
13: SUB B 14
14: SUB C 11
15: ZER E 10 16
16: ADD B 17
17: SUB E 15
18: ZER C 19 20
19: ADD D 20
```

### PRIMO
Nesse teste, resolvemos o seguinte problema proposto: 

**Teste se o valor do registrador é um primo.**
</br>
teste_primo(A)

No programa monolítico abaixo, o teste anterior ([MOD](#mod)) foi usado na linha 11.

#### Programa monolítico
```
1: se ZERO_A então vá_para 16 senão vá_para 2
2: se ZERO_A então vá_para 6 senão vá_para 3
3: faça ADD_B vá_para 4
4: faça ADD_D vá_para 5
5: faça SUB_A vá_para 2
6: se ZERO_D então vá_para 9 senão vá_para 7
7: faça ADD_A vá_para 8
8: faça SUB_D vá_para 6
9: faça SUB_B vá_para 10
10: se ZERO_B então vá_para 14 senão vá_para 11
11: se teste_mod(A, B) então vá_para 13 senão vá_para 12 
12: faça SUB_B vá_para 11
13: faça SUB_B vá_para 14
14: se ZERO_B então vá_para 15 senão vá_para 16
15: faça ADD_C vá_para 16
```
Em caso em que o teste seja verdadeiro e o número do resgistrador `A` seja primo, o registrador `C` armazena o valor de 1, simulando um valor booleano.
#### Arquivo tipo texto lido pelo *Python*
```
A=7, B=0, C=0, D=0
1: ZER A 16 2
2: ZER A 6 3
3: ADD B 4
4: ADD D 5
5: SUB A 2
6: ZER D 9 7
7: ADD A 8
8: SUB D 6
9: SUB B 10
10: ZER B 14 11
11: MOD A B 13 12 
12: SUB B 11
13: SUB B 14
14: ZER B 15 16
15: ADD C 16
```