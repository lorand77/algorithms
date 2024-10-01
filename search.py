# def find(x, v):
#     for i in range(len(x)):
#         if x[i] == v:
#             return i
#     return None


# x = [43, 8, 29, 3, 8]

# print(find(x, 3))
# print(find(x, 8))
# print(find(x, 100))
# print(find([], 54))


def is_even_and_gt_5(x):
    return x % 2 == 0 and x > 5

def is_odd_and_gt_7(x):
    return x % 2 == 1 and x > 7

def find(x, f):
    for i in range(len(x)):
        if f(x[i]):
            return i
    return None


x = [43, 8, 29, 3, 8]

print(find(x, is_even_and_gt_5))
print(find(x, is_odd_and_gt_7))
