def test_function(x):
    def inner_function(y):
        inner_function(y)


y = "Я в области видимости функции test_function"
print(y)
