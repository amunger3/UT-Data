import pandas as pd

# CSV imports
# Returns dictionary of dataframes

def import_data():
    dict_df = pd.read_csv('../Data/DataDictionary.csv')
    cptcode_df = pd.read_csv('../Data/DimCptCode.csv')
    date_df = pd.read_csv('../Data/DimDate.csv')
    diagcode_df = pd.read_csv('../Data/DimDiagnosisCode.csv')
    location_df = pd.read_csv('../Data/DimLocation.csv')
    patient_df = pd.read_csv('../Data/Dimpatient.csv')
    payer_df = pd.read_csv('../Data/DimPayer.csv')
    physician_df = pd.read_csv('../Data/DimPhyscian.csv')
    transaction_df = pd.read_csv('../Data/DimTransaction.csv')
    fact_df = pd.read_csv('../Data/FactTable.csv')
    return {
        'dict_df': dict_df,
        'cptcode_df': cptcode_df,
        'date_df': date_df,
        'diagcode_df': diagcode_df,
        'location_df': location_df,
        'patient_df': patient_df,
        'payer_df': payer_df,
        'physician_df': physician_df,
        'transaction_df': transaction_df,
        'fact_df': fact_df,
    }


# Runs code
if __name__ == "__main__":
    print("Script executed directly")
    data_dict = import_data()
    print(data_dict['cptcode_df'])