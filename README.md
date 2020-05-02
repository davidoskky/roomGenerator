# Random room generator for Dwarf Fortress

This program generates a random pattern of rooms in a square space.

It outputs the results in csv format, so that the rooms can be created with
Quickfort or digfort.

All the generated rooms are in contact with the side of the square, therefore
there won't be any room trapped in the middle.
There is no limitation to the room size, therefore you might obtain huge rooms
near 1 tile wide rooms.
All rooms are divided by 1 tile walls from the other rooms.

A preview of the generated pattern is outputed to the terminal, so if you don't
like the result you can immediately run the program again and overwrite the
results.

In the preview each different room is assigned a different number, the walls
are represented with 0.

In order to run the program you must insert three arguments:

- Dimension of the square
- Numer of rooms
- Filename of the output

```
python roomGenerator.py 40 35 out.csv
```

In order to run the program you need python installed on your system, [you can
find it here](https://wiki.python.org/moin/BeginnersGuide/Download)
