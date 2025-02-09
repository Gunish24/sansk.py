import pandas as pd

# CSV file ka path yahaan daalein
file_path='D:/Ncsvw folder/calori.csv'
brute_force_path ='D:/Ncsvw folder/brute_force.csv'
googlesreach_path='D:/Ncsvw folder/googlesreach.csv'
GOLD_path='D:/Ncsvw folder/googlesreach.csv'
Book1_path='D:/Ncsvw folder/googlesreach.csv'

# CSV files ko pandas dataframe me read karein
df_calori=pd.read_csv(file_path)
df_brute_force=pd.read_csv(brute_force_path)
df_googlesreach=pd.read_csv(googlesreach_path)
df_GOLD=pd.read_csv(GOLD_path)

# Data ko print karein
print("\nCalori Dataframe:")
print(df_calori)

print("\nBrute Force Dataframe:")
print(df_brute_force)

print("\ngooglesreach Dataframe:")
print(df_googlesreach)

print("\nGOLD  dataframe:")
print(df_GOLD)
