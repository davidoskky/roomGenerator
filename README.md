# Random room generator for Dwarf Fortress

This program generates a random pattern of rooms in a shape.

It outputs the results in csv format, so that the rooms can be created with
Quickfort or digfort.

All the generated rooms are in contact with the side of the shape, therefore
there won't be any room trapped in the middle.
There is no limitation to the room size, therefore you might obtain huge rooms
near 1 tile wide rooms.
All rooms are divided by 1 tile walls from the other rooms.

A preview of the generated pattern is outputed to the terminal, so if you don't
like the result you can immediately run the program again and overwrite the
results.

In the preview each different room is assigned a different number, the walls
are represented with 0.
-1 represents the shape inserted.

If you don't provide a shape, you can use the -d argument to create a square
shape, the program will generate the rooms inside the shape, therefore the
pattern will be smaller than the provided shape.
The shape must be in a csv file, containing the character 'd' at the boundary
of the shape.
The shape can be complex, with concave and convex points, though the program
may have some errors if you insert shapes inside of other shapes.
Generally polygons inside other polygons will work, while open lines will
generate problems.
In order for the inner polygon to work correctly it must have an even number of
groups of d's on the rows: the border of an inner square will not be recognized
if defined as 'dddddd' but it will if it is as 'ddd dd'.

i.e. A circle is filled, a circle with a wall in the middle will not work; a
circle with another circle in the middle will work, the annulus will be filled.

In order to run the program you must insert three arguments:

- Dimension of a square
- Shape to fill
- Numer of rooms
- Filename of the output

```
python roomGenerator.py -d 40 35 out.csv
python roomGenerator.py  -s circle.csv 35 out.csv
```

In order to run the program you need python installed on your system, [you can
find it here](https://wiki.python.org/moin/BeginnersGuide/Download)
