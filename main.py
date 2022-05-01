import os
import os.path
from datetime import date
from shutil import rmtree
import stat

details = { "timeLimit" : 5}

def calc_btwn_days(d1, d2):
    date1 = date(d1.year, d1.month, d1.day)
    date2 = date(d2.year, d2.month, d2.day)
    return (date2 - date1).days

