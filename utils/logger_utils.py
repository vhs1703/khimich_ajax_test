import logging

loggers = {}

def get_logger():
    global loggers
    if loggers.get('name'):
        return loggers.get('name')
    else:
        logger = logging.getLogger('log')
        logger.setLevel(logging.INFO)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Set the formatter for the console handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S%p')
        console_handler.setFormatter(formatter)

        # Add the console handler to the logger
        logger.addHandler(console_handler)
        loggers['name'] = logger

        return logger