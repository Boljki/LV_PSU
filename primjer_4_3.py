import pandas as pd


df = pd.read_csv('cars_processed.csv')


n_rows = df.shape[0]
print("1. Broj automobila u datasetu:", n_rows)


print("\n2. Tipovi stupaca:")
print(df.dtypes)


idx_max_price = df['selling_price'].idxmax()
idx_min_price = df['selling_price'].idxmin()
print("\n3. Najskuplji automobil:", df.loc[idx_max_price, 'name'], "s cijenom", df.loc[idx_max_price, 'selling_price'])
print("   Najjeftiniji automobil:", df.loc[idx_min_price, 'name'], "s cijenom", df.loc[idx_min_price, 'selling_price'])

count_2012 = df[df['year'] == 2012].shape[0]
print("\n4. Broj automobila proizvedenih 2012.:", count_2012)


idx_max_km = df['km_driven'].idxmax()
idx_min_km = df['km_driven'].idxmin()
print("\n5. Automobil s najviše km:", df.loc[idx_max_km, 'name'], "s", df.loc[idx_max_km, 'km_driven'], "km")
print("   Automobil s najmanje km:", df.loc[idx_min_km, 'name'], "s", df.loc[idx_min_km, 'km_driven'], "km")

#sjedala
most_common_seats = df['seats'].mode()[0]
print("\n6. Najčešći broj sjedala:", most_common_seats)

avg_km_diesel = df[df['fuel']=='Diesel']['km_driven'].mean()
avg_km_petrol = df[df['fuel']=='Petrol']['km_driven'].mean()
print("\n7. Prosječna kilometraža:")
print("   Diesel:", round(avg_km_diesel,2))
print("   Petrol:", round(avg_km_petrol,2))