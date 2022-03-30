import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import argparse
from xml.etree.ElementTree import register_namespace

class Arguments:
    def __init__(self, botid, pwd, type, tenid, sku, rgname, rglocation, appname, svc_plan_name, svc_plan_location, svc_plan_sku):
        self.botid = botid
        self.password = pwd
        self.type = type
        self.tenantid = tenid
        self.sku = sku
        self.rgname = rgname
        self.rglocation = rglocation
        self.webappname = appname
        self.svc_plan_name = svc_plan_name
        self.svc_plan_location = svc_plan_location
        self.svc_plan_sku = svc_plan_sku

def parse_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-b", "--botid", help="Unique name for the bot", required=True)
    argument_parser.add_argument("-pwd", "--password", help="Azure app password", required=True)
    argument_parser.add_argument("-t", "--type", help="App Type: Multi Tenant, Single Tenant, Managed Identity", action="store_true", required=True)
    argument_parser.add_argument("-tid", "--tenantid", help="Tenant ID. Reuqired for Single Tenant and UAMI")
    argument_parser.add_argument("-s", "--sku", help="Bot pricing tier, F0 or S1", required=True)
    argument_parser.add_argument("-rn", "--group-name", help="Resource group name", required=True)
    argument_parser.add_argument("-rl", "--group-location", help="Resource group Azure region", required=True)
    argument_parser.add_argument("-w", "--web-app-name", help="New web application name", required=True)
    argument_parser.add_argument("-spn", "--svc-plan-name", help="Service plan name", required=True)
    argument_parser.add_argument("-spl", "--svc-plan-location", help="Service plan Azure region", required=True)
    argument_parser.add_argument("-sps", "--svc-plan-sku", help="Service plan pricing tier, default is S1", required=True)

    args = argument_parser.parse_args()
    return Arguments(args.botid, args.password, args.type, args.tenantid, args.sku, args.rgname, args.rglocation, args.webappname, args.svc_plan_name, args.svc_plan_location, args.svc_plan_sku)

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