brus = 24.90
smørbrød = 45
banan = 8.50

print("totalsummen av varene er", brus+smørbrød+banan, "kr")
print("totalsummen av varene med 25% mva er", (brus+smørbrød+banan)*1.25, "kr")
print("Pris per person hvis denne blir delt på fire er", (brus+smørbrød+banan)/4, "kr")
print("Prisforkjellen mellom den dyreste og billigste varen er", smørbrød-banan, "kr")
print(type(smørbrød+brus))
print(type((brus+smørbrød+banan)/4))



# --- Refleksjon ---
# 1. Når jeg la dem sammen så ble det et desimaltall, og når jeg brukte type() så kom det som datatypen float.
# 2. Datatypen ble float altså et desimaltall, og nei jeg ble ikke overasket siden når man regner på det selv blir det riktig.
# 3. Jeg tror det er en fordel siden da slipper du å skrive det samme tallet inn flere tusen ganger, og hvis prisen endrer seg så kan du bare endre tallet til variabelen så endres det over alt i koden. Det er også lettere å lese koden når man bruker variabler, og det gjør det enklere å forstå hva som skjer i koden.

