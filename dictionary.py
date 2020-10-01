dict = {"joy": "happiness", "rapid":"quick", "high":"pick", "stranger":"unknown person", "swap":"interchange" }

print("add word to get meaning: ")
search = input()
if search in dict:
    print(f"\n {search} = { dict[search]} ")
else:
  print("word that has to be searched not found")
