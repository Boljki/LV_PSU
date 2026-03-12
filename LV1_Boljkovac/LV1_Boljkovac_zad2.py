
try:
    print("Unesi vrijednost izmedu 0.0 i 1.0")
    x=float(input())
    if(x<0.0 or x>1.0):
        print("Unesena vrijednost nije u zadanom intervalu")
    elif(x>=0.9):
        print("A")
    elif(x>=0.8):
        print("B")
    elif(x>=0.7):
        print("C")
    elif(x>=6):
        print("D")
    elif(x<0.6):
        print("F")

except:
    print("Niste upisali broj")
    