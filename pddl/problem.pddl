(define (problem pb_logistics)
    (:domain logistics)
    
    (:objects
        b - robot
        g - gold_mine 
		loc_1_2 loc_1_3 loc_1_4 loc_2_2 loc_2_3 loc_2_4 loc_3_2 loc_3_3 loc_3_4 loc_4_2 loc_4_3 loc_4_4 - tiles 
 	)

    (:init
        (at b loc_4_2)
        (at g loc_1_4) 
		(right loc_1_2 loc_2_2) (right loc_1_3 loc_2_3) (right loc_1_4 loc_2_4) (right loc_2_2 loc_3_2) (right loc_2_3 loc_3_3) (right loc_2_4 loc_3_4) (right loc_3_2 loc_4_2) (right loc_3_3 loc_4_3) (right loc_3_4 loc_4_4) 
		(left loc_2_2 loc_1_2) (left loc_2_3 loc_1_3) (left loc_2_4 loc_1_4) (left loc_3_2 loc_2_2) (left loc_3_3 loc_2_3) (left loc_3_4 loc_2_4) (left loc_4_2 loc_3_2) (left loc_4_3 loc_3_3) (left loc_4_4 loc_3_4) 
		(down loc_1_2 loc_1_3) (down loc_1_3 loc_1_4) (down loc_2_2 loc_2_3) (down loc_2_3 loc_2_4) (down loc_3_2 loc_3_3) (down loc_3_3 loc_3_4) (down loc_4_2 loc_4_3) (down loc_4_3 loc_4_4) 
		(up loc_1_3 loc_1_2) (up loc_1_4 loc_1_3) (up loc_2_3 loc_2_2) (up loc_2_4 loc_2_3) (up loc_3_3 loc_3_2) (up loc_3_4 loc_3_3) (up loc_4_3 loc_4_2) (up loc_4_4 loc_4_3) 
	)

    (:goal
        (and (at b loc_4_2) (has_gold))
    )
)
