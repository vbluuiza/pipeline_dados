from process_data import Data

path_json = 'raw_data/dados_empresaA.json'
path_csv = 'raw_data/dados_empresaB.csv'

# Extract 
companyA_data = Data(path_json, 'json')
companyB_data = Data(path_csv, 'csv')

print(f'Path Company A: {companyA_data.path} | File Type: {companyA_data.file_type}\n')
print(f'Path Company B: {companyB_data.path} | File Type: {companyB_data.file_type}\n')

print(f'Company A Data: {companyA_data.data[0]}\n')
print(f'Company B Data: {companyB_data.data[0]}\n')

print(f'Columns from Company A: {companyA_data.columns}\n')
print(f'Columns from Company B: {companyB_data.columns}\n')


# Transform 
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'
            }

companyB_data.rename_columns(key_mapping)
print(f'Renamed Columns from Company B: {companyB_data.columns}\n')

size_data_companyA = companyA_data.size
size_data_companyB = companyB_data.size
print(f'Number of rows in Company A: {size_data_companyA}\n')
print(f'Number of rows in Company B: {size_data_companyB}\n')

merge_data = Data.join_data(companyA_data, companyB_data)
print(f'Merged Data: {merge_data}\n')
print(f'Columns from Mrge Data: {merge_data.columns}\n')
print(f'Number of rows in Merge Data: {merge_data.size}\n')


# Load
path_merge_data = 'processed_data/combined_data.csv'
merge_data.loading_data(path_merge_data)
print(f'Loading Data successfully \n')
