import pandas as pd
import logging
from pathlib import Path
from typing import List, Dict, Optional, Union


class ExcelHandler:
    """
    Classe para manipular arquivos Excel com chaves de NF-e/NFS-e
    """
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.logger = logging.getLogger(__name__)
        
    def read_excel_data(self, sheet_name: str = None, key_column: str = 'CHAVE_NF') -> pd.DataFrame:
        """
        Lê dados do arquivo Excel
        
        Args:
            sheet_name: Nome da aba (None para primeira aba)
            key_column: Nome da coluna que contém as chaves de NF
            
        Returns:
            DataFrame com os dados do Excel
        """
        try:
            if not self.file_path.exists():
                raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")
            
            # Lê o arquivo Excel com engine específico
            try:
                # Tenta primeiro com openpyxl (formato .xlsx)
                result = pd.read_excel(self.file_path, sheet_name=sheet_name, engine='openpyxl')
            except Exception:
                try:
                    # Se falhar, tenta com xlrd (formato .xls)
                    result = pd.read_excel(self.file_path, sheet_name=sheet_name, engine='xlrd')
                except Exception:
                    # Como último recurso, deixa o pandas decidir
                    result = pd.read_excel(self.file_path, sheet_name=sheet_name)
            
            # Se sheet_name é None, pandas pode retornar dict com todas as abas
            if isinstance(result, dict):
                # Pega a primeira aba disponível
                first_key = list(result.keys())[0]
                df = result[first_key]
                self.logger.info(f"Usando primeira aba encontrada: {first_key}")
            else:
                df = result
            
            # Verifica se df é realmente um DataFrame
            if not isinstance(df, pd.DataFrame):
                raise ValueError("Erro ao ler arquivo Excel: formato inválido")
            
            # Verifica se a coluna de chaves existe
            if key_column not in df.columns:
                # Tenta encontrar uma coluna que contenha 'chave' no nome
                possible_columns = [col for col in df.columns if 'chave' in col.lower()]
                if possible_columns:
                    key_column = possible_columns[0]
                    self.logger.warning(f"Coluna '{key_column}' não encontrada. Usando '{key_column}'")
                else:
                    raise ValueError(f"Coluna '{key_column}' não encontrada no arquivo")
            
            # Adiciona colunas de resultado se não existirem
            if 'STATUS_VALIDACAO' not in df.columns:
                df['STATUS_VALIDACAO'] = None
            if 'DATA_VALIDACAO' not in df.columns:
                df['DATA_VALIDACAO'] = None
            if 'DETALHES_ERRO' not in df.columns:
                df['DETALHES_ERRO'] = None
            
            self.logger.info(f"Arquivo Excel lido com sucesso: {len(df)} registros encontrados")
            return df
            
        except Exception as e:
            self.logger.error(f"Erro ao ler arquivo Excel: {str(e)}")
            raise
    
    def save_excel_data(self, df: pd.DataFrame, sheet_name: str = None) -> None:
        """
        Salva dados no arquivo Excel
        
        Args:
            df: DataFrame com os dados para salvar
            sheet_name: Nome da aba para salvar
        """
        try:
            with pd.ExcelWriter(self.file_path, engine='openpyxl', mode='w') as writer:
                df.to_excel(writer, sheet_name=sheet_name or 'Dados', index=False)
            
            self.logger.info(f"Arquivo Excel salvo com sucesso: {self.file_path}")
            
        except Exception as e:
            self.logger.error(f"Erro ao salvar arquivo Excel: {str(e)}")
            raise
    
    def update_validation_status(self, df: pd.DataFrame, index: int, status: str, 
                               details: str = None) -> pd.DataFrame:
        """
        Atualiza o status de validação para uma linha específica
        
        Args:
            df: DataFrame principal
            index: Índice da linha a ser atualizada
            status: Status da validação ('ENCONTRADO', 'NAO_ENCONTRADO', 'ERRO')
            details: Detalhes adicionais ou mensagem de erro
            
        Returns:
            DataFrame atualizado
        """
        try:
            df.at[index, 'STATUS_VALIDACAO'] = status
            df.at[index, 'DATA_VALIDACAO'] = pd.Timestamp.now()
            if details:
                df.at[index, 'DETALHES_ERRO'] = details
                
            return df
            
        except Exception as e:
            self.logger.error(f"Erro ao atualizar status: {str(e)}")
            raise
    
    def validate_nf_key_format(self, key: str) -> bool:
        """
        Valida o formato da chave de NF-e (44 dígitos)
        
        Args:
            key: Chave da NF para validar
            
        Returns:
            True se o formato estiver correto
        """
        if not key:
            return False
            
        # Remove espaços e caracteres especiais
        clean_key = ''.join(filter(str.isdigit, str(key)))
        
        # Verifica se tem 44 dígitos
        return len(clean_key) == 44
    
    def get_pending_validations(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Retorna registros que ainda precisam ser validados
        
        Args:
            df: DataFrame principal
            
        Returns:
            DataFrame filtrado com registros pendentes
        """
        return df[df['STATUS_VALIDACAO'].isna() | (df['STATUS_VALIDACAO'] == '')]
    
    def get_validation_summary(self, df: pd.DataFrame) -> Dict[str, int]:
        """
        Retorna um resumo dos status de validação
        
        Args:
            df: DataFrame principal
            
        Returns:
            Dicionário com contadores por status
        """
        summary = {
            'total': len(df),
            'encontrados': len(df[df['STATUS_VALIDACAO'] == 'ENCONTRADO']),
            'nao_encontrados': len(df[df['STATUS_VALIDACAO'] == 'NAO_ENCONTRADO']),
            'erros': len(df[df['STATUS_VALIDACAO'] == 'ERRO']),
            'pendentes': len(df[df['STATUS_VALIDACAO'].isna() | (df['STATUS_VALIDACAO'] == '')])
        }
        
        return summary