import StringIO

import sys
from scraper import Scraper
from poster import Poster


def main():

    print "ENTER THE YOSPOS"
    print "Using " + sys.argv[1] + " @ threadid: " + sys.argv[3]
    new_scraper = Scraper(sys.argv[1], sys.argv[2], sys.argv[3])
    new_scraper.scrape_thread()

    new_message = raw_input("Reply: ")
    new_poster = Poster(sys.argv[1], sys.argv[2], sys.argv[3])
    new_poster.make_post(new_message)

main()