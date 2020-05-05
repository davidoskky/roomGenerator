import random
import sys
import csv

def check_available(matrix, x, y, room):
    available = True

    if matrix[x][y] != 0:
        available = False

    for i in [-1, 0, 1]:
        xn = x + i
        if xn < 0:
            xn = 0
        elif xn > len(matrix[0])-1:
            xn = len(matrix[0])-1
        for j in [-1, 0, 1]:
            yn = y + j
            if yn < 0:
                yn = 0
            elif yn > len(matrix[0])-1:
                yn = len(matrix[0])-1

            if matrix[xn][yn] != 0 and matrix[xn][yn] != room:
                available = False

    return available

def check_expandable(matrix, rooms, room):
    pixels = []
    for pixel in rooms[room]:
        x = pixel[0]
        y = pixel[1]
        expandable = False

        for i in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            xn = x + i[0]
            yn = y + i[1]

            if xn < 0:
                xn = 0
            elif xn > len(matrix[0])-1:
                xn = len(matrix[0])-1
            if yn < 0:
                yn = 0
            elif yn > len(matrix[0])-1:
                yn = len(matrix[0])-1

            if check_available(matrix, xn, yn, room):
                    expandable = True

        if expandable:
            pixels.append(tuple(pixel))

    return pixels


# Reads a shape from a csv file
# accepts d as the outer shape
# Returns a matrix with 0 inside the shape
# -1 outside the shape
def read_shape(filename):
    fileHandler = open(filename)
    output = list(csv.reader(fileHandler))
    fileHandler.close()

    # Convert to numeric matrix
    for i in range(len(output)):
        for j in range(len(output[i])):
            if output[i][j] == 'd':
                output[i][j] = -1
            elif output[i][j] == '':
                output[i][j] = 0
            else:
                print "Error, unrecognized character in input: " + output[i][j]
                output[i][j] = 0

    # Find the outer limits of the shape and set those to -1
    for i in range(len(output)):
        # Contiguos blocks are counted as one
        contiguos = False
        counter = 0
        for j in range(len(output[i])):
            if output[i][j] == -1 and not contiguos:
                counter += 1
                contiguos = True
            elif output[i][j] == 0:
                contiguos = False
                if counter % 2 ==0:
                    output[i][j] = -1


        # If there is a cuspid point, the whole line is
        # not available
        if counter == 1:
            for j in range(len(output[i])):
                output[i][j] = -1

    return output


# Returns a list of tuples, each one contains the
# coordinates of one point on the perimeter of the shape
# Matrix must be a 2d list, containing a shape obtained
# with the read_shape method
def get_perimeter(matrix):
    perimeter = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            available = False
            if matrix[i][j] == 0:
                for x in [-1, 0, 1]:
                    xn = i + x
                    if xn < 0:
                        xn = 0
                    elif xn > len(matrix[0])-1:
                        xn = len(matrix[0])-1

                    for y in [-1, 0, 1]:
                        yn = j + y
                        if yn < 0:
                            yn = 0
                        elif yn > len(matrix[0])-1:
                            yn = len(matrix[0])-1

                        if matrix[xn][yn] == -1:
                            available = True

                if available:
                    perimeter.append(tuple((i,j)))

    return perimeter


def grow(matrix, rooms, room):
    expandable = check_expandable(matrix, rooms, room)
    if not expandable:
        return False

    pixel = random.randint(0,len(expandable)-1)
    x = expandable[pixel][0]
    y = expandable[pixel][1]

    completed = False
    while not completed:
        move = random.choice([[-1, 0], [1, 0], [0, 1], [0, -1]])
        xn = x + move[0]
        yn = y + move[1]

        if xn < 0:
            xn = 0
        elif xn > len(matrix[0])-1:
            xn = len(matrix[0])-1

        if yn < 0:
            yn = 0
        elif yn > len(matrix[0])-1:
            yn = len(matrix[0])-1

        if check_available(matrix, xn, yn, room):
            completed = True
            rooms[room].append((xn, yn))
            matrix[xn][yn] = room
            return True


if len(sys.argv) < 4:
    sys.exit('Usage: roomgen.py [dimension of the square] [number of rooms] [output file]')

N = int(sys.argv[1])
nroom = 1 + int(sys.argv[2])
filename = sys.argv[3]
rooms = []
roomfinished = [False for i in xrange(nroom)]

for i in range(nroom):
    rooms.append([])
roomfinished[0] = True

matrix = [[ 0 for i in xrange(N)] for j in xrange(N)]
outputMatrix = [[ '' for i in xrange(N)] for j in xrange(N)]
room = 1
while room < nroom:
    s = random.randint(1,4)
    k = random.randint(0,N-1)

    if s == 1:
        s = 0
    elif s == 2:
        s = N-1
    elif s == 3:
        s = k
        k = 0
    elif s == 4:
        s = k
        k = N-1

    if check_available(matrix, s, k, room):
        matrix[s][k] = room
        rooms[room].append((s, k))
    else:
        room -= 1

    room += 1

expandable = True

while expandable:
    for room in range(1, nroom):
        if not roomfinished[room]:
            finished = grow(matrix, rooms, room)
            if not finished:
                roomfinished[room] = True
                if all(roomfinished):
                    expandable = False

for row in matrix:
    for val in row:
        print '{:4}'.format(val),
    print

# Write output for quickfort
for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            outputMatrix[i][j] = 'd'

with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerows(outputMatrix)
