# weekdays = ["Monday", "Tuesday" ,"Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print("Monday: ", weekdays.index("Monday"))
# print("Monday: ", weekdays[weekdays.index("Monday")])
# #print("Mon to Fri", weekdays[0:5])
import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_max_count():
    url = 'https://dhlottery.co.kr/common.do?method=main'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    max_count = int(soup.find('strong', id='lottoDrwNo').text)
    return max_count

print(get_max_count())

data = pd.DataFrame()