# MapReduce Word Count

A simple Python implementation of the MapReduce paradigm for counting word frequencies in text.

## Overview

This project demonstrates the core concepts of MapReduce through a word counting example. MapReduce is a programming model designed for processing large datasets by dividing the work into two main phases: **Map** and **Reduce**.

## How It Works

The implementation follows the classic MapReduce pattern:

1. **Map Phase**: Transform input data into key-value pairs
2. **Shuffle Phase**: Group data by keys
3. **Reduce Phase**: Aggregate values for each key

### Algorithm Steps

1. **Text Preprocessing**: Convert text to lowercase and remove punctuation
2. **Mapping**: Split text into words and create (word, 1) pairs
3. **Shuffling**: Group identical words together
4. **Reducing**: Sum the counts for each word
5. **Output**: Display word frequencies

## Code Structure

```python
# Sample input text
text = """
Map reduce is simple .Mapreduce is powerful.
"""

# MAP PHASE: Create (word, count) pairs
mapped = []
for word in text.lower().replace('.', '').split():
    mapped.append((word, 1))

# SHUFFLE PHASE: Group by word
shuffled = {}
for word, count in mapped:
    if word not in shuffled:
        shuffled[word] = []
    shuffled[word].append(count)

# REDUCE PHASE: Sum counts for each word
reduced = {}
for word, counts in shuffled.items():
    reduced[word] = sum(counts)

# OUTPUT: Display results
for word, count in reduced.items():
    print(f'{word}: {count}')
```

## Sample Output

```
map: 1
reduce: 1
is: 2
simple: 1
mapreduce: 1
powerful: 1
```

## Key Concepts Demonstrated

- **Parallel Processing Foundation**: While this implementation runs sequentially, it shows how the work could be distributed across multiple machines
- **Fault Tolerance**: The clear separation of phases makes it easy to restart failed operations
- **Scalability**: The pattern scales from small text snippets to massive datasets

## Use Cases

This MapReduce pattern is commonly used for:
- Log file analysis
- Search index creation
- Data mining and analytics
- Large-scale text processing

## Requirements

- Python 3.x
- No external dependencies required

## Running the Code

Simply execute the Python script:

```bash
python wordcount.py
```

## Educational Value

This implementation serves as an excellent introduction to:
- Distributed computing concepts
- Big data processing patterns
- Functional programming principles
- Data transformation pipelines

The simplicity of the word count problem makes it easy to understand the MapReduce paradigm before applying it to more complex scenarios.
