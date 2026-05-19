from parsers.ospf_parser import parse_ospf
from validators.ospf_validator import ospf_validator

from utils.logger import get_logger
from utils.retry import retry

logger = get_logger("OSPF_TEST")

@retry(max_attempts = 3, delay=2)
def run_ospf_validation(output):
    logger.info("Parsing OSPF output")
    
    parsed = parse_ospf(output)
    
    logger.info(f'Parsed neighbors: {parsed}')
    
    result = ospf_validator(parsed)
    
    logger.info(f'Validation Result: {result}')
    
    return result
    
def test_ospf():
    logger.info("===== STARTING OSPF TEST")
    
    ospf_output = """
    10.1.1.2 1 FULL/DR 192.168.1.2
    10.1.1.3 1 FULL/BDR 192.168.1.3
    """
    assert run_ospf_validation(ospf_output)
    
    logger.info("===== OSPF TEST PASSED =====")
