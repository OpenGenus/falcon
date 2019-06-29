"""
                     ___     __
 ___  ___  ___ ___  / _/__ _/ /______  ___
/ _ \/ _ \/ -_) _ \/ _/ _ `/ / __/ _ \/ _ |
\___/ .__/\__/_//_/_/ \_,_/_/\__/\___/_//_/
   /_/

An interface to all the services in falcon
"""


import argparse as arg
import sys
from . import search
from . import recommendations
from . import code
from . import stats
from . import index


def init_search_module_args(parser):
    parser.add_argument(
        "--search", help="Search for occurence of a term in Cosmos", type=str
    )
    parser.add_argument("--results", help="Number of search results", type=int)


def init_recommendation_module_args(parser):
    parser.add_argument("--recommend", help="The recommendation term")
    parser.add_argument("--top", help="Number of results to show", type=int)
    parser.add_argument("--type", help="Type of recommendation can be parent/child/all")


def init_code_module_args(parser):
    parser.add_argument(
        "--code", help="Delete/Edit the code sections", action="store_true"
    )
    parser.add_argument("--term", help="The term to look for")
    parser.add_argument("--language", help="Enter the language extension")
    parser.add_argument(
        "--control", help="Enter what to do with end file can be save,edit or delete"
    )


def init_stats_module_args(parser):
    parser.add_argument(
        "--stats", help="Generate statstics of Cosmos repo", action="store_true"
    )
    parser.add_argument(
        "-f",
        "--format",
        default="md",
        help='Ouput can be "txt" for text file and "md" for markdown or "all" for all formats',
    )


def init_index_module_args(parser):
    parser.add_argument(
        "-c", "--clone", action="store_true", help="Clone the cosmos repo"
    )


def main():
    parser = arg.ArgumentParser("openfalcon")
    init_search_module_args(parser)
    init_recommendation_module_args(parser)
    init_code_module_args(parser)
    init_stats_module_args(parser)
    init_index_module_args(parser)
    args = parser.parse_args()

    if len(sys.argv) == 1:
        print("Please refer to help section using openfalcon --help / openfalcon -h")
        sys.exit()

    if args.clone:
        c_repo = index.Cosmos()
        if not c_repo.clone_repo():
            print("Clone the cosmos repo manually")
            exit(0)
    if args.stats:
        stats.main(args.format)
        exit(0)
    if args.search:
        # results arg can only be used when search arg is present
        if args.results and (args.search is None):
            parser.error("--results requires --search argument")
            sys.exit()
        search.main(args.search, args.results)
    if args.recommend:
        recommendations.main(args.recommend, args.top, args.type)
    if args.code:
        if args.term is None or args.language is None or args.control is None:
            parser.error("--code requires --term --language and --control arguments")
            sys.exit()
        code.main(args.term, args.language, args.control)
