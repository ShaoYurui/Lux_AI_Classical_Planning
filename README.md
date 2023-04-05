# Lux_AI_Classical_Planning
This Repo focus on exploring the use of classical planning to solve a grid world problem

# Installation

From the Python package index (PyPI):

    pip install pyperplan
    
Pyperplan is hosted on GitHub: https://github.com/aibasel/pyperplan

# Usage

edit the `main.py` file to change the grid world size and postion of the robot and gold mine:
```
GRID_WORLD_WIDTH = 10
GRID_WORLD_HEIGHT = 10
GOLD_MINE_POS = (7, 8)
ROBOT_POS = (0, 0)
```
Then run the `main.py` file to generate the action queue
```
python main.py
```
