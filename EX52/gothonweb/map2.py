from maps import Scene

forest = Scene("Forest", "forest",
"""
Wuuhu you found a forest on mars...
""", "run, jump")

mountains = Scene("Mountains", "mountains",
"""
you reached the mountains..
""", "make a call, jump")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it!
""", None)

the_end_loser = Scene("...", "the_end_loser",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""", None)

generic_death = Scene("Death...", "death", "You died. You kinda suck at this. Your mom would be proud...if she were smarter.", None)

# Define the action commands available in each Scene
forest.add_paths({
    'run': the_end_winner,
    'jump': the_end_loser
})

mountains.add_paths({
    'make a call': the_end_winner,
    'jump': the_end_loser,
    '*': forest,
})

SCENES = {
    forest.urlname: forest,
    mountains.urlname: mountains,

}
START = forest
