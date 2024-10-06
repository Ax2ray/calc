import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to validate numbers
def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Beam calculations
def hitung_balok():
    try:
        panjang_bentang = float(entry_panjang_balok.get())
        tinggi_balok_induk = 1 / 10 * panjang_bentang
        lebar_balok_induk = 1 / 2 * tinggi_balok_induk
        
        if panjang_bentang >= 600:
            tinggi_balok_anak = 1 / 15 * panjang_bentang
            lebar_balok_anak = 1 / 2 * tinggi_balok_anak
        else:
            tinggi_balok_anak = lebar_balok_anak = 0

        kolom = lebar_balok_induk + (2 * 5)
        plat_lantai = (1 / 40) * panjang_bentang

        label_hasil_balok.config(text=(f"Panjang Bentang: {panjang_bentang:.2f} cm\n"
                                         f"Tinggi Balok Induk: {tinggi_balok_induk:.2f} cm\n"
                                         f"Lebar Balok Induk: {lebar_balok_induk:.2f} cm\n"
                                         f"Tinggi Balok Anak: {tinggi_balok_anak:.2f} cm\n"
                                         f"Lebar Balok Anak: {lebar_balok_anak:.2f} cm\n"
                                         f"Kolom: {kolom:.2f} cm\n"
                                         f"Plat Lantai: {plat_lantai:.2f} cm"))
    except ValueError:
        label_hasil_balok.config(text="Masukkan nilai yang valid.")

