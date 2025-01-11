def calculate_structure_sum(data):
    sum_ = 0
    for element in data:
        if isinstance(element, (int, float)):
            sum_ += element
        elif isinstance(element, str):
            sum_ += len(element)
        elif isinstance(element,(list,tuple,set)):
            sum_ += calculate_structure_sum(element)
        elif isinstance(element, dict):
            sum_ += calculate_structure_sum(element.keys())
            sum_ += calculate_structure_sum(element.values())
    return sum_

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
