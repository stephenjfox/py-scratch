from typing import List, Tuple


# TODO replace with GridSquare class, which has built-in validation
def grid_square() -> str:
    return "[ ]"


class GridAxis:
    "Validation as OneOf('row', 'column')"
    valid_choices = set(['row', 'column'])

    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r}")
        if value not in GridAxis.valid_choices:
            raise ValueError(f"Value {value!r} not of valid choices {GridAxis.valid_choices!r}")
        setattr(obj, self.private_name, value)


# WIP: utilize in ._grid.py
class GridSquare:

    def __init__(self, value=' '):
        self._value = value

    def __repr__(self) -> str:
        return f"[{self.value}]"

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value):
        if len(str(value)) != 1:
            raise ValueError("GridSquare values must be single-character")


class BlankSquare(GridSquare):

    def __init__(self):
        super(GridSquare, self)
        # self.value = ' '

    def __repr__(self) -> str:
        return "   "  # HACK but it works and is internally consistent


def join_row(row: List[GridSquare]) -> str:
    "Convert a row (list of squares) to a single string for printing"
    after = ' '.join(map(str, row))
    return after


class Grid:

    def __init__(self, rows: List[List[GridSquare]] = []):
        self.rows = rows

    # __blank = " " * len(grid_square())

    @staticmethod
    def ensure_capacity(row: List[GridSquare], capacity: int) -> None:
        row_length = len(row)
        grow_by = capacity - row_length
        if grow_by > 0:
            for _ in range(grow_by):
                row.append(BlankSquare())  # TODO: make a blank square

    def __repr__(self) -> str:
        return '\n'.join(map(join_row, self.rows))

    @property
    def n_rows(self) -> int:
        return len(self.rows)

    @property
    def n_columns(self) -> int:
        return len(max(self.rows, key=len))

    @property
    def dimensions(self) -> Tuple[int, int]:
        return self.n_rows, self.n_columns

    # Style: class-based
    def insert_column(self, at: int) -> None:
        "Insert column at index, affecting all rows"
        print(self.insert_column.__doc__)
        for _, r in enumerate(self.rows):
            Grid.ensure_capacity(r, at)
            r.append(GridSquare())

    def grow(self, axis: str) -> None:
        _grow_on_axis(self, axis)


# Style: functions on structs of data
def grow_grid_by_row(g: Grid):
    g.rows.append([GridSquare() for _ in range(g.n_columns)])


def grow_grid_by_column(g: Grid):
    g.insert_column(at=g.n_columns)


def _grow_on_axis(self: Grid, axis: str) -> None:
    "Growing out an access"
    if not isinstance(axis, str):
        raise TypeError(f"Expected {axis!r}")
    if axis not in GridAxis.valid_choices:
        raise ValueError(f"Value {axis!r} not of valid choices {GridAxis.valid_choices!r}")
    if axis == 'row':
        grow_grid_by_row(self)
    elif axis == 'column':
        grow_grid_by_column(self)