def print_star(N):
    if N == 0:
        return
    
    print("* "*N)
    print_star(N-1)
    print("* "*N)

print_star(int(input()))