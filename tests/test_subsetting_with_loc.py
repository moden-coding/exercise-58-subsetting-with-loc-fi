#!/usr/bin/env python3

import unittest

import numpy as np

from src.subsetting_with_loc import subsetting_with_loc


class SubsettingWithLoc(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
