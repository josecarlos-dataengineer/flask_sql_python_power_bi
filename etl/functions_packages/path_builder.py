from os import path
import os

def path_definition(src_layer=1,dstn_layer=2,table_name="table_name",context="dev",src_extension="csv",dstn_extension="csv") -> str:
    """
    Args:
        layer (int): A camada onde será salvo/coletado o arquivo
        context (str): contexto pode ser dev, prod ou teste
        table_name (str): Nome da tabela
        extension (str): Extensão do arquivo

    Returns:
        str: caminho a salvar/coletar um arquivo
    """
 

    layers = {
    1:"1_landing",
    2:"2_processed",
    3:"3_consume"
    }
    
    src_key = f"{table_name}.{src_extension}"
    dstn_key = f"{table_name}.{dstn_extension}"
    src_dir_path = os.path.join(os.getcwd(),layers[src_layer],context,src_key)
    dstn_dir_path = os.path.join(os.getcwd(),layers[dstn_layer],context,dstn_key)
    
    return [src_dir_path,src_extension, dstn_dir_path,dstn_extension]



def path_builder(dir_path: str) -> str:
    # Divide o caminho e obtém a parte anterior ao último separador
    dir = dir_path.rsplit('\\', 1)[0] + '\\'

    # Cria o diretório se ele não existir
    os.makedirs(dir, exist_ok=True)
    
    
    # Retorna o caminho do diretório como string
    return dir


# path, extension = path_definition(1,"vendas",extension="bin")
# path_builder(path) 
