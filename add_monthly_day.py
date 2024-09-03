import customtkinter as ctk
from tkinter import messagebox
import datetime
import mysql.connector
from mysql.connector import Error
from tkcalendar import Calendar
import calendar

class MonthlyStatistics(ctk.CTkToplevel):
    def __init__(self) -> None:
        super().__init__()
        center_window(self, 800, 625)
        self.resizable(width=False, height=False)
        self.label1 = ctk.CTkLabel(self, text="ADICIONAR ESTATÍSTICA MENSAL", font=("Helvetica", 20)).pack(padx=20, pady=10)

        self.title("ADICIONAR ESTATÍSTICA MENSAL")

        frame_top = ctk.CTkFrame(self, width=500, height= 200, border_width=4)
        frame_top.pack(side="top", fill="both")

        frame2 = ctk.CTkFrame(frame_top, width=350, height= 500, border_width=1)
        frame2.pack(side="left", fill="both", expand=True) 

        self.calendario = Calendar(frame2, selectmode = 'day', year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day)
        self.calendario.pack(pady = 5)
        
        self.label_tipo = ctk.CTkLabel(frame2, text="Tipo processual", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.tipo_processual = ctk.CTkComboBox(frame2, values=['Pré-Familia', 'Pré-Civil', 'Pro-Familia', 'Pro-Civil'], width=250)
        self.tipo_processual.pack(padx=10, pady=3)

        self.label_acordos = ctk.CTkLabel(frame2, text="Acordos Obtidos", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_acordos_obtidos = ctk.CTkEntry(frame2, placeholder_text='Acordos obtidos', width=250)
        self.total_acordos_obtidos.pack(padx=10, pady=3)

        self.label_sessoes_infrutiferas = ctk.CTkLabel(frame2, text="Sessões Infrutíferas", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_sessoes_infrutiferas = ctk.CTkEntry(frame2, placeholder_text='Sessões infrutíferas', width=250)
        self.total_sessoes_infrutiferas.pack(padx=10, pady=3)

        self.label_audiencias_designadas = ctk.CTkLabel(frame2, text="Audiências Designadas", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_audiencias_designadas = ctk.CTkEntry(frame2, placeholder_text='Audiências designadas', width=250)
        self.total_audiencias_designadas.pack(padx=10, pady=3)

        self.label_ausencia_requerente = ctk.CTkLabel(frame2, text="Ausência Requerente", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_ausencia_requerente = ctk.CTkEntry(frame2, placeholder_text='Ausência do requerente', width=250)
        self.total_ausencia_requerente.pack(padx=10, pady=3)




        frame_bot = ctk.CTkFrame(frame_top, width=350, height= 200, border_width=4)
        frame_bot.pack(side="left", fill="both", expand=True)

        self.label_ausencia_requerido = ctk.CTkLabel(frame_bot, text="Ausência Requerido", font=("Helvetica", 11)).pack(padx=1, pady=4)
        self.total_ausencia_requerido = ctk.CTkEntry(frame_bot, placeholder_text='Ausência do requerido', width=250)
        self.total_ausencia_requerido.pack(padx=10, pady=3)

        self.label_ausencia_partes = ctk.CTkLabel(frame_bot, text="Ausência das Partes", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_ausencia_partes = ctk.CTkEntry(frame_bot, placeholder_text='Ausência das partes', width=250)
        self.total_ausencia_partes.pack(padx=10, pady=3)        

        self.label_sessoes_canceladas = ctk.CTkLabel(frame_bot, text="Sessões Canceladas", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_sessoes_canceladas = ctk.CTkEntry(frame_bot, placeholder_text='Sessões canceladas', width=250)
        self.total_sessoes_canceladas.pack(padx=10, pady=3)

        self.label_sessoes_redesignadas = ctk.CTkLabel(frame_bot, text="Sessões Redesignadas", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_sessoes_redesignadas = ctk.CTkEntry(frame_bot, placeholder_text='Sessões redesignadas', width=250)
        self.total_sessoes_redesignadas.pack(padx=10, pady=3)

        # self.label_sessoes_realizar = ctk.CTkLabel(frame_bot, text="Sessões à Realizar", font=("Helvetica", 11)).pack(padx=1, pady=1)
        # self.total_sessoes_realizar = ctk.CTkEntry(frame_bot, placeholder_text='Sessões à realizar', width=250)
        # self.total_sessoes_realizar.pack(padx=10, pady=3)

        self.label_pauta_dias = ctk.CTkLabel(frame_bot, text="Pauta em dias", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.pauta_dias = ctk.CTkEntry(frame_bot, placeholder_text='Pauta em dias', width=250)
        self.pauta_dias.pack(padx=10, pady=3)

        self.label_jg_Dativo = ctk.CTkLabel(frame_bot, text="JG Dativo", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_jg_Dativo = ctk.CTkEntry(frame_bot, placeholder_text='JG Dativo', width=250)
        self.total_jg_Dativo.pack(padx=10, pady=3)

        self.label_jg_adv = ctk.CTkLabel(frame_bot, text="JG ADV", font=("Helvetica", 11)).pack(padx=1, pady=1)
        self.total_jg_adv = ctk.CTkEntry(frame_bot, placeholder_text='JG Adv', width=250)
        self.total_jg_adv.pack(padx=10, pady=3)
        
        self.botao_salvar= ctk.CTkButton(self, text="Salvar", command=self.save_estatistica_mensal, corner_radius=32, hover_color="#000000", border_width=1).pack(pady=10)        


    def save_estatistica_mensal(self):

        question = messagebox.askyesno("Estatística", "Deseja adicionar estatística?")
        if question:
            self.validate_empty_fields()
            self.data_atual = (datetime.datetime.strptime(self.calendario.get_date(), "%m/%d/%y").strftime("%Y-%m-%d"))

            self.total_audiencias_realizadas = (int(self.total_acordos_obtidos.get()) + int(self.total_sessoes_infrutiferas.get()))

            self.total_sessoes_nao_realizadas = (int(self.total_ausencia_requerente.get()) + int(self.total_ausencia_requerido.get()) + int(self.total_ausencia_partes.get())
            + int(self.total_sessoes_canceladas.get()) + int(self.total_sessoes_redesignadas.get()))

            print(self.total_sessoes_canceladas.get(), self.total_sessoes_nao_realizadas)

            self.total_sessões_gratuitas = (int(self.total_jg_Dativo.get()) + int(self.total_jg_adv.get()))

            #Total audiencias a realizar é a soma do saldo do mes anterior + designadas no mes atual - audiencias realizadas no mes atual - audiencias nao realizadas no mes atual

            val = [self.data_atual, self.total_acordos_obtidos.get(), self.total_sessoes_infrutiferas.get(), self.total_audiencias_realizadas, self.total_audiencias_designadas.get(), self.total_ausencia_requerente.get(), self.total_ausencia_requerido.get(), self.total_ausencia_partes.get(), self.total_sessoes_canceladas.get(), self.total_sessoes_redesignadas.get(),self.total_sessoes_nao_realizadas, self.pauta_dias.get(), self.total_jg_Dativo.get(), self.total_jg_adv.get(), self.total_sessões_gratuitas, self.tipo_processual.get()]

            connection = create_connection("localhost", "root", "root", "cejusc")     
            query = """
            INSERT INTO estatistica_mensal (data, total_acordos_obtidos, total_sessoes_infrutiferas, total_audiencias_realizadas, total_audiencias_designadas, total_ausencia_requerente, total_ausencia_requerido, total_ausencia_partes, total_sessoes_canceladas, total_sessoes_redesignadas, Total_sessoes_nao_realizadas, pauta_dias, total_jg_Dativo, total_jg_adv, Total_sessões_gratuitas, tipo_processo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            cursor = connection.cursor()
            try:
                cursor.execute(query, val)
                connection.commit()
                messagebox.showinfo("Sucesso","Estatística inserida com sucesso")
                self.clear_fields()
            except Error as e:
                messagebox.showerror("ERRO", f"Erro ao inserir Estatística: {e}")

    def validate_empty_fields(self):
        if self.total_acordos_obtidos.get() == '':
            self.total_acordos_obtidos.insert(0, '0')
        if self.total_sessoes_infrutiferas.get() == '':
            self.total_sessoes_infrutiferas.insert(0, '0')
        if self.total_audiencias_designadas.get() == '':
            self.total_audiencias_designadas.insert(0, '0')
        if self.total_ausencia_requerente.get() == '':
            self.total_ausencia_requerente.insert(0, '0')
        if self.total_ausencia_requerido.get() == '':
            self.total_ausencia_requerido.insert(0, '0')
        if self.total_ausencia_partes.get() == '':
            self.total_ausencia_partes.insert(0, '0')
        if self.total_sessoes_canceladas.get() == '':
            self.total_sessoes_canceladas.insert(0, '0')
        if self.total_sessoes_redesignadas.get() == '':
            self.total_sessoes_redesignadas.insert(0, '0')
        # if self.total_sessoes_realizar.get() == '':
        #     self.total_sessoes_realizar.insert(0, '0')
        if self.pauta_dias.get() == '':
            self.pauta_dias.insert(0, '0')
        if self.total_jg_Dativo.get() == '':
            self.total_jg_Dativo.insert(0, '0')
        if self.total_jg_adv.get() == '':
            self.total_jg_adv.insert(0, '0')

    def clear_fields(self):
        self.id = 0
        self.total_acordos_obtidos.delete(0, ctk.END)
        self.total_sessoes_infrutiferas.delete(0, ctk.END)
        self.total_audiencias_designadas.delete(0, ctk.END)
        self.total_ausencia_requerente.delete(0, ctk.END)
        self.total_ausencia_requerido.delete(0, ctk.END)
        self.total_ausencia_partes.delete(0, ctk.END)
        self.total_sessoes_canceladas.delete(0, ctk.END)
        self.total_sessoes_redesignadas.delete(0, ctk.END)
        #self.total_sessoes_realizar.delete(0, ctk.END)
        self.pauta_dias.delete(0, ctk.END)
        self.total_jg_Dativo.delete(0, ctk.END)
        self.total_acordos_obtidos.delete(0, ctk.END)
        self.total_jg_adv.delete(0, ctk.END)
    
    


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexão com banco de dados bem-sucedida")
    except Error as e:
        messagebox.showerror("ERRO", f"ERRO AO CONECTAR COM BANCO DE DADOS: {e}")
    return connection

def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

