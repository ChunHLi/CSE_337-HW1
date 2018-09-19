import statistics
import time
import urllib.request
from bs4 import BeautifulSoup
from collections import defaultdict
from collections import OrderedDict

def main():
    nf = open("commodities.txt","w+")
    response = urllib.request.urlopen("https://finance.yahoo.com/commodities/")
    soup = BeautifulSoup(response, "html.parser")
    td_soup = soup.find_all('td')
    td_soup_line = ""
    i = 0
    for x in td_soup:
        if x.get_text() == "":
            nf.write(td_soup_line[:-1] + "\n")
            td_soup_line = ""
            i = 0
        else:
            if i < 5:
                td_soup_line = td_soup_line + x.get_text() + ","
                i += 1


if __name__ == "__main__":
    main()