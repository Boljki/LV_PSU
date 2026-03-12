
ime=input("Ime datoteke ")
f=open(ime)
suma=0
mbox.txtbroj=0
for linija in f:
    if linija.startswith("X-DSPAM-Confidence:"):
        dio = linija.split(":")
        vrijednost = float(dio[1])
        suma = suma + vrijednost
        broj = broj + 1

prosjek = suma / broj
print("Average X-DSPAM-Confidence:", prosjek)