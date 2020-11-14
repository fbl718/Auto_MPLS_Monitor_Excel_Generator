# Get node list

import json
import requests


def get_node_list():
    url_list = 'http://10.18.2.31/cs_system/admin/Monitor/fun_network_status_json.php?act=MPLSConnectionInfo&page=1' \
               '&rows=1000&sort=device_TXBS_rate&order=desc '
    resp_list = requests.get(url_list)
    resp_list_json = json.loads(resp_list.text)
    rows_num = resp_list_json['total']
    url_list = 'http://10.18.2.31/cs_system/admin/Monitor/fun_network_status_json.php?act=MPLSConnectionInfo&page=1' \
               '&rows=' + rows_num + '&sort=device_TXBS_rate&order=desc '
    resp_list = requests.get(url_list)
    resp_list_json = json.loads(resp_list.text)
    node_list = resp_list_json['rows']
    print('Get ' + rows_num + ' nodes in total')
    return node_list
