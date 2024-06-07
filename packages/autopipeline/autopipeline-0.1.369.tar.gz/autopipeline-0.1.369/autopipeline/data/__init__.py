import pkg_resources
import pandas as pd
import importlib.resources as resources

def get_persuasion_effect_data():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/17/persuasive-17.csv')
    df = pd.read_csv(data_file_path)
    df = df[['sentence']]
    return df

def get_toxic_data():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/24/toxic.csv')
    df = pd.read_csv(data_file_path)
    df = df[['original_sentence']]
    return df

def get_dog_whistle_data():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/3/dogwhistle.csv')
    df = pd.read_csv(data_file_path)
    df = df[['Linguistic Context']]
    return df

def get_legal_text():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/legal-text.csv')
    df = pd.read_csv(data_file_path)
    return df

def get_legal_doc():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/legal-doc.csv')
    df = pd.read_csv(data_file_path)
    return df

class QUIET_ML:
    def __init__(self):
        data_file_path = pkg_resources.resource_filename('autopipeline', f'data/queries.csv')
        df = pd.read_csv(data_file_path)
        self.queries = df
        data_file_path = pkg_resources.resource_filename('autopipeline', f'data/desc.csv')
        df = pd.read_csv(data_file_path)
        self.desc = df

    def query_text(self, qid):
        return self.queries.loc[self.queries["QID"] == qid, "Query"].iloc[0]
    
    def query_desc(self, qid):
        return self.desc.loc[self.desc["QID"] == qid, "Description"].iloc[0]
    
    def query_data(self, qid):
        if qid in [83, 84, 85, 86, 87, 88, 89, 92, 93, 98, 99, 100, 101]:
            df = get_legal_text()
        elif qid in [90, 91, 94, 95, 96, 97, 102, 103, 104, 105, 106, 107, 108, 109, 110, 116, 117, 118, 119, 120]:
            df = get_legal_doc()
        else:
            data_file_path = pkg_resources.resource_filename('autopipeline', f'data/{qid}/data.csv')
            df = pd.read_csv(data_file_path)
        return df
    
    def query_answer(self, qid):
        if qid > 82:
            return []
        if qid == 8:
            return [0.9401709401709402]
        elif qid == 29:
            dataframes = [38.51447912749153]
        elif qid == 30:
            dataframes = [39.32038834951456]
        elif qid == 41:
            dataframes = [0.4225370762711864]
        elif qid == 44:
            dataframes = [1340]
        elif qid == 46:
            dataframes = [8190]
        elif qid == 69:
            dataframes = [33.324558]
        elif qid == 70:
            dataframes = [46.809986]
        elif qid == 75:
            dataframes = [24]
        elif qid == 78:
            dataframes = [-29.513333333333332]
        elif qid == 31:
            dataframes = [['Jessica Rabbit', 'Tina Carlyle', 'Susie Diamond', 'Sugar Kane Kowalczyk', 'Dorothy Vallens', 'Ellen Aim']]
        elif qid == 82:
            dataframes = ['Evidence']
        else:
            dataframes = []
        package_name = 'autopipeline'
        directory_name = f'data/{qid}'

        with resources.files(package_name) as pkg_path:
            directory_path = pkg_path / directory_name
            all_files = [f for f in directory_path.iterdir() if f.is_file() and f.name.startswith('answer') and f.name.endswith('.csv')]
            for file_path in all_files:
                df = pd.read_csv(file_path)
                dataframes.append(df)

        return dataframes
    
    # Function to load query, data, desc, and answer altogether
    def query(self, qid):
        query = self.query_text(qid)
        data = self.query_data(qid)
        # answer = self.query_answer(qid)[0]
        answer = self.query_answer(qid)
        description = self.query_desc(qid)
        return {
            "query": query,
            "data": data,
            "desc": description,
            "answer": answer
        }


