import os
import shutil
import tkinter as tk
from tkinter import messagebox, ttk
from zipfile import ZipFile

# Пути к лаунчерам
launchers_paths = {
    "Legacy Launcher": os.path.join(os.getenv('APPDATA'), ".tlauncher", "legacy", "Minecraft", "game"),
    "TLauncher": os.path.join(os.getenv('APPDATA'), ".minecraft", "versions"),
    "Prism Launcher": os.path.join(os.getenv('APPDATA'), ".prismlauncher", "instances")
}

# Пути к архивам сборок
modpack_zip = "modpack.zip"  # архив с вашей сборкой для Legacy Launcher и Prism Launcher
tlauncher_zip = "AHAHASHECHKI.zip"  # архив с вашей сборкой для TLauncher

def install_modpack(target_path, zip_file):
    try:
        if os.path.exists(target_path):
            with ZipFile(zip_file, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    # Проверка на недопустимые символы и двойные слэши
                    if any(char in member for char in '<>:"|?*') or '\\\\' in member:
                        raise ValueError(f"Invalid file name in archive: {member}")
                
                zip_ref.extractall(target_path)
                
            messagebox.showinfo("ЭЩКЕРЕ", f"Сборка в {target_path}")
        else:
            messagebox.showerror("ДА БЛЯТЬ", f"Путь проебали: {target_path}")
    except Exception as e:
        messagebox.showerror("пиздец", str(e))

def install_for_all_launchers():
    for launcher_name, target_path in launchers_paths.items():
        messagebox.showinfo("Установка", f"Начинается установка сборки для {launcher_name}. сиди не рыпайся")
        if launcher_name == "TLauncher":
            install_modpack(target_path, tlauncher_zip)
        else:
            install_modpack(target_path, modpack_zip)

# Создание GUI
root = tk.Tk()
root.title("Установщик сборки Minecraft")
root.geometry("400x200")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

label = ttk.Label(root, text="Установщик всех вирусов от арбуза", font=("Helvetica", 16))
label.pack(pady=20)

install_button = ttk.Button(root, text="Установить сборку", command=install_for_all_launchers)
install_button.pack(pady=20)

root.mainloop()
