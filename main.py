def encontrar_menor_numero(a, b, c):
    menor = a

    if b < menor:
        menor = b

    if c < menor:
        menor = c

    return menor
def main():
    # Solicita os três números inteiros
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))

    # Encontra o menor número
    menor_numero = encontrar_menor_numero(numero1, numero2, numero3)

    # Exibe o resultado
    print(f"O menor número é: {menor_numero}")

if __name__ == "__main__":
    main()
