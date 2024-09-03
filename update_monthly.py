import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import datetime
from mysql.connector import Error
from tkcalendar import Calendar
import mysql.connector

class UpdateMonthly(ctk.CTkToplevel):
    def __init__(self) -> None:
        super().__init__()

        self.id = 0
        
        center_window(self, 700, 680)
        self.title("ATUALIZAR/CONSULTAR ESTATÍSTICA MENSAL")
        self.resizable(width=False, height=False)

        frame_top = ctk.CTkFrame(self, width=500, height= 280, border_width=2)
        frame_top.pack(side="top", fill="both")

        self.label1 = ctk.CTkLabel(frame_top, text="ATUALIZAR/CONSULTAR ESTATÍSTICA MENSAL", font=("Helvetica", 20)).pack(padx=20, pady=10)      
        self.calendario = Calendar(frame_top, selectmode = 'day', year = datetime.date.today().year, month = datetime.date.today().month, day = datetime.date.today().day)
        self.calendario.pack(pady = 1)

        self.tipo_processual = ctk.CTkComboBox(frame_top, values=['Pré-Familia', 'Pré-Civil', 'Pro-Familia', 'Pro-Civil', "Pré-GERAL", "Pro-GERAL"], width=250)
        self.tipo_processual.pack(padx=10, pady=1)


        self.button_consultar= ctk.CTkButton(frame_top, text="Consultar", command=self.consultar, corner_radius=32, hover_color="#000000", border_width=1).pack(pady=5)        

        frame_mid = ctk.CTkFrame(self, width=350, height= 500, border_width=1)
        frame_mid.pack(side="top", fill="both") 


        frame2 = ctk.CTkFrame(frame_mid, width=350, height= 500, border_width=1)
        frame2.pack(side="left", fill="both", expand=True) 

        self.label_acordos = ctk.CTkLabel(frame2, text="Acordos Obtidos", font=("Helvetica", 11)).pack(padx=1)
        self.total_acordos_obtidos = ctk.CTkEntry(frame2, placeholder_text='Acordos obtidos', width=250)
        self.total_acordos_obtidos.pack(padx=10)

        self.label_sessoes_infrutiferas = ctk.CTkLabel(frame2, text="Sessões Infrutíferas", font=("Helvetica", 11)).pack(padx=1)
        self.total_sessoes_infrutiferas = ctk.CTkEntry(frame2, placeholder_text='Sessões infrutíferas', width=250)
        self.total_sessoes_infrutiferas.pack(padx=10)

        self.label_audiencias_designadas = ctk.CTkLabel(frame2, text="Audiências Designadas", font=("Helvetica", 11)).pack(padx=1)
        self.total_audiencias_designadas = ctk.CTkEntry(frame2, placeholder_text='Audiências designadas', width=250)
        self.total_audiencias_designadas.pack(padx=10)

        self.label_ausencia_requerente = ctk.CTkLabel(frame2, text="Ausência Requerente", font=("Helvetica", 11)).pack(padx=1)
        self.total_ausencia_requerente = ctk.CTkEntry(frame2, placeholder_text='Ausência do requerente', width=250)
        self.total_ausencia_requerente.pack(padx=10)

        self.label_ausencia_requerido = ctk.CTkLabel(frame2, text="Ausência Requerido", font=("Helvetica", 11)).pack(padx=1)
        self.total_ausencia_requerido = ctk.CTkEntry(frame2, placeholder_text='Ausência do requerido', width=250)
        self.total_ausencia_requerido.pack(padx=10)

        self.label_ausencia_partes = ctk.CTkLabel(frame2, text="Ausência das Partes", font=("Helvetica", 11)).pack(padx=1)
        self.total_ausencia_partes = ctk.CTkEntry(frame2, placeholder_text='Ausência das partes', width=250)
        self.total_ausencia_partes.pack(padx=10)


        frame3 = ctk.CTkFrame(frame_mid, width=350, height= 500, border_width=1)
        frame3.pack(side="left", fill="both", expand=True) 


        self.label_sessoes_canceladas = ctk.CTkLabel(frame3, text="Sessões Canceladas", font=("Helvetica", 11)).pack(padx=1)
        self.total_sessoes_canceladas = ctk.CTkEntry(frame3, placeholder_text='Sessões canceladas', width=250)
        self.total_sessoes_canceladas.pack(padx=10)

        self.label_sessoes_redesignadas = ctk.CTkLabel(frame3, text="Sessões Redesignadas", font=("Helvetica", 11)).pack(padx=1)
        self.total_sessoes_redesignadas = ctk.CTkEntry(frame3, placeholder_text='Sessões redesignadas', width=250)
        self.total_sessoes_redesignadas.pack(padx=10)

        # self.label_sessoes_realizar = ctk.CTkLabel(frame3, text="Sessões à Realizar", font=("Helvetica", 11)).pack(padx=1)
        # self.total_sessoes_realizar = ctk.CTkEntry(frame3, placeholder_text='Sessões à realizar', width=250)
        # self.total_sessoes_realizar.pack(padx=10)

        self.label_pauta_dias = ctk.CTkLabel(frame3, text="Pauta em dias", font=("Helvetica", 11)).pack(padx=1)
        self.pauta_dias = ctk.CTkEntry(frame3, placeholder_text='Pauta em dias', width=250)
        self.pauta_dias.pack(padx=10)

        self.label_jg_Dativo = ctk.CTkLabel(frame3, text="JG Dativo", font=("Helvetica", 11)).pack(padx=1)
        self.total_jg_Dativo = ctk.CTkEntry(frame3, placeholder_text='JG Dativo', width=250)
        self.total_jg_Dativo.pack(padx=10)

        self.label_jg_adv = ctk.CTkLabel(frame3, text="JG ADV", font=("Helvetica", 11)).pack(padx=1)
        self.total_jg_adv = ctk.CTkEntry(frame3, placeholder_text='JG Adv', width=250)
        self.total_jg_adv.pack(padx=10)

        self.botao_update= ctk.CTkButton(self, text="Atualizar", command=self.update_estatistica_mensal, corner_radius=32, hover_color="#000000", border_width=1).pack(pady=5)     
        

    def consultar(self):
        self.tipo = self.tipo_processual.get()
        self.data = (datetime.datetime.strptime(self.calendario.get_date(), "%m/%d/%y").strftime("%Y-%m-%d"))
        connection = create_connection("localhost", "root", "root", "cejusc") 
        
        query = f"SELECT * FROM estatistica_mensal where data = '{self.data}' and tipo_processo like '%{self.tipo_processual.get()}%'"
        
        query_geral = f"""select 
                            max(id),
                            max(data),
                            sum(total_acordos_obtidos), 
                            sum(total_sessoes_infrutiferas),
                            sum(total_audiencias_realizadas),
                            sum(total_audiencias_designadas),
                            sum(total_ausencia_requerente),
                            sum(total_ausencia_requerido),
                            sum(total_ausencia_partes),
                            sum(total_sessoes_canceladas),
                            sum(total_sessoes_redesignadas),
                            sum(Total_sessoes_nao_realizadas),                            
                            '-' as pauta_dias,
                            sum(total_jg_Dativo),
                            sum(total_jg_adv),
                            sum(Total_sessões_gratuitas)
                            from estatistica_mensal 
                            where 
                            data = '{self.data}'
                            and tipo_processo like '%{self.tipo_processual.get()[0:3]}%'
                            """

        cursor = connection.cursor()
        try:
            if "GERAL" in self.tipo_processual.get():                
                cursor.execute(query_geral)
            else:
                cursor.execute(query)                
            myresult = cursor.fetchall()   
        except Error as e:
            print(e)
        
        try:
            self.clear_fields()
            self.id = myresult[0][0]
            self.total_acordos_obtidos.insert(0, myresult[0][2])
            self.total_sessoes_infrutiferas.insert(0, myresult[0][3]) 
            self.total_audiencias_designadas.insert(0, myresult[0][5]) 
            self.total_ausencia_requerente.insert(0, myresult[0][6]) 
            self.total_ausencia_requerido.insert(0, myresult[0][7]) 
            self.total_ausencia_partes.insert(0, myresult[0][8]) 
            self.total_sessoes_canceladas.insert(0, myresult[0][9]) 
            self.total_sessoes_redesignadas.insert(0, myresult[0][10]) 
            #self.total_sessoes_realizar.insert(0, myresult[0][12]) 
            self.pauta_dias.insert(0, myresult[0][12]) 
            self.total_jg_Dativo.insert(0, myresult[0][13]) 
            self.total_jg_adv.insert(0, myresult[0][14]) 
        except:
            self.clear_fields()

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

    def update_estatistica_mensal(self):
        if self.id == 0:
            messagebox.showerror("ERRO", "Selecione um registro válido para atualizar")
        else:
            self.total_audiencias_realizadas = (int(self.total_acordos_obtidos.get()) + int(self.total_sessoes_infrutiferas.get()))

            self.total_sessoes_nao_realizadas = (int(self.total_ausencia_requerente.get()) + int(self.total_ausencia_requerido.get()) + int(self.total_ausencia_partes.get())
            + int(self.total_sessoes_canceladas.get()) + int(self.total_sessoes_redesignadas.get()))

            self.total_sessões_gratuitas = (int(self.total_jg_Dativo.get()) + int(self.total_jg_adv.get()))

            val = [self.total_acordos_obtidos.get(), self.total_sessoes_infrutiferas.get(), self.total_audiencias_realizadas, self.total_audiencias_designadas.get(), self.total_ausencia_requerente.get(), self.total_ausencia_requerido.get(), self.total_ausencia_partes.get(), self.total_sessoes_canceladas.get(), self.total_sessoes_redesignadas.get(),self.total_sessoes_nao_realizadas, self.pauta_dias.get(), self.total_jg_Dativo.get(), self.total_jg_adv.get(), self.total_sessões_gratuitas, self.tipo_processual.get(), self.id]

            connection = create_connection("localhost", "root", "root", "cejusc")     
            query = """
            UPDATE estatistica_mensal set total_acordos_obtidos = %s, total_sessoes_infrutiferas = %s, total_audiencias_realizadas= %s, total_audiencias_designadas= %s, total_ausencia_requerente= %s, total_ausencia_requerido= %s, total_ausencia_partes= %s, total_sessoes_canceladas= %s, total_sessoes_redesignadas= %s, Total_sessoes_nao_realizadas= %s, pauta_dias= %s, total_jg_Dativo= %s, total_jg_adv= %s, Total_sessões_gratuitas= %s, tipo_processo= %s
            WHERE id = %s"""
            
            cursor = connection.cursor()
            try:
                question = messagebox.askyesno("Estatística", "Deseja atualizar estatística?")
                if question and not "GERAL" in self.tipo:
                    cursor.execute(query, val)
                    connection.commit() 
                    messagebox.showinfo("Sucesso","Estatística atualizada com sucesso")                   
                else:
                    messagebox.showerror("ERRO", f"Não foi possível atualizar estatística. Tenha certeza de não estar consultando um tipo GERAL antes de atualizar.")
            except Error as e:
                messagebox.showerror("ERRO", f"Erro ao atualizar estatística: {e}")


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