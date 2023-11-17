"""#dataframe
import pandas as pd
df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)
print("\n------------------\n")
print(df[1])
print("\n------------------\n")
print(df[1][1])
print("\n------------------\n")"""

"""#dictionary
import pandas as pd
data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)
print(fr)
print(fr["x"])
print(fr.x)
print(fr.iloc[2])
print(fr.loc["y축"])"""

"""#열 추가
frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
print(frs)
print("\n------------------\n")
frs["t"] = [60, 120, 180]
print(frs)
print("\n------------------\n")"""
"""
#행추가
frs.loc["t축"] = [100, 200, 300, 400]
print(frs)"""

"""#행수정
print("\n------------------\n")
frs.loc["t축"] = [500, 600, 700, 800]
print(frs)

#행 삭제
frs.drop("x", axis=1, inplace=True)
print(frs)

# 열 삭제
frs.drop("x축", inplace=True)
print(frs)"""

"""#컬럼
dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

df = pd.DataFrame(data=dt,index=row,columns=col)
print(df)
print(["x"])
print("\n------------------\n")"""

"""# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])
print(df2)
print(df.div(df2))
print(df.div(df2,fill_value=100))"""

"""import pandas as pd
dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["col1", "col2", "col3"]
idx = ["row1", "row2", "row3"]
df = pd.DataFrame(data=dt, index=idx, coloums=col)
print(df)
print("\n------------------\n")
print(df.loc("현대"))"""

"""# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])
print(df2)
print("\n------------------\n")
print(df.mul(df2))
print("\n------------------\n")
print(df.div(df2,fill_value=100))"""

#멀티인덱스
"""idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)
print(df)
print("\n------------------\n")
print(df.loc("row3"))
print(df.iloc[0])
print("\n------------------\n")
print(df.loc("row3", "val3"))
print("\n------------------\n")
print(df.loc("row3", "val2", "col1"))"""

"""#랜덤 데이터 생성
import pandas as pd
import numpy as np

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(data=dt)
print(df)
print("\n------------------\n")
print(df[2])

print("\n------------------\n")
print(df.loc[2])

print("\n------------------\n")
print(df.loc[3][1])

print("\n------------------\n")
print(df.head(3))

print("\n------------------\n")
print(df.tall(2))

print("\n------------------\n")
print(df.sample())"""

"""#파일생성
import faker import Faker as fk
import os
fk("ko-KR")
print(temp.name())
folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
    for i in range(30) :
			f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
   """
"""#파일열기
import pandas as pd
folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
print(df)"""

"""#print(type(df))
print("\n------------------\n")
print(df.head())
print("\n------------------\n")

print(df.head(3))
print("\n------------------\n")

print(df.tall())
print("\n------------------\n")

print(df.tall(3))
print("\n------------------\n")

print(df.sample())
print(df.sample(4))"""

"""#인덱스 설정 확인
print(df.index)
print(type(df))

print(df.values)
print("\n------------------\n")

for el in df.values[0] :
    print(el)

    
print(df.info())
df.isnull()
df.isnull().sum()

print(df["name"])
print(df["color"])
print(df["postcode"])
print(df["phone"])
print(df["id"])
print(df["company"])

print(df[["name", "id"]])
post = df[["name", "address", "postcode"]]
print(post)

print(df.postcode.describe())
print(df.color.describe)
print(df.color.count())
df.color.value_counts()"""
"""
temp = df.postcode.sum()
print(temp)

dprint(df.name == "이민석")
temp = df[df.color == "Ivory"].head(1)"""