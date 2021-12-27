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

def create_app_registration(args):
    if args.multitenant:
        os.system("az ad app create --display-name %s --password %s --available-to-other-tenants")
    else:
        os.system("az ad app create --display-name %s --password %s")

def create_deployment(args):
    return

def prepare_deploy(args):
    return

def zip_deploy(args):
    return

def main():
    args = parse_args()
    os.chdir(args.path)
    create_app_registration(args)
    create_deployment(args)
    prepare_deploy(args)
    zip_deploy(args)


# __name__
if __name__=="__main__":
    main()