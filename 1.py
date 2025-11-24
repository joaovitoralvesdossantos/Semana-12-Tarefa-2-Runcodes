# função que calcula o fatorial
def fatorial(n):
    contador = 1       

    # loop que multiplica todos os números de 1 até n
    for i in range(1, n + 1):
        contador = contador * i   

    # saída de dados
    print(f"O fatorial de {n} é {contador}")   


# função principal
def main():
    # entrada
    n = int(input("Digite um número para calcular o fatorial: ").strip())

    # processamento e saída
    fatorial(n)

# chama a função principal
if __name__ == '__main__':
    main()