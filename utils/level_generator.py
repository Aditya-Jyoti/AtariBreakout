from src.Brick import Brick

import random


def generate_level(
    num_cells_row: int,
    brick_cells_col: int,
    brick_cells_row: int,
    cell_size: int,
    single_hit_brick_colour: str,
    double_hit_brick_colour: str,
    triple_hit_brick_colour: str,
    padding: int,
    border_colour: str,
) -> list[Brick]:

    num_rows = random.randint(4, 10)
    bricks_in_row = num_cells_row // brick_cells_row

    bricks: list[Brick] = []

    for idx in range(num_rows * bricks_in_row):
        row = idx // bricks_in_row
        col = idx % bricks_in_row

        hits = random.randint(1, 3)
        colour = (
            single_hit_brick_colour
            if hits == 1
            else double_hit_brick_colour if hits == 2 else triple_hit_brick_colour
        )

        bricks.append(
            Brick(
                colour=colour,
                x=col * brick_cells_row * cell_size + (padding // 2),
                y=row * brick_cells_col * cell_size + (padding // 2),
                cells_col=brick_cells_col,
                cells_row=brick_cells_row,
                cell_size=cell_size,
                border_colour=border_colour,
                strength=hits,
            )
        )

    return bricks
