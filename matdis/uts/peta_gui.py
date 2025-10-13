
import tkinter as tk
from tkinter import font
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Data dari notebook (posisi, status, warna, dll.)
posisi_negara = {
    'Jerman': (13.40, 52.52), 
    'Uni Soviet': (37.61, 55.75), 
    'Inggris Raya': (-0.12, 51.50),
    'Prancis': (2.35, 48.85), 
    'Italia': (12.49, 41.90), 
    'Polandia': (21.01, 52.22),
    'Austria': (16.37, 48.35), 
    'Ceko': (14.43, 50.07), 
    'Slowakia': (17.50, 47.95),
    'Hungaria': (19.04, 47.49), 
    'Rumania': (26.10, 44.42), 
    'Yugoslavia': (20.44, 44.78),
    'Yunani': (23.72, 37.98), 
    'Norwegia': (10.75, 59.91), 
    'Denmark': (12.56, 55.67),
    'Belanda': (4.89, 52.36), 
    'Belgia': (4.35, 50.85), 
    'Finlandia': (24.93, 60.16),
    'Estonia': (24.75, 59.43), 
    'Latvia': (24.10, 56.94), 
    'Lithuania': (25.27, 54.68),
    'Swiss': (7.44, 46.94), 
    'Swedia': (18.06, 59.33), 
    'Spanyol': (-3.70, 40.41),
    'Turki': (32.86, 39.93),
}

status_per_tahun = {
    1939: {'Jerman': 'Axis', 
    'Italia': 'Axis', 
    'Polandia': 'Sekutu', 
    'Inggris Raya': 'Sekutu', 
    'Prancis': 'Sekutu', 
    'Uni Soviet': 'Diduduki Soviet', 
    'Austria': 'Bagian dari Jerman', 
    'Ceko': 'Bagian dari Jerman'},

    1940: {'Jerman': 'Axis', 
    'Italia': 'Axis', 
    'Hungaria': 'Axis', 
    'Rumania': 'Axis', 
    'Slowakia': 'Axis', 
    'Inggris Raya': 'Sekutu', 
    'Uni Soviet': 'Diduduki Soviet', 
    'Polandia': 'Terbagi', 
    'Prancis': 'Diduduki Axis', 
    'Norwegia': 'Diduduki Axis', 
    'Denmark': 'Diduduki Axis', 
    'Belanda': 'Diduduki Axis', 
    'Belgia': 'Diduduki Axis', 
    'Austria': 'Bagian dari Jerman', 
    'Ceko': 'Bagian dari Jerman', 
    'Estonia': 'Diduduki Soviet', 
    'Latvia': 'Diduduki Soviet', 
    'Lithuania': 'Diduduki Soviet'},

    1941: {'Jerman': 'Axis', 
    'Italia': 'Axis', 
    'Hungaria': 'Axis', 
    'Rumania': 'Axis', 
    'Slowakia': 'Axis', 
    'Finlandia': 'Axis', 
    'Inggris Raya': 'Sekutu', 
    'Uni Soviet': 'Sekutu', 
    'Polandia': 'Terbagi', 
    'Prancis': 'Diduduki Axis', 
    'Norwegia': 'Diduduki Axis', 
    'Denmark': 'Diduduki Axis', 
    'Belanda': 'Diduduki Axis', 
    'Belgia': 'Diduduki Axis', 
    'Yugoslavia': 'Diduduki Axis', 
    'Yunani': 'Diduduki Axis', 
    'Estonia': 'Diduduki Axis', 
    'Latvia': 'Diduduki Axis', 
    'Lithuania': 'Diduduki Axis', 
    'Austria': 'Bagian dari Jerman', 
    'Ceko': 'Bagian dari Jerman'},

    1942: {'Jerman': 'Axis', 
    'Italia': 'Axis', 
    'Hungaria': 'Axis', 
    'Rumania': 'Axis', 
    'Slowakia': 'Axis', 
    'Finlandia': 'Axis', 
    'Inggris Raya': 'Sekutu', 
    'Uni Soviet': 'Sekutu', 
    'Polandia': 'Diduduki Axis', 
    'Prancis': 'Diduduki Axis', 
    'Norwegia': 'Diduduki Axis', 
    'Denmark': 'Diduduki Axis', 
    'Belanda': 'Diduduki Axis', 
    'Belgia': 'Diduduki Axis', 
    'Yugoslavia': 'Diduduki Axis', 
    'Yunani': 'Diduduki Axis', 
    'Estonia': 'Diduduki Axis', 
    'Latvia': 'Diduduki Axis', 
    'Lithuania': 'Diduduki Axis', 
    'Austria': 'Bagian dari Jerman', 
    'Ceko': 'Bagian dari Jerman'},

    1943: {'Jerman': 'Axis', 
    'Italia': 'Axis', 
    'Hungaria': 'Axis', 
    'Rumania': 'Axis', 
    'Slowakia': 'Axis', 
    'Finlandia': 'Axis', 
    'Inggris Raya': 'Sekutu', 
    'Uni Soviet': 'Sekutu', 
    'Polandia': 'Diduduki Axis', 
    'Prancis': 'Diduduki Axis', 
    'Norwegia': 'Diduduki Axis', 
    'Denmark': 'Diduduki Axis', 
    'Belanda': 'Diduduki Axis', 
    'Belgia': 'Diduduki Axis', 
    'Yugoslavia': 'Diduduki Axis', 
    'Yunani': 'Diduduki Axis', 
    'Estonia': 'Diduduki Axis', 
    'Latvia': 'Diduduki Axis', 
    'Lithuania': 'Diduduki Axis', 
    'Austria': 'Bagian dari Jerman', 
    'Ceko': 'Bagian dari Jerman'},

    1944: {'Jerman': 'Axis', 
    'Hungaria': 'Diduduki Axis', 
    'Slowakia': 'Diduduki Axis', 
    'Inggris Raya': 'Sekutu', 
    'Uni Soviet': 'Sekutu', 
    'Prancis': 'Sekutu', 
    'Belgia': 'Sekutu', 
    'Rumania': 'Sekutu', 
    'Finlandia': 'Sekutu', 
    'Italia': 'Terbagi', 
    'Polandia': 'Diduduki Axis', 
    'Norwegia': 'Diduduki Axis', 
    'Denmark': 'Diduduki Axis', 
    'Belanda': 'Diduduki Axis', 
    'Yugoslavia': 'Diduduki Axis', 
    'Yunani': 'Diduduki Axis', 
    'Austria': 'Bagian dari Jerman', 
    'Ceko': 'Bagian dari Jerman', 
    'Estonia': 'Diduduki Soviet', 
    'Latvia': 'Diduduki Soviet', 
    'Lithuania': 'Diduduki Soviet'},

    1945: {'Jerman': 'Diduduki Sekutu', 
    'Austria': 'Diduduki Sekutu', 
    'Inggris Raya': 'Sekutu', 
    'Uni Soviet': 'Sekutu', 
    'Prancis': 'Sekutu', 
    'Belgia': 'Sekutu', 
    'Rumania': 'Sekutu', 
    'Finlandia': 'Sekutu', 
    'Italia': 'Sekutu', 
    'Polandia': 'Diduduki Soviet', 
    'Ceko': 'Sekutu', 
    'Yugoslavia': 'Sekutu', 
    'Yunani': 'Sekutu', 
    'Norwegia': 'Sekutu', 
    'Denmark': 'Sekutu', 
    'Belanda': 'Sekutu', 
    'Hungaria': 'Diduduki Soviet', 
    'Estonia': 'Diduduki Soviet', 
    'Latvia': 'Diduduki Soviet', 
    'Lithuania': 'Diduduki Soviet'}
}

