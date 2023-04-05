# Lux_AI_Classical_Planning
This repository explores the use of classical planning to solve a grid world problem where a robot is at position (x1,y1) and a gold mine is at position (x2,y2). The goal is for the robot to reach the gold mine, dig for resources, and return to the original position. In this project, `Pyperplan`, a lightweight STRIPS planner written in Python, is used for the planning process. This tool is designed for teaching and prototyping purposes.

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
