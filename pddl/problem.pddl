(define (problem pb_logistics)
    (:domain logistics)
    
    (:objects
        b - robot
        g - gold_mine 
		loc_2_3 loc_2_4 loc_2_5 loc_3_3 loc_3_4 loc_3_5 loc_4_3 loc_4_4 loc_4_5 loc_5_3 loc_5_4 loc_5_5 loc_6_3 loc_6_4 loc_6_5 - tiles 
 	)

    (:init
        (at b loc_6_3)
        (at g loc_2_5) 
		(right loc_2_3 loc_2_4) (right loc_2_4 loc_2_5) (right loc_3_3 loc_3_4) (right loc_3_4 loc_3_5) (right loc_4_3 loc_4_4) (right loc_4_4 loc_4_5) (right loc_5_3 loc_5_4) (right loc_5_4 loc_5_5) (right loc_6_3 loc_6_4) (right loc_6_4 loc_6_5) 
		(left loc_2_4 loc_2_3) (left loc_2_5 loc_2_4) (left loc_3_4 loc_3_3) (left loc_3_5 loc_3_4) (left loc_4_4 loc_4_3) (left loc_4_5 loc_4_4) (left loc_5_4 loc_5_3) (left loc_5_5 loc_5_4) (left loc_6_4 loc_6_3) (left loc_6_5 loc_6_4) 
		(down loc_2_3 loc_3_3) (down loc_2_4 loc_3_4) (down loc_2_5 loc_3_5) (down loc_3_3 loc_4_3) (down loc_3_4 loc_4_4) (down loc_3_5 loc_4_5) (down loc_4_3 loc_5_3) (down loc_4_4 loc_5_4) (down loc_4_5 loc_5_5) (down loc_5_3 loc_6_3) (down loc_5_4 loc_6_4) (down loc_5_5 loc_6_5) 
		(up loc_3_3 loc_2_3) (up loc_3_4 loc_2_4) (up loc_3_5 loc_2_5) (up loc_4_3 loc_3_3) (up loc_4_4 loc_3_4) (up loc_4_5 loc_3_5) (up loc_5_3 loc_4_3) (up loc_5_4 loc_4_4) (up loc_5_5 loc_4_5) (up loc_6_3 loc_5_3) (up loc_6_4 loc_5_4) (up loc_6_5 loc_5_5) 
	)

    (:goal
        (and (at b loc_6_3) (has_gold))
    )
)
