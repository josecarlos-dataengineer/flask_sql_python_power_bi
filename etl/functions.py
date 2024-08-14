import requests
import json
from io import BytesIO,StringIO
import pandas as pd
from functions_packages.path_builder import path_definition,path_builder
import datetime as dt

def is_api_available(table_name:str) -> list:
    """
    Args:
        table_name (str): Nome da tabela a qual se consulta via API

    Raises:
        Exception: Indisponibilidade do serviço

    Returns:
        str: lista com mensagem 'Disponíve', response e url
    """
    url = f"http://127.0.0.1:5000/api/tabela/{table_name}"
    response = requests.get(url)

    if str(response) == "<Response [200]>":
        return ["disponível",str(response),url]
    else:
        raise Exception(f"Url: {url} indisponível: {response}")

def get_data_from_api(table_name) -> tuple: 
    """_summary_

    Args:
        table_name (_type_): Nome da tabela a qual se consulta via API

    Returns:
        tuple: response.content,table_name
    """
    resp_list = is_api_available(table_name)
    if resp_list[0] == "disponível":
        response = requests.get(resp_list[2])
        # data = json.load(response.content)
    
    return response.content,table_name

def writeson_landing(table_name:str,layer=1,extension="json") -> object:
    """_summary_

    Args:
        table_name (str): Nome da tabela a qual se consulta via API
        layer (int, optional): Camada na qual será escrito o arquivo. Defaults to 1.
        extension (str, optional): Extensão do arquivo. Defaults to "json".
    Calls: 
        get_data_from_api(): Requisita API através do nome da tabela
        path_definition(): Define o diretório conforme table_name,layer e extension
        path_builder(): Cria o diretório, caso não exista

    Writes:
        object: Escreve o objeto no diretorio definido
    """
    
    data, table_name = get_data_from_api(table_name)

    src_path, src_extension,dstn_path,dstn_extension = path_definition(
        src_layer=layer,
        table_name=table_name,
        src_extension=extension)

    path_builder(src_path)

    with BytesIO(data) as file_like_object:

        # Abre um arquivo local em modo binário para escrita
        with open(src_path, 'wb') as local_file:

            # Escreve o conteúdo do BytesIO no arquivo local
            local_file.write(file_like_object.getbuffer())



def read_from_landing(table_name:str,layer=1,extension="json") -> object:
    """_summary_

    Args:
        table_name (str): Nome da tabela a qual se consulta via API
        layer (int, optional): Camada na qual será escrito o arquivo. Defaults to 1.
        extension (str, optional): Extensão do arquivo. Defaults to "json".

    Returns:
        object: Pandas DataFrame
    """

    src_path, src_extension,dstn_path,dstn_extension = path_definition(
        src_layer=layer,
        table_name=table_name,
        src_extension=extension)    

    with open(src_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        df = pd.DataFrame(data)

        return df    
    
def add_columns(df:pd.DataFrame,table_name:str) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): Pandas Dataframe a ser tratado
        table_name (str): Nome da tabela fonte do Dataframe

    Returns:
        pd.DataFrame: Pandas Dataframe com a nova coluna 'load_date'
    """
    # df["table_name"] = table_name
    df["load_date"] = dt.datetime.now()
    return df 
    

def writeson_processed(table_name:str,layer=2,extension="csv") -> object:
    """
    Args:
        table_name (str): Nome da tabela a ser coletada e escrita
        layer (int, optional): Camada na qual será escrito o arquivo. Defaults to 2.
        extension (str, optional): Extensão do arquivo. Defaults to "csv".

    Writes:
        object: csv file
    
    example: 
        writeson_processed(table_name="vendedores")
    """
    src_path, src_extension,dstn_path,dstn_extension = path_definition(
        dstn_layer=layer,
        table_name=table_name,
        dstn_extension=extension)
    
    path_builder(dstn_path)
    
    df = read_from_landing(table_name=table_name) 
    df = add_columns(df,table_name)
    df.to_csv(dstn_path,sep=";",index=None,encoding="utf-8")



def writeson_consume(table_name:list,layer=3,extension="csv") -> object:
    """
    Args:
        table_name (list): Lista de nomes das tabelas a ser coletadas, integradas e escritas
        layer (int, optional): Camada na qual será escrito o arquivo. Defaults to 3.
        extension (str, optional): Extensão do arquivo. Defaults to "csv".

    Writes:
        object: arquivo csv com a integração das tabelas produtos. clientes,vendedores e vendas
        
    writeson_consume(table_name="vendedores")
    """
    src_path, src_extension,dstn_path,dstn_extension = path_definition(
        src_layer=2,
        dstn_layer=layer,
        table_name=table_name,
        dstn_extension=extension)
    
    src = path_builder(src_path)
    dtsn = path_builder(dstn_path)
    
    df_dict = {}
    idx = 0
    for table in table_name:        
        
        df = pd.read_csv(src + table_name[idx] + "." +src_extension,encoding="utf-8",sep=";") 
        df = df.drop(columns=["table_id","load_date"])
        df_dict[table] = df 
        
        # df_dict[idx] = df
        idx += 1
    
    df = df_dict["vendas"] \
    .merge(df_dict["clientes"],on="id_cliente")  \
    .merge(df_dict["produtos"],on="id_produto") \
    .merge(df_dict["vendedores"],on="id_vendedor")  
    
    df.to_csv(dtsn + "obt." + dstn_extension,sep=";",encoding="utf-8",index=None)
        
    return 
        
        # df.to_csv(dstn_path,sep=";",index=None,encoding="utf-8")

if __name__ == "__main__":
    lst = ["produtos","clientes","vendas","vendedores"]
    api_ = []
    for i in lst:
        x = is_api_available(i)
        api_.append(x)
        writeson_landing(table_name=i)
        writeson_processed(table_name=i)
        
    writeson_consume(table_name=lst)
    
