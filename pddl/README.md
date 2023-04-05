#Appendix PDDL for classical planning: 


We then can model this problem in PDDL for classical planning: 
```
Objects: 
    robot (robot)
    gold_mine (gold_mine)
    location(loc_0_0)
    location(loc_0_1)
    ……

Predicates:
    at (object, location)
    right (location, location_at_right)
    left (location, location_at_left)
    up (location, location_on_top)
    down ( location, location_below)
    has_gold(object)

Initial State:
    at (robot, loc_6_3) AND
    at (gold_mine, loc_2_5) AND
    right (loc_0_0 loc_0_1) AND right (loc_0_1 loc_0_2) AND ……
    left (loc_0_1 loc_0_0) AND left (loc_0_2 loc_0_1) AND ……
    down (loc_0_0 loc_1_0) AND down (loc_0_1 loc_1_1) AND ......
    up (loc_1_0 loc_0_0) AND up (loc_1_1 loc_0_1) AND ……

Goal State:
    at (robot, loc_3_3) AND has_gold (robot)

Action: 
    move_right
    parameters: (robot, loc-from, loc-to)
    precondition: (at (robot, loc-from)) AND (right (loc-from, loc-to))
    effect: ¬(at (robot, loc-from)) AND (at (robot, loc-to))

    move_left
    parameters: (robot, loc-from, loc-to)
    precondition: (at (robot, loc-from)) AND (left (loc-from, loc-to))
    effect: ¬(at (robot, loc-from)) AND (at (robot, loc-to))
    
    move_up
    parameters: (robot, loc-from, loc-to)
    precondition: (at (robot, loc-from)) AND (up (loc-from, loc-to))
    effect: ¬(at (robot, loc-from)) AND (at (robot, loc-to))
    
    move_down
    parameters: (robot, loc-from, loc-to)
    precondition: (at (robot, loc-from)) AND (down (loc-from, loc-to))
    effect: ¬(at (robot, loc-from)) AND (at (robot, loc-to))

    dig
    parameters: (robot, loc-from)
    precondition: (at (robot, loc-from) AND (at (gold_mine, loc-from))
    effect: (has_gold(robot))
```
With that we can run the planner and get the following solution:
```
move_right  (robot, loc_6_3 loc_6_4)
move_right  (robot, loc_6_4 loc_6_5)
move_up  (robot, loc_6_5 loc_5_5)
move_up  (robot, loc_5_5 loc_4_5)
move_up  (robot, loc_4_5 loc_3_5)
move_up  (robot, loc_3_5 loc_2_5)
move_dig  (robot, loc_2_5)
move_left  (robot, loc_2_5 loc_2_4)
move_left  (robot, loc_2_4 loc_2_3)
move_down  (robot, loc_2_3 loc_3_3)
move_down  (robot, loc_3_3 loc_4_3)
move_down  (robot, loc_4_3 loc_5_3)
move_down  (robot, loc_5_3 loc_6_3)
```

