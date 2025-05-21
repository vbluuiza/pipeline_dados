import json
import csv

class Data:
    def __init__(self, path, file_type): 
        self.path = path
        self.file_type = file_type
        self.data = self.read_data()
        self.columns = self.get_columns()
        self.size = self.size_data()
        
    
    def read_json(self):
        json_data = []
        with open(self.path, 'r') as file:
            json_data = json.load(file)
        return json_data

    def read_csv(self):
        csv_data = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                csv_data.append(row)
        return csv_data

    def read_data(self):
        data = []
        if self.file_type == 'json':
            data = self.read_json( )
        elif self.file_type == 'csv':
            data = self.read_csv()
        elif self.file_type == 'list':
            data = self.path
            self.path = 'List in memory'
        else:
            raise ValueError("Unsupported file type. Use 'json' or 'csv'.")
        
        return data
    
    def get_columns(self):
        return list(self.data[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_data = []

        for old_dict in self.data:
            new_dict = {}
            for old_key, value in old_dict.items():
                new_dict[key_mapping.get(old_key, old_key)] = value
            new_data.append(new_dict)

        self.data = new_data
        self.columns = self.get_columns()

    def size_data(self):
        return len(self.data)
    
    def join_data(dataA, dataB):
        combined_list = []
        combined_list.extend(dataA.data)
        combined_list.extend(dataB.data)
        return Data(combined_list, 'list')
    
    def transform_data_table(self):
        data_combined_table = [self.columns]

        for row in self.data:
            row_temp = [] 
            for column in self.columns:
                row_temp.append(row.get(column, 'Indisponível'))
            data_combined_table.append(row_temp)
            
        return data_combined_table
    
    def loading_data(self, path):
        
        data_combined_table = self.transform_data_table()
        
        with open(path, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data_combined_table)