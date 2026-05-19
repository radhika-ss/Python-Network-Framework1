def validate_interfaces(interfaces):
    for i in interfaces:
        if i["status"] != "up":
            return False
    return True
