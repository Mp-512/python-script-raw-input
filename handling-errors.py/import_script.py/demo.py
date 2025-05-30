import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores) # type: ignore
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original mean:", mean, "New mean:", mean_c)

print(__name__)
print(uf.__name__)