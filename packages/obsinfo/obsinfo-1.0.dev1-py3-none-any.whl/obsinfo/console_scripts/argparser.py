"""
 Main functions for obsinfo-makeStationXML

 Creates obsinfo objects starting with a network object in a hierarchy which
 strongly follows the hierarchy of StationXML files.
 Then converts the objects to a StationXML file using obspy.
"""
import sys
import warnings
from pathlib import Path  # , PurePath
from argparse import ArgumentParser

from ..misc.const import EXIT_SUCCESS
from ..helpers import init_logging
from .xml import main as xml_main
from .setup import main as setup_main
from .print import main as print_main
from .schema import main as schema_main

warnings.simplefilter("once")
warnings.filterwarnings("ignore", category=DeprecationWarning)
logger = init_logging("makeStationXML")


def _print_version(args):
    file = Path(__file__).parent.parent.joinpath("version.py")
    version = {}
    with open(file) as fp:
        exec(fp.read(), version)
    version = version['__version__']

    print(f"{version=}")


def main():
    """
    Entry point all obsinfo sub-commands
    """
    # create the top-level parser
    parser = ArgumentParser(prog="obsinfo")

    subparsers = parser.add_subparsers(title='subcommands')

    # create the parser for the "version" command
    parser_version = subparsers.add_parser(
        'version', help='Print obsinfo version',
        description='Print obsinfo version')
    parser_version.set_defaults(func=_print_version)

    # create the parser for the "setup" command
    parser_setup = subparsers.add_parser(
        'setup',
        description='Set up the obsinfo environment',
        help='Set up obsinfo environment')
    # flags
    parg = parser_setup.add_argument
    parg("-x", "--no_examples", action='store_true', default=False,
         help="Don't import examples, only templates, and "
              "remove examples directory from the datapath")
    parg("-c", "--no_copy", action='store_true', default=False,
         help="Don't import anything at all, don't create "
              "dest directory, which will be removed from datapath")
    parg("-n", "--no_remote", action='store_true', default=False,
         help="Install obsinfo without access to a gitlab repository.\n"
              "May be needed in some operating systems for compatibility")
    parg("-v", "--invert_datapath", action='store_true', default=False,
         help="Put remote gitlab repositorey first. "
              "All local directories will keep their order")
    parg("-b", "--branch", action='store_true', default=False,
         help="Specifies the git branch to use, if not master")
    # optional arguments
    parg("-d", "--dest", default=None,
         help="Destination directory for templates and examples.")
    parg("-g", "--gitlab", default="https://www.gitlab.com",
         help="Gitlab repository)")
    parg("-p", "--project", default="resif/obsinfo",
         help="path to project and the directory where "
              "information files lie within the Gitlab repository")
    parg("-l", "--local_repository", default=None,
         help="Specify local repository for information "
              "files and include it as first or second option in datapath")
    parg("-w", "--working_directory", default=None,
         help="Specify working directory for obsinfo and "
              "include it as first option in datapath")
    parg("-P", "--remote_path",
         default="obsinfo/_examples/Information_Files",
         help="Specify remote directory under project")
    parser_setup.set_defaults(func=setup_main)

    # create the parser for the "schema" command
    parser_schema = subparsers.add_parser(
        'schema',
        description='Validate an information file against its schema',
        help='Validate an information file against its schema')
    parg = parser_schema.add_argument
    parg("-q", "--quiet", action='store_true', default=False,
         help="Quiet operation. Don't print informative messages")
    parg("-s", "--schema",
         help="Force validation against the given schema file "
              "(sets --check_schema)")
    parg("-r", "--remote", action='store_true', default=False,
         help="Search for the input_filename in the DATAPATH repositories")
    parg("-d", "--debug", action='store_true', default=False,
         help="Print traceback for exceptions")
    parg("--drilldown", action='store_true', default=False,
         help="Drill down through all subdirectories (if a directory "
              "was specified)")
    parg("--continue_on_fail", action='store_true', default=False,
         help="Continue validating if a file fails (and a directory "
              "was specified)")
    parg("--check_schema", action='store_true', default=False,
         help="Check the schema before validating")
    # positional arguments
    parg("input", type=str,
         help="Information file or directory to be validated. If a directory, "
              "tests all files in the directory.  If 'DATAPATH', "
              "will test all files in the DATAPATH (sets --drilldown)")
    parser_schema.set_defaults(func=schema_main)

    # create the parser for the "print" command
    parser_print = subparsers.add_parser(
        'print',
        help='Print the obsinfo class created by a file',
        description='Print the obsinfo class created by a file')
    parg = parser_print.add_argument
    parg("-n", "--n_levels", type=int, default=1,
         help="Prints up to N levels")
    parg("-d", "--debug", action='store_true', default=False,
         help="Print traceback for exceptions")
    parg("--drilldown", action='store_true', default=False,
         help="Drill down through all subdirectories (if a "
              "directory was specified)")
    parg("--configs", action='store_true', default=False,
         help="Print configurations instead of object")
    parg("--verbose", action='store_true', default=False, help="Be verbose")
    # positional arguments
    parg("input", type=str,
         help="Information file or directory to be validated. "
              "If a directory, tests all files in the "
              "directory.  If 'DATAPATH', will test all files "
              "in the DATAPATH (sets --drilldown and "
              "--n_sublevels=0)")
    parser_print.set_defaults(func=print_main)

    # create the parser for the "xml" command
    parser_xml = subparsers.add_parser(
        'xml',
        description='Create a stationxml file from a subnetwork file',
        help='Create a stationxml file from a subnetwork file')
    # positional arguments
    parg = parser_xml.add_argument
    parg("input_filename", type=str, nargs=1,
         help="is required and must be a single value")
    # optional arguments
    parg("-t", "--test", action='store_true', default=False,
         help="Produces no output")
    parg("-S", "--station", action="store_true", default=False,
         help="Create a StationXML file with no instrumentation")
    parg("-o", "--output", default=None,
         help="Names the output file. Default is <input stem>.station.xml")
    parg("-v", "--verbose", action='store_true', default=False,
         help="Prints processing progression")
    parg("-q", "--quiet", action='store_true', default=False,
         help="Silences a human-readable summary of processed information "
              "file")
    parg("-d", "--debug", action='store_true', default=False,
         help="Turns on exception traceback")
    parg("-r", "--remote", action='store_true', default=False,
         help="Assumes input filename is discovered through OBSINFO_DATAPATH "
              "environment variable. Does not affect treatment of $ref in "
              "info files")
    parser_xml.set_defaults(func=xml_main)

    args = parser.parse_args()
    args.func(args)  # run the appropriate function
    sys.exit(EXIT_SUCCESS)


if __name__ == '__main__':
    main()
