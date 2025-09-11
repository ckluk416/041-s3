def print_matrix(matrix, label=""):
    if label:
        print(label)
    for baris in matrix:
        print("[", end="")
        for i, val in enumerate(baris):
            print(f"{val:8.2f}", end="")
            if i < len(baris) - 1:
                print("  ", end="")
        print("]")
    print()

def get_matrix_input():
    matrix = []
    print("masukkan elemen-elemen matriks 3x3 (angka):")
    for i in range(3):
        while True:
            try:
                baris_input = input(f"masukkan 3 elemen untuk baris ke-{i+1} (pisahkan dengan spasi): ")
                baris = [float(x) for x in baris_input.split()]
                if len(baris) != 3:
                    print("harap masukkan tepat 3 elemen")
                    continue
                matrix.append(baris)
                break
            except ValueError:
                print("input tidak valid,masukkan angka saja")
            except Exception as e:
                print(f"Terjadi error: {e}")
    return matrix

def calculate_determinant_obe(matrix):
    # salin matriks u/ diolah
    mat = [baris[:] for baris in matrix]
    
    #faktor pengali u/ determinan
    det_multiplier = 1.0

    print("=== Proses Operasi Baris Elementer (OBE) ===")
    print_matrix(mat, "Matriks Awal:")

    #=======> Langkah 1: Membuat nol di bawah pivot pertama (mat[0][0])
    # jika pivot mat[0][0] adalah 0, tukar dengan baris di bawahnya
    if mat[0][0] == 0:
        # cari baris di bawahnya yang elemen pertamanya tidak nol
        swap_baris_idx = -1
        if mat[1][0] != 0:
            swap_baris_idx = 1
        elif mat[2][0] != 0:
            swap_baris_idx = 2

        if swap_baris_idx != -1:
            print(f"Pivot adalah 0. Menukar Baris 1 dengan Baris {swap_baris_idx + 1}.")
            mat[0], mat[swap_baris_idx] = mat[swap_baris_idx], mat[0]
            det_multiplier *= -1  #pertukaran baris mengubah tanda determinan
            print_matrix(mat, f"Hasil setelah B1 <-> B{swap_baris_idx + 1}:")
        else:
            #jika semua elemen di kolom pertama adalah 0, determinan adalah 0
            print("Kolom pertama berisi semua nol. Determinan adalah 0.")
            return 0

    #membuat nol elemen mat[1][0]
    if mat[1][0] != 0:
        factor = mat[1][0] / mat[0][0]
        print(f"Langkah: B2 -> B2 - ({factor:.2f} * B1)")
        for j in range(3):
            mat[1][j] = mat[1][j] - factor * mat[0][j]
        print_matrix(mat, "Hasil:")

    #membuat nol elemen mat[2][0]
    if mat[2][0] != 0:
        factor = mat[2][0] / mat[0][0]
        print(f"Langkah: B3 -> B3 - ({factor:.2f} * B1)")
        for j in range(3):
            mat[2][j] = mat[2][j] - factor * mat[0][j]
        print_matrix(mat, "Hasil:")

    #=======> Langkah 2: Membuat nol di bawah pivot kedua (mat[1][1])
    #jika pivot mat[1][1] adalah 0, tukar dengan baris di bawahnya (Baris 3)
    if mat[1][1] == 0:
        if mat[2][1] != 0:
            print("Pivot kedua adalah 0. Menukar Baris 2 dengan Baris 3.")
            mat[1], mat[2] = mat[2], mat[1]
            det_multiplier *= -1 #pertukaran baris mengubah tanda determinan
            print_matrix(mat, "Hasil setelah B2 <-> B3:")
        else:
            #jika mat[1][1] dan mat[2][1] keduanya 0, matriks sudah dalam bentuk segitiga atas, dan diagonalnya ada yg 0. Determinan pasti 0.
            print("Pivot kedua (dan elemen di bawahnya) adalah 0. Determinan adalah 0.")
            return 0

    # Membuat nol elemen mat[2][1]
    if mat[2][1] != 0:
        factor = mat[2][1] / mat[1][1]
        print(f"Langkah: B3 -> B3 - ({factor:.2f} * B2)")
        for j in range(3):
            mat[2][j] = mat[2][j] - factor * mat[1][j]
        print_matrix(mat, "Hasil:")

    #=======> perhitungan determinan
    print("=== Matriks Eselon Baris (Segitiga Atas) Tercapai ===")
    print_matrix(mat, "Matriks Akhir:")

    #dterminan adalah hasil kali elemen diagonal
    determinant = det_multiplier * mat[0][0] * mat[1][1] * mat[2][2]
    
    print("Determinan dihitung dengan mengalikan elemen diagonal:")
    print(f"Determinan = {det_multiplier:.1f} * {mat[0][0]:.2f} * {mat[1][1]:.2f} * {mat[2][2]:.2f}")
    
    return determinant

def main():
    print("=======================================================")
    print("   Program Penghitung Determinan Matriks 3x3 (OBE)   ")
    print("=======================================================")
    
    user_matrix = get_matrix_input()
    print_matrix(user_matrix, "\nmatriks yang anda masukkan adalah:")
    determinant_value = calculate_determinant_obe(user_matrix)

    print("\n================ HASIL AKHIR ================")
    print(f"    determinan dari matriks adalah: {determinant_value:.2f}")
    print("=============================================")

if __name__ == "__main__":
    main()