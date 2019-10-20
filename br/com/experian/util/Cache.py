import logging


class Cache:

    parameters = {}

    @staticmethod
    def addParameter( key, value):
        """ addParameter adds a value into the parameter cache
            Returns: True if suceed or False otherwise
        """

        try:
            Cache.parameters[ key ] = value

            logging.debug("Incluido o valor: " + value + " com a chave: " + key + " no cache.")
            return True
        except Exception as e:
            logging.error("Ocorreu um erro ao inserir o valor: " + value + " com a chave: " + key + " no cache.")
            logging.error("Erro: " + str( e ) )
            return False

    @staticmethod
    def getParameter( key ):
        """ getParameter gets the value vinculated with the inputed key
            Returns: The value vinculated with the inputed key
        """

        value = ""

        try:
            value = Cache.parameters[ key ]

            logging.debug("Encontrado o valor: " + value + " com a key: " + key )
            return value
        except Exception as e:
            logging.error("Ocorreu ao buscar o valor: " + value + " com a chave: " + key + " no cache.")
            logging.error("Erro: " + str( e ) )