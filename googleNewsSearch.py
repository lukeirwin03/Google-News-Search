from GoogleNews import GoogleNews
import datetime
from time import sleep
import csv
import pandas as pd

partnerList = ['Conagra Nebraska', 'Gallup Nebraska', 'Nebraska Tech Collaborative']
today = datetime.date.today()
endDay = today.strftime('%m/%d/%Y')
startDay = (today - datetime.timedelta(days=5)).strftime('%m/%d/%Y')


def main():
    createDataFrame(getData(partnerList))


def getData(partnerList):
    global startDay, endDay
    print(f'Start Date: {startDay}\nEnd Date: {endDay}')
    news = GoogleNews(lang='en', region='US', start=startDay, end=endDay)

    linkList = []
    resultsInPastWeek = []

    for partner in partnerList:
        articleLinks = []

        news.search(partner)
        results = news.results()
        numResults = len(results)
        resultsInPastWeek.append(len(results))
        news.clear()
        sleep(1)

        print(f'{partner}:   ')

        for i in range(5):
            if(len(results) > i):
                result = results[i]
                print(result['title'] + '\t' + result['date'])
                articleLinks.append({result['title']: result['link']})
        print('Total Results in the Last Week: ' + str(numResults) + '\n')

        linkList.append(articleLinks)

    masterDict = {'Partner': partnerList, 'Articles': linkList, 'Articles in Past Week': resultsInPastWeek}
    return masterDict

def createDataFrame(masterDict):
    df = pd.DataFrame(masterDict)
    print(df)

def createPartnerList(file):
    with open(file, 'r', newline='') as f:
        partnerList = []
        lineCounter = 0
        csv_reader = csv.reader(f, delimiter=':')
        for row in csv_reader:
            pass




if __name__ == '__main__':
    main()