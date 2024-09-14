def f_divide(first, second):
    if second == 0:
        print("Ошибка")
        return None
    else:
        result_ = first / second
        return result_


result_ = f_divide(4, 2)
res_ = f_divide(8, 0)
print(result_)
print(res_)

