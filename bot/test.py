import json
import random

with open(f'opdracht{2}.json', 'r') as file:
    opdracht: dict = json.load(file)


print(type(opdracht))
question_word = random.choice(list(opdracht.keys()))
question = f"Как переводится <b>{question_word}</b>:"
print(question)
data = [opdracht.pop(question_word), random.choice(list(opdracht.values())), random.choice(list(opdracht.values())), random.choice(list(opdracht.values()))]
print(data)
