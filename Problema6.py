def ser_fibonacci(limite):
    fib = [0, 1]
    while True:
        siguiente = fib[-1] + fib[-2]
        if siguiente > limite:
            break
        fib.append(siguiente)
    return fib

limite = 50
fibonacci = ser_fibonacci(limite)

print(fibonacci)