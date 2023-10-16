import pandas as pd

valid_chars = "abcdefghijklmnopqrstuvwxyz ."

def verify_string(string):
    # This function will receive every value from a cell which is a string and delete not wanted characters
    # It will return text strings whose characters are valid
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
    # This function will iterate the Dataframe and will check every value that is a string
    for columnName in df:
        if (df[columnName].dtype == object):
            df[columnName] = df[columnName].apply(verify_string)
    return

def get_max_value(group, value):
    # This function will receive a group and the value from which you want to obtain the maximum.
    # It will return the element from the group with the highest value, and that value.
    max_value_group = merged_df.groupby(group)[value].sum().idxmax()
    max_value = merged_df.groupby(group)[value].sum().max()
    return (max_value_group, max_value)

def get_min_value(group, value):
    # This function will receive a group and the value from which you want to obtain the minimum.
    # It will return the element from the group with the lowest value, and that value.
    min_value_group = merged_df.groupby(group)[value].sum().idxmin()
    min_value = merged_df.groupby(group)[value].sum().min()
    return (min_value_group, min_value)

df = pd.read_csv('media_source.csv')
df2 = pd.read_csv('mmp.csv')


# ------ Mergeo ---------
merged_df = pd.merge(df, df2, on=["date", "app_id", "campaign_id", "campaign_name", "creative_name", "country"])


# ------ Creacion de variables -------
merged_df["CPI"] = merged_df["spend_x"] / merged_df["installs"]
merged_df["CPC"] = merged_df["spend_y"] / merged_df["clicks"]

# ------ Depuracion de los dataframes ---------
data_depuration(df)
data_depuration(df2)

print(merged_df)

# ------- Respuestas -------
print("El pais con mas gasto es %s, con un gasto de %s" % get_max_value("country","spend_x"))
print("La campania con mejor performance es %s, con un CPI de %s" % get_min_value("campaign_name","CPI"))
print("La campania con mas installs es %s, con %s installs" % get_max_value("campaign_name","installs"))
print("El dia con mas installs es %s, con %s installs" % get_max_value("date","installs"))