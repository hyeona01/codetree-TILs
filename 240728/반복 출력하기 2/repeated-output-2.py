def print_hello(n):
    if n < 1:
        return
    print("HelloWorld")
    print_hello(n-1)
    
print_hello(int(input()))