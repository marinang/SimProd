#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json as js
import pyparsing

from tinydb import JSONStorage, TinyDB
from tinydb.middlewares import CachingMiddleware

from .utilities import red, blue

Suppress = pyparsing.Suppress
Word = pyparsing.Word
Literal = pyparsing.Literal
alphas = pyparsing.alphas
number = Word(pyparsing.nums)
OneOrMore = pyparsing.OneOrMore

simprod = os.getenv("SIMPRODPATH")
jobsfile = "{0}/simjobs.json".format(simprod)


class CorruptedDB(Exception):
    """Exception class for corrupted database."""

    pass


def getdatabase():

    for ntry in range(3):
        try:
            storage = CachingMiddleware(JSONStorage)
            storage.WRITE_CACHE_SIZE = 600
            db = TinyDB(jobsfile, storage=storage), storage
            if ntry > 0:
                print(blue("The database was successfully fixed."))
            return db
        except ValueError:
            if ntry == 0:
                print(blue("The database is corrupted. Attempting to fix it."))
            debug_json(jobsfile)
    else:
        msg = "The database coulnd't be fixed. Please open an issue in https://github.com/marinang/SimProd/issues"
        msg += " with the 'simjobs.json' file attached."
        raise CorruptedDB(red(msg))


def debug_json(jsfile):

    with open(jsfile, "r") as f:
        try:
            js.load(f)
        except ValueError as e:
            pass

    parser = (
        Suppress(OneOrMore(Word(alphas)) + Literal(":") + Word(alphas))
        + number.setResultsName("line")
        + Suppress(Word(alphas))
        + number.setResultsName("column")
    )

    try:
        parsed_error_msg = dict(parser.parseString(e.message))
        parsed_error_msg = {k: int(v) - 1 for k, v in parsed_error_msg.items()}

        assert all(key in parsed_error_msg for key in ["column", "line"])

        with open(jsfile, "r") as f:
            lines = f.readlines()

        new_lines = []
        for i, l in enumerate(lines):
            if i == parsed_error_msg["line"]:
                new_lines.append(l[0 : parsed_error_msg["column"]])
            else:
                new_lines.append(l)

        with open(jsfile, "w") as f:
            f.writelines(new_lines)

    except pyparsing.ParseException:
        pass

    return jsfile
