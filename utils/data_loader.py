import pandas as pd

def load_market_data():
    data = {
        "Year": [2019, 2020, 2021, 2022, 2023, 2024],
        "DataCenterGrowth_MX_%": [8, 10, 14, 18, 22, 25],
        "CloudInvestment_BillionUSD": [1.2, 1.6, 2.1, 2.8, 3.6, 4.5],
        "EnergyConsumption_TWh": [3.5, 3.8, 4.2, 4.8, 5.3, 6.0]
    }
    return pd.DataFrame(data)