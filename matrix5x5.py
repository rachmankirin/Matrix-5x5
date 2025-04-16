# perkalian matrix 5x5
a = [
    [0,1,2,4,1],
    [0,2,2,1,1],
    [1,0,1,0,2],
	[1,2,1,0,3],
	[2,0,1,0,1]
]

b = [
    [0,2,1,1,0],
    [1,3,0,0,3],
    [1,2,3,4,0],
	[0,1,2,2,4],
	[2,2,1,1,1]
]

c = [[0 for _ in range(5)] for _ in range(5)]

for x in range(5):
    for y in range(5):
        for z in range(5):
            c[x][y] += a[x][z] * b[z][y]

for row in c:
    print(row)