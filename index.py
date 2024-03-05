import random

lista_de_filmes = ['Avatar','Vingadores','Titanic', 'Jurassic World','O Rei Leão']
lista_de_livros = ['O Pequeno Príncipe','1984','A Cabana','Os Miseráveis','Romeu E Julieta']
lista_de_carros = ['Lamborghini','Ferrari','Porshe','HB20','Uno']
lista_de_nome = ['Vinícius', 'João','Gabriel','Mateus','Timóteo']

def nome_do_jogo():
    jogo = "    JOGO DA FORCA   "
    print("="*len(jogo))
    print(jogo)
    print("="*len(jogo))

def jogar_forca():
    categoria = int(input("Escolha a categoria:\n1-FILMES\n2-LIVROS\n3-CARROS\n4-NOMES"))
    if categoria == 1:
        palavras = lista_de_filmes
    elif categoria == 2:
        palavras = lista_de_livros
    elif categoria == 3:
        palavras = lista_de_carros
    elif categoria == 4:
        palavras = lista_de_nome

    palavra = random.choice(palavras).upper()

    palavra_escondida = ["_"] * len(palavra)
    letras_utilizadas = []

    tentativas = 6
    while tentativas > 0:
        letra = input("\nDigite uma letra: ").upper()

        if letra in letras_utilizadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_utilizadas.append(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_escondida[i] = letra
            print("".join(palavra_escondida))
        else:
            tentativas -= 1
            print("Letra não encontrada. Tentativas restantes:", tentativas)

        if "_" not in palavra_escondida:
            print("\nParabéns! Você acertou a palavra:", palavra)
            break

    if tentativas == 0:
        print("\nFim de jogo. A palavra era:", palavra)

nome_do_jogo()
jogar_forca()