warna_status = {
    'Axis': '#ff4d4d', 
    'Sekutu': '#4a7fdd', 
    'Diduduki Axis': '#ffb347',
    'Diduduki Soviet': '#d5efff', 
    'Diduduki Sekutu': '#add8e6', 
    'Netral': '#a9a9a9',
    'Bagian dari Jerman': '#a42a2a', 
    'Terbagi': '#9370db'
}

faksi_map = {
    'Axis': 'Axis', 
    'Diduduki Axis': 'Axis', 
    'Bagian dari Jerman': 'Axis',
    'Sekutu': 'Sekutu', 
    'Diduduki Soviet': 'Sekutu', 
    'Diduduki Sekutu': 'Sekutu',
    'Netral': 'Netral', 
    'Terbagi': 'Terbagi', 
    'Co-belligerent Axis': 'Axis'
}

perbatasan_geografis = [
    ('Spanyol', 'Prancis'), 
    ('Prancis', 'Jerman'), 
    ('Prancis', 'Swiss'), 
    ('Prancis', 'Italia'),
    ('Prancis', 'Belgia'), 
    
    ('Jerman', 'Belgia'), 
    ('Jerman', 'Belanda'), 
    ('Jerman', 'Denmark'),
    ('Jerman', 'Polandia'), 
    ('Jerman', 'Ceko'), 
    ('Jerman', 'Austria'), 
    ('Jerman', 'Swiss'),

    ('Swiss', 'Austria'), 
    ('Swiss', 'Italia'), 
    
    ('Austria', 'Italia'), 
    ('Austria', 'Ceko'),
    ('Austria', 'Slowakia'), 
    ('Austria', 'Hungaria'), 
    ('Austria', 'Yugoslavia'),

    ('Italia', 'Yugoslavia'), 
    
    ('Polandia', 'Uni Soviet'), 
    ('Polandia', 'Ceko'),
    ('Polandia', 'Slowakia'), 
    ('Polandia', 'Lithuania'), 
    ('Ceko', 'Slowakia'),

    ('Slowakia', 'Hungaria'), 
    
    ('Hungaria', 'Rumania'), 
    ('Hungaria', 'Yugoslavia'),
    
    ('Rumania', 'Uni Soviet'), 
    ('Rumania', 'Yugoslavia'), 
    
    ('Yugoslavia', 'Yunani'),
    
    ('Norwegia', 'Swedia'), 
    ('Norwegia', 'Finlandia'), 
    
    ('Swedia', 'Finlandia'),
    ('Finlandia', 'Uni Soviet'), ('Estonia', 'Latvia'), ('Latvia', 'Lithuania'),
    ('Estonia', 'Uni Soviet'), ('Latvia', 'Uni Soviet'), ('Lithuania', 'Uni Soviet'),
    ('Turki', 'Uni Soviet'), ('Turki', 'Yunani'), ('Inggris Raya', 'Belgia'),
    ('Inggris Raya', 'Prancis'), ('Inggris Raya', 'Belanda'),
]

