sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "prueba": 100}
sensors ["dinosaurio", "personas"] = 0

nada = {}
nada ["hola"] = 10

num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"], "geografìa": "Angel", "cursos": 3}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
user_ids["hola"] = 0

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"

drinks = ["expresso", "chai", "decaf", "satisfaction"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

print(translations)
print(sensors)
print(subtotal_to_total)
print(students_in_classes)
print(nada)
print(user_ids)
print(oscar_winners)
