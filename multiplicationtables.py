def opening_file() -> list[tuple[str, int, int]]:
    while True:
        yo_file = str(input('Please enter the CSV file name: '))
        try:
            with open(yo_file, 'r') as f:
                liness: list[tuple[str, int, int]] = []
                for line in f:
                    tokens = line.strip().split(',')
                    file_name = tokens[0]
                    rows = int(tokens[1])
                    columns = int(tokens[2])
                    liness.append((file_name, rows, columns))
            return liness
        except FileNotFoundError:
            print(f'File "{yo_file}" not found. Please try again.')
        except OSError:
            print(f'File "{yo_file}" does not exist.')

def multiplying(rows: int, columns: int) -> list[list[int]]:
    mult_table:list[list[int]] = []
    for i in range(1, rows + 1):
        current_row = []
        for j in range(1, columns + 1):
            current_row.append(i * j)
        mult_table.append(current_row)
    return mult_table

def writing_file(mult_table: list[list[int]], file_name: str) -> None:
    with open(file_name,'w') as f:
        for row in mult_table:
            row_formatted = ','.join(str(value) for value in row)
            f.write(row_formatted + '\n')

def main() -> None:
    user_input = opening_file()
    for file_name, rows, columns in user_input:
        product = multiplying(rows, columns)
        writing_file(product, file_name)

if __name__ == '__main__':
    main()
