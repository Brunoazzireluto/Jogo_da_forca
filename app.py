from palavras import palavras
import random as rd

#Selecionar a palavra

def selecionar_palavra():
    palavra = rd.choice(palavras)
    return palavra.upper()

#iniciar o jogo
def jogar(palavra):
    palavra_a_completar =  "_" * len(palavra)
    adivinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6


    # Boas Vindas ao Jogador
    print('Bem vindo, vamos jogar!')
    print(exibir_forca(tentativas))
    print(' Esta é a Palavra: %s' % palavra_a_completar)


    #Enquanto o jogador não adivinhar e ainda houver tentativas
    while not  adivinhou and tentativas > 0:

        tentativa = input('Digite uma palavra ou letra para continuar: ').upper()
        print(tentativa)

        #tentativa de letra única
        #Verificar se a tentativa é uma única letra
        if len(tentativa) == 1 and tentativa.isalpha():
            #verificando se a lerta já foi utilizada
            if tentativa in letras_utilizadas:
                print('Você já utilizou essa letra antes: %s' % tentativa)
            #verificando se a tentativa  não está na palavra  
            elif tentativa not in palavra:
                print('A letra %s não está na palavra' % tentativa)
                tentativas -= 1
                letras_utilizadas.append(tentativa)
            #Quando a Letra está na palavra
            else:
                print('Você acertou! A letra %s está na palavra' % tentativa)
                letras_utilizadas.append(tentativa)
                #transformar a palavra em lista
                palava_lista = list(palavra_a_completar)


                #Verificar onde pode susbstituir o underline com base na letra que foi passada
                indice = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indice:
                    palava_lista[indice] = tentativa
                    
                palavra_a_completar = ''.join(palava_lista)


                if "_" not in palavra_a_completar:
                    adivinhou = True
        #Tentativa de Palavra completa
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
            #palavras utilizadas
            if tentativa in palavras_utilizadas:
                print('Você já utilizou essa palavra %s' % tentativa)   
            #Palavra errada     
            elif tentativa != palavra:
                print('A palavra %s está incorreta!' % tentativa)
                tentativas -=1
                palavras_utilizadas.append(tentativa)
            #Acertou a palavra
            else:
                adivinhou = True
                palavra_a_completar = palavra




        #Tentativa Inválida
        else:
            print('Tentativa inválida, tente novamente!')
        # exibir status do jogo
        print(exibir_forca(tentativas))
        print(palavra_a_completar)

    # Finaliza o jogo se o usuarario  acertou o acabaram as tentativas
    if adivinhou:
        print('Parabéns! Você adivinhou a palavra!')
    else:
        print("Acabaram as tentativas, a palavra era: %s" % palavra)

#Status do jogo 
def exibir_forca(tentativas):
    estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
    ]

    return estagios[tentativas]

#inicializador do jogo e continuar jogando
def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)
    #quando o jogo acabar
    while input('Jogar novamente? (S/N)').upper() == 'S':
        palavra = selecionar_palavra()
        jogar(palavra)

iniciar()