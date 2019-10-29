from br.com.experian.util.Cache import Cache
from xml.etree.ElementTree import ElementTree
from pathlib import Path
import xml.etree.ElementTree as ET
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

    def correctEarPom( outputFolder ):

        earPomLocation = outputFolder + '\\' + Cache.getParameter('@artifactory-id@') + '-ear\\pom.xml'
        logging.debug("Localizacao do earPomLocation: " + str(earPomLocation) )

        fin = open( earPomLocation, "rt")
        data = fin.read()
        data = Writer.__replaceParameters( data )
        fin.close()

        fin = open( earPomLocation, "wt")
        fin.write( data )
        fin.close()

    def correctWebPom( outputFolder ):

        ns = {'maven': 'http://maven.apache.org/POM/4.0.0',
              'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

        ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")
        ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")

        webPom = outputFolder + '\\' + Cache.getParameter('@artifactory-id@') + '-web\\pom.xml'
        logging.info("Localizacao do webPomLocation: " + str( webPom ))

        tree = ElementTree()

        tree.parse( webPom )
        root = tree.getroot()

        root.find('maven:artifactId', ns ).text = Cache.getParameter('@artifactory-id@') + '-web'
        root.find('maven:version', ns ).text = Cache.getParameter('@version@')

        root.find('maven:parent', ns ).find('maven:artifactId', ns).text = Cache.getParameter('@artifactory-id@')
        root.find('maven:parent', ns ).find('maven:version', ns).text = '${custom.project.version}'

        scm = root.find('maven:scm', ns )
        root.remove( scm )

        tree.write( webPom )


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
