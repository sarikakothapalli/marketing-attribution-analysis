import pandas as pd

df = pd.read_csv("digital_marketing_campaign_dataset.csv")
print(df.head())
print(df.columns)

df = pd.read_csv("digital_marketing_campaign_dataset.csv")
df['Conversion'] = (df['ConversionRate'] > 0.1).astype(int)

import numpy as np

channels = df['CampaignChannel'].unique()

expanded_rows = []

for _, row in df.iterrows():
    num_touches = np.random.randint(2, 5)  # 2–4 touchpoints
    
    for i in range(num_touches):
        expanded_rows.append({
            'CustomerID': row['CustomerID'],
            'Channel': np.random.choice(channels),
            'TouchDate': pd.Timestamp('2024-01-01') + pd.Timedelta(days=i),
            'Conversion': 0
        })
    
    # last touch = conversion
    expanded_rows[-1]['Conversion'] = row['Conversion']

journey_df = pd.DataFrame(expanded_rows)

#attribution Models

#first touch
first_touch = journey_df.sort_values('TouchDate').groupby('CustomerID').first()
first_result = first_touch['Channel'].value_counts()

#last touch
last_touch = journey_df.sort_values('TouchDate').groupby('CustomerID').last()
last_result = last_touch['Channel'].value_counts()

#multi-touch
journey_df['credit'] = 1 / journey_df.groupby('CustomerID')['Channel'].transform('count')
multi_result = journey_df.groupby('Channel')['credit'].sum()

result = pd.DataFrame({
    'First Touch': first_result,
    'Last Touch': last_result,
    'Multi Touch': multi_result
}).fillna(0)

print(result)

result['Bias'] = result['Last Touch'] - result['First Touch']
print(result)

result[['First Touch', 'Last Touch', 'Multi Touch']].plot(kind='bar')

result.to_csv("attribution_results.csv")