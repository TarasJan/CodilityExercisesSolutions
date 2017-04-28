

odd one out
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    B=set(A) 
    for val in B: 
        if A.count(val)%2==1:
            return val

shifting elements
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7
    length = len(A)
    rot = K%length or length == 0
    if rot==0 or length == 0:
        return A
    
    half = A[length-rot:length]
    half.extend(A[0:length-rot])
    return half

    frog jump

    # you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(X, Y, D):
    # write your code in Python 2.7
    if(X==Y):
        return 0
    delta = Y-X
    val = delta/D
    if (delta%D >0):
        val+=1
    return val


# missing element

# solution 1 - crappy but leeme see 60% 100 correct 20% performance
def solution(A):
    # write your code in Python 2.7
    if(len(A)==0):
        return 1
    vals = range(1,(len(A)+2))

    for elem in vals:
        if elem not in A:
            return elem

# bettur ? with sums?
