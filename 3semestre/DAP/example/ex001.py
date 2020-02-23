import json
x = '{"nome": "Joao da Silva","idade": "20","cidade": "Sao Paulo"}'
#y = json.dumps(x)
# print(y)
print("-" * 20)
y = json.loads(x)
type(y)
print(y)

print(y["idade"])
