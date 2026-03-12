
brojevi=[]
while True:
    unos=(input("unesi broj ili Done za kraj "))
    if(unos=="Done"):
        print ("Kraj")
        break
    
    try:
        unos = float(unos)
        brojevi.append(unos)
    except:
        print("Unesena vrijednost nije broj")

        
print(len(brojevi))
print(sum(brojevi)/len(brojevi))
print(min(brojevi))
print(max(brojevi))