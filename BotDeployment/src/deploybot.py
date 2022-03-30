import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import argparse

class Arguments:
    def __init__(self, r, g, b, sv, w, a, p, s, m, pt):
        self.region = r
        self.groupname = g
        self.botname = b
        self.svcplanname = sv
        self.webappname = w
        self.appsvcname = a
        self.password = p
        self.sku = s
        self.multitenant = m
        self.path = pt


def parse_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-r", "--region", help="Valid Azure region", required=True)
    argument_parser.add_argument("-g", "--groupname", help="Azure resource group name", required=True)
    argument_parser.add_argument("-b", "--botname", help="Unique name for the bot", required=True)
    argument_parser.add_argument("-sv", "--svcplanname", help="Service plan name", required=True)
    argument_parser.add_argument("-w", "--webappname", help="Azure web app name", required=True)
    argument_parser.add_argument("-a", "--appsvcname", help="Azure app service name", required=True)
    argument_parser.add_argument("-p", "--password", help="Azure app password", required=True)
    argument_parser.add_argument("-s", "--sku", help="Bot Pricing SKU/Tier", required=True)
    argument_parser.add_argument("-m", "--multitenant", help="Select tenant type, single or multi", required=True, action="store_true")
    argument_parser.add_argument("-pt", "--path", help="Path to project folder", required=True)
    args = argument_parser.parse_args()
    return Arguments(args.region, args.groupname, args.botname, args.svcplanname, args.webappname, args.appsvcname, args.password, args.sku, args.tenant, args.path)

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