E = [4,2,3,1]
A = [2,1,0,0]

R = [
    [2,0,0,1], #PA
    [1,0,1,0], #PB
    [2,1,0,0] #PC
    ]
C = [
    [0,0,1,0],
    [2,0,0,1],
    [0,1,2,0]
]

def verificarBloqueo (): 
    for Ri in R:
        for Rj in Ri:
            if(Rj != -1):
                print Rj
                return True
    return False

def addition(Ri,Ci):
    return Ri + Ci


def subtract(Ri,Ai):
    return Ri -  Ai

def eliminarRecursos(l):
    return -1

def verificarmenorIgual(Ri,Ai): 
    return Ri <= Ai


def comparar ():
    for i in range(0,len(R)):
        counter = 0
        for j in range(0,len(R[i])):
            if(R[i][j] == -1):
                break
            if (verificarmenorIgual(R[i][j],A[j])):
                counter = counter +1
            if (counter == 4):
                return i
    return -1

def main ():
    for proceso in procesos:
        for p in proceso:
            print p


if __name__ == "__main__":

    while True:
        n = comparar()
        if (n == -1 and verificarBloqueo()):
            print "bloqueo"
            print n
            break
        if (n == -1 ): 
            print "solucion"
            break
        C[n] = map(addition,R[n],C[n])
        A = map(subtract,A,R[n])
        A = map(addition,C[n],A)
        R[n] = map(eliminarRecursos,R[n])
        C[n] = map(eliminarRecursos,R[n])
        print ('R = ', R)
        print ('C = ', C)
        print ('A =' , A)
        