import os
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-r", "--region", help="Valid Azure region", required=True)
argument_parser.add_argument("-rg", "--resgroupname", help="Azure resource group name", required=True)
argument_parser.add_argument("-b", "--botname", help="Unique name for the bot", required=True)
argument_parser.add_argument("-sv", "--svcplanname", help="Service plan name", required=True)
argument_parser.add_argument("-w", "--webappname", help="Azure web app name", required=True)
argument_parser.add_argument("-a", "--appsvcname", help="Azure app service name", required=True)
argument_parser.add_argument("-p", "--password", help="Azure app password", required=True)
argument_parser.add_argument("-s", "--sku", help="Bot Pricing SKU/Tier", required=True)

argument_parser.parse_args()