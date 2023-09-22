#콜백함수
def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func)

