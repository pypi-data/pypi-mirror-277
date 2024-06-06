import sys
from .logs_to_db import logs_to_db

if __name__ == "__main__":
    resultsPath = sys.argv[1]
    logs_to_db(resultsPath)
