A, B, C = map(int, input().split())

def divide(b):
    if b == 1:
        return A % C

    elif b % 2:
        return (divide(b//2)**2 * A) % C
    
    else:
        return (divide(b//2)**2) % C

print(divide(B))