class WW2MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Peta Okupasi PD2 di Eropa")
        self.root.geometry("1200x800")

        # Main frame
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame Konten (Kiri: Status, Kanan: Peta + Tombol)
        content_frame = tk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Frame Kiri untuk Keterangan Status
        left_frame = tk.Frame(content_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))

        title_font = font.Font(family="Helvetica", size=12, weight="bold")
        status_title_label = tk.Label(left_frame, text="Status Wilayah", font=title_font)
        status_title_label.pack(anchor="n", pady=(0, 10))

        self.status_label = tk.Label(left_frame, text="", justify=tk.LEFT, anchor="nw", wraplength=280)
        self.status_label.pack(fill=tk.BOTH, expand=True)

        # Frame Kanan untuk Peta dan Tombol
        right_frame = tk.Frame(content_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Matplotlib Figure and Canvas
        self.fig = plt.Figure(figsize=(10, 7), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Frame untuk Tombol Tahun
        button_frame = tk.Frame(right_frame, pady=10)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        years = sorted(status_per_tahun.keys())
        for year in years:
            button = tk.Button(button_frame, text=str(year), command=lambda y=year: self.update_map_and_status(y))
            button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Disclaimer
        disclaimer_label = tk.Label(main_frame, text="Disclaimer: Peta ini adalah representasi graf sederhana dan tidak 100% akurat secara geografis maupun historis.", wraplength=1100, justify=tk.CENTER)
        disclaimer_label.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))

        # Tampilkan peta untuk tahun pertama saat aplikasi dimulai
        self.update_map_and_status(years[0])

    def update_map_and_status(self, tahun):
        # 1. Update Keterangan Status (Panel Kiri)
        status_tahun_ini = status_per_tahun[tahun]
        status_text = f"Ikhtisar Situasi Tahun {tahun}:\n"
        
        # Mengurutkan negara berdasarkan nama untuk tampilan yang konsisten
        sorted_negara = sorted(status_tahun_ini.keys())

        status_ke_kalimat = {
            'Axis': "berada di pihak Axis",
            'Sekutu': "berada di pihak Sekutu",
            'Diduduki Axis': "diduduki oleh kekuatan Axis",
            'Diduduki Soviet': "diduduki oleh Uni Soviet",
            'Diduduki Sekutu': "diduduki oleh pasukan Sekutu",
            'Netral': "mempertahankan status netral",
            'Bagian dari Jerman': "telah menjadi bagian dari Jerman",
            'Terbagi': "wilayahnya terbagi"
        }
        
        for negara in sorted_negara:
            status = status_tahun_ini[negara]
            deskripsi = status_ke_kalimat.get(status, f"memiliki status '{status}'")
            status_text += f"\n• {negara} {deskripsi}."
        
        self.status_label.config(text=status_text)

        # 2. Update Peta (Panel Kanan)
        self.ax.clear()

        node_colors = [warna_status.get(status_tahun_ini.get(node, 'Netral'), '#a9a9a9') for node in posisi_negara.keys()]

        G = nx.Graph()
        G.add_nodes_from(posisi_negara.keys())

        edge_tahun_ini = []
        for negara1, negara2 in perbatasan_geografis:
            if negara1 not in G.nodes or negara2 not in G.nodes:
                continue
            status1 = status_tahun_ini.get(negara1, 'Netral')
            status2 = status_tahun_ini.get(negara2, 'Netral')
            faksi1 = faksi_map.get(status1, 'Netral')
            faksi2 = faksi_map.get(status2, 'Netral')

            if faksi1 == faksi2 and faksi1 != 'Netral':
                edge_tahun_ini.append((negara1, negara2))
            elif faksi1 == 'Terbagi' and faksi2 in ['Axis', 'Sekutu']:
                edge_tahun_ini.append((negara1, negara2))
            elif faksi2 == 'Terbagi' and faksi1 in ['Axis', 'Sekutu']:
                edge_tahun_ini.append((negara1, negara2))

        G.add_edges_from(edge_tahun_ini)

        nx.draw(G,
                pos=posisi_negara, with_labels=True, node_size=500,
                node_color=node_colors, font_size=7, font_color='black',
                font_weight='bold', edge_color='#666666', width=1.5,
                ax=self.ax
               )

        legend_handles = [mpatches.Patch(color=warna, label=status) for status, warna in warna_status.items()]
        self.ax.legend(handles=legend_handles, loc='lower left', title="Status", fontsize='small')

        self.ax.set_title(f"Peta Pendudukan Axis dan Sekutu di Eropa - per 1 September {tahun}", fontsize=16)
        
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = WW2MapApp(root)
    root.mainloop()