def ospf_validator(neighbors):
    for n in neighbors:
        if "FULL" not in n["state"]:
            return False
    return True
