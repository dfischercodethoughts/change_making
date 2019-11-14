import numpy as np

def change_making(denoms,max_coins,total_val):
    A = np.zeros((max_coins+1,total_val))
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = False
    A[0][0] =True
    # for i in range(len(A)):
    #     A[i][0] = True
    for i in range(len(A)):
        for j in range(len(A[0])):
            for denom in denoms:
                if A[i][j] and j+denom-1 < total_val and i< max_coins:
                    A[i+1][j+denom-1] = True

    for i in range(len(A)):
        if A[i][total_val-1]:
            return True
    return False


if __name__ == "__main__":
    denoms = [5,10]
    max = 6
    val = 50
    print(change_making(denoms,max,val))
