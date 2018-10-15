from pyzabbix import ZabbixAPI
import socket


host_list = ['host1.local','host2.local']

zapi = ZabbixAPI("http://zabbix_server",user="user", password="password")

for item in host_list:
    item_ip = socket.gethostbyname(item.strip())
    zapi.host.create(
        host=item,
        status=0,
        interfaces=[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": item_ip,
            "dns": item,
            "port": 10050
        },{
            "type": 2,
            "main": "1",
            "useip": 1,
            "ip": item_ip,
            "dns": item,
            "port": 161
        }],
        groups=[{
            "groupid": 17
        },{
            "groupid": 268
        }],
        templates=[{
            "templateid": 10107
        }]
    )