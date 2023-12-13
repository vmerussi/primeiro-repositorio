#Desafios da aula 09:

#exercício 22

#Crie um programa que leia o nome completo de uma pessoa e mostre:

# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo ( sem considerar espaços )
# - Quantas letras tem o primeiro nome

#nome = input('Digite o seu nome completo: ')
#nome1 = (nome.upper())
#nome2 = (nome.lower())
#nome3 = len(nome.strip())
#nome4 = len(nome.split()[0])
#print(f"O seu nome com todas as letras maiúsculas fica {nome1}")
#print(f"O seu nome com todas as letras minúsculas fica {nome2}")
#print(f"O seu nome possui um total de {nome3} letras sem considerar os espaços")
#print(f"O seu primeiro nome possui {nome4} letras")

#No fatiamento, a frase ou texto começa no zero (0,1,2,3...), considera os espaços como mais 1 caractere, e sempre exclui o último caractere que vc colocou.
#Ex: C u r s o
    #0 1 2 3 4

#Se vc pedir 0 - 4, ele vai exluir o 4, e vai ler Curs, sem a letra o. Aí o ideal seria colocar 0 - 5 ( pq 5 seria o espaço para a próxima palavra.)
#Ex: frase[9:21:2] ele vai de 9 até 21 pulando de 2 em 2

#frase[:5] qdo coloca 2 pontos no início, ele começa do caractere zero 0, e vai até o número informado, no exemplo aqui é o 5.

#frase[15:] qdo colocamos 2 pontos no final, ele começa no caractere informado (15), e vai até o final da frase.

#frase[9::3] começa no 9 e vai até o final.

#len significa comprimento, vai mostrar o comprimento da frase, ex: Curso em Vídeo Python tem 21 caracteres. Comando len(frase)

#count frase.count('o') na frase Curso em Vídeo Python, ele mostra o valor 3 como resultado, pq só tem 3 letras o na frase.

#count frase.count('o', 0, 13) é uma contagem com fatiamento: ele vai contar quantas letras o tem do 0 ao 13, mas vai considerar até o 12, a resposta será 1.

#find => frase.find('deo') ele mostra onde começou o 'deo', resposta será 11

#find => frase.find('Android') qdo tem uma palavra que não existe ele mostra o resultado -1, que não foi encontrado

#'Curso' in frase ( na frase Curso em Vídeo Python ) existe a palavra Curso? Pra dizer a posição teríamos que colocar find, que acabamos de usar.
# Nesse caso o operador in vai dizer: Existe a palavra Curso em frase? Sim! Então o resultado será True.

#Replace frase.replace('Python', 'Android') ele vai substituir Python por Android

#Upper frase.upper() ex: Curso em Vídeo Python ele vai pegar o q for minúsculo e transformar em maiúsculo CURSO EM VÍDEO PYTHON
#Lower frase.lower() ex: Curso em Vídeo Python ele vai pegar o q for maiúsculo e transformar em minúsculo curso em vídeo python
#Capitalize frase.capitalize() ex: Curso em Vídeo Python ele vai jogar tudo pra minúsculo e só a primeira letra ele vai deixar em maiúsculo:
#ex: Curso em vídeo python

#Title frase.title() ele vai analisar quantas palavras tem na string (frase) ,ex: Curso em Vídeo Python ( tem 4 palavras ), e ele consegue contar
#pela posição dos espaços, onde ele faz uma quebra de palavras, e depois faz o Capitalize palavra por palavra.
#Ex: Curso em Vídeo Python vai ficar com o title: Curso Em Vídeo Python ( note que a palavra em virou Em ), e os demais caracteres permanecem minúsculos.

#Strip frase.strip serve para remover os espaços inúteis que uma pessoa coloca quando vai preencher ou digitar algo em um campo (input).
#Ex:       A p r e n d a P y t h on
    #0 1 2 3
