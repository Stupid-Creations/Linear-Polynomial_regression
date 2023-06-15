# import random

def transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

def s_mult(X,scalar):
    return [[x*scalar for x in j] for j in X]

def adds(X,scalar):
    return [[x+scalar for x in j] for j in X]

def sum(X):
    ans = 0
    for i in X:
        for j in i:
            ans += j
    return ans

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
        try:
            result = zero_matrix(get_cols(X),get_rows(Y))
            for i in range(len(X)):
                for j in range(len(Y[0])):
                    for k in range(len(Y)):
                        result[i][j] += X[i][k] * Y[k][j]
            return result
        except:
            raise Exception("Wrong Matrix Shape")
        
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
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
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

# def random_matrix(a,b):
#     return [[random.randint(0,1) for i in range(b)] for j in range(a)]
def zero_matrix(a,b):
    return [[0 for i in range(b)]for j in range(a)]
def get_shape(a):
    return [len(a),len(a[0])]
def get_cols(a):
    return len(a)
def get_rows(a):
    return len(a[0])