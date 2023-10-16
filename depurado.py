import pandas as pd

def verify_string(string):
    new_str = string.lower()
    for char in new_str:
        try:
            if char not in valid_chars:
                return string.replace(char,'') 
        except Exception as e:
               print("Error en el depurado de caracteres: ", str(e))
               return None
    return string

def data_depuration(df):
    for columnName in df:
        if (df[columnName].dtype == object):
            df[columnName] = df[columnName].apply(verify_string)
    return

def get_max_value(group, value):
    max_value_group = merged_data.groupby(group)[value].sum().idxmax()
    max_value = merged_data.groupby(group)[value].sum().max()
    return (max_value_group, max_value)

def get_min_value(group, value):
    min_value_group = merged_data.groupby(group)[value].sum().idxmin()
    min_value = merged_data.groupby(group)[value].sum().min()
    return (min_value_group, min_value)

valid_chars = "abcdefghijklmnopqrstuvwxyz ."

df = pd.read_csv('media_source.csv')
df2 = pd.read_csv('mmp.csv')

merged_data = pd.merge(df, df2, on=["date", "app_id", "campaign_id", "campaign_name", "creative_name", "country"])

merged_data["CPI"] = merged_data["spend_x"] / merged_data["installs"]
merged_data["CPC"] = merged_data["spend_y"] / merged_data["clicks"]

data_depuration(df)
data_depuration(df2)

print(merged_data)

print("El pais con mas gasto es %s, con un gasto de %s" % get_max_value("country","spend_x"))
print("La campaña con mejor performance es %s, con un CPI de %s" % get_min_value("campaign_name","CPI"))
print("La campaña con más installs es %s, con %s installs" % get_max_value("campaign_name","installs"))
print("El día con más installs es %s, con %s installs" % get_max_value("date","installs"))