#Ele remove os primeiros, e remove tb os 2 últimos espaços do final  espaços e mantém os demais. O que era 3 agora vai ser 0.
  #   A p r e n d a   P y t  h  o  n
  #   0 1 2 3 4 5 6 7 8 9 10 11 12 13

#De forma similar temos o frase.rstrip() que r é de right direita. Muitas funções dentro do Python que tratam strings tem a variação r.
#Tem algumas funcionalidades que vc pode colocar um r na frente pra começar a tratar pela direita. Fica a dica!
#frase.rstrip() ele vai remover só os últimos espaços, os espaços do início ele vai manter.
#       A p r e n d a    P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
#então ele vai remover os 2 últimos espaços, então a string vai de 0 a 16, tendo um len de 17 caracteres.

#De forma análoga( parecida, semelhante ), temos o frase.lstrip() l é de left q é esquerda. Ele vai remover os espaços da esquerda, mas vai manter
#os da direita.
#       A p r e n d a    P  y  t  h  o  n
#       3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

#Em resumo:
#Tirar os espaços da direita: rstrip
#Tirar os espaços da esquerda : lstrip
#Tirar todos os espaços indesejados nas extremidades: strip
#Tirar todos os espaços do meio : dá pra fazer mas é outra funcionalidade q ele não falou. É raciocínio e algumas funcionalidades q vimos nessa aula.

#Divisão
# C u r s o   e m    V  í d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7  8 9 10 11 12 13 14 15 16 17 18 19 20

#A primeira funcionalidade q vamos ver é o Split
# frase.split() dentro dos parênteses tem algumas funcionalidades pra pesquisar, pq o Guanabara nao falou.
# O split é feito em seus espaços.  Vai ocorrer uma divisão dentro da sua string, ele vai fazer uma divisão entre os espaços, logo, eles
# recebem uma indexação nova. Cada uma dessas palavras será colocada dentro de uma outra lista. Ele vai gerar tecnicamente uma lista, com todas as
#palavras de uma cadeia de caracteres, onde ele vai separar esses pedaços, que receberão uma numeração de acordo com a quantidade de palavras, ex:
# C u r s o  e m  V í d e o  P y t h o n
# 0 1 2 3 4  0 1  0 1 2 3 4  0 1 2 3 4 5
#    0        1       2           3

#O split divide uma string em uma lista, onde cada elemento vai ser separado pelo seu splitador, pelo seu caractere de split, que por padrão é o espaço.

# Junção - Join

#Se eu tenho os nomes separados em listas , eu consigo utilizar o join que é pra juntar uma coisa na outra, ex:
# Ex: '-'.join(frase)

#Então esse tracinho vai se juntar aos espaços da frase, e ficará assim:
# C u r s o-e m-V í d e o-P y t h o n

#frase = 'Curso em Vídeo Python'
#print(frase[13:])

#print("""Welcome! Are you completely bla bla bla bla""")
#Isso quando vc quer colocar um textao e nao quiser ficar colocando print linha a linha, pode colocar 3 aspas no começo e 3 aspas no final.

#frase = 'Curso em Vídeo Python' Aqui ele conta quantas letras o tem e transforma elas em maiúsculas.
#print(frase.upper().count('O'))

#frase = 'Curso em Vídeo Python' A única forma de mudar, trocar é usando replace
#print(frase.replace('Python', 'Android'))
#print(frase) nesse caso vc não pediu pra substituir, ou seja, salvar os resultados.

#Para salvar os resultados e fazer a substituição:
# frase = 'Curso em Vídeo Python'
# frase = frase.replace('Python', 'Android') Nesse caso sim, vc consegue fazer uma alteração.
#print(frase)
#Uma string em seus microelementos ela é imutável. A não ser que eu utilize uma função de transformação de string frase.replace('Python', 'Android')
# e faça uma atribuição (frase). Aí sim vai funcionar.

#Para verificar se uma palavra está na frase:
#frase = 'Curso em Vídeo Python'
#print('Curso' in frase)
#resposta True

