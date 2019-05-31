"""
                     ___     __
 ___  ___  ___ ___  / _/__ _/ /______  ___
/ _ \/ _ \/ -_) _ \/ _/ _ `/ / __/ _ \/ _ \
\___/ .__/\__/_//_/_/ \_,_/_/\__/\___/_//_/
   /_/

An interface to all the services in falcon
"""


import argparse as arg
import sys
from . import search


def init_search_module_args(parser):
    parser.add_argument(
        "--search", help="Search for occurence of a term in Cosmos", type=str
    )
    parser.add_argument(
        "--results", default=5, help="Number of search results", type=int
    )


def main():
    parser = arg.ArgumentParser("openfalcon")
    init_search_module_args(parser)
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
