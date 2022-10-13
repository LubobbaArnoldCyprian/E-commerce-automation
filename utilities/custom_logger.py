import logging


class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        # Incase you're using Mac-Os use command below
        # logging.basicConfig(filename="../logs/tests.log", format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m'
        #                                                                                                           '/%d/%y %H:%M:%S %p')

        logging.basicConfig(filename=".\\logs\\tests.log", format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m'
                                                                                                                 '/%d/%y %H:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger