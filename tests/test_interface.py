from parsers.interface_parser import parse_interfaces
from validators.interface_validator import validate_interfaces

def test_interface():
    output = """
    g0/0 up up
    g0/1 up up
    """
    
    parsed = parse_interfaces(output)
    assert validate_interfaces(parsed)