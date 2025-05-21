import json
import csv

# Read CSV file
def read_json(path_json):
    json_data = []
    with open(path_json, 'r') as file:
        json_data = json.load(file)
    return json_data

# Read CSV file
def read_csv(path_csv):
    csv_data = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            csv_data.append(row)
    return csv_data

# Read data from JSON or CSV file
def read_data(path, file_type):
    if file_type == 'json':
        data = read_json(path)
    elif file_type == 'csv':
        data = read_csv(path)
    else:
        raise ValueError("Unsupported file type. Use 'json' or 'csv'.")
    
    return data

# Get columns from the data
def get_columns(data):
    return list(data[-1].keys())
 
# Rename columns based on a mapping   
def rename_columns(data, key_mapping):
    """
    Rename columns in the data based on the provided key mapping.
    
    Parameters:
    - data: List of dictionaries representing the data.
    - key_mapping: Dictionary mapping old column names to new column names.
    
    Returns:
    - List of dictionaries with renamed columns.
    """
    return [
        { key_mapping.get(old_key): value 
            for old_key, value in old_dict.items() } 
        for old_dict in data
        ]

# Size data
def size_data(data):
    return len(data)

# Join data from two lists
def join_data(dataA, dataB):
    combined_list = []
    combined_list.extend(dataA)
    combined_list.extend(dataB)
    return combined_list

# Transform data in a table format    
def transform_data_table(data, columns_names):
    data_combined_table = [columns_names]

    for row in data:
        row_temp = [] 
        for column in columns_names:
            row_temp.append(row.get(column, 'Indisponível'))
        data_combined_table.append(row_temp)
        
    return data_combined_table

# Loading data to CSV
def loading_data(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
path_json = 'raw_data/dados_empresaA.json'
path_csv = 'raw_data/dados_empresaB.csv'


# Starting read the data
data_json = read_data(path_json, 'json')      
data_csv = read_data(path_csv, 'csv')
print(f'Data from JSON: {data_json[0]}\n')
print(f'Data from CSV: {data_csv[0]}\n')

name_csv_columns = get_columns(data_csv)
name_json_columns = get_columns(data_json)
print(f'Columns from CSV: {name_csv_columns}\n')
print(f'Columns from JSON: {name_json_columns}\n')

size_data_json = size_data(data_json)
size_data_csv = size_data(data_csv)
print(f'Number of rows in JSON: {size_data_json}\n')
print(f'Number of rows in CSV: {size_data_csv}\n')


# Transforming Data
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'
            }

new_csv_data = rename_columns(data_csv, key_mapping)
print(f'New CSV Data: {new_csv_data[0]}\n')

merge_data = join_data(data_json, new_csv_data)
name_columns_merge = get_columns(merge_data)
size_data_merge = size_data(merge_data)
print(f'Columns from Merge Data: {name_columns_merge}\n')
print(f'Number of rows in Merge Data: {size_data_merge}\n')
print(f'Merge Data [0]: {merge_data[0]}\n')
print(f'Merge Data [-1]: {merge_data[-1]}\n')


# Loading Data
data_merge_table = transform_data_table(merge_data, name_columns_merge)
print(f'Data Combined Table: {data_merge_table[0]}\n')

path_merge_data = 'processed_data/combined_data.csv'

loading_data(path_merge_data, data_merge_table)
print(f'Loading data to {path_merge_data} completed.\n')

