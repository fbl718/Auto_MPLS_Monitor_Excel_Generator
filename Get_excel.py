# Function
# Potential bug warning: During the date switch, the date got from "datetime" may not be accurate
import datetime
import json
import requests
import sys
from Excel import Excel


def get_excel(node_list):
    filename = datetime.datetime.now().strftime('%Y-%m-%d') + ' MPLS监控.xlsx'
    colums_name = ['节点', '节点', '专线', 'CE->PE', '瞬时接收流量占比', '瞬时上传流量占比', '瞬时接收流量Mbps(RXBS)', '瞬时上传流量Mbps(TXBS)',
                   '数据接收流量MAX(Mpbs)', '数据上传流量MAX(Mpbs)', '带宽Mbps', '更新时间']
    book = Excel(filename)
    book.write_column_name(colums_name)
    row = 1
    length = node_list.__len__()
    output = sys.stdout
    print('Extracting data to "' + filename+'"')
    for node in node_list:
        url = 'http://10.18.2.31/cs_system/admin/Monitor/fun_network_status_json.php'
        url = url + '?' + 'act' + '=' + 'NetworksPerfAVGInfo' + '&perf_type=' + 'bps' + '&device_name=' + node[
            'device_name'] + '&device_host=' + node['device_host'] + '&device_port_name=' + node[
                  'device_port_name'] + '&start_date=' + datetime.datetime.now().strftime(
            '%Y-%m-%d') + '&end_date=' + datetime.datetime.now().strftime('%Y-%m-%d') + '&date_range_type=' + '5min'
        response = requests.get(url)
        resp_json = json.loads(response.text)
        rxbs_max = max(resp_json['rxbs_usage'])
        txbs_max = max(resp_json['txbs_usage'])
        node_name = node['node_name']
        rxbs = float(node['device_RXBS']) / 1000000
        txbs = float(node['device_TXBS']) / 1000000
        bandwidth = node['device_bandwidth']
        rxbs_rate = node['device_RXBS_rate'] + '%'
        txbs_rate = node['device_TXBS_rate'] + '%'
        time = node['update_time']
        data = [node_name, '', '', '', rxbs_rate, txbs_rate, rxbs, txbs, rxbs_max, txbs_max, bandwidth, time]
        firewall = node['firewall_connect_success_rate']
        router = node['router_connect_success_rate']
        device = node['device_connect_success_rate']
        if firewall == '100':
            book.insert_image(row, 1, 'ball_green.png')
        elif firewall == '0':
            book.insert_image(row, 1, 'ball_red.png')
        else:
            book.insert_image(row, 1, 'ball_yellow.png')

        if router == '100':
            book.insert_image(row, 2, 'ball_green.png')
        elif router == '0':
            book.insert_image(row, 2, 'ball_red.png')
        else:
            book.insert_image(row, 2, 'ball_yellow.png')

        if device == '100':
            book.insert_image(row, 3, 'ball_green.png')
        elif device == '0':
            book.insert_image(row, 3, 'ball_red.png')
        else:
            book.insert_image(row, 3, 'ball_yellow.png')
        book.write_content(row, data)
        output.write(f'\rNodes completed: {row}/{length}')
        output.flush()
        row = row + 1
    book.close()
    print()
    print('All MPLS data is successfully imported to "'+filename+'" in the current folder')
