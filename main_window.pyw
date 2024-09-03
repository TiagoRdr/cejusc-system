import customtkinter as ctk
from generate_statistics import GenereteStatistics
from add_monthly_day import MonthlyStatistics
from update_monthly import UpdateMonthly
from minimum_wage import MinimumWage
import mysql.connector
from mysql.connector import Error
from PIL import Image

def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def add_monthly_daily():
    cejusc_main_window.iconify()
    global add_mensal_open_window
    add_mensal_open_window = MonthlyStatistics()

def update_monthly_window():
    cejusc_main_window.iconify()
    global update_monthly_open_window
    update_monthly_open_window = UpdateMonthly()

def minimum_wage_window():
    cejusc_main_window.iconify()
    global minimum_wage_open_window
    minimum_wage_open_window = MinimumWage()

def generate_statistics_window():
    cejusc_main_window.iconify()
    global generate_statistics_open_window
    generate_statistics_open_window = GenereteStatistics()


ctk.set_appearance_mode("System")

cejusc_main_window = ctk.CTk()
cejusc_main_window.title("CEJUSC")
center_window(cejusc_main_window, 400, 370)
cejusc_main_window.resizable(width=False, height=False)

#path_imgs = "C:/system_cejusc/main_window/"
path_imgs = 'C:/Users/tiago/Desktop/Projetos e Cursos/CEJUSC V2/'

button_add_monthly = ctk.CTkButton(cejusc_main_window, text="Adicionar Estatíscia Mensal".upper(), command=add_monthly_daily, anchor=ctk.CENTER, width=400, height=45, corner_radius=32, hover_color="#000000", border_width=1, image=ctk.CTkImage(dark_image=Image.open(path_imgs + "add_monthly.png")))
button_add_monthly.pack(padx=20, pady=20)

button_update_monthly = ctk.CTkButton(cejusc_main_window, text="Consultar/Atualizar Estatíscia Mensal".upper(), command=update_monthly_window, anchor=ctk.CENTER, width=400, height=45, corner_radius=32, hover_color="#000000", border_width=1, image=ctk.CTkImage(dark_image=Image.open(path_imgs +"update_statistics.png")))
button_update_monthly.pack(padx=20, pady=20)

button_minimum_wage = ctk.CTkButton(cejusc_main_window, text="Gerar planilha de Salário Mínimo".upper(), command=minimum_wage_window, anchor=ctk.CENTER, width=400, height=45, corner_radius=32, hover_color="#000000", border_width=1, image=ctk.CTkImage(dark_image=Image.open(path_imgs +"money.png")))
button_minimum_wage.pack(padx=20, pady=20)

button_generate_statistics = ctk.CTkButton(cejusc_main_window, text="Gerar Estatística Mensal/Anual".upper(), command=generate_statistics_window, anchor=ctk.CENTER, width=400, height=45, corner_radius=32, hover_color="#000000", border_width=1, image=ctk.CTkImage(dark_image=Image.open(path_imgs + "analytics.png")))
button_generate_statistics.pack(padx=20, pady=20)

cejusc_main_window.mainloop()