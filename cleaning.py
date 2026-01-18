import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv('customer_shopping_behavior.csv')

df = pd.DataFrame(data)
# filling the null values in the Review Rating thorugh the median of the category from which the product belongs
df['Review Rating']  = (df.groupby('Category')['Review Rating'].transform(lambda x : x.fillna(x.median())))
# making the column names to snake case to make the readability easy
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df.columns = df.columns.str.replace('purchase_amount_(usd)','purchase_amount')
# feature Engineering
# 1.Age grouping 
ageLabels = ['young_adult','adult','middle_aged','senior']
# qcut divides the values into 4 grps and then label accordingly
df['age_grp'] = pd.qcut(df['age'],q=4,labels=ageLabels)
# 2.ReviewRating_grp
bins = [0, 3, 3.5, 4, 4.5, 5]
ratingLabels =['1 Star (Very Poor)','2 Stars (Poor)','3 Stars (Average)','4 Stars (Good)','5 Stars (Excellent)']
df['rating_label']=pd.cut(df['review_rating'],bins = bins,labels = ratingLabels)
# 3. purchase frequency days
frequency_mapings = {
    'Fortnightly':14,
    'Weekly':7,
    'Monthly':30,
    'Quarterly':90,
    'Bi-Weekly':14,
    'Annually':365,
    'Every 3 Months':90
}
df['purchase_frequency_level'] = df['frequency_of_purchases'].map(frequency_mapings)
# droping this columns cause discount applied column and promo code used are the same because if promocode apllied
# then there would be discount appplied and both columns are the same 
df=df.drop('promo_code_used',axis=1)

print(df.columns)
print(df.info())
print(df.head())
print(df.describe())



# 1. Create the connection string
# Format: 'dialect+driver://username:password@host:port/database'
engine = create_engine('postgresql://postgres:1234@localhost:5432/customer_behaviourDB')

# 2. Dump the dataframe directly
# This creates 'raw_shopping_data' table automatically!
df.to_csv('cleaned_data.csv', index=False)

print("Data dumped successfully, bro!")