# Concrete volume calculations
def volume_beton(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def hitung_material():
    try:
        P = float(entry_panjang_volume.get())
        L = float(entry_lebar_volume.get())
        T = float(entry_tinggi_volume.get())
        
        volume_beton_value = volume_beton(P, L, T) / 1000000  # Convert cm³ to m³
        
        volume_semen = (1 / 6) * volume_beton_value
        volume_pasir = (2 / 6) * volume_beton_value
        volume_kerikil = (3 / 6) * volume_beton_value

        berat_semen = volume_semen * 1440  # kg
        
        label_hasil_volume.config(text=(f"Volume Beton: {volume_beton_value:.2f} m³\n" 
                                        f"Volume Semen: {volume_semen:.2f} m³ ({berat_semen:.2f} kg)\n" 
                                        f"Volume Pasir: {volume_pasir:.2f} m³\n" 
                                        f"Volume Kerikil: {volume_kerikil:.2f} m³"))
    except ValueError:
        label_hasil_volume.config(text="Masukkan nilai yang valid.")

# Foundation volume calculations
def hitung_luas_volume():
    try:
        A = float(entry_A.get())
        B = float(entry_B.get())
        T = float(entry_T.get())
        P = float(entry_P.get())

        L = (A + B) / 2 * T / 10000  # Convert to m²
        V = L * P  # V in m³

        label_hasil_luas_volume.config(text=f"Nilai L (m²): {L:.4f}\nNilai V (m³): {V:.2f} m³")
        entry_volume.delete(0, tk.END)
        entry_volume.insert(0, f"{V:.2f}")
    except ValueError:
        label_hasil_luas_volume.config(text="Masukkan angka yang valid.")

def hitung_material_beton():
    try:
        V = float(entry_volume.get())

        volume_batu_belah = 1.2  # m³
        berat_semen = 202  # kg
        volume_pasir = 0.485  # m³

        total_volume = volume_batu_belah + volume_pasir + (berat_semen / 1440)

        proporsi_batu_belah = volume_batu_belah / total_volume
        proporsi_pasir = volume_pasir / total_volume
        proporsi_semen = (berat_semen / 1440) / total_volume

        semen = V * proporsi_semen
        pasir = V * proporsi_pasir
        batu_belah = V * proporsi_batu_belah

        label_hasil_material_beton.config(text=f"Jumlah Material untuk Beton:\n"
                                                 f"Semen: {semen:.2f} m³\n"
                                                 f"Pasir: {pasir:.2f} m³\n"
                                                 f"Batu Belah: {batu_belah:.2f} m³")
    except ValueError:
        label_hasil_material_beton.config(text="Masukkan angka yang valid.")
        
def hitung():
    try:
        # Mengambil input dari entry
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tebal = float(entry_tebal.get())

        # Fungsi 1: Menghitung Luas Dinding
        luas_dinding = panjang * lebar
        
        # Fungsi 2: Luas Batako
        luas_batako = 0.28 * 0.15
        
        # Fungsi 3: Menghitung Jumlah Batako
        jumlah_batako = luas_dinding / luas_batako
        
        # Fungsi 4: Menghitung Volume Material Plesteran
        volume_plesteran = panjang * lebar * tebal
        
        # Menghitung kebutuhan semen, pasir, dan air
        total_bagian = 1 + 4  # 1 bagian semen + 4 bagian pasir
        semen_volume = (1 / total_bagian) * volume_plesteran
        pasir_volume = (4 / total_bagian) * volume_plesteran
        
        # Konversi ke kg dan liter
        semen_kg = semen_volume * 1440  # 1 m³ semen ≈ 1440 kg
        pasir_volume_m3 = pasir_volume  # Pasir tetap dalam m³
        air_volume = 0.5 * volume_plesteran  # Misalkan air setengah dari total volume
        air_liter = air_volume * 1000  # 1 m³ air = 1000 liter

        # Menampilkan hasil
        label_hasil.config(text=f"Luas Dinding: {luas_dinding:.2f} m²\n"
                                 f"Luas Batako: {luas_batako:.2f} m²\n"
                                 f"Jumlah Batako: {jumlah_batako:.0f}\n"
                                 f"Volume Material Plesteran: {volume_plesteran:.2f} m³\n"
                                 f"Kebutuhan Semen: {semen_kg:.2f} kg\n"
                                 f"Kebutuhan Pasir: {pasir_volume_m3:.2f} m³\n"
                                 f"Kebutuhan Air: {air_liter:.2f} liter")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

def hitung_urugan_kembali():
    try:
        panjang = float(entry_panjang_urug.get())
        lebar = float(entry_lebar_urug.get())
        kedalaman = float(entry_kedalaman_urug.get())
        ketinggian_urugan = float(entry_ketinggian_urug.get())

        # Menghitung volume galian
        volume_galian = panjang * lebar * ketinggian_urugan

        # Menghitung volume pondasi dengan mengonversi A dan B ke float
        #A = float(entry_A.get())
        #B = float(entry_B.get())
        volume_pondasi = (panjang + lebar) / 2 * kedalaman / 1000000  # konversi ke m³
        
        # Menghitung urugan
        urugan = (volume_galian - volume_pondasi) / 1000000

        label_hasil_urugan.config(text=f"Volume Urugan Kembali (m³): {urugan:.2f} m³")
    except ValueError:
        label_hasil_urugan.config(text="Mohon masukkan angka yang valid.")

def calculate_volume_rectangle():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        height = float(entry_height.get())
        volume = length * width * height
        area = length * width

        label_result_luas.config(text=f"Luas Area: {area:.2f} m³")
        label_result_volume.config(text=f"Volume: {volume:.2f} m³")
    except ValueError:
        label_result_volume.config(text="Input tidak valid!")

def calculate_rebar_usage():
    try:
        total_length = float(entry_total_length.get())  # Panjang total
        length_per_rod = 12  # Panjang besi/btg
        rebars_per_element = int(entry_rebars_per_element.get())  # Jumlah batang besi utama per kolom/sloof/balok
        
        # Hitung jumlah batang besi utama yang dibutuhkan
        total_rebars = (total_length * rebars_per_element) / length_per_rod
        
        result_rebar_label.config(text=f"Jumlah Batang Besi: {total_rebars:.2f} batang")
    except ValueError:
        result_rebar_label.config(text="Input tidak valid!")

def Hitung_Besi_Behel():
    try:
        # Mengambil nilai dari entri
        panjang_sloof = float(entry_panjang_sloof.get())
        panjang_keliling = float(entry_panjang_keliling.get())
        jarak_behel = float(entry_jarak_behel.get())

        # Hitung jumlah behel
        jumlah_behel = panjang_sloof * 100 / jarak_behel  #cm
        total_panjang_behel = jumlah_behel * panjang_keliling  # Total panjang behel
        jumlah_besi = total_panjang_behel / 12  # Jumlah batang besi (12 meter per batang)

        # Tampilkan hasil
        label_result1.config(text=f"Hasil Perhitungan:\nTotal Panjang Behel: {total_panjang_behel:.2f} meter\n"
                                 f"Jumlah Besi: {jumlah_besi:.2f} batang")
    except ValueError:
        label_result1.config(text="Input Error: Mohon masukkan angka yang valid.")

def volume_truk():
    try:
        P = float(entry_panjang_area.get())  # Panjang dalam meter
        L = float(entry_lebar_area.get())     # Lebar dalam meter
        T = float(entry_tinggi_area.get())    # Tinggi dalam meter
        Vol = P * L * T
        jumlah_truk = Vol / 4  # 4 m³ per truk
        
        # Menampilkan hasil
        label_hasil_area.config(text=f"Volume Total: {Vol:.2f} m³\nJumlah Truk: {jumlah_truk:.2f}")
    except ValueError:
        label_hasil_area.config(text="Mohon masukkan angka yang valid.")

def hitung_cat():
    try:
        P = float(entry_panjang_dinding.get())  # Panjang dinding
        L = float(entry_lebar_dinding.get())     # Lebar dinding
        daya_sebar = float(entry_sebar.get())
        area_dinding = P * L                       # Hitung area dinding
        liter_cat = area_dinding / daya_sebar        # Hitung kebutuhan cat (daya sebar)
        
        # Menampilkan hasil
        label_hasil_cat.config(text=f"Kebutuhan Cat: {liter_cat:.2f} liter")
    except ValueError:
        label_hasil_cat.config(text="Masukkan angka yang valid.")

def on_return(event):
    # Memanggil semua fungsi yang diinginkan
    hitung_cat()
    calculate_volume_rectangle()
    hitung_balok()
    hitung_luas_volume()
    hitung_material()
    hitung_material_beton()
    hitung()
    hitung_urugan_kembali()
    volume_truk ()
    calculate_rebar_usage ()
    Hitung_Besi_Behel ()
    hitung_cat ()

entries = []
def clear_entries():
    # Mengosongkan semua entrian
    for entry in entries:
        entry.delete(0, tk.END)

    entries.extend([
        entry_panjang_balok, entry_tinggi_volume, entry_lebar_volume, entry_panjang_volume,
        entry_A, entry_B, entry_T, entry_P, entry_volume,
        entry_panjang, entry_lebar, entry_tebal, entry_panjang_urug, entry_lebar_urug,
        entry_kedalaman_urug, entry_ketinggian_urug, entry_length, entry_width, entry_height,
        entry_total_length, entry_rebars_per_element, entry_panjang_sloof,
        entry_panjang_keliling, entry_jarak_behel, entry_panjang_area, entry_lebar_area,
        entry_tinggi_area, entry_panjang_dinding, entry_lebar_dinding, entry_sebar
    ])

def add_watermark_full_frame(tab):
    watermark_path = "F:\\Aplikasi\\HItungVol.01\\Axvolpic.png"
    try:
        # Load and convert the watermark image
        watermark = Image.open(watermark_path).convert("RGBA")
        photo = ImageTk.PhotoImage(watermark)

        # Create a label for the watermark
        watermark_label = tk.Label(tab, image=photo)
        watermark_label.image = photo  
        watermark_label.place(relx=0.5, rely=0.5, anchor='center', relwidth=1.0, relheight=1.0)
    except Exception as e:
        print(f"Error loading watermark image: {e}")

def add_logo_to_tab(tab):
    Logo_path = "F:\\Aplikasi\\HItungVol.01\\logo2_0012.jpg"
    try:
        # Load and convert the logo image
        Logo = Image.open(Logo_path).convert("RGBA")
        photo = ImageTk.PhotoImage(Logo)

        # Create a label for the logo
        logo_label = tk.Label(tab, image=photo)
        logo_label.image = photo 
        padding_horizontal = 20
        logo_label.place(relx=1.0, rely=1.0, anchor='se', x=-padding_horizontal, y=-10)
    except Exception as e:
        print(f"Error loading logo image: {e}")

# Setup the main GUI
def setup_gui():
    global entry_panjang_balok, entry_tinggi_volume, entry_lebar_volume, entry_panjang_volume
    global entry_A, entry_B, entry_T, entry_P, entry_volume
    global label_hasil_balok, label_hasil_volume, label_hasil_luas_volume, label_hasil_material_beton
    global entry_panjang, entry_lebar, entry_tebal, entry_panjang_urug, entry_lebar_urug, entry_kedalaman_urug, entry_ketinggian_urug
    global label_hasil, label_hasil_urugan, entry_length, entry_width, entry_height
    global label_result_volume, entry_total_length, entry_rebars_per_element, result_rebar_label, entry_panjang_sloof
    global entry_panjang_keliling, entry_jarak_behel, label_result1, label_result_luas, entry_panjang_area, entry_lebar_area
    global entry_tinggi_area, label_hasil_area, entry_panjang_dinding, entry_lebar_dinding, label_hasil_cat, entry_sebar, root
    global tab_material, tab_balok, tab_beton
    
    root = tk.Tk()
    root.title("Kalkulator Konstruksi")

    root.bind('<Return>', on_return)
    root.state('zoomed')

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", pady=10, expand=True)
    
    # Beam Tab
    tab_balok = ttk.Frame(notebook)
    notebook.add(tab_balok, text="Hitung Balok")
    add_watermark_full_frame(tab_balok)
    add_logo_to_tab(tab_balok)

    ttk.Label(tab_balok, text="Panjang Bentang (cm):").grid(row=0, column=0, pady=10, padx=10)
    entry_panjang_balok = ttk.Entry(tab_balok)
    entry_panjang_balok.grid(row=0, column=1, pady=10, padx=10)

    ttk.Button(tab_balok, text="Hitung", command=hitung_balok).grid(row=1, column=0, pady=10, padx=10)
    label_hasil_balok = ttk.Label(tab_balok, text="")
    label_hasil_balok.grid(row=1, column=1, pady=10, padx=10)
    

    # Concrete Tab
    tab_beton = ttk.Frame(notebook)
    notebook.add(tab_beton, text="Volume Beton")
    add_watermark_full_frame(tab_beton)
    add_logo_to_tab(tab_beton)

    tk.Label(tab_beton, text="Panjang (cm):").grid(row=0, column=0, pady=10, padx=10)
    entry_panjang_volume = ttk.Entry(tab_beton)
    entry_panjang_volume.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(tab_beton, text="Lebar (cm):").grid(row=1, column=0, padx=10, pady=10)
    entry_lebar_volume = ttk.Entry(tab_beton)
    entry_lebar_volume.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(tab_beton, text="Tinggi (cm):").grid(row=2, column=0)
    entry_tinggi_volume = ttk.Entry(tab_beton)
    entry_tinggi_volume.grid(row=2, column=1, pady=10, padx=10)

    ttk.Button(tab_beton, text="Hitung", command=hitung_material).grid(row=3, column=1)
    label_hasil_volume = ttk.Label(tab_beton, text="")
    label_hasil_volume.grid(column=1)
    

    # Foundation Volume Tab
    tab_pondasi = ttk.Frame(notebook)
    notebook.add(tab_pondasi, text='Volume Pondasi')
    add_logo_to_tab(tab_pondasi)

    tk.Label(tab_pondasi, text="Lebar Atas (cm):").grid(row=0, column=0, padx=10, pady=10)
    entry_A = ttk.Entry(tab_pondasi)
    entry_A.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(tab_pondasi, text="Lebar Bawah (cm):").grid(row=1, column=0, padx=10, pady=10)
    entry_B = ttk.Entry(tab_pondasi)
    entry_B.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(tab_pondasi, text="Tinggi (cm):").grid(row=2, column=0, padx=10, pady=10)
    entry_T = ttk.Entry(tab_pondasi)
    entry_T.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(tab_pondasi, text="Panjang (m):").grid(row=3, column=0, padx=10, pady=10)
    entry_P = ttk.Entry(tab_pondasi)
    entry_P.grid(row=3, column=1, padx=10, pady=10)

    ttk.Button(tab_pondasi, text="Hitung", command=hitung_luas_volume).grid(row=4, column=0)
    label_hasil_luas_volume = ttk.Label(tab_pondasi, text="")
    label_hasil_luas_volume.grid(row=5, columnspan=2)


    # Material Tab
    tab_material = ttk.Frame(notebook)
    notebook.add(tab_material, text='Material Pondasi')
    add_watermark_full_frame(tab_material)
    add_logo_to_tab(tab_material)

    tk.Label(tab_material, text="Masukkan volume beton (m³):").grid(row=0, column=0, padx=10, pady=10)
    entry_volume = ttk.Entry(tab_material)
    entry_volume.grid(row=0, column=1, padx=10, pady=10)

    ttk.Button(tab_material, text="Hitung", command=hitung_material_beton).grid(row=1, columnspan=2, padx=10, pady=10)
    label_hasil_material_beton = ttk.Label(tab_material, text="")
    label_hasil_material_beton.grid(row=2, columnspan=2, padx=10, pady=10)
    
    # plesteran Tab
    tab_pelesteran = ttk.Frame(notebook)
    notebook.add(tab_pelesteran, text='Pelesteran/Acian')
    add_logo_to_tab(tab_pelesteran)

    # Label dan Entry untuk panjang
    label_panjang = tk.Label(tab_pelesteran, text="Panjang Dinding (m):")
    label_panjang.grid(row=0, column=0, padx=10, pady=10)
    entry_panjang = ttk.Entry(tab_pelesteran)
    entry_panjang.grid(row=0, column=2, padx=10, pady=10)

    # Label dan Entry untuk lebar
    label_lebar = tk.Label(tab_pelesteran, text="Lebar Dinding (m):")
    label_lebar.grid(row=1, column=0, padx=10, pady=10)
    entry_lebar = ttk.Entry(tab_pelesteran)
    entry_lebar.grid(row=1, column=2, padx=10, pady=10)

    # Label dan Entry untuk ketebalan
    label_tebal = tk.Label(tab_pelesteran, text="Ketebalan Plesteran (m):")
    label_tebal.grid(row=2, column=0, padx=10, pady=10)
    entry_tebal = ttk.Entry(tab_pelesteran)
    entry_tebal.grid(row=2, column=2, padx=10, pady=10)

    # Tombol untuk menghitung
    button_hitung = ttk.Button(tab_pelesteran, text="Hitung", command=hitung)
    button_hitung.grid(row=3, column=2, padx=10, pady=10)
    
    # Label untuk menampilkan hasil
    label_hasil = tk.Label(tab_pelesteran, text="")
    label_hasil.grid(row=4, column=2, padx=10, pady=10)

    #tab urug
    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text='Urugan Kembali')
    add_logo_to_tab(tab3)

    # Label dan Entry untuk urugan
    tk.Label(tab3, text="Panjang (cm):").grid(row=0, column=0, padx=10, pady=10)
    entry_panjang_urug = ttk.Entry(tab3)
    entry_panjang_urug.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(tab3, text="Lebar Bawah (cm):").grid(row=1, column=0, padx=10, pady=10)
    entry_lebar_urug = ttk.Entry(tab3)
    entry_lebar_urug.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(tab3, text="Kedalaman pondasi (cm):").grid(row=2, column=0, padx=10, pady=10)
    entry_kedalaman_urug = ttk.Entry(tab3)
    entry_kedalaman_urug.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(tab3, text="Ketinggian urugan (cm):").grid(row=3, column=0, padx=10, pady=10)
    entry_ketinggian_urug = ttk.Entry(tab3)
    entry_ketinggian_urug.grid(row=3, column=1, padx=10, pady=10)

    # Tombol untuk menghitung urugan
    button_hitung_urugan = ttk.Button(tab3, text="Hitung Urugan Kembali", command=hitung_urugan_kembali)
    button_hitung_urugan.grid(row=4, columnspan=2)
    
    # Label untuk menampilkan hasil urugan
    label_hasil_urugan = tk.Label(tab3, text="", font=("Helvetica", 12))
    label_hasil_urugan.grid(row=5, columnspan=2)

    
    #tab hitung Volume m3___________________________
    tab4 = ttk.Frame(notebook)
    notebook.add(tab4, text='Volume kubik')
    add_logo_to_tab(tab4)

    # Persegi Panjang
    ttk.Label(tab4, text="Panjang (m):").grid(row=0, column=0, padx=10, pady=10)
    entry_length = ttk.Entry(tab4)
    entry_length.grid(row=0, column=1, padx=10, pady=10)
    #entries.append(entry_length)

    ttk.Label(tab4, text="Lebar (m):").grid(row=1, column=0, padx=10, pady=10)
    entry_width = ttk.Entry(tab4)
    entry_width.grid(row=1, column=1, padx=10, pady=10)
    #entries.append(entry_width)

    ttk.Label(tab4, text="Tinggi (m):").grid(row=2, column=0, padx=10, pady=10)
    entry_height = ttk.Entry(tab4)
    entry_height.grid(row=2, column=1, padx=10, pady=10)
    #entries.append(entry_height)

    ttk.Button(tab4, text="Hitung Meter Kubik", command=calculate_volume_rectangle).grid(row=3, column=1)
    label_result_volume = ttk.Label(tab4, text="Volume:")
    label_result_volume.grid(row=4, column=0, columnspan=8)
    label_result_luas = ttk.Label(tab4, text="Luas Area:")
    label_result_luas.grid(row=6, column=0, columnspan=8)
    

    # tab batang besi
    tab5 = ttk.Frame(notebook)
    notebook.add(tab5, text='Jumlah Besi')
    add_logo_to_tab(tab5)

    ttk.Label(tab5, text="Panjang Total (m):").grid(row=0, column=0, padx=10, pady=10)
    entry_total_length = ttk.Entry(tab5)
    entry_total_length.grid(row=0, column=1)
    #entries.append(entry_total_length)

    ttk.Label(tab5, text="Jumlah Besi per kolom:").grid(row=1, column=0, padx=10, pady=10)
    entry_rebars_per_element = ttk.Entry(tab5)
    entry_rebars_per_element.grid(row=1, column=1)
    #entries.append(entry_rebars_per_element)

    ttk.Button(tab5, text="Hitung Batang Besi", command=calculate_rebar_usage).grid(row=2, column=0, columnspan=2, pady=10)
    result_rebar_label = ttk.Label(tab5, text="Hasil Batang Besi:")
    result_rebar_label.grid(row=3, column=0, columnspan=4)
    

    # tab behel
    tab6 = ttk.Frame(notebook)
    notebook.add(tab6, text='Besi Behel')
    add_logo_to_tab(tab6)

    ttk.Label(tab6, text="Panjang Sloof (meter):").grid(row=0, column=0, pady=10, padx=10)
    entry_panjang_sloof = ttk.Entry(tab6)
    entry_panjang_sloof.grid(row=0, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_sloof)

    # Input untuk panjang keliling sloof
    ttk.Label(tab6, text="Panjang Behel (meter):").grid(row=1, column=0, pady=10, padx=10)
    entry_panjang_keliling = ttk.Entry(tab6)
    entry_panjang_keliling.grid(row=1, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_keliling)

    # Input untuk jarak antar behel
    ttk.Label(tab6, text="Jarak Antar Behel (cm):").grid(row=2, column=0, pady=10, padx=10)
    entry_jarak_behel = ttk.Entry(tab6)
    entry_jarak_behel.grid(row=2, column=1,  pady=10, padx=10)
    #entries.append(entry_jarak_behel)

    # Tombol hitung
    button_hitung = ttk.Button(tab6, text="Hitung", command=Hitung_Besi_Behel)
    button_hitung.grid(row=3, column=0, pady=10)


    # Label untuk menampilkan hasil
    label_result1 = ttk.Label(tab6, text="", font=("Arial",10), style="Custom.TLabel")
    label_result1.grid(row=4, column=0, columnspan=2, pady=10)


