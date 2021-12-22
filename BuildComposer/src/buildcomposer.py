import os
import shutil
import argparse
import webbrowser

class Arguments:
  def __init__(self, v, p, w, vb, s):
    self.version = v
    self.path = p
    self.wipe = w
    self.verbose = vb
    self.start = s


def parse_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-v", "--version", help="Specify the Composer version in the format vX.X.X corresponding to the Release tag on Github [REQUIRED]", required=True)
    argument_parser.add_argument("-p", "--path", help="Specify desired directory file path to store the Composer version [REQUIRED]", required=True)
    argument_parser.add_argument("-w", "--wipe", help="Delete the existing version before installing", action="store_true")
    argument_parser.add_argument("-vb", "--verbose", help="Enable verbose errors", action="store_true")
    argument_parser.add_argument("-s", "--start", help="Skip download and installation and just start and open Composer", action="store_true")
    args = argument_parser.parse_args()
    return Arguments(args.version, args.path, args.wipe, args.verbose, args.start)

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
        if os.path.isdir(os.path.join(args.path, "Composer %s" % args.version)):
            print("\n[Deleting existing version of Composer %s]" % args.version)
            print("\n[This can take some time, please wait...]")
            path = os.path.join(os.getcwd(), "Composer %s\\" % args.version)
            try:
                shutil.rmtree(path)
                print("\n[Wipe of Composer %s Complete]" % args.version)
            except Exception as e:
                print("[Error Deleting Directory]")
                if args.verbose:
                    print(e)
        else:
            print("\n[Composer version %s not found. Skipping Deletion]" % args.version)
    else:
        print("\n[Wipe flag not set. Skipping Deletion]")
        return

#TODO: Fix failure to stop on exist
def make_composer_dir(args):
    if not os.path.isdir(".\Composer %s" % args.version):#and not args.wipe:
        print("\n[Creating new directory at %s\Composer %s]" % (args.path, args.version))
        try:
            os.system("mkdir \"Composer %s\"" % args.version)
            os.chdir(".\Composer %s\\" % args.version)
        except Exception as e:
            print("[Error Creating Directory]")
            if args.verbose:
                    print(e)
    else:
        print("[Composer %s directory already exists. Please specify -w/--wipe to delete and reinstall this version.]" % args.version)

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


def check_out_version(args):
    print("\n[Checking out %s]\n" %args.version)
    try:
        os.system("git checkout tags/%s" % args.version)
    except Exception as e:
        print("[Error Checking Out %s]" % args.version)
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
        check_out_version(args)
        build(args)
        install(args)

    start(args)

# __name__
if __name__=="__main__":
    main()