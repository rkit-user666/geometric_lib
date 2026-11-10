# Math Formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

---

# Документация проекта (Лабораторная работа №2)

## Общее описание решения
Данный проект представляет собой библиотеку на языке Python для вычисления параметров геометрических фигур. Проект был расширен: помимо исходных кругов и квадратов, добавлены модули для работы с прямоугольниками (`rectangle.py`) и треугольниками (`triangle.py`).

## Описание функций с примерами вызова

### Круг (circle.py)
* **`area(r)`** — Вычисляет площадь круга по заданному радиусу `r`.
  * *Пример вызова:* `area(5)` -> `78.53981633974483`
* **`perimeter(r)`** — Вычисляет длину окружности по заданному радиусу `r`.
  * *Пример вызова:* `perimeter(5)` -> `31.41592653589793`

### Квадрат (square.py)
* **`area(a)`** — Вычисляет площадь квадрата по длине его стороны `a`.
  * *Пример вызова:* `area(4)` -> `16`
* **`perimeter(a)`** — Вычисляет периметр квадрата по длине его стороны `a`.
  * *Пример вызова:* `perimeter(4)` -> `16`

### Прямоугольник (rectangle.py)
* **`area(a, b)`** — Вычисляет площадь прямоугольника по двум сторонам.
  * *Пример вызова:* `area(10, 5)` -> `50`
* **`perimeter(a, b)`** — Вычисляет периметр прямоугольника.
  * *Пример вызова:* `perimeter(10, 5)` -> `30`

### Треугольник (triangle.py)
* **`area(a, h)`** — Вычисляет площадь треугольника по основанию и высоте.
  * *Пример вызова:* `area(6, 4)` -> `12.0`
* **`perimeter(a, b, c)`** — Вычисляет периметр треугольника по трем сторонам.
  * *Пример вызова:* `perimeter(3, 4, 5)` -> `12`

## История изменения проекта
История коммитов репозитория (последняя запись исключена согласно заданию):
* **2260623** Add unit tests for rectangle, square, triangle and circle
* **4976c36** Update docs/README.md with new functions and commit history
* **6007de5** Add docstrings to rectangle and triangle functions
* **4871284** Fix perimeter formula in file rectangle.py
* **11e4eba** Added the file triangle.py
* **79904a2** Added the file rectangle.py
* **d078c8d** L-03: Docs added
* **8ba9aeb** L-03: Circle and square added