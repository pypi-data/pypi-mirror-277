#%%

# fibonacci.py
# comment to test CI/CD workflow

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def main():
    N = int(input("Enter a positive integer N: "))
    result = fibonacci(N)
    print(f"The {N}th number in the Fibonacci sequence is: {result}")

if __name__ == "__main__":
    main()    
