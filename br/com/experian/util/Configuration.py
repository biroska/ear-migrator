import logging

class Configuration:
    """Classe utilitaria para configurar o arquivo de logging"""

    @staticmethod
    def initialize():
        logging.basicConfig(level=logging.INFO)