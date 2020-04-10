#!/usr/bin/env python3
# Author: Mark Kaiser
# Date: 03/28/2020
# Description: Parses weather from the web.

import bs4, requests, argparse

def getTemp(URL):
    res = requests.get(URL)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#main-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b > div > div > section > div.today_nowcard-main.component.panel.today-card-night-clear > div.today_nowcard-section.today_nowcard-condition > div.today_nowcard-temp > span')
    #print(elems)
    temp = elems[0].text.strip()
    print(f'The temperature is: {temp}')


def main():
    parser = argparse.ArgumentParser(description='Provide a url to extract the temperature')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display version number.')
    parser.add_argument('-u', '--url', dest='url', required=False, type=str, help="provide a url")
    args = parser.parse_args()
    if args.ver:
        print("getTemp version 0.1")
        exit()
    url = args.url
    if url == None:
        print('Usage: python3 getTemp.py -u [url]')
        exit(0)
    else:
        getTemp(args.url)
        
if __name__ == '__main__':
    main()
