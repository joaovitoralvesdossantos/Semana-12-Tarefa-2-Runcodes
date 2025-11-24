# transforma um número em uma sequencia fibonacci.
def fibonacci(n):
    a = 0
    b = 1

    # Exibe o início da sequência
    print(a, end=", ")
    print(b, end="")
    
    #loop
    for i in range(n - 2):
        c = a + b
        print(",", c, end="")
        a = b
        b = c 
    
    print()

    return f"teste, {i}"  

# Função principal
def main():

    #entrada de dados
    n = int(input("Quantos termos da sequência Fibonacci você deseja gerar? ").strip())
    
    #processamento e saida de dados
    print(f"Aqui estão os {n} primeiros termos:")
    fibonacci(n)
    

# Chama a função principal
if __name__ == '__main__':
    main()