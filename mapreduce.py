text = """
Map reduce is simple .Mapreduce is powerful.
"""
mapped = []
for word in text.lower().replace('.', '').split():
    mapped.append((word, 1))

shuffled = {}
for word, count in mapped:
    if word not in shuffled:
        shuffled[word] = []
    shuffled[word].append(count)

reduced = {}
for word, counts in shuffled.items():
    reduced[word] = sum(counts)

for word, count in reduced.items():
    print(f'{word}: {count}')
    
