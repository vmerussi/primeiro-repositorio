#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#O x que é passado como parâmetro ele não está em graus centígrados, ele está representado em radianos.
#Para verificar se o comando está atualizado, olhar na documentação no site do python . org , na página inicial vc vai clicar em
#docs, em docs vc escolhe sua a versão mais próxima, library reference, item 9 que é a parte matemática ( Numeric and Mathematical Modules ),
#aí vc procura seno (sin) , e cosseno (). Na biblioteca diz que Retorna o seno de x sendo radiano, então não adianta passar em graus, tem que converter
#para radianos. Para converter para radianos, é fácil demais, vc coloca: math.ra (ra significa radians),

#import math
#ang = float(input('Digite o ângulo que você deseja: '))
#sen = math.sin(math.radians(ang))
#print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
#cos = math.cos(math.radians(ang))
#print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
#tan = math.tan(math.radians(ang))
#print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))

#exemplo de código mais simplificado:
#No módulo math eu só utilizei os métodos: radians, sin, cos, tan.
#Então dá pra fazer isso aqui ó:

#tira todas as referências a math que eu coloquei anteriormente, vamos tirar aqui rapidamente, pq sempre que eu importo dessa maneira, eu não preciso mais referenciar o módulo que eu importei.

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tan = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))

#Seno e Cosseno tem o mesmo valor, que é raiz de 2 sobre 2.
