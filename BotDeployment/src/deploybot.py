import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import argparse

class Arguments:
    def __init__(self, b, pwd):
        self.botid = b
        self.password = pwd


def parse_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-b", "--botid", help="Unique name for the bot", required=True)
    argument_parser.add_argument("-pwd", "--password", help="Azure app password", required=True)
    args = argument_parser.parse_args()
    return Arguments(args.botid, args.password)


def find_az():
    cmd = 'where az'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    res = output.splitlines()[1]
    az_location = str(res)[2:len(str(res))-1]
    return az_location

def create_app_registration(args, az_location):
    subprocess.check_call([az_location, "ad", "app", "create", "--display-name", args.botid, "--password", args.password, "--available-to-other-tenants"])

# def create_resources(args):
#     return

# def build_project(args):
#     return

# def prepare_deploy(args):
#     return

# def zip_deploy(args):
#     return

def main():
    args = parse_args()
    az_location = find_az() 
    os.chdir(args.path)
    create_app_registration(args, az_location)
    #create_resources(args)
    #build_project(args)
    #prepare_deploy(args)
    #zip_deploy(args)

# __name__
if __name__=="__main__":
    main()