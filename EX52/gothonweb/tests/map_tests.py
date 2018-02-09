from nose.tools import *
from map47 import *

def test_room():
    gold = Scene("GoldRoom", "goldroom",
                """This room has gold in it you can grab. There's a door to the north.""")
    assert_equal(gold.title, "GoldRoom")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Scene("Center", "center", "Test room in the center.")
    north = Scene("North", "north", "Test room in the north.")
    south = Scene("South", "south", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "You can go west and down a hole.")
    west = Scene("Trees", "trees", "There are trees here, you can go east.")
    down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), generic_death)
    assert_equal(START.go('dodge!'), generic_death)
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)

#def setup():
    #print "Running setup for automated tests!"

#def teardown():
    #print "Running teardown for automated tests!"

#def test_basic():
    #print "Running the first and only automated test!"
