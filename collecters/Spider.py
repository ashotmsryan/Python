import argparse

def recursiveSearch(args):
    print ("r is working")

def dephtSetiing(args):
    print ("l is working")

def saveingInPath(args):
    print ("p is working")

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-r", "--recursive", dest="rec", action="store_true", help="Recursivly read in all directories")
        parser.add_argument("-l", "--level", dest="lvl", type=int, nargs='?', const=5, help="Sets the depht of search")
        parser.add_argument("-p", "--path", dest="pth", type=str, nargs='?', const="./data/", help="The path of page")
        parser.add_argument("url", type=str, help="The URL to process")
        args = parser.parse_args()

        if args.rec:
            recursiveSearch(args)
        if args.lvl:
            dephtSetiing(args)
        if args.pth:
            saveingInPath(args)
    except Exception as e:
        print("ape stop: ".format(e))


if __name__ == "__main__":
    main()