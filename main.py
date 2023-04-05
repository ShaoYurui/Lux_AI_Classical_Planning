import os
import pyperplan

ROBOT_POS = (6, 3)
GOLD_MINE_POS = (2, 5)

GRID_WORLD_X_MIN = min(GOLD_MINE_POS[0], ROBOT_POS[0])
GRID_WORLD_X_MAX = max(GOLD_MINE_POS[0], ROBOT_POS[0])
GRID_WORLD_Y_MIN = min(GOLD_MINE_POS[1], ROBOT_POS[1])
GRID_WORLD_Y_MAX = max(GOLD_MINE_POS[1], ROBOT_POS[1])
domain_file = "./pddl/domain.pddl"
problem_file = "./pddl/problem.pddl"
solution_file = "./pddl/problem.pddl.soln"


def main():
    generate_problem_file()
    # run pyperplan with terminal command, did not find any useful API guide
    os.system(f"pyperplan {domain_file} {problem_file}")
    parse_solution_file()


def generate_problem_file():
    content = ""
    content = content + getString_problem_file_prefix()
    content = content + getString_problem_file_tiles()
    content = content + getString_problem_file_init_prefix()

    content = content + getString_right_tiles()
    content = content + getString_left_tiles()
    content = content + getString_down_tiles()
    content = content + getString_up_tiles()

    content = content + getString_problem_file_init_endfix()
    content = content + getString_problem_file_endfix()

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


def getString_problem_file_prefix():
    prefix = f"""(define (problem pb_logistics)
    (:domain logistics)
    
    (:objects
        b - robot
        g - gold_mine \n"""
    return prefix


def getString_problem_file_init_prefix():
    prefix = f"""
    (:init
        (at b loc_{ROBOT_POS[0]}_{ROBOT_POS[1]})
        (at g loc_{GOLD_MINE_POS[0]}_{GOLD_MINE_POS[1]}) \n"""
    return prefix


def getString_problem_file_init_endfix():
    endfix = f"""\t)\n"""
    return endfix


def getString_problem_file_endfix():
    endfix = f"""
    (:goal
        (and (at b loc_{ROBOT_POS[0]}_{ROBOT_POS[1]}) (has_gold))
    )
)\n"""
    return endfix


def getString_problem_file_tiles():
    prefix = "\t\t"
    endfix = "- tiles \n \t)\n"
    result = prefix
    for row_id in range(GRID_WORLD_X_MIN, GRID_WORLD_X_MAX + 1):
        for col_id in range(GRID_WORLD_Y_MIN, GRID_WORLD_Y_MAX + 1):
            result = result + f"loc_{row_id}_{col_id} "
    result = result + endfix
    return result


def is_within_grid_world(x, y):
    if GRID_WORLD_X_MIN <= x <= GRID_WORLD_X_MAX and \
            GRID_WORLD_Y_MIN <= y <= GRID_WORLD_Y_MAX:
        return True
    return False


def getString_right_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_X_MIN, GRID_WORLD_X_MAX + 1):
        for y in range(GRID_WORLD_Y_MIN, GRID_WORLD_Y_MAX + 1):
            if is_within_grid_world(x, y + 1):
                result = result + f"(right loc_{x}_{y} loc_{x}_{y + 1}) "
    result = result + "\n"
    return result


def getString_left_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_X_MIN, GRID_WORLD_X_MAX + 1):
        for y in range(GRID_WORLD_Y_MIN, GRID_WORLD_Y_MAX + 1):
            if is_within_grid_world(x, y - 1):
                result = result + f"(left loc_{x}_{y} loc_{x}_{y - 1}) "
    result = result + "\n"
    return result


def getString_down_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_X_MIN, GRID_WORLD_X_MAX + 1):
        for y in range(GRID_WORLD_Y_MIN, GRID_WORLD_Y_MAX + 1):
            if is_within_grid_world(x + 1, y):
                result = result + f"(down loc_{x}_{y} loc_{x + 1}_{y}) "
    result = result + "\n"
    return result


def getString_up_tiles():
    result = "\t\t"
    for x in range(GRID_WORLD_X_MIN, GRID_WORLD_X_MAX + 1):
        for y in range(GRID_WORLD_Y_MIN, GRID_WORLD_Y_MAX + 1):
            if is_within_grid_world(x - 1, y):
                result = result + f"(up loc_{x}_{y} loc_{x - 1}_{y}) "
    result = result + "\n"
    return result


if __name__ == "__main__":
    main()
