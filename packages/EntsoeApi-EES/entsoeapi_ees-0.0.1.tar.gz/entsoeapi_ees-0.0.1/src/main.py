from EntsoeApi_EES.EntsoeApi import EntsoeApi
from EntsoeApi_EES.EntsoeApi import BiddingZones
from datetime import datetime

def main():
    api = EntsoeApi("db0dabb3-0a32-45c8-a7cb-ff284b2001ca")
    start_date_data = datetime(2024,6,5,0,0,0)
    end_date_data = datetime(2024,6,6,0,0,0)
    dataframe_day_ahead_prices = api.get_day_ahead_prices_for_zone(BiddingZones.Netherlands, start_date_data, end_date_data )
    dataframe_day_ahead_prices.to_csv('out.csv', index=False)

if __name__ == "__main__":
    exit(main())