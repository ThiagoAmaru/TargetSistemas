Fibonacci = [0, 1]

NumeroDeEntrada = int(input("Digite um número inteiro: "))

while Fibonacci[len(Fibonacci)-1] <= NumeroDeEntrada:
   
    PenultimoNumero= Fibonacci[len(Fibonacci)-2]

    UltimoNumero= Fibonacci[len(Fibonacci)-1]

    Fibonacci.append(PenultimoNumero + UltimoNumero)


if NumeroDeEntrada in Fibonacci:
    print("O numero", NumeroDeEntrada,"Faz parte da sequencia de Fibonacci")

else:
    print("O numero", NumeroDeEntrada,"Nao faz parte da sequencia de Fibonacci")


print("Esses sao os numeros da sequencia de Fibonacci", Fibonacci)