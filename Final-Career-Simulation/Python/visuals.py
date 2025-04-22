# local imports
from load_data import DataProcessor
import seaborn as sns
import matplotlib.pyplot as plt

# Apply seaborn theme
sns.set_theme()

dp = DataProcessor()

patient_df = dp.df_dict['patient_df']
fact_df = dp.df_dict['fact_df']

# Histogram of age
def age_hist():
    sns.histplot(patient_df['PatientAge'], bins=20, kde=True)
    plt.title('Distribution of Age in Healthcare Data')
    plt.xlabel('Age')
    plt.ylabel('Patients')
    plt.show()
    # plt.savefig('Visuals/age-distribution.png')

# Boxplot of age by gender
def age_box():
    sns.boxplot(x='PatientGender', y='PatientAge', data=patient_df)
    plt.title('Age Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Age')
    plt.show()
    # plt.savefig('Visuals/age-boxplot.png')

# Bar chart of charge by payer (still shows payer code and not category)
def charge_by_payer():
    sns.barplot(fact_df, x='dimPayerPK', y='GrossCharge')
    plt.title('Gross Charge By Payer')
    plt.xlabel('Payer')
    plt.ylabel('Gross Charge ($1,000s)')
    plt.show()
    # Shows payer category as a table, simple, if not elegant workaround
    print(dp.df_dict['payer_df'])
    # plt.savefig('Visuals/charge-by-payer.png')


# Exeucte visual functions
if __name__ == '__main__':
    print('Script executed')
    age_hist()
    age_box()
    charge_by_payer()


