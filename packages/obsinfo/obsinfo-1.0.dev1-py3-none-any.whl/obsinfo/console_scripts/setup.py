"""
Application to configure variables used by obsinfo in file .obsinforc
and to copy examples and templates out of the distribution directories
"""
import os
# import sys
import re
# import site
import shutil
import datetime
import platform
from pathlib import Path
import warnings
from errno import ENOENT

from ..misc.const import EXIT_IOERR
from ..version import __version__
from ..helpers import init_logging

logger = init_logging("setup")


def main(args):
    """
    Entry point to configure variables in file .obsinforc

    and to copy examples and templates out of the distribution directories
    """
    # initialize variables
    version = platform.python_version()
    path_to_package = Path(__file__).parent.parent
    examples_dir = path_to_package.joinpath("_examples/Information_Files")
    templates_dir = path_to_package.joinpath("templates")
    home = Path.home()
    configuration_file = home.joinpath('.obsinforc')

    validate_arguments(args)

    # create logging directory if it doesn't exist
    logdir = Path().home().joinpath('.obsinfo').resolve()
    if not os.path.isdir(logdir):
        os.mkdir(logdir)

    # copy examples and templates
    if args.dest and not args.no_copy:
        try:
            dest = Path(args.dest).resolve()
            # if dest dir exists rename it with timestamp to preserve it
            if os.path.isdir(dest) or os.path.isfile(dest):
                new_dest = str(dest) + "." + str(datetime.datetime.today())
                os.rename(dest, new_dest)

            shutil.copytree(examples_dir, dest.joinpath("Information_Files"))
            shutil.copytree(templates_dir, dest.joinpath("templates"))
        except NotADirectoryError:
            print("Directory not found")
            exit(EXIT_IOERR)
        except OSError as e:
            print("Operating system error")
            print(e)
            exit(EXIT_IOERR)
    # create configuration file
    output = []

    output.append("gitlab_repository: " + args.gitlab + "\n")
    output.append("gitlab_project: " + args.project + "\n")
    output.append("gitlab_path: " + args.remote_path + "\n")
    pat = re.compile("^[0-9]+\.[0-9]+")
    version = pat.match(__version__)
    branch = "v" + version.group(0) if args.branch else "master"

    output.append('obsinfo_branch: ' + branch + '\n')

    if args.no_remote:
        remote_repository = ""
    else:
        remote_repository = "/".join([args.gitlab, args.project,
                                      args.remote_path])

    s = build_datapath_list(args, remote_repository)
    if s:
        output.append(s + "\n")
    try:
        with open(configuration_file, "w") as fp:
            fp.writelines(output)
    except OSError:
        warnings.warn("Could not create configuration file. "
                      "Fix problem and run obsinfo-setup again\n")
        exit(EXIT_IOERR)


def validate_arguments(args):
    """
    Validate that directories in command line arguments exist.

    Raise an exception if not.
    Args:
        args (dict of str): directory with command line argument, but status
            and directories
    Raises:
        OSError, ValueError
    """
    if args.dest:
        if not Path(args.dest):
            raise OSError(ENOENT, "Path for example and template destination "
                                  "directory is an illegal path")

    if args.local_repository:
        if not Path(args.local_repository):
            raise OSError(ENOENT, "Path for local repository for information "
                                  "files is an illegal path")

    if args.working_directory:
        if not Path(args.working_directory):
            raise OSError(ENOENT, "Path for obsinfo working directory is an "
                                  "illegal path")

    if not args.no_remote:
        if not Path(args.gitlab).as_uri:
            raise ValueError('Gitlab repository must be specified as a legal '
                             'URI unless "-n" is on')

    if not args.no_remote:
        if not Path(args.project):
            raise ValueError('Project must be specified as a legal URI unless '
                             '"-n" is on')


def build_datapath_list(args, remote_repository):
    """
    Build datapath as a list of directories to search

    Similar to the PATH environment variable.

    #. Add working_directory as first option if it exists
    #. Next add local repository first if it exists (wll be first if no
       working directory specified)
    #. Finally add destination, where standard examples lie.
       This won't be used if -x is on
    #. Final directory will be the remote one unless -v (invert) is specified
    """
    if args.dest and not args.no_examples:
        default_information_files = str(
            Path(args.dest).joinpath("Information_Files").resolve())
    else:
        default_information_files = None
    if args.invert_datapath:
        dir_list = (remote_repository,
                    args.working_directory,
                    args.local_repository,
                    default_information_files)
    else:
        dir_list = (args.working_directory,
                    args.local_repository,
                    default_information_files,
                    remote_repository, )
    directories = [x for x in dir_list if x is not None]
    s = "datapath: [" + ",".join(directories) + "]"

    # default_information_files = str(Path(args.dest).joinpath("Information_Files").resolve()) if args.dest else ""
    # remote_first = remote_repository + ", " if args.invert_datapath else ""
    # remote_last = remote_repository if not args.invert_datapath else ""
    # s = "datapath: ["
    # s += remote_first
    # s += args.working_directory + ", " if args.working_directory else ""
    # s += args.local_repository + ", " if args.local_repository else ""
    # s += default_information_files + ", " if default_information_files and not args.no_examples else ""
    # s += remote_last if remote_last else ""
    # s += "]"
    # if not remote_last:
    #     s.replace(", ]", "]")

    return s
