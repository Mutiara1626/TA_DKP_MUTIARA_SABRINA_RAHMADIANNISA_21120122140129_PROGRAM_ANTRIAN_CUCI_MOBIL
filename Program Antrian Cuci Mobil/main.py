import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox, Progressbar
import threading
import time

class LoadingScreen(tk.Toplevel):           # class
    def __init__(self, root):               # method untuk inisialisasi
        tk.Toplevel.__init__(self, root)
        self.title("Loading")

        # Mendapatkan lebar dan tinggi layar
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Menghitung posisi x dan y untuk jendela agar berada di tengah
        window_width = 300
        window_height = 60
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Mengatur posisi dan ukuran jendela
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.label = tk.Label(self, text="Memuat...")
        self.label.pack()
        self.progressbar = Progressbar(self, length=200, mode="determinate")
        self.progressbar.pack()

    
    def update(self, value):
        self.label.config(text=f"Memuat... {value}%")
        self.progressbar["value"] = value
        self.update_idletasks()

    def close(self):        
        self.destroy()     


def show_loading_screen(root, main_window):
    loading_screen = LoadingScreen(root)
    for i in range(1, 101):                  #perulangan
        loading_screen.update(i)
        time.sleep(0.05)  # sleep for 0.05 seconds
    loading_screen.close()
    main_window.deiconify()  # show the main window


class AntrianCuciMobil:             # class
    def __init__(self):             # constructor 
        self.antrian = []           # Inisialisasi antrian kosong menggunakan array
        self.riwayat_cucian = []

    def tambah_mobil(self, mobil):
        self.antrian.append(mobil)      # Menambahkan mobil ke antrian menggunakan append 
        print(f"Mobil {mobil} telah ditambahkan ke dalam antrian.")

    def cuci_mobil_berikutnya(self):         
        if len(self.antrian) > 0:                   # pengkondisian
            mobil = self.antrian.pop(0)             # Menghapus dan mengembalikan mobil dari depan antrian dengan dequeue
            self.riwayat_cucian.append(mobil)       # Menambahkan mobil ke riwayat cucian
            print(f"Mobil {mobil} sedang dicuci.")
        else:
            print("Tidak ada mobil dalam antrian.")

    def jumlah_mobil_dalam_antrian(self):          
        return len(self.antrian)

    def get_riwayat_cucian(self):       
        return self.riwayat_cucian
    

