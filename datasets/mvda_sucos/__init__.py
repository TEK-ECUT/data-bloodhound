#!/usr/bin/env
# -*- coding: utf-8 -*-
# Copyright (C) CENATAV, DATYS - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Victor M. Mendiola Lau <vmendiola@cenatav.co.cu>, March 2017

import os

import utils.datasets as utils

# ---------------------------------------------------------------

# data set paths
__data_set_path = "{}/data/sucos-raw-data.txt".format(os.path.split(__file__)[0])

__pickle_path = "{}/cache/mvda_sucos.pickle".format(os.path.split(__file__)[0])

# ---------------------------------------------------------------

# TODO: Add docstring with usage examples (see 'uv_fuel' data set)


@utils.load_data_from_pickle(__pickle_path)
def load_mvda_sucos():
    # parsing the raw data file
    with open(__data_set_path, 'r') as f:
        # declaring variables holding labels and data
        samples_labels = []
        data = []

        # reading header
        header = f.readline()
        features_labels = [h.strip() for h in header.split(' ')]

        # for each line in the file
        for line in f:
            # parsing current line
            line_parsed = [s.strip() for s in line.split(' ')]

            # adding sample name to labels list
            samples_labels.append(line_parsed[0])

            data.append([float(s) for s in line_parsed[1:]])

    # building classes from samples names
    classes = [s_name[:-1] for s_name in samples_labels]

    # returning the built data set
    return utils.build_data_set(data, samples_labels, features_labels, extra_cols={'class': classes})