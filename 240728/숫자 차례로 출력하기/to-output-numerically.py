def print_number(n):
    if n == 0:
        return

    print_number(n-1)
    print(n, end=" ")

def print_reverse(n):
    if n == 0:
        print()
        return

    print(n, end=" ")
    print_reverse(n-1)

N = int(input())
print_number(N)
print()
print_reverse(N)