"""import matplotlib.pyplot as plt

#다중그래프
# 사용데이터
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

plt.subplot(2, 1, 1)    # 1set
plt.subplot(1, 2, 1)   
plt.subplot(3, 1, 1)   
plt.subplot(2, 2, 1)   
plt.plot(x1, y1, "o-")


plt.title("x1.graph")
plt.xlabel("x.data")
plt.ylabel("y.data")


plt.subplot(2, 1, 2)
plt.subplot(1, 2, 2)   
plt.subplot(2, 1, 1)   
plt.subplot(2, 2, 2) 
plt.plot(x2, y2, ".-")

plt.style.use("ggplt")
plt.style.use("bmh")
plt.style.use("classic")

plt.title("x2.graph")
plt.xlabel("x2.data")
plt.ylabel("y2.data")

plt.show()

plt.subplot(2, 2, 1)
plt.subplot(2, 2, 4)

#스타일 지정
plt.style.use("Solarize_light2")
plt.tight_layout()

#결과 이미지 저장
plt.savefig("data/img.jpg")
plt.savefig("data/img.png")
plt.show()
"""
"""#다중 막대그래프 만들기
x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.bar(x_years, y_data)
ax2.bar(x_years, y_data)
ax3.bar(x_years, y_data)
ax4.bar(x_years, y_data)
plt.tight_layout()

ax1.bar(x_years, y_data, color= "aquamaine", edgecolor= "black", hatch= "/")
ax2.bar(x_years, y_data, color="slamon", edgecolor="black", hatch= "\\")
ax3.bar(x_years, y_data, color="navajowhite", edgecolor="black", hatch= "+")
ax4.bar(x_years, y_data, color="lightskyblue", edgecolor="black", hatch= "*")"""



"""import seaborn as sns
import pandas as pd
import FinanceDataReader as fdr
#pip install plotly
tips = sns.load_dataset("tips")
print(tips)
#plt.figure(figsize=(10,6))

sns.barplot(x="day", y="tip", data=tips)
sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
sns.barplot(x="tip", y="total_bill", data=tips)
sns.barplot(x="sex", y="total_bill", data=tips)
sns.barplot(x="sex", y="tip", data=tips)
sns.barplot(x="smoker", y="total_bill", data=tips)
sns.barplot(x="smoker", y="tip", data=tips)
sns.barplot(x="time", y="total_bill", data=tips)

plt.show()

plt.title("Average Tips")
plt.xlabel("x")"""
"""

#타이타닉 데이터
titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)
plt.show()


# 탑승클래스별 인원구성
sns.countplot(x="class", hue="who", data=titanic)

# 클래스별 생존자
sns.countplot(x="class", hue="alive", data=titanic)

# 성별별 생존자
sns.countplot(x="sex", hue="alive", data=titanic)

# 싱글 여행자별 인원구성
sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별
sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)

plt.show()"""

"""#주식
import FinanceDataReader as fdr

df = fdr.DataReader("KS11")
df0 = df.loc["2023"]
print(df0)

df0["Open"].plot()
df0["High"].plot()
df0["Low"].plot()
df0["Close"].plot()

plt.grid(True)
plt.show()

#다우지수와 코스피 비교
dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# 각 지수별 종가 기준 그래프 출력
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

plt.grid(True)

d = (dow.Close / dow.Close.loc["2010-06-01")]) * 100
k = (kospi.Close / kospi.Close.loc["2010-06-01")]) * 100
kospi = fdr.DataReader("KS11", "2010-06-01")

#국내 개별 종목 분석
# 해당 데이터를 가져오는 URL
# code 는 종목명
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/item/sise_day.nhn?code=005930

res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)

"""
""""
#페이지 수 동적으로 결정
page = 1
for page in range(1, 10):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break
print(df_list)
"""

"""
#리스트에 담긴 DataFrame을 한 번에 해결
df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.plot(df["날짜"], df["종가"], "co-")

#nasdaq
pip install yfinance
import yfinance as yf

#MS
ticker = "MSFT"

# Apple
ticker = "APPL"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

#시각화
plt.figure(figure(12, 6))
plt.plot(data["Close"], label="Close Price")

#평균 계산
# 50일 평균
data["MA_50"] = data["Close"].rolling(window=50).mean()

# 200일 평균
data["MA_200"] = data["Close"].rolling(window=200).mean()

#웹 페이지에서 데이터 수집
url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#국가 및 인구 데이터 추출
countries = []
populations = []
rows = soup.select("#example2 tbody tr")
for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))
    
    countries.append(country)
    populations.append(population)

#상위 10개 국가 시각화
top_countries = countries[:10]
top_populations = populations[:10]
plt.figure(figsize=(12, 6))
plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show()
"""