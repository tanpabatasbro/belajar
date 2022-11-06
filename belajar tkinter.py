import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="black")
window.geometry("400x300")
window.resizable(False,False)
window.title("siapa dia?")
#variabel
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''fungsi ini akan di panggil pada tombol'''
    pesan = f"halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} guanteeng"
    showinfo(title="whazzuppp",message=pesan)
#frame input
input_frame = ttk.Frame(window)
#penempatan grid, pack, plase
input_frame.pack(padx=10,pady=10,fill="x",expan=True)
#komponen-komponen
#1.label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,fill="x",expan=True)
#2.entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=10,fill="x",expan=True)
#3.label nama belakang 
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang")
nama_belakang_label.pack(padx=10,fill="x",expan=True)
#4.entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,pady=10,fill="x",expan=True)
#5.tombol
tombol_ok = ttk.Button(input_frame,text="ok",command=tombol_click)
tombol_ok.pack(fill="x",expan=True,pady=10,padx=10)

window.mainloop()
