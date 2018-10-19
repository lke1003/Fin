import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_data(url_list):
    df_list = []
    for url in url_list:
        df_list.append(pd.read_excel(url, sheet_name = 'Data'))
    return df_list

def get_long_df(wide_df_list):
    long_df_list = []
    source_var = ['Total population', 'GDP per capita', 'Life expectancy']
    renamed_var = ['pop', 'gdpPercap', 'lifeExp']
    for (i, old_var, new_var) in zip(range(3), source_var, renamed_var):
        df = pd.melt(wide_df_list[i], id_vars = [old_var])
        df.columns = ['country', 'year', new_var]
        long_df_list.append(df)
    return long_df_list

url_list = ['https://storage.googleapis.com/learn_pd_like_tidyverse/indicator_gapminder_population.xlsx', 'https://storage.googleapis.com/learn_pd_like_tidyverse/indicator_gapminder_gdp_per_capita_ppp.xlsx', 'https://storage.googleapis.com/learn_pd_like_tidyverse/indicator_life_expectancy_at_birth.xlsx']
wide_df_list = get_data(url_list)
long_df_list = get_long_df(wide_df_list)
print(long_df_list[0].head())
print(long_df_list[1].head())
print(long_df_list[2].head())

merged_df = pd.merge(long_df_list[0], long_df_list[1], on = ['country', 'year'])
merged_df = pd.merge(merged_df, long_df_list[2], on = ['country', 'year'])
merged_df = merged_df.dropna()
merged_df = merged_df.sort_values(['year', 'country'])
merged_df = merged_df.reset_index(drop = True)
print(merged_df.head())
merged_df.to_csv('gapminder.csv', index = False)