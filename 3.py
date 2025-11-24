# calcular o valor de H com 4 casas decimais
def soma(n):
    h = 0
    n = int(n)

    #loop
    for i in range(1, n+1):
        h = h + 1 / i
    return f"{h:.4f}"

# Função principal
def main():

    #entrada de dados
    n = input("Digite um número: ").strip()
    
    #processamento
    resultado = soma(n)
    
    #saida de dados
    print(f"O resultado é: {resultado}")

# Chama a função principal
if __name__ == '__main__':
    main()