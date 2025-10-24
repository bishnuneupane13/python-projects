n = int(input("Enter a number to create a multiplication table: "))

def create_table():
    result = []
    for i in range(1, 11):
        final = n * i
        line = f"{n} x {i} = {final}"
        result.append(line)
    return "\n".join(result)

table_text = create_table()

with open(f"multiply/multiplication_table_{n}.txt", "w") as file:
    file.write(f"{table_text}")

