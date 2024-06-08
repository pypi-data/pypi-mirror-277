
"""Script that contains utility definitions common to most import scripts

Author: Alok M
Date:   11/2015

This script contains some common function definitions that are needed
by most python file import scripts.  The goal of this script is to
reduce the amount of coding required to generate a new file import
script.

The anticipated usage is as follows:

1) include a line at the top of a specific script as follows:

    from fileimport_util import *

2) Define specific functions to read an instrument file
and write a corresponding clims file.

    def read_file(filename):
        ...

    def write_file(filename):
        ...

In both function definitions, the "filename" corresponds to the
fully specified filename that the user has selected.  If the user
selects multiple files, these functions will be called once for
each file.  In these, if something goes wrong, the function should
raise an exception; any data that needs to be communicated between
these should be managed through global variables.  Some commonly used
filename parsing functions are imported:

3) Call the main function to kick off the processing

    transform(read_file, write_file)

----

What you get from this file:
    - pre-imports of commonly used python modules
    - pre-imports of specific useful components of modules:
      - pprint()
      - OrderedDict()
      - dirname()
        Example: dirname("a/b/c/a.csv") => "a/b/c"
      - basename()
        Example: basename("a/b/c/a.csv") => "a.csv"
      - splitext()
        Example: file_part, extension = splitext("a/b/c/a.csv")
        => ("a/b/c/a", ".csv")
    - get_input_filenames: provides support to prompt user for filenames;
    - main(): supports drag/drop of files onto script; if none
      are provided, then prompts user; then alternates between
      calling read_file and write_file to process each.
    - Logger (LOG), useful for logging errors and warnings.

Change Log:
AKM 11/2015:    Created.
"""

import csv
import logging
import sys
import os
import datetime
import time
import re
import tkinter
import tkinter.filedialog
from pprint import pprint
from collections import OrderedDict
from os.path import dirname, basename, splitext

# Object that handles logging of errors/messages
# (set it to log INFO or more severe messages to the screen)
LOG = logging.Logger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def transform(read_function, write_function):
    """Call this function to kick off the conversion process"""

    # The typical steps involved, when everything's working fine
    filenames = get_input_filenames()
    for filename in filenames:
        try:
            read_function(filename)
            dirname = os.path.dirname(filename)
            write_function(filename)
        except Exception as err:
            # Something went wrong; output the errors we ran into
            LOG.warning("----- At Error Handler")
            LOG.exception(err)
            LOG.warning("----- Aborted processing of file: '" + filename + "'")

    # Additional warning
    if read_function == read_file or write_function == write_file:
        LOG.warning("---- Completed self-test of fileimport_util")

    # Let the user know we're done
    input ("Press <Enter> to Continue: ")

def get_input_filenames():
    """Acquires and returns the desired list of files to be input"""

    # See if user specified them already on the command line
    # or by dragging the files onto this program
    filenames = sys.argv[1:]  # Everything except first item would be filenames

    # Uncomment this if you want to hardcode filenames (use only for testing)
    dir = dirname(__file__) + "/"
    # filenames = [ dir + "FLAVI MIA.csv" ]
    # filenames = [ dir + "FLAVI_avidity 12-14-16.csv" ]

    # If we don't have a list of filenames yet, ask the user for them
    if not filenames:
        # Let the user know we're about to prompt them for files
        LOG.warning ("Choose all files that contain data to be imported.")

        # Prompt the user
        root = tkinter.Tk()
        root.withdraw()
        filenames_as_string = tkinter.filedialog.askopenfilenames()
        filenames = root.tk.splitlist(filenames_as_string)

    # If we don't have a list of filenames even after asking the user
    # not much more we can do, so abort script execution.
    if not filenames:
        raise Exception ("Script terminated.  No files were specified.")

    return filenames
        

def read_file(filename):
    """Stub function; must be redefined to read in and load contents of file"""
    LOG.warning("Inside stub function to read_file; ignoring: " + filename)


def write_file(filename):
    """Stub function; must be redefined to write file for import to CLIMS"""
    LOG.warning("Inside stub function to write_file; ignoring: " + filename)


def read_standard_csv_with_any_headers(filename):
    """Reads in and loads contents of the specified file"""
    LOG.info ("Reading: " + filename)
    global headers, data

    # Open the file
    with open(filename,newline='') as f:
        # Read the header line, figure out the delimiter and the type of file
        try:
            header_line = f.readline().strip()
            file_dialect = csv.Sniffer().sniff(header_line)
            delimiter = file_dialect.delimiter  # typically tab or comma
            headers = header_line.split(delimiter)
            header_set = set(headers)
        except Exception as err:
            LOG.warning("... ignoring file because of exceptions raised.")
            LOG.exception(err)
            return

        # Read the data rows and populate the appropriate dictionary
        reader = csv.DictReader(f, headers, dialect=file_dialect)
        data = [row for row in reader]

        if not data:
            LOG.warning("...ignoring file because it is empty (no data found).")
            raise Exception("No data found in file: " + filename)
        
        return data


def read_standard_csv_with_headers(filename,
                                   required_headers,
                                   other_headers = None):

    # Load in the entire file
    data = read_standard_csv_with_any_headers(filename)

    # Extract headers
    headers = set(data[0].keys())

    # Verify that required headers are present
    missing_headers = required_headers.difference(headers)
    if missing_headers:
        LOG.warning("... Ignoring file: unable to find required headers.")
        LOG.warning("... Required columns that were missing: " +
                    str(missing_headers))
        return

    all_headers = set(required_headers)
    if other_headers: all_headers.update(other_headers)
        
    # Warn user about other missing headers, but don't abort
    missing_headers = all_headers.difference(headers)
    if missing_headers: LOG.info("Missing headers: " + str(missing_headers))
        
    # Warn user about extra headers, but don't abort
    extra_headers = headers.difference(all_headers)
    if extra_headers: LOG.info("Extra headers: " + str(extra_headers))

    return data

def show_file(filename):
    print ("------ Contents of '" + filename + "' --------")
    with open(filename) as f:
        for line in f:
            LOG.info (line.strip())

if __name__ == "__main__":
    transform(read_file, write_file)
