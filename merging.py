domestic_animals = []
wild_animals = []

print("----Enter 4 domestic animals below----")
for a in range(4):
    animal = input(f"  {a+1}. ")
    domestic_animals.append(animal)
print("\nDomestic Animals", domestic_animals)

print("\n----Enter 4 wild animals below----")
for a in range(4):
    animal = input(f"  {a+1}. ")
    wild_animals.append(animal)
print("\nWild Animals", wild_animals)

All_animals = domestic_animals + wild_animals
All_animals.sort()
print("\nAll animals", All_animals)