# tab timbunan__________________________________
    tab7 = ttk.Frame(notebook)
    notebook.add(tab7, text='Timbunan')
    add_logo_to_tab(tab7)

    ttk.Label(tab7, text="Panjang (meter):").grid(row=0, column=0, pady=10, padx=10)
    entry_panjang_area = ttk.Entry(tab7)
    entry_panjang_area.grid(row=0, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_sloof)

    ttk.Label(tab7, text="Lebar (meter):").grid(row=1, column=0, pady=10, padx=10)
    entry_lebar_area = ttk.Entry(tab7)
    entry_lebar_area.grid(row=1, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_keliling)

    ttk.Label(tab7, text="Tinggi (meter):").grid(row=2, column=0, pady=10, padx=10)
    entry_tinggi_area = ttk.Entry(tab7)
    entry_tinggi_area.grid(row=2, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_keliling)

    # Tombol hitung
    button_hitung = ttk.Button(tab7, text="Hitung", command=volume_truk)
    button_hitung.grid(row=3, column=0, pady=10)
    
    
    label_hasil_area = ttk.Label(tab7, text="", font=("Arial",10), style="Custom.TLabel")
    label_hasil_area.grid(row=4, column=0, columnspan=2, pady=10)

# tab cat_______________________________________
    tab8 = ttk.Frame(notebook)
    notebook.add(tab8, text='Pengecatan')
    add_logo_to_tab(tab8)

    ttk.Label(tab8, text="Panjang (meter):").grid(row=0, column=0, pady=10, padx=10)
    entry_panjang_dinding = ttk.Entry(tab8)
    entry_panjang_dinding.grid(row=0, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_sloof)

    label = ttk.Label(tab8, text="Lebar (meter):", anchor='w')
    label.grid(row=1, column=0, pady=10, padx=10)
    entry_lebar_dinding = ttk.Entry(tab8)
    entry_lebar_dinding.grid(row=1, column=1,  pady=10, padx=10)
    #entries.append(entry_panjang_keliling)

    label = ttk.Label(tab8, text="Daya Sebar (meter):", anchor='w')
    label.grid(row=2, column=0, pady=10, padx=10)
    entry_sebar = ttk.Entry(tab8)
    entry_sebar.grid(row=2, column=1,  pady=10, padx=10)
    entries.append(entry_sebar)   

    # Tombol hitung
    button_hitung = ttk.Button(tab8, text="Hitung", command=hitung_cat)
    button_hitung.grid(row=3, column=0, pady=10)

    label_hasil_cat = ttk.Label(tab8, text="", font=("Arial",10), style="Custom.TLabel")
    label_hasil_cat.grid(row=4, column=0, columnspan=2, pady=10)
    
    # Tombol untuk menutup aplikasi
    close_button = ttk.Button(root, text="Tutup", command=root.quit)
    close_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

    # style entry
    style = ttk.Style()
    style.configure("TEntry", Fieldbackground="lightblue")

    #Style label
    style = ttk.Style()
    style.configure("Custom.TLabel", background="lightgreen")

    # style button
    style = ttk.Style()
    style.configure("TButton", background="lightgreen", padding=5)

    # Tombol untuk mengosongkan entrian
    clear_button = ttk.Button(root, text="Hapus", command=clear_entries, style="TButton")
    clear_button.place(relx=1.0, rely=0.035, anchor='ne', x=-10, y=10)


    root.mainloop()

# Execute the setup
setup_gui()
