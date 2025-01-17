# TES 1
matrix = [
     [5,3,2,1],
     [1,2,10,1],
     [4,3,2,20],
     [2,1,2,1]
]
# TES 2
matrix2 = [
     [5,3,2,1,5],
     [1,4,5,1,7],
     [4,3,4,20,8],
     [2,1,2,9,8],
     [2,1,2,4,8]
 ]   

def get_maximum_movement(matrix):
    # rumus : ndim + ndim - 2
    return len(matrix) + len(matrix) - 2

def get_dim(matrix):
    x = len(matrix[0])
    y = len(matrix)
    return (x,y)
    
def find_best_path(matrix):
    ndim = get_dim(matrix)
    
    path = [(0,0)]
    a,b = 0,0
    for _ in range(get_maximum_movement(matrix)):
        if a < ndim[0] - 1:
            bottom = matrix[a+1][b]
        else:
            bottom = -1
        if b < ndim[1] - 1:
            right = matrix[a][b+1]
        else: 
            right = -1


        if right < bottom:
            a += 1
            path.append(tuple([a,b]))
        else:
            b += 1
            path.append(tuple([a,b]))
            
    return path

def get_value_of_best_path(matrix):
    res = 0
    list_path = find_best_path(matrix)
    for p in list_path:
        res += matrix[p[0]][p[1]]
    return {
        'jalur': list_path,
        'Jumlah air maksimal': res
    }


print( get_value_of_best_path(matrix) )
print( get_value_of_best_path(matrix2) )


