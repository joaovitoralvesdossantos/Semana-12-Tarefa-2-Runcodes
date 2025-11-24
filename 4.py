# lê um número e determina se ele é ou não primo.
def primo(n):
    contador = 0

    #loop
    for i in range(2, n):
        if n % i == 0:
            contador += 1

    if contador == 0:
        print(f"O número {n} é primo.")
    else:
        print(f"O número {n} não é primo.")

# Função principal
def main():

    #entrada de dados
    n = int(input("Digite um número para verificar se é primo: ").strip())
    
    #processamento e saida de dados
    primo(n)
    
# Chama a função principal
if __name__ == '__main__':
    main()