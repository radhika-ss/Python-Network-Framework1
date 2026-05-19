'''
ospf_output =
Neighbor ID     Pri   State           Dead Time   Address
10.1.1.2        1     FULL/DR         00:00:33    192.168.1.2
10.1.1.3        1     FULL/BDR        00:00:31    192.168.1.3

'''




import re

def parse_ospf(output):

    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+\d+\s+(FULL|INIT|2WAY|LOADING|FULL/DR|FULL/BDR)"
    matches = re.findall(pattern, output)
    
    return [{'neighbor': ip, 'state': state} for ip, state in matches]
