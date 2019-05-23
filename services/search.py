import sys
import argparse
import getSearchResults

parser = argparse.ArgumentParser()
parser.add_argument("--search", help='The search term')
parser.add_argument("--results", help='Required number of results')

args = parser.parse_args()

searchTerm = args.search
display = args.results

if searchTerm==None:
    print("Enter a valid Search Term")
    sys.exit()

getSearchResults.getSearchResults(searchTerm,display)

