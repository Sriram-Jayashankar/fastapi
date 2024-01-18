
#input 2 values number of rows and number of columns then take in values to build a 2d matrix of these dimensions

def matrix(rows,columns):
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(columns):
            row.append(int(input()))
        matrix.append(row)
    return matrix

#input 2 values from user and send those values to matrix funcion

rows=int(input())
columns=int(input())
matrix=matrix(rows,columns)
print(matrix)
