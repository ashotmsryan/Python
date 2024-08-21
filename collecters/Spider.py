import argparse
from bs4 import BeautifulSoup
import requests
import os


def recursiveSearch(args):
    print ("r is working")

def dephtSetiing(args):
    print ("l is working")

def saveingInPath(args):
    print ("p is working")

def getReqImg(name):
    n = name
    ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    lastDot = name.rfind('.')
    if (lastDot != -1 and n[lastDot:len(n)] in ext):
        return True
    return False
        
def main():
    # try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recursive", dest="rec", action="store_true", help="Recursivly read in all directories")
    parser.add_argument("-l", "--level", dest="lvl", type=int, nargs='?', const=5, help="Sets the depht of search")
    parser.add_argument("-p", "--path", dest="pth", type=str, nargs='?', const="./data/", help="The path of page")
    parser.add_argument("url", type=str, help="The URL to process")
    
    args = parser.parse_args()

    response = requests.get(args.url)
    html_cont = response.text
    soup = BeautifulSoup(html_cont, 'html.parser')
    imgs = soup.find_all('img')

    for img in imgs:
        img_url = img.get('src')
        if not img_url:
            continue
        if not img_url.startswith(('http:', 'https:')):
            img_url = requests.compat.urljoin(args.url, img_url)
        
        name = os.path.basename(img_url)
        if (getReqImg(name) == False):
            continue
        result = requests.get(img_url)

        with open(name, 'wb') as f:
            f.write(result.content)

    # if args.rec:
    #     recursiveSearch(args)
    # if args.lvl:
    #     dephtSetiing(args)
    # if args.pth:
    #     saveingInPath(args)
    # except Exception as e:
        # print("ape stop: ".format(e))


if __name__ == "__main__":
    main()