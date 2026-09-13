#!/usr/bin/env python3

import unittest

import numpy as np
import pandas as pd

from src.subsetting_with_loc import subsetting_with_loc


class SubsettingWithLoc(unittest.TestCase):

    def test_returns_a_dataframe(self):
        df = subsetting_with_loc()
        self.assertIsInstance(
            df, pd.DataFrame, msg="Must return a pandas DataFrame!"
        )

    def test_shape(self):
        df = subsetting_with_loc()
        self.assertEqual(df.shape, (311, 3), msg="Incorrect shape!")

    def test_columns_and_indices(self):
        df = subsetting_with_loc()
        np.testing.assert_array_equal(
            df.columns,
            [
                "Population",
                "Share of Swedish-speakers of the population, %",
                "Share of foreign citizens of the population, %",
            ],
            err_msg="Incorrect column names!",
        )
        self.assertEqual(df.index[0], "Akaa", msg="Incorrect first index!")
        self.assertEqual(
            df.index[-1], "Äänekoski", msg="Incorrect last index!"
        )

    def test_aggregate_rows_excluded(self):
        df = subsetting_with_loc()
        self.assertNotIn(
            "WHOLE COUNTRY",
            df.index,
            msg="'WHOLE COUNTRY' comes before 'Akaa' in the file and "
            "should not be included!",
        )
        self.assertNotIn(
            "Äänekoski sub-regional unit",
            df.index,
            msg="'Äänekoski sub-regional unit' comes after the "
            "municipality 'Äänekoski' and should not be included!",
        )

    def test_akaa_row_values(self):
        df = subsetting_with_loc()
        row = df.loc["Akaa"]
        self.assertEqual(
            row["Population"], 16769, msg="Incorrect Population for Akaa!"
        )
        self.assertAlmostEqual(
            row["Share of Swedish-speakers of the population, %"],
            0.2,
            msg="Incorrect Swedish-speaker share for Akaa!",
        )
        self.assertAlmostEqual(
            row["Share of foreign citizens of the population, %"],
            1.6,
            msg="Incorrect foreign-citizen share for Akaa!",
        )

    def test_aanekoski_row_values(self):
        df = subsetting_with_loc()
        row = df.loc["Äänekoski"]
        self.assertEqual(
            row["Population"],
            19144,
            msg="Incorrect Population for Äänekoski!",
        )
        self.assertAlmostEqual(
            row["Share of Swedish-speakers of the population, %"],
            0.1,
            msg="Incorrect Swedish-speaker share for Äänekoski!",
        )
        self.assertAlmostEqual(
            row["Share of foreign citizens of the population, %"],
            1.2,
            msg="Incorrect foreign-citizen share for Äänekoski!",
        )


if __name__ == "__main__":
    unittest.main()
