# -*- coding: utf-8 -*-

def command():
    return "enable-zabbix-monitoring-instance"

def init_argument(parser):
    parser.add_argument("--instance-no", required=True)

def execute(requester, args):
    instance_no = args.instance_no

    parameters = {}
    parameters["InstanceNo"] = instance_no

    return requester.execute("/EnableZabbixMonitoringInstance", parameters)
