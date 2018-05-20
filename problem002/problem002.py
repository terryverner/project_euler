def fib_seq(threshold):
    values = [0, 1]
    
    while(values[-1] < threshold):
        values.append(values[-1] + values[-2])

    return values

threshold = int(input('Enter maximum number for Fibonacci sequence: '))

values = fib_seq(threshold)
summation = sum([i for i in values if i % 2 == 0])

print(f"Sum of even values: {summation}")
