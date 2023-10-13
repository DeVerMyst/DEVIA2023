def fibonacci(order):
    fib_list = [0, 1]

    while len(fib_list) < order:
        next_term = fib_list[-1] + fib_list[-2]
        fib_list.append(next_term)

    return fib_list

def main():
    n = int(input("Entrez l'ordre de la suite de Fibonacci : "))
    result = fibonacci(n)
    print("Suite de Fibonacci jusqu'à l'ordre", n, ":", result)

if __name__ == "__main__":
    main()
