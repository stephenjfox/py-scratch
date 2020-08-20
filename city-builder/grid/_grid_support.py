from ._grid import GridSquare
from typing import List


def grid_cells(length: int) -> List[GridSquare]:
    return [GridSquare() for _ in range(length)]