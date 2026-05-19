def ping_parser(output):
    return "0% packet loss" in output.lower()
