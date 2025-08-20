def get_matrix():
    while True:
        try:
            rows = int(input("Masukkan jumlah baris (m): "))
            cols = int(input("Masukkan jumlah kolom (n): "))
            if rows > 0 and cols > 0:
                break
            else:
                print("Jumlah baris dan kolom harus lebih besar dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    matrix = []
    print("Masukkan elemen matriks:")
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = int(input(f"Elemen [{i+1}][{j+1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Input tidak valid. Masukkan bilangan bulat.")
        matrix.append(row)
    return matrix, rows, cols

def print_matrix(matrix, rows, cols):
    print("\nMatriks m x n:")
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end="\t")
        print()

def get_element(matrix, rows, cols):
    while True:
        try:
            row = int(input("\nMasukkan nomor baris untuk mendapatkan elemen: "))
            col = int(input("Masukkan nomor kolom untuk mendapatkan elemen: "))
            if 1 <= row <= rows and 1 <= col <= cols:
                print(f"Elemen pada baris {row} dan kolom {col} adalah: {matrix[row-1][col-1]}")
                break
            else:
                print("Nomor baris atau kolom di luar jangkauan.")
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

def print_diagonal(matrix, rows, cols):
    if rows != cols:
        print("\nMatriks bukan matriks persegi, tidak dapat menentukan diagonal.")
        return
    print("\nNilai diagonal matriks:")
    for i in range(rows):
        print(matrix[i][i], end="\t")
    print()

def print_upper_triangle(matrix, rows, cols):
    if rows != cols:
        print("\nMatriks bukan matriks persegi, tidak dapat menentukan segitiga atas.")
        return
    print("\nVisualisasi segitiga atas:")
    for i in range(rows):
        for j in range(cols):
            if j >= i:
                print(matrix[i][j], end="\t")
            else:
                print(" ", end="\t")
        print()

def print_lower_triangle(matrix, rows, cols):
    if rows != cols:
        print("\nMatriks bukan matriks persegi, tidak dapat menentukan segitiga bawah.")
        return
    print("\nVisualisasi segitiga bawah:")
    for i in range(rows):
        for j in range(cols):
            if j <= i:
                print(matrix[i][j], end="\t")
            else:
                print(" ", end="\t")
        print()

def is_upper_triangular(matrix, rows, cols):
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if i > j and matrix[i][j] != 0:
                return False
    return True

def is_lower_triangular(matrix, rows, cols):
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if j > i and matrix[i][j] != 0:
                return False
    return True

def is_identity_matrix(matrix, rows, cols):
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if i == j and matrix[i][j] != 1:
                return False
            if i != j and matrix[i][j] != 0:
                return False
    return True

def is_zero_matrix(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                return False
    return True

def is_sparse_matrix(matrix, rows, cols):
    zero_count = 0
    total_elements = rows * cols
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_count += 1
    return zero_count > (total_elements / 2)

def main():
    matrix, rows, cols = get_matrix()

    # 2. Output: Matriks m x n
    print_matrix(matrix, rows, cols)

    # 3. Output: Nilai elemen matriks baris ke-m dan kolom ke-n
    get_element(matrix, rows, cols)

    # 4. Output: Nilai diagonal matriks
    print_diagonal(matrix, rows, cols)

    # 5. Output: Nilai segitiga atas
    print_upper_triangle(matrix, rows, cols)
    if is_upper_triangular(matrix, rows, cols):
        print("Matriks ini adalah matriks segitiga atas.")
    else:
        print("Matriks ini bukan matriks segitiga atas.")

    # 6. Output: Nilai segitiga bawah
    print_lower_triangle(matrix, rows, cols)
    if is_lower_triangular(matrix, rows, cols):
        print("Matriks ini adalah matriks segitiga bawah.")
    else:
        print("Matriks ini bukan matriks segitiga bawah.")

    # 7. Output: Apakah matriks merupakan matriks identitas?
    if is_identity_matrix(matrix, rows, cols):
        print("\nMatriks ini adalah matriks identitas.")
    else:
        print("\nMatriks ini bukan matriks identitas.")

    # 8. Output: Apakah matriks merupakan matriks nol?
    if is_zero_matrix(matrix, rows, cols):
        print("Matriks ini adalah matriks nol.")
    else:
        print("Matriks ini bukan matriks nol.")

    # 9. Output: Apakah matriks merupakan matriks sparse?
    if is_sparse_matrix(matrix, rows, cols):
        print("Matriks ini adalah matriks sparse.")
    else:
        print("Matriks ini bukan matriks sparse.")

if __name__ == "__main__":
    main()