#tampilan utama program di tengah
def start_program(): 
    root = tk.Tk()
    root.withdraw()  # halaman utama tetap ditampilkan 

    main_window = tk.Toplevel(root)  # this is the main window
    main_window.withdraw()  # halaman utama tetap ditampilkan 
    main_window.title("Program Antrian Cuci Mobil")

    # Menghitung lebar dan tinggi layar
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # Menghitung lebar dan tinggi jendela 
    window_width = 400
    window_height = 300

    # Hitung koordinat x dan y agar tampilan ditengah
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Mengatur geometri jendela
    main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create an instance of AntrianCuciMobil
    antrian_cuci_mobil = AntrianCuciMobil()

    def show_tambah_mobil_menu():
        tambah_mobil_menu = tk.Toplevel(main_window)
        tambah_mobil_menu.title("Tambah Mobil")

        label_mobil = tk.Label(tambah_mobil_menu, text="Nama Mobil:")
        label_mobil.pack()

        # Create a combo box widget
        combo_mobil = Combobox(tambah_mobil_menu, values=["Avanza", "Pajero", "Inova", "Jazz", "Fortuner", "BMW"])
        combo_mobil.pack()

        def tambah_mobil_button_clicked():
            mobil = combo_mobil.get().strip()
            if mobil:  # Check if a car model is selected
                antrian_cuci_mobil.tambah_mobil(mobil)
                combo_mobil.set("")  # Clear the combo box selection
                update_jumlah_mobil_label()  # Update the label after adding a car
            else:
                messagebox.showerror("Error", "Pilih sebuah mobil dari daftar.")

        tambah_mobil_button = tk.Button(tambah_mobil_menu, text="Tambah mobil ke antrian", command=tambah_mobil_button_clicked)
        tambah_mobil_button.pack(pady=5)

        # Calculate the screen width and height
        screen_width = tambah_mobil_menu.winfo_screenwidth()
        screen_height = tambah_mobil_menu.winfo_screenheight()

        # Calculate the window width and height
        window_width = tambah_mobil_menu.winfo_reqwidth()
        window_height = tambah_mobil_menu.winfo_reqheight()

        # Calculate the x and y coordinates to center the window
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        # Set the window position
        tambah_mobil_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def show_riwayat_mobil_menu():
        riwayat_mobil_menu = tk.Toplevel(main_window)
        riwayat_mobil_menu.title("Riwayat Mobil yang Sudah Dicuci")

        # Calculate the screen width and height
        screen_width = riwayat_mobil_menu.winfo_screenwidth()
        screen_height = riwayat_mobil_menu.winfo_screenheight()

        # Calculate the window width and height
        window_width = 400
        window_height = 300

        # Calculate the x and y coordinates to center the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the window position
        riwayat_mobil_menu.geometry(f"{window_width}x{window_height}+{x}+{y}")

        riwayat_cucian = antrian_cuci_mobil.get_riwayat_cucian()

        if len(riwayat_cucian) > 0:
            for mobil in riwayat_cucian:
                label_mobil = tk.Label(riwayat_mobil_menu, text=f"Mobil: {mobil}")
                label_mobil.pack()
        else:
            label_tidak_ada_riwayat = tk.Label(riwayat_mobil_menu, text="Tidak ada riwayat mobil yang sudah dicuci")
            label_tidak_ada_riwayat.pack()

    def cuci_mobil_button_clicked():
        antrian_cuci_mobil.cuci_mobil_berikutnya()
        update_jumlah_mobil_label()

    def update_jumlah_mobil_label():
        jumlah_mobil = antrian_cuci_mobil.jumlah_mobil_dalam_antrian()
        label_jumlah_mobil.config(text=f"Jumlah mobil dalam antrian: {jumlah_mobil}")

    def keluar_button_clicked():
        result = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin ingin keluar?")
        if result == "yes":
            root.destroy()

    # UI setup
    canvas = tk.Canvas(main_window, width=400, height=300, bg="#2c3a8a")
    canvas.pack()

    frame = tk.Frame(main_window, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # Add the following code to set the background image
    background_image = Image.open("background1.jpg")  # Replace "background_image.jpg" with your image file
    resized_image = background_image.resize((400, 300), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(resized_image)
    background_label = tk.Label(frame, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    label_judul = tk.Label(frame, text="Program Antrian Cuci Mobil", font=("Times New Roman", 16, "bold"), bg=frame["background"], highlightbackground=frame["background"])
    label_judul.pack(pady=10)

    tambah_mobil_button = tk.Button(frame, text="Tambah Mobil", command=show_tambah_mobil_menu, bg="#3d50ba", fg="white")
    tambah_mobil_button.pack(pady=5)

    riwayat_mobil_button = tk.Button(frame, text="Riwayat Mobil yang Sudah Dicuci", command=show_riwayat_mobil_menu, bg="#3d50ba", fg="white")
    riwayat_mobil_button.pack(pady=5)

    label_jumlah_mobil = tk.Label(frame, text="Jumlah mobil dalam antrian: 0", bg="#24b554", fg="white")
    label_jumlah_mobil.pack(pady=10)

    cuci_mobil_button = tk.Button(frame, text="Cuci mobil berikutnya", command=cuci_mobil_button_clicked, bg="#3d50ba", fg="white")
    cuci_mobil_button.pack(pady=5)

    keluar_button = tk.Button(frame, text="Keluar", command=keluar_button_clicked, bg="#3d50ba", fg="white")
    keluar_button.pack(pady=1)

    threading.Thread(target=show_loading_screen, args=(root, main_window)).start()
    root.mainloop()

start_program()
