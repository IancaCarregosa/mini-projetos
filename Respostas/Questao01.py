def fibonacci(n):
    def calculaFibonacci(x):
        s = int(x ** 0.5)
        return s * s == x

    return calculaFibonacci(5 * n * n + 4) or calculaFibonacci(5 * n * n - 4)

num = int(input("Digite um número e descubra se ele pertence a sequência de Fibonacci ou não: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")

