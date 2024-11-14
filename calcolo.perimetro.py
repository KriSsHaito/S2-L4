import math

print(("Ciao, calcoleró il perimetro delle figure che mi chiedi."))

print("Che figura stai prendendo in esame?")
print("1. Quadrato")
print("2. Cerchio")
print("3. Rettangolo")

scelta = input("[1/2/3]: ")

if scelta == "1":
    lato = float(input("...Davvero non sai farlo?\n Dimmi il valore del lato va...\n"))
    risultato = 4 * lato
    print(f"Il tuo risultato é: {risultato: .0f}")

elif scelta == "2":
    raggio = float(input("Dimmi il valore del raggio:\n"))
    risultato = raggio * math.pi * 2
    print(f"La tua circonferenza é: {risultato: .2f}")

elif scelta == "3":
    base = float(input("Dimmi il valore della tua base:\n"))
    altezza = float(input("Dimmi il valore della tua altezza:\n"))
    risultato = base * altezza
    print(f"Il tuo risultato é: {risultato: .0f}")
else:
    print("Non farmi perdere tempo dai, scegli un opzione valida.")