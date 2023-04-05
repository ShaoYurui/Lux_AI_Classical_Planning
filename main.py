import os
import pyperplan

GRID_WORLD_WIDTH = 10
GRID_WORLD_HEIGHT = 10
GOLD_MINE_POS = (2, 5)
ROBOT_POS = (6, 3)

domain_file = "./pddl/domain.pddl"
problem_file = "./pddl/problem.pddl"
solution_file = "./pddl/problem.pddl.soln"


def main():
    generate_task_file()
    os.system(f"pyperplan {domain_file} {problem_file}")
    parse_solution_file()


def getString_task_file_prefix():
    prefix = f"""(define (problem pb_logistics)
    (:domain logistics)
    
    (:objects
        b - robot
        g - gold_mine \n"""
    return prefix


def getString_task_file_init_prefix():
    prefix = f"""
    (:init
        (at b loc_{ROBOT_POS[0]}_{ROBOT_POS[1]})
        (at g loc_{GOLD_MINE_POS[0]}_{GOLD_MINE_POS[1]}) \n"""
    return prefix


def getString_task_file_init_endfix():
    endfix = f"""\t)\n"""
    return endfix


def getString_task_file_endfix():
    endfix = f"""
    (:goal
        (and (at b loc_{ROBOT_POS[0]}_{ROBOT_POS[1]}) (has_gold))
    )
)\n"""
    return endfix


def getString_task_file_tiles():
    prefix = "\t\t"
    endfix = "- tiles \n \t)\n"
    result = prefix
    for row_id in range(GRID_WORLD_WIDTH + 1):
        for col_id in range(GRID_WORLD_HEIGHT + 1):
            result = result + f"loc_{row_id}_{col_id} "
    result = result + endfix
    return result


def is_within_grid_world(x, y):
    if 0 <= x <= GRID_WORLD_WIDTH and 0 <= y <= GRID_WORLD_HEIGHT:
        return True
    return False


def getString_right_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_WIDTH + 1):
        for y in range(GRID_WORLD_HEIGHT + 1):
            if is_within_grid_world(x, y + 1):
                result = result + f"(right loc_{x}_{y} loc_{x}_{y + 1}) "
    result = result + "\n"
    return result


def getString_left_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_WIDTH + 1):
        for y in range(GRID_WORLD_HEIGHT + 1):
            if is_within_grid_world(x, y - 1):
                result = result + f"(left loc_{x}_{y} loc_{x}_{y - 1}) "
    result = result + "\n"
    return result


def getString_down_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_WIDTH + 1):
        for y in range(GRID_WORLD_HEIGHT + 1):
            if is_within_grid_world(x + 1, y):
                result = result + f"(down loc_{x}_{y} loc_{x + 1}_{y}) "
    result = result + "\n"
    return result


def getString_up_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_WIDTH + 1):
        for y in range(GRID_WORLD_HEIGHT + 1):
            if is_within_grid_world(x - 1, y):
                result = result + f"(up loc_{x}_{y} loc_{x - 1}_{y}) "
    result = result + "\n"
    return result


def generate_task_file():
    content = ""
    content = content + getString_task_file_prefix()
    content = content + getString_task_file_tiles()
    content = content + getString_task_file_init_prefix()

    content = content + getString_right_tiles()
    content = content + getString_left_tiles()
    content = content + getString_down_tiles()
    content = content + getString_up_tiles()

    content = content + getString_task_file_init_endfix()
    content = content + getString_task_file_endfix()

    f = open(problem_file, "w")
    f.write(content)
    f.close()


def parse_solution_file():
    prefix = "\nAction Queue = ["
    endfix = "]\n"
    result = prefix
    f = open(solution_file, "r")
    content = f.readlines()
    for line in content:
        # extract the action only from the line, discard other information
        result = result + (line.split()[0][1:]) + ", "
    result = result[:-2] + endfix
    print(result)


if __name__ == "__main__":
    main()
