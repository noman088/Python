# 6. Write a python program to create a dictionary that contains three dictionaries.
# (nested)
nested_dict = {"nomanDict : ": {'name : ': "Noman", 'age : ': 20, "ghar": "khawaspur"}, 'misterDict : ': {
    'name : ': "Mister", 'age : ': 21, "ghar": "khawaspur"}, 'AarifDict : ': {'name : ': "Arif", 'age : ': 22, "ghar": "Shekhpura"}}
print(type(nested_dict))
print(nested_dict)
print(nested_dict.keys())
for keys in nested_dict:
    print(keys, nested_dict[keys])
