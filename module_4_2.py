def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()

inner_function() # при вызове внутренней функии выходит ошибка, т.к. функция не определена в глобальном пространстве

