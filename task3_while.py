i_kg_price = 1

i_current_kg = 1.0
i_kg_delta = 0.2

while i_current_kg < 1.9:
    i_current_kg = i_current_kg + i_kg_delta
    print("{}kg of sweets costs {}".format(i_current_kg, i_current_kg * i_kg_price))

