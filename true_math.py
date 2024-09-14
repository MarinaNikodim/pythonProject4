from math import inf

def t_divide(first, second):
    if second == 0:
        return float(inf)
    else:
        result = first / second
        return result


result = t_divide(5, 4)
result1 = t_divide(48, 0)
print(result)
print(result1)


# def main():
#     g = 5**5
#     print(g)
#
#
# print(__name__)
# if __name__ == '__main__':
#     main()
#
#     print("Good weather")
