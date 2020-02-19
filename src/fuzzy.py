from fuzzypy.variables import *

TA = FuzzyVariable()
fria = TriFunc(-30, 0, 30)
quente = TriFunc(0, 30, 60)

LOT = FuzzyVariable()
vazia = TriFunc(-60, 0, 60)
cheia = TriFunc(0, 60, 120)

POT = FuzzyVariable()
baixa = TriFunc(-50, 0, 50)
media = TriFunc(0, 50, 100)
alta = TriFunc(50, 100, 150)

regras = []
regras.append(FuzzyRule([TA.is_(fria), LOT.is_(vazia)], POT, baixa))
regras.append(FuzzyRule([TA.is_(fria), LOT.is_(cheia)], POT, media))
regras.append(FuzzyRule([TA.is_(quente), LOT.is_(vazia)], POT, media))
regras.append(FuzzyRule([TA.is_(quente), LOT.is_(cheia)], POT, alta))

TA.value = 25
LOT.value = 45

v = apply_defuzzyfy_COG(regras)

print(POT.value)
