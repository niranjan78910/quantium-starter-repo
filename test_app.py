"""Basic callback behaviour tests for the Dash sales visualiser."""
import unittest
from unittest.mock import patch
import pandas as pd

from app import update_chart


class SalesChartTests(unittest.TestCase):
    def setUp(self):
        self.sample = pd.DataFrame({
            "date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
            "region": ["North", "South", "North"],
            "Sales": [10, 20, 30],
        })

    def test_all_regions(self):
        with patch("app.df", self.sample):
            fig = update_chart("all")
        self.assertEqual(len(fig.data[0].x), 3)

    def test_north_region(self):
        with patch("app.df", self.sample):
            fig = update_chart("north")
        self.assertEqual(len(fig.data[0].x), 2)


if __name__ == "__main__":
    unittest.main()
