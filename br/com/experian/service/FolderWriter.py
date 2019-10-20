from shutil import copytree, ignore_patterns
import logging


class FolderWriter:

    def copyFolder( source, dest ):
        try:
            logging.info("Copiando os diretorios de: " + source + " para: " + dest)
            copytree( source, dest, ignore=ignore_patterns('*.class', 'target*') )
        except Exception as e:
            logging.error("Ocorreu um erro ao copiar os diretorios de: " + source + " para: " + dest )
            logging.error("Erro: " + str(e))
