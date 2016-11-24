import pandas as pd


df_loc = pd.read_csv("res_loc.csv")

df_loc = df_loc.loc[df_loc["idTypeBien"] != 6]
df_loc["surface gr"] = pd.cut(df_loc["surface"], [0, 35, 50, 80, 999999])

df_loc_gr = df_loc.groupby(["ville", "idTypeBien", "surface gr"])["prix"].mean()


df_achat = pd.read_csv("res_achat.csv")

df_achat = df_achat.loc[df_achat["idTypeBien"] != 6]
df_achat["surface gr"] = pd.cut(df_loc["surface"], [0, 35, 50, 80, 999999])

df_achat_gr = df_achat.groupby(["ville", "idTypeBien",  "surface gr"])["prix"].mean()

df_datas = pd.concat([df_loc_gr, df_achat_gr], axis=1)

df_datas.columns = ["prix loc", "prix achat"]

df_datas = df_datas.dropna()

df_datas["yield"] = df_datas["prix loc"] / df_datas["prix achat"] * 12


df_datas_final = pd.read_csv("results_top25.csv")

