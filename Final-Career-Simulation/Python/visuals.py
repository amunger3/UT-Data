# local imports
from load_data import DataProcessor
import seaborn as sns

# Apply seaborn theme
sns.set_theme()

dp = DataProcessor()

patient_df = dp.df_dict['patient_df']
print(patient_df)



