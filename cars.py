
import pandas as pd  
import numpy as np 

df = pd.read_csv("Cars Datasets 2025.csv",encoding='latin')
df.head()

df.columns = df.columns.str.replace(r'\(0 - 100 \)', '', regex=True).str.replace(r'/', '_', regex=True).str.replace(' ', '_')
df.head()

dim_company = pd.DataFrame(df['Company_Names'].str.upper().str.strip().unique(), columns=['CompanyName'])
dim_company.head()

dim_company.isnull().sum()

dim_company.head()

dim_company['Company_SK'] = range(1, len(dim_company) + 1)
dim_company = dim_company[['Company_SK', 'CompanyName']]
dim_company.head()

print(len(dim_company))

dim_model = pd.DataFrame(df['Cars_Names'].str.strip().unique(), columns=['ModelName'])

dim_model.isnull().sum()

dim_model['Model_SK'] = range(1, len(dim_model) + 1)
dim_model = dim_model[['Model_SK', 'ModelName']]
dim_model.head()

dim_engine = df[['Engines', 'CC_Battery_Capacity']].copy()
dim_engine.head()

dim_engine.isnull().sum()

dim_engine.dropna(inplace=True)
dim_engine.head()

dim_engine.isnull().sum()

dim_engine = dim_engine.drop_duplicates()
dim_engine.head()

dim_engine['Engine_SK'] = range(1, len(dim_engine) + 1)
dim_engine.rename(columns={'Engines': 'Engine_Name', 'CC_Battery_Capacity': 'Engine_Capacity'}, inplace=True)
dim_engine = dim_engine[['Engine_SK', 'Engine_Name', 'Engine_Capacity']]
dim_engine.head()

dim_fuel_type = pd.DataFrame(df['Fuel_Types'].str.strip().unique(), columns=['FuelType'])
dim_fuel_type.dropna(inplace=True)
dim_fuel_type['FuelType_SK'] = range(1, len(dim_fuel_type) + 1)
dim_fuel_type = dim_fuel_type[['FuelType_SK', 'FuelType']]
dim_fuel_type.head()

def clean_and_average(series):
    numbers = series.astype(str).str.findall(r'\d+\.?\d*')
    return numbers.apply(lambda x: np.mean([float(n) for n in x]) if x else np.nan)

fact_car = df.copy()

fact_car['Price_USD'] = clean_and_average(fact_car['Cars_Prices'])

fact_car['Horsepower'] = clean_and_average(fact_car['HorsePower'])

fact_car['Torque_NM'] = clean_and_average(fact_car['Torque'])

fact_car['Top_Speed_KPH'] = clean_and_average(fact_car['Total_Speed'])
fact_car['Acceleration_Sec'] = clean_and_average(fact_car['PerformanceKM_H'])

fact_car['Seats'] = fact_car['Seats'].astype(str).str.extract(r'(\d+)').astype(float)

fact_car.head()

fact_car['CompanyName'] = fact_car['Company_Names'].str.upper().str.strip()
fact_car['ModelName'] = fact_car['Cars_Names'].str.strip()
fact_car['FuelType'] = fact_car['Fuel_Types'].str.strip()
fact_car.rename(columns={'Engines': 'Engine_Name', 'CC_Battery_Capacity': 'Engine_Capacity'}, inplace=True)
fact_car.head()

fact_car = fact_car.merge(dim_company, on='CompanyName')

fact_car = fact_car.merge(dim_model, on='ModelName')

fact_car = fact_car.merge(dim_engine, on=['Engine_Name', 'Engine_Capacity'])

fact_car = fact_car.merge(dim_fuel_type, on='FuelType')

fact_car['Car_SK'] = range(1, len(fact_car) + 1)

final_fact_columns = [
    'Car_SK',
    'Model_SK',
    'Company_SK',
    'Engine_SK',
    'FuelType_SK',
    'Price_USD',
    'Horsepower',
    'Torque_NM',
    'Top_Speed_KPH',
    'Acceleration_Sec',
    'Seats'
]
fact_car = fact_car[final_fact_columns]

fact_car.head()

fact_car.to_csv("Fact_Car.csv", index=False)
dim_company.to_csv("Dim_Company.csv", index=False)
dim_model.to_csv("Dim_Model.csv", index=False)
dim_engine.to_csv("Dim_Engine.csv", index=False)
dim_fuel_type.to_csv("Dim_FuelType.csv", index=False)