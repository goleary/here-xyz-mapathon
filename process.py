import numpy as np
import pandas as pd

# read using code headers
data = pd.read_csv('./data/metro/ACS_17_5YR_DP03_with_ann.csv',
                   encoding="ISO-8859-1", skiprows=[1], index_col=False)
# read using descriptive headers
# data = pd.read_csv('./data/metro/ACS_17_5YR_DP03_with_ann.csv',
#                 encoding="ISO-8859-1", header =1, index_col=2)
# print(df.head())
mapping = pd.read_csv('./data/column_mappings.csv',
                      converters={'keep': np.bool}, index_col=False)
filtered_fields = mapping[mapping.keep == True]

print('data')
print(data)

filtered_data = data[filtered_fields['code']]
filtered_data.columns = filtered_fields['new_name']
print(' data with filtered columns')
print(filtered_data)
# data_t[]


# #merge_df = pd.merge(data, mapping, on='id')
# print('transposed data')
# print(data.transpose().head())
#data_t = data.transpose().replace
# data= data.transpose().replace
# df_merge_difkey = pd.merge(
#     filtered_fields, data.transpose(),  left_on='code', right_index=True)
# print(df_merge_difkey.head())

# df.to_csv('./data/metro/processed_data.csv')
