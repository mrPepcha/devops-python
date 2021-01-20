#3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно


class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)
        print(f"{self._count} - {other._count}: разность ячеек <= 0")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"



c1 = Cell(16)
print(c1)
c2 = Cell(7)
print(c2)

print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
print((c1 * c2).make_order(13))
