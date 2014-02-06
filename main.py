import StringIO

import sys
from scraper import Scraper


def main():

    print "ENTER THE YOSPOS"
    print "Using " + sys.argv[1] + " @ threadid: " + sys.argv[3]
    new_scraper = Scraper(sys.argv[1], sys.argv[2], sys.argv[3])
    new_scraper.scrape_thread()

main()