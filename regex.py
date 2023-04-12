# Regular Expression


import re


def search():
    line = "I think I understand regular expressions"
    
    matchResult = re.match("think", line, re.M|re.I)
    if (matchResult):
        print(f"Mach found: {matchResult.group()}")
    else:
        print(f"No Match was found")

    searchResult = re.search("think", line, re.M|re.I)
    if (searchResult):
        print(f"Search Found: {searchResult.group()}")
    else:
        print("Nothink found in search")


if __name__ == "__main__":
    search()

