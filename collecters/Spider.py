import argparse
from selenium import webdriver
import requests


def recursiveSearch(args):
    print ("r is working")

def dephtSetiing(args):
    print ("l is working")

def saveingInPath(args):
    print ("p is working")

def main():
    ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    # try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recursive", dest="rec", action="store_true", help="Recursivly read in all directories")
    parser.add_argument("-l", "--level", dest="lvl", type=int, nargs='?', const=5, help="Sets the depht of search")
    parser.add_argument("-p", "--path", dest="pth", type=str, nargs='?', const="./data/", help="The path of page")
    parser.add_argument("url", type=str, help="The URL to process")
    args = parser.parse_args()
    driver = webdriver.Chrome(executable_path="~/Applications/Chrome")
    print("hasnuma")
    driver.get(args.url)
    img = driver.find_element(By.XPATH, "//div[matches(@class, '.*\.jpg')]")
    img_url = img.get_attribute("src")
    response = requests.get(img_url)
    with open('image.jpg', 'wb') as file:
        file.write(response.content) 
    if args.rec:
        recursiveSearch(args)
    if args.lvl:
        dephtSetiing(args)
    if args.pth:
        saveingInPath(args)
    # except Exception as e:
        # print("ape stop: ".format(e))


if __name__ == "__main__":
    main()