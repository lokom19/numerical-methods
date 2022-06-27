# -*- coding: utf-8 -*-

try:
    ycor = []
    xcor = []
    diff_list = []

    # your_function = float(eval(input('Введите вашу функцию: ')))
    def f(x):
        return math.exp(-x ** 2 / 0.0000001)


    c = (int(input('Введите число >= 1000')))


    def f2(a, b, h):
        # z=int((b-a)/h)
        for x in range(int(a * c), int(b * c) + 1, int(h * c)):
            diff_ = (f((x / c) + h) - f((x / c) - h)) / (2 * h)
            xcor.append(x / c)
            ycor.append(f(x / c))
            diff_list.append(diff_)


    f2(float(input('Введите начало интервала: ')), float(input('Введите конец интервала: ')),
       float(input('Введите шаг: ')))


    df = pd.DataFrame({'x': [i for i in xcor],
                       'y': [i for i in ycor],
                       'Производная': [i for i in diff_list]})


    graph = df.plot(x='x', y='Производная', color='red')

    print(df)


except:
    print('Ошибка')
