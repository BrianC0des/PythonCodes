x = [483, 651, 495, 567, 690, 265]
y = []

# Normalize values in x
total_sum = sum(x)
for i in x:
    normalized_value = i / total_sum
    y.append(normalized_value)

print("Original list x:", x)
print("Normalized list y:", y)
print("Sum of normalized values:", sum(y))
print("Sum of original values:", total_sum)

print("Programming is Fun")