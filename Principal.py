from br.com.experian.service.FolderWriter import FolderWriter
from br.com.experian.util.Cache import Cache
from br.com.experian.service.FileWriter import Writer
from br.com.experian.util.Configuration import Configuration
import logging


def inputUserParameters():
    artifactory = input("Forneca o artifactory id: ")
    version = input("Forneca a versao: ")
    application = input("Forneca o nome da aplicacao: ")
    outputFolder = input("Forneca o diretorio para a migraca do projeto: ")

    if ( outputFolder == '' ):
        logging.info('Utilizando o diretorio c:\\Temp para a migracao do projeto')
        outputFolder = 'C:\\Temp\\Copiados'

    Cache.addParameter('@version@', version )
    Cache.addParameter('@outputFolder@', outputFolder )
    Cache.addParameter('@artifactory-id@', artifactory )
    Cache.addParameter('@application-name@', application )

    Cache.getParameter('@outputFolder@')
    Cache.getParameter( '@version@' )
    Cache.getParameter( '@artifactory-id@' )
    Cache.getParameter( '@application-name@' )


def executarAplicativo():
    Configuration.initialize()

    inputUserParameters()

    logging.info("iniciando copia do web")
    FolderWriter.createWebModule(Cache.getParameter('@outputFolder@'))

    logging.info("Copiando o parent pom")
    FolderWriter.createEarModule(Cache.getParameter('@outputFolder@'))

    Writer.writeParentPom( Cache.getParameter('@outputFolder@') )
    logging.info("iniciando copia do ear")

    logging.info("Execucao concluida com sucesso!")


executarAplicativo()

# Configuration.initialize()
#
# logging.info('parentPomPath: ' + str( parentPomPath ) )
# logging.info('parentPomPath: ' + str( parentPomPath ) )
# print( 'pathOfThisFile ' + str( pathOfThisFile )  )
