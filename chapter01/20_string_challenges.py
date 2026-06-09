# Printing each character of the word "Factory" incrementally repeated on each line.


print("Challenge 1")
message = "Factory"
for i in range(len(message)):
    print(message[i] * (i + 1))


    # Printing each character of the word "Factory" incrementally repeated,
# followed by a decreasing number of asterisks to form a right-aligned triangle.print("Challenge 2")

for i in range(len(message)):
    print(message[i] * (i + 1), end="*" * (len(message) - i - 1))
    print()