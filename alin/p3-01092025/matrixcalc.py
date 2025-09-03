import tkinter as tk
from tkinter import ttk, messagebox, Toplevel

#fungsi u/ operasi
def add(a, b):
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Dimensi matriks harus sama untuk penjumlahan")
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(a, list) and isinstance(b, (int, float)):
        return [[a[i][j] + b for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(b, list) and isinstance(a, (int, float)):
        return [[a + b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
    return a + b

def subtract(a, b):
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Dimensi matriks harus sama untuk pengurangan")
        return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(a, list) and isinstance(b, (int, float)):
        return [[a[i][j] - b for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(b, list) and isinstance(a, (int, float)):
        return [[a - b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
    return a - b

def multiply(a, b):
    if isinstance(a, list) and isinstance(b, list):
        if len(a[0]) != len(b):
            raise ValueError("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B")
        result = [[0] * len(b[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result
    if isinstance(a, list) and isinstance(b, (int, float)):
        return [[a[i][j] * b for j in range(len(a[0]))] for i in range(len(a))]
    if isinstance(b, list) and isinstance(a, (int, float)):
        return [[a * b[i][j] for j in range(len(b[0]))] for i in range(len(b))]
    return a * b

#fungsi bantu
def parse_input(text_content):
    content = text_content.strip()
    if not content:
        raise ValueError("Input tidak boleh kosong")
    try:
        return float(content)
    except ValueError:
        matrix = []
        rows = content.split('\n')
        for r in rows:
            if not r.strip(): continue
            matrix.append([float(val) for val in r.split()])
        if matrix:
            first_row_len = len(matrix[0])
            if not all(len(row) == first_row_len for row in matrix):
                raise ValueError("Setiap baris matriks harus memiliki jumlah kolom yang sama")
        return matrix

def format_matrix(matrix):
    if isinstance(matrix, (int, float)):
        return str(matrix)
    return '\n'.join(['\t'.join(map(str, row)) for row in matrix])

#window input dialog
class InputDialog(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tambah Data Baru")
        self.geometry("300x250")
        self.parent = parent
        self.data = None

        ttk.Label(self, text="Masukkan matriks atau skalar:").pack(pady=5, padx=10)
        self.text_input = tk.Text(self, height=10, width=35)
        self.text_input.pack(pady=5, padx=10)

        save_button = ttk.Button(self, text="Simpan", command=self.save)
        save_button.pack(pady=10)
        self.transient(parent)
        self.grab_set()

    def save(self):
        try:
            raw_text = self.text_input.get("1.0", "end-1c")
            self.data = parse_input(raw_text)
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error Input", str(e), parent=self)

#main app
class MatrixCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator Matriks 041_2B")
        self.geometry("800x600")

        self.data_storage = {}
        self.next_char_code = ord('A')
        self.result_count = 0
        self.operation_var = tk.StringVar(value='+')

        #frame kiri (data dn previw)
        left_frame = ttk.Frame(self)
        left_frame.place(x=10, y=10, width=250, height=580)

        data_frame = ttk.LabelFrame(left_frame, text="Data Tersimpan")
        data_frame.pack(fill="x", expand=False)

        self.data_listbox = tk.Listbox(data_frame, height=10)
        self.data_listbox.pack(pady=5, padx=10, fill="x", expand=True)
        self.data_listbox.bind("<<ListboxSelect>>", self.show_preview)

        add_button = ttk.Button(data_frame, text="Tambah Data", command=self.add_new_data)
        add_button.pack(pady=5, padx=10, fill="x")
        
        reset_button = ttk.Button(data_frame, text="Reset Semua", command=self.reset_all)
        reset_button.pack(pady=(0, 5), padx=10, fill="x")

        preview_frame = ttk.LabelFrame(left_frame, text="Preview Data Terpilih")
        preview_frame.pack(pady=10, fill="both", expand=True)

        self.preview_text = tk.Text(preview_frame, state="disabled", bg="#f0f0f0")
        self.preview_text.pack(pady=5, padx=10, fill="both", expand=True)

        #frame kanan (operasi(menu) dan hasil)
        main_frame = ttk.Frame(self)
        main_frame.place(x=270, y=10, width=520, height=580)

        op_frame = ttk.LabelFrame(main_frame, text="Menu Operasi")
        op_frame.pack(pady=5, padx=10, fill="x")

        self.op1_combo = ttk.Combobox(op_frame, state="readonly", width=15)
        self.op1_combo.pack(side="left", padx=5, pady=10)

        op_radio_frame = ttk.Frame(op_frame)
        ops = ['+', '-', '*']
        for op in ops:
            ttk.Radiobutton(op_radio_frame, text=op, variable=self.operation_var, value=op).pack(side="left")
        op_radio_frame.pack(side="left", padx=5, pady=10)

        self.op2_combo = ttk.Combobox(op_frame, state="readonly", width=15)
        self.op2_combo.pack(side="left", padx=5, pady=10)

        calc_button = ttk.Button(op_frame, text="Hitung", command=self.calculate)
        calc_button.pack(side="left", padx=10, pady=10)

        result_frame = ttk.LabelFrame(main_frame, text="Hasil")
        result_frame.pack(pady=5, padx=10, fill="both", expand=True)

        self.result_text = tk.Text(result_frame, state="disabled", bg="#f0f0f0")
        self.result_text.pack(pady=5, padx=10, fill="both", expand=True)

    def add_new_data(self):
        dialog = InputDialog(self)
        self.wait_window(dialog)

        if dialog.data is not None:
            name = chr(self.next_char_code)
            self.next_char_code += 1
            self.data_storage[name] = dialog.data
            self.update_widgets()

    def update_widgets(self):
        variable_names = sorted(self.data_storage.keys())
        
        self.data_listbox.delete(0, "end")
        for name in variable_names:
            data = self.data_storage[name]
            preview = str(data) if isinstance(data, (int, float)) else f"Matriks {len(data)}x{len(data[0])}"
            self.data_listbox.insert("end", f"{name}: {preview}")

        self.op1_combo['values'] = variable_names
        self.op2_combo['values'] = variable_names
        if variable_names:
            if not self.op1_combo.get(): self.op1_combo.set(variable_names[0])
            if not self.op2_combo.get(): self.op2_combo.set(variable_names[0])

    def show_preview(self, event=None):
        selected_indices = self.data_listbox.curselection()
        if not selected_indices: return

        item_string = self.data_listbox.get(selected_indices[0])
        var_name = item_string.split(':')[0]
        data_to_preview = self.data_storage.get(var_name)

        self.preview_text.config(state="normal")
        self.preview_text.delete("1.0", "end")
        self.preview_text.insert("1.0", format_matrix(data_to_preview))
        self.preview_text.config(state="disabled")

    def calculate(self):
        try:
            op1_name = self.op1_combo.get()
            op2_name = self.op2_combo.get()
            op = self.operation_var.get()

            if not op1_name or not op2_name:
                raise ValueError("Operand belum dipilih")

            val_a = self.data_storage[op1_name]
            val_b = self.data_storage[op2_name]

            result = None
            if op == "+": result = add(val_a, val_b)
            elif op == "-": result = subtract(val_a, val_b)
            elif op == "*": result = multiply(val_a, val_b)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", format_matrix(result))
            self.result_text.config(state="disabled")

            self.result_count += 1
            result_name = f"Hasil_{self.result_count}"
            self.data_storage[result_name] = result
            self.update_widgets()
            messagebox.showinfo("Info", f"Hasil perhitungan disimpan sebagai '{result_name}'", parent=self)

        except Exception as e:
            messagebox.showerror("Calculation Error", f"Gagal melakukan perhitungan: {e}", parent=self)

    def reset_all(self):
        if messagebox.askyesno("Konfirmasi Reset", "Apakah Anda yakin ingin menghapus semua data dan hasil?"):
            self.data_storage = {}
            self.next_char_code = ord('A')
            self.result_count = 0
            self.update_widgets()
            self.op1_combo.set('')
            self.op2_combo.set('')
            self.result_text.config(state="normal")
            self.result_text.delete("1.0", "end")
            self.result_text.config(state="disabled")
            self.preview_text.config(state="normal")
            self.preview_text.delete("1.0", "end")
            self.preview_text.config(state="disabled")

if __name__ == "__main__":
    app = MatrixCalculatorApp()
    app.mainloop()
