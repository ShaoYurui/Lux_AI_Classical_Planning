import os
import pyperplan

def main():
    domain_file = "./pddl/domain.pddl"
    problem_file = "./pddl/task.pddl"

    os.system(f"pyperplan {domain_file} {problem_file}")


if __name__ == "__main__":
    main()
