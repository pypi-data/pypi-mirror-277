from chembl_webresource_client.new_client import new_client
from functools import lru_cache, wraps
import pandas as pd
import requests
import time

# DECORADORES #
def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapper

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('\n'f'Runtime {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper
#             #
class Chembl:
    '''
    Busca as Smiles das ids do Chembl
    (Search for Smiles from Chembl IDs) '''
 
    @cache_decorator
    @timing_decorator
    def read_text_file(self, filename): 

        with open(filename, 'r') as file:
            data = file.read()
        values = data.replace('\n', ' ').split()

        return values

    def extract_canonical_smiles(self, structures):
        return structures['canonical_smiles']
 
    @timing_decorator
    def smiles_chembl(self, df, output_file): 

        print('\nLooking for Smiles for Chembl IDs...')

        values = df['ID_Molecula'].tolist()
        smiles = pd.DataFrame(new_client.molecule.filter(molecule_chembl_id__in=values).only(['molecule_chembl_id', 'molecule_structures']))

        smiles['SMILES'] = smiles['molecule_structures'].apply(self.extract_canonical_smiles)

        smiles = smiles.rename(columns={'molecule_chembl_id': 'ID_Molecula'}).drop(['molecule_structures'], axis=1)
        final = pd.merge(df, smiles, on='ID_Molecula', how='left')
    
        print('Search Completed')
        return final.to_csv(output_file, index=False, sep=";")

class Mcule:
    '''
    Busca as Smiles das ids do MCULE
    (Search for Smiles from MCULE IDs) '''

    def __init__(self):
        pass
    
    @cache_decorator
    @timing_decorator
    def ler_txt_mcule(self, nome_arquivo):

        with open(nome_arquivo, 'r') as file:
            data = file.read()
        values = list(set(data.splitlines()))
        values = [x for x in values if x.strip()]

        return values

    @cache_decorator
    def buscar_smiles(self, id_molecula):
        url = f'https://mcule.com/api/v1/search/lookup/?query={id_molecula}'
        r = requests.get(url)
        r.raise_for_status()  # Levanta um erro para requisições que falham
        response = r.json()
        dados = pd.DataFrame(response['results'])
        if dados.empty:
            return None
        return dados[['mcule_id', 'smiles']]

    @timing_decorator
    def smiles_mcule(self, df: pd.DataFrame, saida: str):

        print('\nLooking for Smiles for MCULE IDs...')
        valores = df['ID_Molecula'].tolist()
        resultados_errados = []
        final_data = pd.DataFrame()

        for item in valores:
            resultado = self.buscar_smiles(item)
            if resultado is not None:
                final_data = pd.concat([final_data, resultado], ignore_index=True)
            else:
                resultados_errados.append(item)

        smiles = final_data.rename(columns={'mcule_id': 'ID_Molecula', 'smiles': 'SMILES'})
        final = pd.merge(df, smiles, on='ID_Molecula', how='left')

        if resultados_errados:
            print(f'{len(resultados_errados)} Molecule(s) not found')

        final = final.drop_duplicates()
        final.to_csv(saida, index=False, sep=';')
        print('Search Completed')

class PubChem:
    '''
    Busca as Smiles das ids do PubChem
    (Search for Smiles from PubChem IDs)'''
    
    @cache_decorator
    @timing_decorator
    def ler_txt_pub(self, input):

        with open(input, 'r') as file:
            data = file.read()
        values = str(data.split("\n")).replace("'", '').replace(' ', '')
        translation_table = values.maketrans('', 'PubChem', '[]''' )
        filtered_values = values.translate(translation_table)

        return filtered_values

    def values_dataframe(self, df: pd.DataFrame) -> str:

        df['CID'] = df['ID_Molecula'].str.extract(r'(\d+)')
        formatted_string = ','.join(df['CID'])

        return formatted_string

    @timing_decorator
    def smiles_pubchem(self, df, saida: str):

        print('\nLooking for Smiles for PubChem IDs...')
        
        df['CID'] = df['ID_Molecula'].str.extract(r'(\d+)')
        values = self.values_dataframe(df)
        cids = values.split(',')

        chunk_size = 100
        smiles_list = []

        for i in range(0, len(cids), chunk_size):
            chunk = cids[i:i + chunk_size]
            values_chunk = ','.join(chunk)
            url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{values_chunk}/property/CanonicalSMILES/JSON'

            r = requests.get(url)
            if r.status_code != 200:
                print(f"Error Establishing Connection, Code: {r.status_code}")
                continue
            data = r.json()

            properties = data.get('PropertyTable', {}).get('Properties', [])
            
            smiles_list.extend(properties)

        if not smiles_list:
            print("Nenhum dado SMILES foi recuperado.")
            return

        smiles = pd.DataFrame(smiles_list).drop_duplicates(subset="CID")

        df['CID'] = df['CID'].astype(str)
        smiles['CID'] = smiles['CID'].astype(str)

        final = pd.merge(df, smiles, on='CID', how='left')
        final = final.drop(['CID'], axis=1)

        final.to_csv(saida, index=False, sep=';')

        print('Search Completed')
        return final

class Molport:
    '''
    Busca as Smiles das ids do Molport
    (Search for Smiles from Molport IDs) '''

    def __init__(self, key: str) -> None:
        self.key = key
    
    @cache_decorator
    @timing_decorator
    def ler_txt_mol(self, input):

        with open(input, 'r') as file:
            data = file.read()
        values = list(set(data.split("\n")))

        return values
    
    def extrair_smile(self, data):

        data = dict(data)
        smiles = data['Data']['Molecule']['SMILES']
        return str(smiles)

    def verificar_key(self):
        url = f'https://api.molport.com/api/molecule/load?molecule=TEST&apikey={self.key}'
        r = requests.get(url)
        if r.status_code == 200:
            response_data = r.json()
            if response_data.get('Result', {}).get('Message') == 'User is not recognized or allowed request count exceeded!':
                return False
            return True
        return False

    @timing_decorator
    def smiles_molport(self, df, saida):

        print('\nLooking for Smiles for Molport IDs...')

        values = list(df['ID_Molecula'])
        smiles = pd.DataFrame()
        ids_not_found= []

        for valor in values:
            url =f'https://api.molport.com/api/molecule/load?molecule={valor}&apikey={self.key}'
            r = requests.get(url)
            if r.status_code == 200:
                r = r.json()
                smile = self.extrair_smile(r)
                data = pd.DataFrame({'ID_Molecula': valor ,'SMILES': [smile]})

                smiles = pd.concat([smiles, data], axis=0, ignore_index=True)
            else:
                ids_not_found.append(valor)
        
        final = pd.merge(df, smiles, on='ID_Molecula', how='left')

        if len(ids_not_found) > 0:
            print(f'\nEssas ids não foram encontradas: {ids_not_found}')

        print('Search Completed')
        return final.to_csv(saida, index = False, sep =';')

class Processing:

    '''
    Separa as ids e afinidades do arquivo de saída do pharmit 
    (Separates the ids and affinities from the pharmit output file) '''

    def __init__(self, input = None):
        self.input = input

    def extrair_ids_afinidades_df(self, input, db):
        ids_affinity = []
        mol_id = None
        affinity = None
        id = None
        with open(input, 'r') as arquivo:
            linhas = arquivo.readlines()
        print('\nSeparating IDS and Affinities...')

        for i in range(len(linhas)):
            # Procurar por linhas que começam com "<minimizedAffinity>"
            if db in linhas[i]:
                mol_id = linhas[i].split(" ")
                id = [x for x in mol_id if db in x]
        
            elif 'minimizedAffinity' in linhas[i] :
                affinity = float(linhas[i+1])

            # Se ambos ID e afinidade foram encontrados, adicione à lista e resete as variáveis
            if id is not None and affinity is not None:
                if affinity <= -7.00:
                    if len(id) > 1:
                        for j in id:
                            j = j.replace('\n', '')
                            ids_affinity.append((j , affinity))
                    else:
                        ids_affinity.append((id[0].replace('\n', ''), affinity))

                mol_id = None
                affinity = None

        # Criar DataFrame com as IDs e afinidades
        df = pd.DataFrame(ids_affinity, columns=['ID_Molecula', 'Afinidade']).drop_duplicates(subset="ID_Molecula")

        print('Separation Completed')
        return df
    
    def to_save(self, df, output):
        ''' 
        Caso necessário salva o arquivo
        (If necessary, it saves the file) '''

        df = df.to_csv(output, index=False, sep=";")
        return df

class AdmetSpreadsheetAnalysis:
    '''   Faz a analise da planilha do AdmetLab 3.0   '''

    def __init__(self, input, output, weights=None):
        self.input = input
        self.output = output
        self.df = None
        self.df_analysis = None
        self.new_cols_to_move = ['SCORE', 'ABSORTION', 'DISTRIBUTION', 'TOXICITY', 'TOX21_PATHWAY', 'METABOLISM', 'TOXICOPHORE_RULES', 'EXCRETION', 'MEDICINAL_CHEMISTRY']
        self.required_columns = ['smiles', 'MW', 'Vol', 'Dense', 'nHA', 'nHD', 'TPSA', 'nRot', 'nRing', 'MaxRing','nHet', 'fChar', 'nRig', 'Flex', 'nStereo', 'gasa', 'QED', 'Synth', 'Fsp3', 'MCE-18', 'Natural Product-likeness', 'Alarm_NMR', 'BMS', 'Chelating', 'PAINS', 'Lipinski', 'Pfizer', 'GSK', 'GoldenTriangle', 'logS', 'logD', 'logP', 'mp', 'bp', 'pka_acidic', 'pka_basic', 'caco2', 'MDCK', 'PAMPA', 'pgp_inh', 'pgp_sub', 'hia', 'f20', 'f30', 'f50', 'OATP1B1', 'OATP1B3', 'BCRP', 'BSEP', 'BBB', 'MRP1', 'PPB', 'logVDss', 'Fu', 'CYP1A2-inh', 'CYP1A2-sub', 'CYP2C19-inh', 'CYP2C19-sub', 'CYP2C9-inh', 'CYP2C9-sub', 'CYP2D6-inh', 'CYP2D6-sub', 'CYP3A4-inh', 'CYP3A4-sub', 'CYP2B6-inh', 'CYP2B6-sub', 'CYP2C8-inh', 'LM-human', 'cl-plasma', 't0.5', 'BCF', 'IGC50', 'LC50DM', 'LC50FM', 'hERG', 'hERG-10um', 'DILI', 'Ames', 'ROA', 'FDAMDD', 'SkinSen', 'Carcinogenicity', 'EC', 'EI', 'Respiratory', 'H-HT', 'Neurotoxicity-DI', 'Ototoxicity', 'Hematotoxicity', 'Nephrotoxicity-DI', 'Genotoxicity', 'RPMI-8226', 'A549', 'HEK293', 'NR-AhR', 'NR-AR', 'NR-AR-LBD', 'NR-Aromatase', 'NR-ER', 'NR-ER-LBD', 'NR-PPAR-gamma', 'SR-ARE', 'SR-ATAD5', 'SR-HSE', 'SR-MMP', 'SR-p53', 'NonBiodegradable', 'NonGenotoxic_Carcinogenicity', 'SureChEMBL', 'LD50_oral', 'Skin_Sensitization', 'Acute_Aquatic_Toxicity', 'Toxicophores', 'Genotoxic_Carcinogenicity_Mutagenicity', 'Aggregators', 'Fluc', 'Blue_fluorescence', 'Green_fluorescence','Reactive', 'Other_assay_interference', 'Promiscuous']
        self.pesos = weights if weights is not None else {
            "ABSORTION": 2,
            "DISTRIBUTION": 1,
            "TOXICITY": 8,
            "TOX21_PATHWAY": 3,
            "METABOLISM": 2,
            "TOXICOPHORE_RULES": 3,
            "EXCRETION": 1,
            "MEDICINAL_CHEMISTRY": 5
        }

    def verify_format(self):
    # Carregar a planilha
        df = pd.read_csv(self.input)
        
        # Verificar se todas as colunas obrigatórias estão presentes
        missing_columns = [col for col in self.required_columns if col not in df.columns]
        
        if missing_columns:
            raise KeyError ('Spreadsheet is not formatted for analysis')
        else:
            print('\nAnalyzing Spreadsheet...')

    def load_data(self, input):
        self.df = pd.read_csv(input)
        self.df = self.df.rename(columns={
            'cl-plasma': 'cl_plasma',
            't0.5': 't_0_5',
            'MCE-18': 'MCE_18',
        })

    def replace_interval(self, valor, intervals, values):
        for interval, valor_substituido in zip(intervals, values):
            if interval[0] <= valor <= interval[1]:
                return valor_substituido
        return valor

    def replace_values(self, df, columns, intervals, values):
        replace = lambda x: self.replace_interval(pd.to_numeric(x, errors='coerce'), intervals, values)
        for col in columns:
            df[col] = df[col].apply(replace)
        return df

    def substituir_string(self, valor, string, valor1, valor2):
        return valor1 if valor == string else valor2

    def process_data(self):

        self.verify_format()
        self.load_data(self.input)

        out_of_analysis = ['BCF', 'bp', 'Dense', 'fChar', 'Flex', 'IGC50', 'LC50DM', 'LC50FM', 'LD50_oral', 'logD', 'logP', 'logS', 'logVDss', 'MaxRing', 'MDCK', 'mp', 'MW', 'Natural Product-likeness', 'nHA', 'nHD', 'nHet', 'nRig', 'nRing', 'nRot', 'nStereo', 'Other_assay_interference', 'pka_acidic', 'pka_basic', 'Toxicophores', 'TPSA', 'Vol']
        absorption_columns = ['PAMPA', 'pgp_inh', 'pgp_sub', 'hia', 'f20', 'f30', 'f50']
        distribution_columns = ['OATP1B1', 'OATP1B3', 'BCRP', 'BSEP', 'BBB', 'MRP1']
        toxicity_columns = ['hERG', 'hERG-10um', 'DILI', 'Ames', 'ROA', 'FDAMDD', 'SkinSen', 'Carcinogenicity', 'EC', 'EI', 'Respiratory', 'H-HT', 'Neurotoxicity-DI', 'Ototoxicity', 'Hematotoxicity', 'Nephrotoxicity-DI', 'Genotoxicity', 'RPMI-8226', 'A549', 'HEK293']
        tox21_columns = ['NR-AhR', 'NR-AR', 'NR-AR-LBD', 'NR-Aromatase', 'NR-ER', 'NR-ER-LBD', 'NR-PPAR-gamma', 'SR-ARE', 'SR-ATAD5', 'SR-HSE', 'SR-MMP', 'SR-p53']
        metabolism_columns = ['CYP1A2-inh', 'CYP1A2-sub', 'CYP2C19-inh', 'CYP2C19-sub', 'CYP2C9-inh', 'CYP2C9-sub', 'CYP2D6-inh', 'CYP2D6-sub', 'CYP3A4-inh', 'CYP3A4-sub', 'CYP2B6-inh', 'CYP2B6-sub', 'CYP2C8-inh', 'LM-human']
        toxicophore_columns = ['NonBiodegradable', 'NonGenotoxic_Carcinogenicity', 'SureChEMBL', 'Skin_Sensitization', 'Acute_Aquatic_Toxicity', 'Genotoxic_Carcinogenicity_Mutagenicity']
        medicinal_chemistry_columns_str = ['Alarm_NMR', 'BMS', 'Chelating', 'PAINS']
        medicinal_chemistry_columns_float_divergent = ['gasa', 'QED', 'Synth', 'Fsp3', 'MCE_18', 'Lipinski', 'Pfizer', 'GSK', 'GoldenTriangle']
        medicinal_chemistry_columns_float_similar = ['Aggregators', 'Fluc', 'Blue_fluorescence', 'Green_fluorescence', 'Reactive', 'Promiscuous']
        medicinal_chemistry = medicinal_chemistry_columns_str + medicinal_chemistry_columns_float_divergent + medicinal_chemistry_columns_float_similar

        self.df = self.replace_values(self.df, absorption_columns, [(0, 0.3), (0.3, 0.7), (0.7, 1.0)], [1.25, 0.62, 0.0])
        self.df = self.replace_values(self.df, distribution_columns, [(0, 0.3), (0.3, 0.7), (0.7, 1.0)], [1.25, 0.62, 0.0])
        self.df = self.replace_values(self.df, toxicity_columns, [(0, 0.3), (0.3, 0.7), (0.7, 1.0)], [0.5, 0.25, 0.0])
        self.df = self.replace_values(self.df, tox21_columns, [(0, 0.3), (0.3, 0.7), (0.7, 1.0)], [0.83, 0.41, 0.0])
        self.df = self.replace_values(self.df, metabolism_columns, [(0, 0.3), (0.3, 0.7), (0.7, 1.0)], [0.71, 0.35, 0.0])

        for col in toxicophore_columns:
            self.df[col] = self.df[col].apply(self.substituir_string, args=("['-']", 1.6, 0))

        for col in medicinal_chemistry_columns_str:
            self.df[col] = self.df[col].apply(self.substituir_string, args=("['-']", 0.5, 0))

        self.df = (
            self.df.assign(
                caco2=pd.to_numeric(self.df['caco2'], errors='coerce').apply(lambda x: 1.25 if x > -5.15 else 0),
                PPB=pd.to_numeric(self.df['PPB'], errors='coerce').apply(lambda x: 1.25 if x <= 90 else 0),
                Fu=pd.to_numeric(self.df['Fu'], errors='coerce').apply(lambda x: 1.25 if x >= 5 else 0),
                cl_plasma=pd.to_numeric(self.df['cl_plasma'], errors='coerce').apply(lambda x: 5 if 0 <= x <= 5 else (2.5 if 5 < x <= 15 else 0)),
                t_0_5=pd.to_numeric(self.df['t_0_5'], errors='coerce').apply(lambda x: 5 if x > 8 else (2.5 if 1 <= x <= 8 else 0)),
                Lipinski=pd.to_numeric(self.df['Lipinski'], errors='coerce').apply(lambda x: 0.5 if x < 2 else 0),
                Pfizer=pd.to_numeric(self.df['Pfizer'], errors='coerce').apply(lambda x: 1 if x < 2 else 0),
                GSK=pd.to_numeric(self.df['GSK'], errors='coerce').apply(lambda x: 0.5 if x == 0 else 0),
                GoldenTriangle=pd.to_numeric(self.df['GoldenTriangle'], errors='coerce').apply(lambda x: 0.5 if x == 0 else 0),
                gasa=pd.to_numeric(self.df['gasa'], errors='coerce').apply(lambda x: 0.5 if x == 1 else 0),
                QED=pd.to_numeric(self.df['QED'], errors='coerce').apply(lambda x: 0.5 if x > 670 else 0),
                Synth=pd.to_numeric(self.df['Synth'], errors='coerce').apply(lambda x: 0.5 if x <= 6.000 else 0),
                Fsp3=pd.to_numeric(self.df['Fsp3'], errors='coerce').apply(lambda x: 0.5 if x >= 420 else 0),
                MCE_18=pd.to_numeric(self.df['MCE_18'], errors='coerce').apply(lambda x: 0.5 if x >= 45.000 else 0)
            )
        )

        for col in medicinal_chemistry_columns_float_similar:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce').apply(lambda x: 0.5 if x < 1.000 else 0)

        new_cols = pd.DataFrame({
            'ABSORTION': self.df[absorption_columns + ['caco2']].sum(axis=1, skipna=True),
            'DISTRIBUTION': self.df[['PPB', 'Fu'] + distribution_columns].sum(axis=1, skipna=True),
            'TOXICITY': self.df[toxicity_columns].sum(axis=1, skipna=True),
            'TOX21_PATHWAY': self.df[tox21_columns].sum(axis=1, skipna=True),
            'METABOLISM': self.df[metabolism_columns].sum(axis=1, skipna=True),
            'TOXICOPHORE_RULES': self.df[toxicophore_columns].sum(axis=1, skipna=True),
            'EXCRETION': self.df[['cl_plasma', 't_0_5']].sum(axis=1, skipna=True),
            'MEDICINAL_CHEMISTRY': self.df[medicinal_chemistry].sum(axis=1, skipna=True)
        })

        self.df_analysis = pd.concat([self.df, new_cols], axis=1)
        self.df_analysis = self.df_analysis.drop(columns=out_of_analysis)

        self.df_analysis['SCORE'] = (self.df_analysis['ABSORTION'] * self.pesos['ABSORTION'] +
                                     self.df_analysis['DISTRIBUTION'] * self.pesos['DISTRIBUTION'] +
                                     self.df_analysis['TOXICITY'] * self.pesos['TOXICITY'] +
                                     self.df_analysis['TOX21_PATHWAY'] * self.pesos['TOX21_PATHWAY'] +
                                     self.df_analysis['METABOLISM'] * self.pesos['METABOLISM'] +
                                     self.df_analysis['TOXICOPHORE_RULES'] * self.pesos['TOXICOPHORE_RULES'] +
                                     self.df_analysis['EXCRETION'] * self.pesos['EXCRETION'] +
                                     self.df_analysis['MEDICINAL_CHEMISTRY'] * self.pesos['MEDICINAL_CHEMISTRY']) / sum(self.pesos.values())
        
        df_results = pd.read_csv(self.input)

        analysis_df = pd.merge(df_results, self.df_analysis[['smiles'] + self.new_cols_to_move], on='smiles', how='left')

        all_cols = analysis_df.columns.tolist()
        smiles_index = all_cols.index('smiles')
        smiles_col = all_cols[smiles_index]

        remaining_cols = [col for col in all_cols if col not in self.new_cols_to_move and col != smiles_col]
        new_cols = [smiles_col] + self.new_cols_to_move + remaining_cols

        analysis_df = analysis_df[new_cols]
        analysis_df[self.new_cols_to_move] = analysis_df[self.new_cols_to_move].round(2)

        self.analysis_df = analysis_df

        print('Analysis created\n')

        return self.analysis_df.to_csv(self.output, index=False)
