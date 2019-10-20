from br.com.experian.util.Cache import Cache
from pathlib import Path
import logging


class Writer:

    def writeParentPom(outputFolder):
        pathOfThisFile = Path(__file__).parent

        parentPomPath = (pathOfThisFile / "../../../../resources/parent-pom.xml").resolve()
        logging.debug("Localizacao do parent-pom: " + str(parentPomPath))

        outputPom = outputFolder + '\pom.xml'
        logging.debug("Parent pom a ser gerado: " + outputPom)

        fin = open( parentPomPath, "rt")
        data = fin.read()
        data = Writer.__replaceParameters( data )
        fin.close()

        fin = open( outputPom, "wt")
        fin.write( data )
        fin.close()

    def writeParentPom_OLD( outputFolder ):

        pathOfThisFile = Path(__file__).parent

        parentPomPath = (pathOfThisFile / "../../../../resources/parent-pom.xml").resolve()
        logging.debug("Localizacao do parent-pom: " + str(parentPomPath))

        outputPom = outputFolder +'\pom.xml'
        logging.debug("Parent pom a ser gerado: " + outputPom )

        fileWrite = open( outputPom, 'w')

        with open(parentPomPath, 'r') as parentPom:
            reader = parentPom
            for row in reader:
                fileWrite.write( Writer.__replaceParameters( row ) )

        fileWrite.close()

    def __replaceParameters( row ):
        retorno = row

        retorno = str( retorno ).replace('@version@', Cache.getParameter('@version@') )
        retorno = str( retorno ).replace('@artifactory-id@', Cache.getParameter('@artifactory-id@') )
        retorno = str( retorno ).replace('@application-name@', Cache.getParameter('@application-name@') )

        return retorno
