import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import logging
from pathlib import Path
import pandas as pd
from modules.excel_handler import ExcelHandler
from modules.nfe_validator import NFEValidator
from modules.nfse_validator import NFSEValidator


class NFValidatorGUI:
    """
    Interface gráfica para validação de chaves NF-e/NFS-e
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Validador de Chaves NF-e/NFS-e")
        self.root.geometry("800x700")
        
        # Variáveis
        self.file_path = tk.StringVar()
        self.validation_type = tk.StringVar(value="NFE")
        self.city_selection = tk.StringVar(value="sao_paulo")
        self.headless_mode = tk.BooleanVar(value=True)
        self.is_running = False
        
        # Configuração de logging
        self.setup_logging()
        
        # Criar interface
        self.create_widgets()
        
    def setup_logging(self):
        """Configura o sistema de logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/validation.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def create_widgets(self):
        """Cria os widgets da interface"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuração do grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Seleção de arquivo
        ttk.Label(main_frame, text="Arquivo Excel:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.file_path, width=50).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        ttk.Button(main_frame, text="Procurar", command=self.browse_file).grid(row=0, column=2, pady=5)
        
        # Tipo de validação
        ttk.Label(main_frame, text="Tipo de Validação:").grid(row=1, column=0, sticky=tk.W, pady=5)
        type_frame = ttk.Frame(main_frame)
        type_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Radiobutton(type_frame, text="NF-e (Receita Federal)", 
                       variable=self.validation_type, value="NFE").grid(row=0, column=0, sticky=tk.W)
        ttk.Radiobutton(type_frame, text="NFS-e (Prefeituras)", 
                       variable=self.validation_type, value="NFSE").grid(row=0, column=1, sticky=tk.W, padx=20)
        
        # Seleção de cidade (apenas para NFS-e)
        ttk.Label(main_frame, text="Cidade (NFS-e):").grid(row=2, column=0, sticky=tk.W, pady=5)
        city_combo = ttk.Combobox(main_frame, textvariable=self.city_selection, 
                                 values=["sao_paulo", "rio_de_janeiro", "belo_horizonte", "brasilia"])
        city_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Opções avançadas
        options_frame = ttk.LabelFrame(main_frame, text="Opções", padding="5")
        options_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        options_frame.columnconfigure(0, weight=1)
        
        ttk.Checkbutton(options_frame, text="Modo headless (navegador oculto)", 
                       variable=self.headless_mode).grid(row=0, column=0, sticky=tk.W)
        
        # Botões de controle
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=3, pady=10)
        
        self.start_button = ttk.Button(control_frame, text="Iniciar Validação", 
                                      command=self.start_validation)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(control_frame, text="Parar", 
                                     command=self.stop_validation, state="disabled")
        self.stop_button.grid(row=0, column=1, padx=5)
        
        ttk.Button(control_frame, text="Limpar Log", 
                  command=self.clear_log).grid(row=0, column=2, padx=5)
        
        # Barra de progresso
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, 
                                          maximum=100, length=300)
        self.progress_bar.grid(row=5, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E))
        
        # Label de status
        self.status_label = ttk.Label(main_frame, text="Pronto para iniciar")
        self.status_label.grid(row=6, column=0, columnspan=3, pady=5)
        
        # Área de log
        log_frame = ttk.LabelFrame(main_frame, text="Log de Execução", padding="5")
        log_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(7, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, width=80)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configuração do handler de log personalizado
        log_handler = TextHandler(self.log_text)
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(log_handler)
        
    def browse_file(self):
        """Abre diálogo para seleção de arquivo"""
        filename = filedialog.askopenfilename(
            title="Selecionar arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx *.xls"), ("Todos os arquivos", "*.*")]
        )
        if filename:
            self.file_path.set(filename)
    
    def start_validation(self):
        """Inicia o processo de validação"""
        if not self.file_path.get():
            messagebox.showerror("Erro", "Por favor, selecione um arquivo Excel")
            return
        
        if not Path(self.file_path.get()).exists():
            messagebox.showerror("Erro", "Arquivo não encontrado")
            return
        
        self.is_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.progress_var.set(0)
        
        # Inicia validação em thread separada
        thread = threading.Thread(target=self.run_validation, daemon=True)
        thread.start()
    
    def stop_validation(self):
        """Para o processo de validação"""
        self.is_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_label.config(text="Validação interrompida pelo usuário")
    
    def run_validation(self):
        """Executa a validação (executado em thread separada)"""
        try:
            # Lê o arquivo Excel
            self.update_status("Lendo arquivo Excel...")
            excel_handler = ExcelHandler(self.file_path.get())
            df = excel_handler.read_excel_data()
            
            if df.empty:
                self.update_status("Arquivo Excel está vazio")
                return
            
            # Pega registros pendentes
            pending_df = excel_handler.get_pending_validations(df)
            total_records = len(pending_df)
            
            if total_records == 0:
                self.update_status("Todas as chaves já foram validadas")
                return
            
            self.logger.info(f"Iniciando validação de {total_records} registros")
            
            # Inicializa o validador apropriado
            if self.validation_type.get() == "NFE":
                validator = NFEValidator(headless=self.headless_mode.get())
                self.update_status(f"Validando {total_records} chaves NF-e...")
            else:
                validator = NFSEValidator(headless=self.headless_mode.get())
                self.update_status(f"Validando {total_records} chaves NFS-e...")
            
            # Processa cada registro
            for idx, (df_idx, row) in enumerate(pending_df.iterrows()):
                if not self.is_running:
                    break
                
                chave = row.get('CHAVE_NF', '')
                self.logger.info(f"Validando chave {idx+1}/{total_records}: {chave}")
                
                # Executa validação
                try:
                    if self.validation_type.get() == "NFE":
                        result = validator.validate_nfe_key(chave)
                    else:
                        result = validator.validate_nfse_key(chave, self.city_selection.get())
                    
                    # Atualiza o DataFrame
                    if result['status'] == 'ENCONTRADO':
                        df = excel_handler.update_validation_status(df, df_idx, 'ENCONTRADO', result.get('details', ''))
                    elif result['status'] == 'NAO_ENCONTRADO':
                        df = excel_handler.update_validation_status(df, df_idx, 'NAO_ENCONTRADO', result.get('details', ''))
                    else:
                        df = excel_handler.update_validation_status(df, df_idx, 'ERRO', result.get('error_message', ''))
                    
                except Exception as e:
                    self.logger.error(f"Erro ao validar chave {chave}: {str(e)}")
                    df = excel_handler.update_validation_status(df, df_idx, 'ERRO', str(e))
                
                # Atualiza progresso
                progress = ((idx + 1) / total_records) * 100
                self.progress_var.set(progress)
                
                # Salva progresso a cada 5 registros
                if (idx + 1) % 5 == 0 or idx == total_records - 1:
                    excel_handler.save_excel_data(df)
                    self.logger.info(f"Progresso salvo: {idx+1}/{total_records}")
            
            # Fecha o navegador
            validator.close_driver()
            
            # Salva resultado final
            excel_handler.save_excel_data(df)
            
            # Mostra resumo
            summary = excel_handler.get_validation_summary(df)
            self.logger.info(f"Validação concluída - Resumo: {summary}")
            
            self.update_status("Validação concluída com sucesso!")
            
            # Mostra mensagem de conclusão
            messagebox.showinfo("Concluído", 
                              f"Validação concluída!\n\n"
                              f"Total: {summary['total']}\n"
                              f"Encontrados: {summary['encontrados']}\n"
                              f"Não encontrados: {summary['nao_encontrados']}\n"
                              f"Erros: {summary['erros']}\n"
                              f"Pendentes: {summary['pendentes']}")
            
        except Exception as e:
            self.logger.error(f"Erro durante validação: {str(e)}")
            self.update_status(f"Erro: {str(e)}")
            messagebox.showerror("Erro", f"Erro durante validação:\n{str(e)}")
        
        finally:
            self.is_running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
    
    def update_status(self, message):
        """Atualiza a label de status"""
        self.status_label.config(text=message)
    
    def clear_log(self):
        """Limpa a área de log"""
        self.log_text.delete(1.0, tk.END)
    
    def run(self):
        """Inicia a interface gráfica"""
        self.root.mainloop()


class TextHandler(logging.Handler):
    """Handler personalizado para exibir logs no widget Text"""
    
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget
    
    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.configure(state='normal')
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.configure(state='disabled')
            self.text_widget.see(tk.END)
        
        # Usa after para executar na thread principal
        self.text_widget.after(0, append)


if __name__ == "__main__":
    app = NFValidatorGUI()
    app.run()