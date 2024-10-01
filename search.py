x = [43, 8, 29, 3, 8]

def find(x, v):
    for i in range(len(x)):
        if x[i] == v:
            return i
    return None

print(find(x, 3))
print(find(x, 8))
print(find(x, 100))
print(find([], 54))
