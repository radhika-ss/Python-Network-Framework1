import re

def parse_interfaces(output):
    interfaces = []
    
    for line in output.splitlines():
        if 'up' in line.lower() or 'down' in line.lower():
            parts = line.split()
            interfaces.append({
                "interface": parts[0],
                "status": parts[1]
            })   
    return interfaces
  