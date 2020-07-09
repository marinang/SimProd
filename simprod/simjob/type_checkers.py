#!/usr/bin/python
# -*- coding: utf-8 -*-


def check_int(n, what):

    if isinstance(n, int):
        return n
    else:
        raise TypeError(
            "{0} has a non valid {1} type for {2}, must be a str!".format(
                n, type(n), what
            )
        )


def check_str(string, what):

    if isinstance(string, str):
        return string
    else:
        raise TypeError(
            "{0} has a non valid {1} type for {2}, must be a str!".format(
                string, type(string), what
            )
        )


def check_year(year):

    year = check_int(year, "year")

    if year not in [2011, 2012, 2015, 2016, 2017, 2018]:
        raise ValueError("year must be 2011, 2012, 2015, 2016, 2017 or 2018!")

    return year


def check_simcond(version):

    version = check_str(version, "simcond")

    if version not in ["Sim09b", "Sim09c", "Sim09e", "Sim09f", "Sim09h"]:
        raise ValueError("simcond must be Sim09b, Sim09c, Sim09d, Sim09f or Sim09h!")

    return version


def check_simmodel(model):

    model = check_str(model, "simmodel")

    if model not in ["pythia8", "BcVegPy"]:
        raise ValueError("simmodel must be pythia8 or BcVegPy!")

    return model


def check_stripping(version):

    if version is not None:

        version = check_str(version, "stripping")

        if version not in [
            "21",
            "24",
            "28",
            "24r1",
            "24r1p1",
            "28r1",
            "28r1p1",
            "28r2",
            "29r2",
            "29r2p1",
            "34",
            "34r0p1",
        ]:
            msg = "Stripping must be '21, '24', '28', '24r1', '24r1p1'"
            msg += ", '28r1', '28r1p1', '28r2', '29r2', '29r2p1', '34' or '34r0p1'!"
            raise ValueError(msg)

    return version


def check_polarities(polarity):

    if polarity is None:
        return polarity

    polarity = check_str(polarity, "polarities")

    if polarity not in ["MagUp", "MagDown"]:
        msg = "Invalid value '{}' for polarities. Valid choices are ['MagUp', 'MagDown'].".format(
            polarity
        )
        raise ValueError(msg)

    return polarity


def check_flag(boolean, what):

    if isinstance(boolean, bool):
        return boolean
    else:
        raise TypeError(
            "{0} has a non valid {1} type for {2}, must be a bool!".format(
                boolean, type(boolean), what
            )
        )
