import pandas as pd
from matplotlib import pyplot as plt
url = 'https://raw.githubusercontent.com/MajorLeagueBaseball/google-cloud-mlb-hackathon/main/datasets/2016-mlb-homeruns.csv'
# Corrected URL to point to the raw data for 2017
url2 = 'https://raw.githubusercontent.com/MajorLeagueBaseball/google-cloud-mlb-hackathon/main/datasets/2017-mlb-homeruns.csv'
# Corrected URL to point to the raw data for 2024
url3 = 'https://raw.githubusercontent.com/MajorLeagueBaseball/google-cloud-mlb-hackathon/main/datasets/2024-mlb-homeruns.csv'

df = pd.read_csv(url)
df.describe()
df2 = pd.read_csv(url2)
df.head(2)
df2.head(2)
df3 = pd.read_csv(url3)
df3.head(2)
df3.describe()

_df_30['HitDistance'].plot(kind='line', figsize=(8, 4), title='HitDistance')
plt.gca().spines[['top', 'right']].set_visible(False)
