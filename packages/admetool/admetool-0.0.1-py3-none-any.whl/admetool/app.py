from models import *
import argparse
import json
import os

def main():

    parser = argparse.ArgumentParser(
        prog='Admet_Analysis_Tool',
        description='Ferramenta que usa os dados do Pharmit para fazer uma analise ADMET'
    )

    parser.add_argument('-i', '--input',
                        type=str,
                        required=True,
                        help='Arquivo da triagem do Pharmit (.SDF) (Pharmit screening file (.SDF))')

    parser.add_argument('-db', '--database',
                        type=str,
                        choices=['CHEMBL', 'MCULE', 'MolPort', 'PubChem'],
                        help='Banco de Dados que está sendo feita a analise (CHEMBL, MCULE, MolPort, PubChem) (Database that is being analyzed (CHEMBL, MCULE, MolPort, PubChem))')

    parser.add_argument('-mk', '--molport_key',
                        type=str,
                        help='Chave de acesso para o banco de dados MolPort (Access key for MolPort database)')

    parser.add_argument('-o', '--output',
                        type=str,
                        required=True,
                        help='Caminho do arquivo de saída(.CSV) (output file path (.CSV))')

    parser.add_argument('-w', '--weights',
                        type=str,
                        help='Arquivo para mudar os pesos na analise da planilha do AdmetLab (.JSON) (File to change weights in the AdmetLab spreadsheet analysis (.JSON))')

    parser.add_argument('-a','--analyze_only',
                        action='store_true',
                        help='Apenas realizar a análise da planilha com dados do AdmetLab 3.0 (Just perform the spreadsheet analysis with data from AdmetLab 3.0)')

    parser.add_argument('-p','--processing_only',
                        action='store_true',
                        help='Apenas separar ids e afinidade (Requer a definição do Banco de dados) (Just separate ids and affinity (Requires database definition))'
                        )
    


    args = parser.parse_args()



    weights = None
    if args.weights:
        with open("test_files/pesos_diferentes.json", "r", encoding="utf-8") as f:
            weights = json.loads(f.read())

    chembl_instance = Chembl()
    mcule_instance = Mcule()
    molport_instance = Molport(args.molport_key)
    puchem_instance = PubChem()
    processing_instance = Processing()
    analysis_instance = AdmetSpreadsheetAnalysis(args.input, args.output, weights)

    if args.database == 'MolPort':
        if not args.molport_key:
            parser.error('--molport_key is required when database is MolPort')
        if not molport_instance.verificar_key():
            parser.error('Invalid Molport key.')

    if args.analyze_only:
        # Processa apenas a analise da planilha do AmetLab
        analysis_instance.process_data()

    elif args.processing_only:
        df = processing_instance.extrair_ids_afinidades_df(args.input, args.database)
        processing_instance.to_save(df, args.output)

    else:
        # Escolha do Banco de dados
        match args.database:
            case 'CHEMBL':
                df = processing_instance.extrair_ids_afinidades_df(args.input, args.database)
                chembl_instance.smiles_chembl(df, args.output)

            case 'MCULE':
                df = processing_instance.extrair_ids_afinidades_df(args.input, args.database)
                mcule_instance.smiles_mcule(df, args.output)

            case 'MolPort':
                df = processing_instance.extrair_ids_afinidades_df(args.input, args.database)
                molport_instance.smiles_molport(df, args.output)

            case 'PubChem':
                df = processing_instance.extrair_ids_afinidades_df(args.input, args.database)
                puchem_instance.smiles_pubchem(df, args.output)

    output_path = os.path.abspath(args.output)
    print(f' File Created in: {output_path}''\n')

if __name__ == "__main__":
    main()