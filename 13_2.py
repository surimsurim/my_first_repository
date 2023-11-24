"""#rank매기기
import pandas as pd
df["aver"] = df.postcode.rank(method="average")
print(df[["postcode", "aver"]])"""

""""df["min"] = df.postcode.rank(method="min")
print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "aver"]])""""

"""#컬럼 로우 변경
print(df.transpose())"""

"""#누적 계산
print(df["postcode"].expanding().sum())
print(df["postcode"].expanding().max())"""

"""#내림차순 기준
print(df.postcode.idxmax(axis=0))
print(df.postcode.idxmin(axis=0))"""
"""
print(df.empty)
print(df.postcode.empty)
#empty 추가
print(df.empty)
print(df.case.empty)"""

"""#검색
print(df.isin[78742])
print(df.isin["장성호"])
print(df.isin[78742, 12843])
print(df.isin[78742, 12843. "장성호"])"""
"""
#기간 계산
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.Dataframe(data=df, index=idx)
print(pf)"""

"""#인덱스 시간 - 간격 생성
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n--------------------\n")
#득정 시간 찾기
print(df.at_time("09:00"))
print(df.at_time("03:00"))

#시간 범위 출력
print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="03:00", end_time="09:00"))"""

"""#x일 간격 생성 - 기간별 찾기
i = pd.date_range("2023-11-10", periods=10, freq="3D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)
print(df.first("3D"))
print(df.first("7D"))"""

"""#pip instal Finance-DataReader
import Finance-DataReader as fdr
ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n-------------\n")"""

"""#최고가
res = ksp["High"].max()
print(res)

res = ksp["High"].idxmax()
print(res)

#최저가
res = ksp["Low"].min()
print(res)

#최고가
res = ksp["Volume"].nlargest(n=5)
print(res)
#최저가
res = ksp["Volume"].nsmallest(n=5)
res = ksp["Close"].nsmallest(n=5)
print(res)
"""
"""#3000최초일
cond = ksp["Close"] >= 3000
res = ksp[cond].index[0]
print(res)

ksp["Volume"] > ksp["Volume"].shift()
print(res)"""

"""#위 값 참조 처리
ksp["Volume"] > ksp["Volume"].shift()
print(ksp)"""

"""res = ksp["up"] != ksp["up"].shift().cumsum()
print(res)

ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)"""

"""#연속 증가값 확인
ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1    
print(ksp)

print(ksp["up_cnt"].max())"""

"""import pandas as pd
target = "./data/apt.csv"
df = pd.read_csv(target, encoding='CP949')
df.to_csv("./data/apt.csv", encoding='utf8')
print(df.head())"""

"""import pandas as pd
df = pd.read_csv(". /data/conv_apt.csv", )
print(df.haed())"""

"""df.rename(columns={"분양가격(제곱미터)":"분양가"})
print(df)
print(df.dtypes)
df = df["분양가"].convert_dtypes()
print(df.dtypes)

arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr))"""

"""print(df.describe())
print(df.transpose())
print("\n-------------\n")
df.T.head()"""