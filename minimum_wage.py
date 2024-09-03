import customtkinter as ctk
import tkinter as tk
from mysql.connector import Error
from tkinter import messagebox
import pandas as pd

class MinimumWage(ctk.CTkToplevel):
    def __init__(self) -> None:
        super().__init__()

        center_window(self, 350, 150)
        self.title("PLANILHA DE SALÁRIO MÍNIMO")
        self.resizable(width=False, height=False)

        self.label_tipo = ctk.CTkLabel(self, text="Insira o salário mínimo atual", font=("Helvetica", 20)).pack(padx=1, pady=10)
        self.salario_atual = ctk.CTkEntry(self, placeholder_text='Salário Mínimo', width=150)
        self.salario_atual.pack(padx=10, pady=1)

        self.button_generate= ctk.CTkButton(self, text="Gerar Planilha", command=self.create_salary_sheet, corner_radius=32, hover_color="#000000", border_width=1).pack(pady=10)     

    def create_salary_sheet(self):
        try:
            salary = float(str(self.salario_atual.get()).replace(",","."))

            valor = ["R$ " + str(salary), "R$ " + str(round((salary / 3),2)), "R$ " + str(round((salary / 2),2))]
            porcentagem = ['100%',"1/3" , "1/2"]

            for i in range(10, 2010, 10):
                valor.append('R$ ' + str(i))
                porcent = round(i * 100 / salary, 2)
                porcentagem.append(str(porcent) + '%')

            list_salary = {'VALOR': valor[0:29], "%%%%1": porcentagem[0:29], 'VALOR2': valor[29:58], "%%%%2": porcentagem[29:58], 'VALOR3': valor[58:87], "%%%%3": porcentagem[58:87], 'VALOR4': valor[87:116], "%%%%4": porcentagem[87:116], 'VALOR5': valor[116:145], "%%%%5": porcentagem[116:145], 'VALOR6': valor[145:174], "%%%%6": porcentagem[145:174], 'VALOR7': valor[174:203], "%%%%7": porcentagem[174:203]}
            
            df_salary = pd.DataFrame(list_salary)
            df_salary = df_salary.rename(columns={'VALOR2':'VALOR', 'VALOR3':'VALOR', 'VALOR4':'VALOR', 'VALOR5':'VALOR', 'VALOR6':'VALOR', 'VALOR7':'VALOR', '%%%%1':'%%%%', '%%%%2':'%%%%', '%%%%3':'%%%%','%%%%4':'%%%%','%%%%5':'%%%%','%%%%6':'%%%%','%%%%7':'%%%%',})
            df_salary.to_excel("C:/Users/CEJUSC-01/Desktop/Salario.xlsx", index=False)
            messagebox.showinfo("Sucesso","Planilha exportada com sucesso")
        except Error as e:
            messagebox.showerror("ERRO", f"ERRO AO GERAR PLANILHA. VERIFIQUE SE O VALOR INSERIDO ESTÁ CORRETO E TENTE NOVAMENTE: {e}")

def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")