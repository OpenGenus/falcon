########################
####### BRIDGE #########
########################

# This acts as a bridge between the services and the launcher for the application

import argparse as arg
import sys
from . import search


def main():
    parser = arg.ArgumentParser("openfalcon")
    # Intiailize args for Search module
    parser.add_argument(
        "--search", help="Search for occurence of a term in Cosmos", type=str
    )
    parser.add_argument(
        "--results", default=5, help="Number of search results", type=int
    )
    # End args for Search module
    args = parser.parse_args()
    # results arg can only be used when search arg is present
    if args.results and (args.search is None):
        parser.error("--results requires --search argument")
        sys.exit()
    if len(sys.argv) == 1:
        print("Please refer to help section using openfalcon --help / openfalcon -h")
        sys.exit()
    if args.search:
        search.main(args.search, args.results)
