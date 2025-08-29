"""op matirks"""

def get_matrix(name="Matriks"):
    while True:
        try:
            rows = int(input(f"Masukkan jumlah baris {name} (m): "))
            cols = int(input(f"Masukkan jumlah kolom {name} (n): "))
            if rows > 0 and cols > 0:
                break
            else:
                print("Jumlah baris dan kolom harus lebih besar dari 0")
        except ValueError:
            print("Input tidak valid, masukkan bilangan bulat")

    matrix = []
    print(f"Masukkan elemen-elemen {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = float(input(f"Elemen [{i+1}][{j+1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Input tidak valid, masukkan bilangan real/integer")
        matrix.append(row)
    return matrix, rows, cols

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(str(x) for x in row))
    print()

def get_scalar(name="Skalar"):
    while True:
        try:
            val = float(input(f"Masukkan nilai {name}: "))
            return val
        except ValueError:
            print("Input tidak valid, masukkan bilangan real")

def add(a, b):
    # matriks + matriks
    if isinstance(a, list) and isinstance(b, list):
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    # matriks + skalar / skalar + matriks
    if isinstance(a, list) and isinstance(b, (int, float)):
        return [[a[i][j] + b for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(b, list) and isinstance(a, (int, float)):
        return [[a + b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
    # skalar + skalar
    return a + b

def subtract(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(a, list) and isinstance(b, (int, float)):
        return [[a[i][j] - b for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(b, list) and isinstance(a, (int, float)):
        return [[a - b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
    return a - b

def multiply(a, b):
    # matriks * matriks
    if isinstance(a, list) and isinstance(b, list):
        result = [[0] * len(b[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result
    # matriks * skalar
    if isinstance(a, list) and isinstance(b, (int, float)):
        return [[a[i][j] * b for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(b, list) and isinstance(a, (int, float)):
        return [[a * b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
    # skalar * skalar
    return a * b


def main():
    data = {}
    num_inputs = int(input("Masukkan jumlah data (matriks/skalar): "))

    matrix_count = 0
    for i in range(num_inputs):
        name = chr(65 + i)
        jenis = input(f"Apakah {name} Matriks atau Skalar? (M/S): ").upper()
        if jenis == "S":
            data[name] = get_scalar(name)
        else:
            m, rows, cols = get_matrix(name)
            data[name] = m
            matrix_count += 1

    if matrix_count == 0:
        print("Minimal harus ada 1 matriks! Program berhenti.")
        return

    ekspresi = input("Masukkan ekspresi operasi (contoh: A + B - C * D): ")

    try:
        # Parse token: "A + B - C * D" (operand dan operator dipisah spasi)
        tokens = ekspresi.split()
        if len(tokens) == 0:
            raise ValueError("Ekspresi kosong")

        if len(tokens) % 2 == 0:
            raise ValueError("ekspresi tidak valid (format harus operand operator operand ...)")

        # pisah operand dan operator
        vals = [data[tokens[i]] for i in range(0, len(tokens), 2)]
        ops = [tokens[i] for i in range(1, len(tokens), 2)]

        # prioritas: kerjain perkalian dlu (kiri ke kanan)
        i = 0
        while i < len(ops):
            if ops[i] == '*':
                combined = multiply(vals[i], vals[i+1])
                vals[i] = combined
                del vals[i+1]
                del ops[i]
            else:
                i += 1

        # kerjain penjumlahan dan pengurangan (kiri ke kanan)
        result = vals[0]
        for idx, op in enumerate(ops):
            right = vals[idx+1]
            if op == '+':
                result = add(result, right)
            elif op == '-':
                result = subtract(result, right)
            else:
                raise ValueError(f"operator tidak diknal: {op}")

        print("\nekspresi operasi:", ekspresi)
        print("hasil operasi:")
        if isinstance(result, (int, float)):
            print(result)
        else:
            print_matrix(result)

    except Exception as e:
        print("terjadi kesalahan saat menghitung:", e)

if __name__ == "__main__":
    main()
