"""#선스타일 설정
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", ".", label="PData(km)")


#선스타일 지정
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
plt.xlabel("x축")
plt.ylabel("y축")"""
"""
# linestyle(0, (픽셀크기, 여백간격))
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (4, 2)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (10, 0)), label="PData(km)")

#문자열 색 지정
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")

#모양 설정
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
# plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)"

#마커 지정
plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

#마커  선 동시 설정
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")

#marker 파라메터 사용
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")

#그래프 영역 채우기
xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, ydata)
plt.xlabel("x_data")
plt.ylabel("y_data")

#세로 축 채우기
plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

#가로 축 세우기
plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

#두선간의 영역 채우기
plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
plt.fill_between(xdata[1:4], ydata[1:3], y1data[1:3], alpha=0.5)
plt.fill_between(xdata[1:4], ydata[:4], y1data[:4], alpha=0.5)

#범위 지정 영역 채우기
plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 7.1], [0.5, 2.5, 2.5, 4.1], alpha=0.5)
plt.show()

#배경 그리드 변경
plt.grid()
plt.show()

# x축 그리드
plt.grid(axis="x")

# y축 그리드
plt.grid(axis="y")

# 색상 설정
plt.grid(axis="y", color="g")
plt.grid(axis="y", color="b")

# 투명도 설정
plt.grid(axis="y", color="g", alpha=0.5)
plt.grid(axis="y", color="g", alpha=0.5)

# 선 종류 선택
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
plt.grid(axis="x", color="r", alpha=0.3, linestyle="--")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")
"""
"""#눈금 표시
plt.xticks()
plt.yticks()

# 임의 데이터 지정
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])

# 라벨 지정
plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 눈금 안쪽/바깥쪽 지
plt.tick_params(axis="x", direction="in")

#막대 그래프 그리기
x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

plt.bar(x_years, y_data)
plt.show()

#색지정
plt.bar(x_years, y_data, color="g")
plt.bar(x_years, y_data, color="C7")
plt.bar(x_years, y_data, color="#57320")

#개별 색 지정
plt.bar(x_years, y_data, color=clr)

#막대 너비 설정
plt.bar(x_years, y_data, color=clr, width=2)
plt.bar(x_years, y_data, color=clr, width=0.5)
plt.bar(x_years, y_data, color=clr, width=0.1)

#막대 위치 선정
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", width=0.3)

#막대 테두리 설정
# 라인 색 선택
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)

# 테두리 라인 설정
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="C3", linewidth=3, width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)

#축 지표 설정
plt.xticks(x_years)
plt.yticks(y_data, y_data)
plt.ytriks([100, 200, 300, 400, 500, 900])

#수평 그래프 그리기
plt.barh(x_years, y_data)

#그래프 설정
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)
plt.show()"""