import logging

def get_logger(name="network_framework"):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:

        file_handler = logging.FileHandler("framework.log")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger