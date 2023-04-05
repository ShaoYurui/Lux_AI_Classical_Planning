(define (problem pb_logistics)
    (:domain logistics)
    
    (:objects
        b - robot
        g - gold_mine 
		loc_0_0 loc_0_1 loc_0_2 loc_0_3 loc_1_0 loc_1_1 loc_1_2 loc_1_3 loc_2_0 loc_2_1 loc_2_2 loc_2_3 loc_3_0 loc_3_1 loc_3_2 loc_3_3 - tiles 
 	)

    (:init
        (at b loc_0_0)
        (at g loc_3_3) 
		(right loc_0_0 loc_0_1) (right loc_0_1 loc_0_2) (right loc_0_2 loc_0_3) (right loc_1_0 loc_1_1) (right loc_1_1 loc_1_2) (right loc_1_2 loc_1_3) (right loc_2_0 loc_2_1) (right loc_2_1 loc_2_2) (right loc_2_2 loc_2_3) (right loc_3_0 loc_3_1) (right loc_3_1 loc_3_2) (right loc_3_2 loc_3_3) 
		(left loc_0_1 loc_0_0) (left loc_0_2 loc_0_1) (left loc_0_3 loc_0_2) (left loc_1_1 loc_1_0) (left loc_1_2 loc_1_1) (left loc_1_3 loc_1_2) (left loc_2_1 loc_2_0) (left loc_2_2 loc_2_1) (left loc_2_3 loc_2_2) (left loc_3_1 loc_3_0) (left loc_3_2 loc_3_1) (left loc_3_3 loc_3_2) 
		(down loc_0_0 loc_1_0) (down loc_0_1 loc_1_1) (down loc_0_2 loc_1_2) (down loc_0_3 loc_1_3) (down loc_1_0 loc_2_0) (down loc_1_1 loc_2_1) (down loc_1_2 loc_2_2) (down loc_1_3 loc_2_3) (down loc_2_0 loc_3_0) (down loc_2_1 loc_3_1) (down loc_2_2 loc_3_2) (down loc_2_3 loc_3_3) 
		(up loc_1_0 loc_0_0) (up loc_1_1 loc_0_1) (up loc_1_2 loc_0_2) (up loc_1_3 loc_0_3) (up loc_2_0 loc_1_0) (up loc_2_1 loc_1_1) (up loc_2_2 loc_1_2) (up loc_2_3 loc_1_3) (up loc_3_0 loc_2_0) (up loc_3_1 loc_2_1) (up loc_3_2 loc_2_2) (up loc_3_3 loc_2_3) 
	)

    (:goal
        (and (at b loc_0_0) (has_gold))
    )
)
