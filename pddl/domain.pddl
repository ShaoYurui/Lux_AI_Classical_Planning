(define (domain logistics)

  (:requirements :strips :typing)

  (:types
        physobj location - object
        robot gold_mine - physobj
        tiles - location
  )

  (:predicates
		(at ?obj - physobj ?loc - location)
		(right ?loc-from - location ?loc-to - location)
		(left ?loc-from - location ?loc-to - location)
		(up ?loc-from - location ?loc-to - location)
		(down ?loc-from - location ?loc-to - location)
		(has_gold)
  )


 (:action right
    :parameters (?b - robot ?loc-from - location ?loc-to - location)
    :precondition (and (at ?b ?loc-from) (right ?loc-from ?loc-to))
    :effect (and (not (at ?b ?loc-from)) (at ?b ?loc-to))
 )

 (:action left
    :parameters (?b - robot ?loc-from - location ?loc-to - location)
    :precondition (and (at ?b ?loc-from) (left ?loc-from ?loc-to))
    :effect (and (not (at ?b ?loc-from)) (at ?b ?loc-to))
 )

 (:action down
    :parameters (?b - robot ?loc-from - location ?loc-to - location)
    :precondition (and (at ?b ?loc-from) (down ?loc-from ?loc-to))
    :effect (and (not (at ?b ?loc-from)) (at ?b ?loc-to))
 )

 (:action up
    :parameters (?b - robot ?loc-from - location ?loc-to - location)
    :precondition (and (at ?b ?loc-from) (up ?loc-from ?loc-to))
    :effect (and (not (at ?b ?loc-from)) (at ?b ?loc-to))
 )

 (:action dig
    :parameters (?b - robot ?loc-from - location )
    :precondition (and (at ?b ?loc-from) (at g ?loc-from ))
    :effect (has_gold)
 )
)
