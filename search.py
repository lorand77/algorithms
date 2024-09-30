x = [43, 8, 29, 3, 8]

def search(x, v):
    for i in range(len(x)):
        if x[i] == v:
            return i
    return None

print(search(x, 3))
print(search(x, 8))
print(search(x, 100))
print(search([], 54))
