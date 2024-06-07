from EntsoeApi_EES.RestApiBase import RestApiBase
from datetime import datetime, timedelta
import pandas as pd
import xml.etree.ElementTree as ET
from EntsoeApi_EES.PriceValue import PriceValue
from typing import List
import re

class BiddingZones:
    Netherlands = "10YNL----------L"

class EntsoeApi(RestApiBase):

    resolution_to_timedelta_seconds_dict = {
        'PT60M' : 3600
    }

    def __init__(self, api_key : str):
        super().__init__("https://web-api.tp.entsoe.eu/api")
        self.api_key = api_key

    def get_day_ahead_prices_for_zone(self, bidding_zone : str, from_date : datetime, to_date : datetime) -> pd.DataFrame:
        query_params = {
            "securityToken" : self.api_key,
            "documentType": "A44",
            "in_Domain" : bidding_zone,
            "out_Domain" : bidding_zone,
            "periodStart" : from_date.strftime("%Y%m%d%H%M"), 
            "periodEnd" : to_date.strftime("%Y%m%d%H%M")
        }
        xml_string = self.get_request("", query_params).decode("utf-8")
        xml_string = re.sub('xmlns=".*"', "", xml_string)
        xml_tree_root = ET.fromstring(xml_string)
        data_points : List[PriceValue] = []
        for time_serie in xml_tree_root.findall('TimeSeries'):
            period = time_serie.find('Period')
            time_interval = period.find('timeInterval')
            period_start = datetime.strptime(time_interval.find('start').text, "%Y-%m-%dT%H:%MZ")
            resolution_delta = self.resolution_to_timedelta_seconds_dict[period.find('resolution').text]
            price_unit = time_serie.find('price_Measure_Unit.name').text

            for point in period.findall('Point'):
                position = int(point.find('position').text)
                price = float(point.find('price.amount').text)
                start_delta = timedelta(seconds=(position - 1) * resolution_delta)
                end_delta = timedelta(seconds=position * resolution_delta)
                value_date_start = period_start + start_delta 
                value_date_end = period_start + end_delta 
                data_points.append(PriceValue(value_date_start, value_date_end, price, price_unit))

        data_points = sorted(data_points, key=lambda price_value : price_value.date_start)

        data_frame_data = {
            'data_valid_start': [price_value.date_start for price_value in data_points], 
            'data_valid_end': [price_value.date_end for price_value in data_points], 
            'price' : [price_value.price for price_value in data_points],
            'price_unit' : [price_value.unit for price_value in data_points]
        }

        return pd.DataFrame(data=data_frame_data)



