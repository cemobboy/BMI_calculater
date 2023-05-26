from tkinter import *

window = Tk()
window.title("BMI calculator")
window.minsize(width=250, height=350)

# Kilo Label
kilo_label = Label(text="Kilonuzu girin (kg):", font=('Arial', 14, 'normal'))
kilo_label.grid(row=0, column=0, padx=10, pady=10)

# Boy Label
boy_label = Label(text="Boyunuzu girin (cm):", font=('Arial', 14, 'normal'))
boy_label.grid(row=1, column=0, padx=20, pady=20)

# Kilo Entry
kilo_entry = Entry(width=10)
kilo_entry.grid(row=0, column=1, padx=10, pady=10)

# Boy Entry
boy_entry = Entry(width=10)
boy_entry.grid(row=1, column=1, padx=10, pady=10)

# Hesapla Butonu
def hesapla():
    try:
        kilo = int(kilo_entry.get())
        boy = int(boy_entry.get())
        boy_m = (boy) / 100
        vki = kilo / (boy_m ** 2)
        vki_sonuc = round(vki,2)
        if vki < 18.5:
            vki_label["text"] = f"Vücut Kitle İndeksi: {vki_sonuc} - Zayıf"
        elif vki < 24.9:
            vki_label["text"] = f"Vücut Kitle İndeksi: {vki_sonuc} - Normal"
        elif vki < 29.9:
            vki_label["text"] = f"Vücut Kitle İndeksi: {vki_sonuc} - Fazla kilolu"
        elif vki < 39.9:
            vki_label["text"] = f"Vücut Kitle İndeksi: {vki_sonuc} - Obez"
        else:
            vki_label["text"] = f"Vücut Kitle İndeksi: {vki_sonuc} - Aşırı obez"
    except ValueError:
            vki_label["text"] = "Lütfen girdiginiz değerleri kontrol edin ."


Hesapla_button = Button(text="Hesapla", command=hesapla)
Hesapla_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# VKİ Sonucu Label
vki_label = Label(text="", font=('Arial', 14, 'normal'))
vki_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()