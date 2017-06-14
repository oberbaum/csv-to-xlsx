#!/usr/bin/env python

import sys
import csv
import openpyxl

ANSI_GREEN = "\u001B[32m"
ANSI_RED = "\u001b[31m"
ANSI_RESET = "\u001b[0m"

def arg_input():
    #command line input
    try:
        arg_in = sys.argv[1]
        if arg_in.split(".")[-1] == "csv":
            a = open(arg_in)
            return a
        else:
            print(ANSI_RED + "need .csv file" + ANSI_RESET)
            sys.exit(2)
    except FileNotFoundError:
        print(ANSI_RED + "File was not found!" + ANSI_RESET)
        sys.exit(2)
    except NameError:
        sys.exit(2)


def arg_output():
    #guess what
    arg_out = sys.argv[2]
    return arg_out

def convertcsv(inputcsv, out):
    #converting csv to xlsx
    wb = openpyxl.Workbook()
    ws = wb.active

    reader = csv.reader(inputcsv, delimiter = ',')
    for row in reader:
        if not row:
            print("empty row")
        else:
            ws.append(row)
    inputcsv.close()
    try:
        wb.save(out)
        print(ANSI_GREEN + "success\o/" + ANSI_RESET)
    except NameError:
        sys.exit(2)

def usage():
    print("Usage: {0} <input file> <output file>".format(sys.argv[0]))

def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit(2)

    convertcsv(arg_input(), arg_output())

if __name__ == "__main__":
    main()
