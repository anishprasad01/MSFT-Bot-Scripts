import os
import shutil
import argparse
import webbrowser

class Arguments:
  def __init__(self, r, p, w, v, s):
    self.release = r
    self.path = p
    self.wipe = w
    self.verbose = v
    self.start = s


def parse_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-r", "--release", help="Specify the Composer release in the format vX.X.X corresponding to the Release tag on Github [REQUIRED]", required=True)
    argument_parser.add_argument("-p", "--path", help="Specify desired directory file path to store the Composer release [REQUIRED]", required=True)
    argument_parser.add_argument("-w", "--wipe", help="Delete the existing release before installing", action="store_true")
    argument_parser.add_argument("-v", "--verbose", help="Enable verbose errors", action="store_true")
    argument_parser.add_argument("-s", "--start", help="Skip download and installation and just start and open Composer", action="store_true")
    args = argument_parser.parse_args()
    return Arguments(args.release, args.path, args.wipe, args.verbose, args.start)

def change_dir(args):
    if args.path is not None:
        try:
            os.chdir(args.path)
        except Exception as e:
            print("[Error Changing Directory]")
            if args.verbose:
                print(e)
            exit()
    else:
        return

def wipe(args):
    if args.wipe:
        if os.path.isdir(os.path.join(args.path, "Composer %s" % args.release)):
            print("\n[Deleting existing release of Composer %s]" % args.release)
            print("\n[This can take some time, please wait...]")
            path = os.path.join(os.getcwd(), "Composer %s\\" % args.release)
            try:
                shutil.rmtree(path)
                print("\n[Wipe of Composer %s Complete]" % args.release)
            except Exception as e:
                print("[Error Deleting Directory]")
                if args.verbose:
                    print(e)
        else:
            print("\n[Composer release %s not found. Skipping Deletion]" % args.release)
    else:
        print("\n[Wipe flag not set. Skipping Deletion]")
        return

#TODO: Fix failure to stop on exist
def make_composer_dir(args):
    if not os.path.isdir(".\Composer %s" % args.release):#and not args.wipe:
        print("\n[Creating new directory at %s\Composer %s]" % (args.path, args.release))
        try:
            os.system("mkdir \"Composer %s\"" % args.release)
            os.chdir(".\Composer %s\\" % args.release)
        except Exception as e:
            print("[Error Creating Directory]")
            if args.verbose:
                    print(e)
    else:
        print("[Composer %s directory already exists. Please specify -w/--wipe to delete and reinstall this release.]" % args.release)

def clone_repo(args):
    print("\n[Cloning Composer Repository]\n")
    if not os.path.isdir(".\BotFramework-Composer"):
        try:
            os.system("git clone https://github.com/microsoft/BotFramework-Composer.git")
        except Exception as e:
            print("[Error Cloning Composer Repository]")
            if args.verbose:
                print(e)
            exit()
    else:
        print("[Composer Already Cloned]")
    os.chdir("BotFramework-Composer\Composer")


def check_out_release(args):
    print("\n[Checking out %s]\n" %args.release)
    try:
        os.system("git checkout tags/%s" % args.release)
    except Exception as e:
        print("[Error Checking Out %s]" % args.release)
        if args.verbose:
            print(e)
        exit()


def build(args):
    print("\n[Building Composer]\n")
    try:
        os.system("yarn install")
    except Exception as e:
        print("[Error running yarn install]")
        if args.verbose:
            print(e)
        exit()

def install(args):
    print("\n[Installing Composer]\n")
    try:
        os.system("yarn build")
    except Exception as e:
        print("]Error running yarn build]")
        if args.verbose:
            print(e)
        exit()

def start(args):
    print("\n[Starting Composer & Opening in Default Browser]\n")

    if args.start:
        os.chdir("BotFramework-Composer\Composer")

    try:
        webbrowser.open("http://localhost:3000")
        os.system("yarn startall")
    except Exception as e:
        print("[Error starting Composer]")
        if args.verbose:
            print(e)
        exit()

def main():
    args = parse_args()

    change_dir(args)

    if not args.start:
        wipe(args)
        make_composer_dir(args)
        clone_repo(args)
        check_out_release(args)
        build(args)
        install(args)

    start(args)

# __name__
if __name__=="__main__":
    main()