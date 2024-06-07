
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '\\..\\src')

import unittest
from unittest.mock import MagicMock
from EntsoeApi_EES.EntsoeApi import EntsoeApi
from EntsoeApi_EES.EntsoeApi import BiddingZones
from datetime import datetime, timedelta

class TestEntsoeApi(unittest.TestCase):

    def setUp(self):
        with open("./testresponse.xml", "r") as f:
            self.response_str = f.read().encode("utf-8")

    def test_da_ahead_response_is_parsed_correctly(self):
        # Arrange
        api = EntsoeApi(api_key="test")
        api.get_request = MagicMock(return_value=self.response_str)
        ptu_time_delta = timedelta(seconds=3600)
        start_date_data = datetime(2024,1,1,0,0,0)
        start_date_data_first_day = datetime(2023,12,31,23,0,0)
        start_date_data_second_day = datetime(2024,1,1,23,0)
        end_date_data = datetime(2024,1,3,0,0,0)

        # Execute
        df_results = api.get_day_ahead_prices_for_zone(BiddingZones.Netherlands, start_date_data, end_date_data)

        # Assert
        # First Day
        self.assertEqual(df_results.iloc[0]['data_valid_start'], start_date_data_first_day)
        self.assertEqual(df_results.iloc[0]['data_valid_end'], start_date_data_first_day + ptu_time_delta)
        self.assertEqual(df_results.iloc[0]['price'], 0.10)
        self.assertEqual(df_results.iloc[1]['data_valid_start'], start_date_data)
        self.assertEqual(df_results.iloc[1]['data_valid_end'], start_date_data + ptu_time_delta)
        self.assertEqual(df_results.iloc[1]['price'], 0.01)

        # Second Day
        self.assertEqual(df_results.iloc[2]['data_valid_start'], start_date_data_second_day)
        self.assertEqual(df_results.iloc[2]['data_valid_end'], start_date_data_second_day + ptu_time_delta)
        self.assertEqual(df_results.iloc[2]['price'], 29.39)        
        self.assertEqual(df_results.iloc[3]['data_valid_start'], start_date_data_second_day + ptu_time_delta)
        self.assertEqual(df_results.iloc[3]['data_valid_end'], start_date_data_second_day + 2 * ptu_time_delta)
        self.assertEqual(df_results.iloc[3]['price'], 19.60)        
        self.assertEqual(df_results.iloc[4]['data_valid_start'], start_date_data_second_day + 2 * ptu_time_delta)
        self.assertEqual(df_results.iloc[4]['data_valid_end'], start_date_data_second_day + 3 * ptu_time_delta)
        self.assertEqual(df_results.iloc[4]['price'], 27.33)

if __name__ == '__main__':
    unittest.main()