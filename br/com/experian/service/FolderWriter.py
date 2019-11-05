import os
import logging
from pathlib import Path
from br.com.experian.util.Cache import Cache
from shutil import copytree, ignore_patterns, move


class FolderWriter:

    def copyFolder( source, dest ):
        """Funcao utilitaria para copiar diretorios e arquivos"""
        try:
            logging.info("Copiando os diretorios de: " + source + " para: " + dest)
            copytree( source, dest, ignore=ignore_patterns('*.class', 'target*', '.git', '.settings', '.classpath', '.project',
                                                           '.gitignore', '.jenkins.yml', 'README.md' ) )
        except Exception as e:
            logging.error("Ocorreu um erro ao copiar os diretorios de: " + source + " para: " + dest )
            logging.error("Erro: " + str(e))

    def createEarModule(dest):
        """Copia o modulo ear do resources para a estrutura do projeto"""
        try:
            logging.info("Copiando diretorio ear")

            pathOfThisFile = Path(__file__).parent
            pathOfEarFolder = (pathOfThisFile / "../../../../resources/ear").resolve()
            logging.info('localizacao do diretorio ear: ' + str(pathOfEarFolder))

            FolderWriter.copyFolder(str(pathOfEarFolder), dest + '\\'+ Cache.getParameter('@artifactory-id@') +'-ear')

        except Exception as e:
            logging.error("Ocorreu um erro ao copiar os diretorios de: resources/ear para: " + dest )
            logging.error("Erro: " + str(e))

    def createWebModule( orig ):
        """Cria o modulo web, criando o diretorio artifactoryId-web e copiando os arquivos modulo principal"""
        try:
            logging.info("Copiando diretorio web")

            finalWebFolder = orig + '\\' + Cache.getParameter('@artifactory-id@') + '-web'

            arquivosNaoCopiar = set( [ '*.class', 'target*', '.git', '.settings', '.classpath', '.project',
                                       '.gitignore', '.jenkins.yml', 'README.md' ] )
            contents = set( os.listdir( orig ) )
            resul = contents.difference( arquivosNaoCopiar )

            logging.info('localizacao do diretorio web: ' + finalWebFolder )

            for f in resul:
                logging.info("Conteudo: " + orig + '\\' + f )
                move( orig + '\\' + f,
                      finalWebFolder,
                      copy_function=copytree)

        except Exception as e:
            logging.error("Ocorreu um erro ao copiar os diretorios de: " + orig + " para: " + finalWebFolder)
            logging.error("Erro: " + str(e))
