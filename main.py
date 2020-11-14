import os
from Get_excel import get_excel
from Get_node_list import get_node_list
from Auto_login import auto_login

print('#####Auto MPLS Monitor Excel Generator#####')
print('Proudly presented by Fang Baole')
print('Version 1.0 Updated on 2019/12/19')
print()

if os.path.exists('ball_green.png') & os.path.exists('ball_yellow.png') & os.path.exists('ball_red.png'):
    auto_login()
    get_excel(get_node_list())
else:
    print('Error: Image elements are missing. Please put them in the current directory.')

print()
input('Press Enter to quit')
