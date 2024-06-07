import pkg_resources
import pandas as pd
import importlib.resources as resources
import numpy as np

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
        if qid == 84:
            return ['ORDINAL']
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
        elif qid == 85:
            dataframes = [np.array(['ADP', 'PROPN', 'PUNCT', 'SPACE', 'PRON', 'NOUN', 'AUX', 'VERB', 'DET', 'SCONJ', 'ADV', 'ADJ', 'PART', 'NUM', 'CCONJ', 'SYM', 'X'], dtype = object), 'NOUN']
        elif qid == 86:
            return [np.array(['ADP', 'PROPN', 'PUNCT', 'SPACE', 'PRON', 'NOUN', 'AUX', 'VERB', 'DET', 'SCONJ', 'ADV', 'ADJ', 'PART', 'NUM', 'CCONJ', 'SYM', 'X'], dtype = object)]
        elif qid == 87:
            return ['NOUN']
        elif qid == 89:
            dataframes = [[' An attorney admits that the record was tendered late due to a mistake on his part . We find that such error, admittedly made by a criminal defendant, is good cause to grant motion .',
  ' Keith Melvin Dubray, by his attorney, has filed a motion for a rule on the clerk . His attorney admitted it was his fault that the record was not timely tendered .',
  ' Per Curiam. reviewed the record tendered late due to a mistake on his part .',
  ' The transcript of the case was not timely filed and it was no fault of the appellant . We find that such an error, admittedly made by the attorneys for a criminal defendant, is good cause to grant the motion .',
  ' Curtis and Billy Howard, brothers, were charged with and convicted of aggravated robbery and theft of property . Curtis, as an habitual offender, was sentenced to consecutive terms of life and 30 years . Billy Howard was convicted of concurrent terms of 10',
  ' Appellant, Michael Daniel Herrington, by his attorney, has filed for a rule on the clerk . His attorney, Bruce D. Switzer, admits that the record was tendered late due to a mistake on his part .',
  ' The transcript of the case was not timely filed and it was no fault of the appellant . The appellant’s former attorney, Ralph Lowe, admitted by affidavit attached to the motion that the transcript was filed late due to a mistake on',
  ' The transcript of the case was not timely filed and it was no fault of the appellant . His attorney admits that the transcript was filed late due to a mistake on his part .',
  ' An attorney admits that the trial court’s order granting an extension of time was not timely filed and it was no fault of the appellant . We find that such an error, admittedly made by the attorney for a criminal defendant, is',
  ' Petitioner pleaded guilty to aggravated robbery, in the Circuit Court of Randolph County . He was sentenced as an habitual offender to 20 years imprisonment . Petitioner subsequently filed numerous pro se petitions in circuit court, all of which raised grounds for post']]
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


