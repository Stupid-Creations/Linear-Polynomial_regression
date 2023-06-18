import random

def zero_matrix(row,column):
    return [[0 for i in range(column)] for i in range(row)]
def random_matrix(row,column):
    return [[random.random()*random.choice([1,-1]) for i in range(column)] for i in range(row)]
def get_rows(M):
    return len(M)
def get_cols(M):
    return len(M[0])
def get_shape(M):
    return get_rows(M),get_cols(M)
def display_matrix(M):
    for i in M:
        print(i)
    print()
def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
def s_mult(X,scalar):
    return [[x*scalar for x in j] for j in X]
def adds(X,scalar):
    return [[x+scalar for x in j] for j in X]
def subtract(X,Y):
    output = X
    for i in range(len(X)):
        for j in range(len(X[0])):
            output[i][j] = X[i][j]-Y[i][j]
    return output
def add(X,Y):
    output = zero_matrix(get_cols(X),get_rows(X))
    for i in range(get_cols(X)):
        for j in range(get_rows(X)):
            output[i][j] = X[i][j]+Y[i][j]
    return output
def v_m(X):
    return[[i] for i in X]
def m_v(X):
    return[i[0] for i in X]
def hadamard(X,Y):
    a,b = m_v(X),m_v(Y)
    try:
        return v_m([x[0]*x[1] for x in zip(a,b)])
    except:
        raise Exception("Oops! (Hadamard)")
def dot(X,Y):
    if get_cols(X) != get_rows(Y):
        raise ValueError("Wrong shapes :(")
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
def getMatrixDeterminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m,0,c))
    
    return determinant
def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    if get_shape(m)[0] == 1 and get_shape(m)[1] == 1:
        return [[1/m[0][0]]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
def copy_matrix(A):
    a = zero_matrix(get_rows(A),get_cols(A))
    for i in A:
        for j in i:
            a[A.index(i)][i.index(j)] = j
    return a
