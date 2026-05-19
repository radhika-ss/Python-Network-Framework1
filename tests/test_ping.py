from parsers.ping_parser import ping_parser
from validators.ping_validator import ping_validator

def test_ping():
    output = "0% packet loss"

    result = ping_parser(output)
    
    assert ping_validator(result)
