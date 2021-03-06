# -*- coding: utf-8 -*-

def command():
    return "list-image"

def init_argument(parser):
    parser.add_argument("--platform-no", required=True)

def execute(requester, args):
    platform_no = args.platform_no

    parameters = {}
    parameters["PlatformNo"] = platform_no

    return requester.execute("/ListImage", parameters)
