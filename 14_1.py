"""import pandas as pd

df = pd.read_csv("./data/apt.csv", index_col=0)

df = df.rename(colums={"분양가격(제곱미터)":"분양가"})
df["분양가"] = df["분양가"].convert_dtypes()
print(df.dtypes)
print("\n----------------")
"""
"""정렬
res = df.sort_values(by="연도")
res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[10:20]
print(res)
print(res.head())"""
"""
#칼럼 이름 출력
res = df["지역명"][:5]
res = df["지역명", "연도"]
res = df["지역명", "연도", "분양가"]
res = df["지역명", "연도", "분양가"][:7]
res = df[["지역명", "연도"]][:5]
print(res)"""
"""
print("\n----------------\n")
res = df.loc[:, ["지역명", "연도", "분양가"]][:5]
res = df.loc[:][:5]
res = df.loc[:][:]
res = df.iloc[1]
print(res)"""

"""res = df.loc[:6, ["지역명", "얀도"]]
res = df.loc[:6, ["지역명", "얀도"]][:3]
res = df.loc[:6, ["지역명", "얀도"]][:7]
print(res)"""
"""
res = df.loc[df["지역명"]=="강원"]
res = df.loc[df["연도"] > 2020]
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:]
print(res)"""

"""df0 = df.copy()
print(df0)

res = df.iloc[2]
res = df.iloc[2][2]
print(res)

res = df[df.index > 3560]
print(res)"""

"""res = df[df.연도 == 2023]
res = df[df.월 == 3]
print(res)

res = df[(df.연도 == 2023) & (df.지역명 == "서울")]
res = df[(df.연도 == 2023)` & (df.지역명 == "서울") & (df.월 == 6)]
print(res)
"""
"""
columns = list(df.cloumns)
print(columns + '컬럼')
df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
df1 = df.reindex(columns=list(df.columns) + ["extra"])
print(df)
print("\n----------------\n")
print(df1)
"""

"""print("\n----------------\n")
df1.loc[:6, "extra"] = "0"
df1.loc[:4, "extra"] = False
print(df1)

#복사
df2 = df1.copy()

res = df2.dropna(how="any")
df1.fillna(value="1234")
print(res)
res = df2.fillna(how="any", inolac=True)
print(df2)
print("\n----------------\n")
res = df2.dropna(how="any", inolac=True)
print(res)
print("\n----------------\n")
print(df2)"""

"""res = pd.isna(df1)
res = pd.isna(df)
res = pd.isna(df0)
res = pd.isna(df2)
print(res)"""
"""
res = df["연도"].value_counts()
res = df["지역명"].value_counts()
res = df["월"].value_counts()
print(res)"""
"""
res = df.groupby(["지역명", "연도", "월"]).sum()
print(res)
res = df.groupby(["지역명", "연도", "월"]).all()
res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")"""