import csv

def getDataFromFile():
    fileLocation = "C:\\Users\\Aimbere Galdino\\PycharmProjects\\MachineLearningStudy\\resources\\pharmaceutical-drug-spending.csv"

    lista = []

    with open( fileLocation, 'r') as csvFile:
        reader = csv.DictReader( csvFile )
        for row in reader:
            data = pharm.buildFromCsv(row)
            lista.append( data )

    return lista
