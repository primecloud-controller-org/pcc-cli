# -*- coding: utf-8 -*-

def command():
    return "describe-component"

def init_argument(parser):
    parser.add_argument("--component-no", required=True)

def execute(requester, args):
    component_no = args.component_no

    parameters = {}
    parameters["ComponentNo"] = component_no

    return requester.execute("/DescribeComponent", parameters)
