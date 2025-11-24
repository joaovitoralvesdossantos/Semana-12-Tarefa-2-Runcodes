# lê dois valores inteiros (x e y) e mostra todos os números primos entre x e y
def primo(n, n2):

    for numero in range(n, n2 + 1):    
        if numero < 2:
            continue               
        contador = 0              

        # testa todos os possíveis divisores
        for divisor in range(2, numero):
            if numero % divisor == 0:        
                contador += 1
                break               
            
        # se contador continuou 0 o numero é primo
        if contador == 0:
            print(f"Primo encontrado: {numero}")            


# função principal
def main():
    # entrada de dados
    x = int(input("Digite o início do intervalo: ").strip())
    y = int(input("Digite o fim do intervalo: ").strip())

    # processamento e saída de dados
    print(f"\nVerificando números primos entre {x} e {y}:")
    primo(x, y)

# chama a função principal
if __name__ == '__main__':
    main()