#Para localizar a posição em que a palavra está:
#frase = 'Curso em Vídeo Python'
#print(frase.find('Curso'))
#resposta será zero 0, pq a palavra começa na posição zero.

#Quando a palavra estiver em maiúsculo, e vc colocar para localizar em minúsculo, e sem acento:
#frase = 'Curso em Vídeo Python'
#print(frase.find('video'))
#ele retornará -1 pq não existe

#Se quiser transformar essa palavra, e jogar para minúsculo:
#frase = 'Curso em Vídeo Python'
#print(frase.lower().find('vídeo'))
#retorna 9 pq o lower transformou em minúsculo.

#Para splitar ( dividir ) a frase:
#frase = 'Curso em Vídeo Python'
#print(frase.split())
#resposta = ['Curso', 'em', 'Vídeo', 'Python'] ele criou uma lista (colchetes) com separador de frase, fatiou a frase.

#Para fatiar e pegar somente 1 palavra na posição que vc pediu, no ex abaixo será no zero 0.
#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[0]) aqui ele está pedindo a posição zero 0
#resposta = Curso

#Para fatiar uma palavra de acordo com a posição q vc pediu, e a posição da letra escolhida:
#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[2][3]) pq a palavra curso vale 0, em vale 1, Vídeo vale 2 e Python 3.
#Logo, palavra 2: Vídeo, letra 3: e ( a contagem das letras começa no zero 0 tb.

#Crie um programa que leia o nome completo de uma pessoa e mostre:

# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo ( sem considerar espaços )
# - Quantas letras tem o primeiro nome

#nome = input('Digite o seu nome completo: ')
#nome1 = (nome.upper())
#nome2 = (nome.lower())
#nome3 = len(nome.strip())
#nome4 = len(nome.split()[0])
#print(f"O seu nome com todas as letras maiúsculas fica {nome1}")
#print(f"O seu nome com todas as letras minúsculas fica {nome2}")
#print(f"O seu nome possui um total de {nome3} letras sem considerar os espaços")
#print(f"O seu primeiro nome possui {nome4} letras")

#nome = str(input('Digite seu nome completo: ')).strip()
#print('Analisando seu nome...')
#print('Seu nome em maiúscula é {}'.format(nome.upper()))
#print('Seu nome em minúscula é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#O Guanabara colocou sinal de menos antes do nome.count
#Dica Vc pode pesquisar dentro do nome  
#nome.find()

#len vc vai chamar sempre que quiser saber o tamanho, por exemplo, o tamanho do nome:
#print('Seu nome tem ao todo {} letras'.format(len(nome)))
#split vai jogar dentro de uma lista os nomes inteiros
#count vai contar o q vc colocar dentro do parentêses, isso serve para espaço, por ex:
#nome.count(' ') tem um espaço entre os parênteses, fazendo o código entender que isso será contado
#Logo, para remover os espaços, e contar a quantidade de letras ficará assim:
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))
#eliminar espaço no início: format(len(nome) - nome.count(' ')))
#eliminar espaço no final   .strip

#nome = str(input('Digite seu nome completo: ')).strip()
#print('Analisando seu nome... ')
#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#outra forma de pesquisar para localizar o nome
#nome.find(' ')

#ex 24 programa q leia se uma cidade começa com a palavra Santo
# .strip() tira os espaços

#cidade = str(input('Em que cidade você nasceu? ')).strip()
#print(cidade[:5].upper() == 'SANTO')

#Jogamos tudo pra maiúsculo pq independente do q for digitado ele será transformado em maiúsculo para localizar a palavra.
# Aqui vc resolve o problema de maiúsculo/minúsculo: print(cidade[:5].upper() == 'SANTO') os 2 pontos antes do 5 é para começar do início a palavra.

#nome = str(input('Digite seu nome completo: '))
#print(nome.find('SILVA'))

#nome = str(input('Qual o seu nome? ')).strip()
#print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))

#nome = str(input('Qual o seu nome? ')).strip()
#print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))



