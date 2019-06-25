import sys
import argparse
from . import getSearchResults


def main(*args):
    """
    similar to grep -ir "term" in cosmos repo,
    we try to find sentences having the given term
    and display n-number of results
    """
    if len(args) == 0:
        parser = argparse.ArgumentParser()
        parser.add_argument("--search", help="The search term")
        parser.add_argument("--results", help="Required number of results")
        args = parser.parse_args()
        searchTerm = args.search
        display = args.results
    else:
        searchTerm = args[0]
        display = args[1]
    if searchTerm == None:
        print("Enter a valid Search Term")
        sys.exit()

    print(getSearchResults.getSearchResults(searchTerm, display))


if __name__ == "__main__":
    main()
