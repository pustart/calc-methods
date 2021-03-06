### Задание №1:
* Используя Python, Numpy, Matplotlib, написать программу, вычисляющую
численный градиент функции двух переменных.
* Придумать такую функцию (достаточно сложную, содержащую
тригонометрию, возведения в степень и логарифмы), взять производную
аналитически и сравнить.
* Визуализировать трехмерный график функции с помощью Matplotlib.
* Покрыть код тестами.

### Задание №2:
1) Реализовать для функции одной переменной расчет интеграла пятью методами:
прямоугольников, трапеций, парабол, кубических парабол и Буля. Сравнить с готовыми
математическими пакетами. Например,
https://docs.scipy.org/doc/scipy/tutorial/integrate.html
2) Провести исследование для разных функций на точность методов в зависимости от h.
Построить график ошибки, на котором в виде пяти кривых будет отображен результат
исследования. В качестве “достоверного”, “идеального” значения функции можно взять
результат вычисления интеграла с очень маленьким h, либо аналитическое решение с
подставленными числами
3) Реализовать метод Гаусса (применить квадратурные формулы для 2-6 узлов на
отрезке). Сравнить результаты для разных функций. Сравнить метод с реализованными
в 1 пункте.
4) Реализовать для функции одной переменной расчет интеграла методом Монте-
Карло. Повторить для функции двух переменных. Подумать, возможно ли использовать
другие из перечисленных методов для больших размерностей. Если возможно,
запрограммировать любой понравившийся метод для функции двух переменных.
Может помочь:
https://stackoverflow.com/questions/14071704/integrating-a-multidimensional-integral-in-sci


Для выполнения задания разрешается объединяться в группы, максимум, из 3-х
человек. Желательно брать людей из своей подгруппы.
В случае выполнения задания в одиночку или вдвоем “3” ставится за успешную
сдачу первых двух пунктов. “4” - за них и любой из следующих пунктов, “5” - за
выполнение всех задач.

### Задание №3:
Реализовать метод прогонки для трехдиагональной матрицы (размера в 5-6
строк будет достаточно для финального теста). Сравнить результат с расчетом
каким-нибудь другим методом, реализованным в стороннем модуле. Например,
https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

Отдельно подумайте о структуре хранения трехдиагональной матрицы (можете
в качестве точки отправления использовать compressed sparse storage, о
котором мы говорили на паре:
https://www.gormanalysis.com/blog/sparse-matrix-storage-formats/). Но он в общем
виде тут тоже неоптимальный, поскольку мы заранее знаем, что вокруг трех
основных диагоналей будут только нули.