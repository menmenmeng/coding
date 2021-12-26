# 사칙연산 클래스
# 클래스 상속
# 메소드 오버라이딩(SafeFourCal) : ZeroDivisionError를 방지하는 FourCal
# 클래스 변수(!=객체 변수)

# 사칙연산 클래스
class FourCal:
    def __init__(self):
        self.result = 0

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        self.result = self.first + self.second
        return self.result

    def sub(self):
        self.result = self.first - self.second
        return self.result
    
    def mul(self):
        self.result = self.first * self.second
        return self.result

    def div(self):
        self.result = self.first / self.second
        return self.result
        


# 클래스 상속 : FourCal의 모든 메소드가 여기에 이미 다 들어있다고 볼 수 있음
class MoreFourCal(FourCal):
    def pow(self):
        self.result = self.first ** self.second
        return self.result

print("--클래스 상속")
a = MoreFourCal()
a.setdata(4, 2)
print(a.add())
print(a.pow())


# 클래스 메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

print('--메소드 오버라이딩')
b = SafeFourCal()
b.setdata(4, 0)
print(b.div())
b.setdata(4, 2)
print(b.div())


# 모든 클래스 인스턴스에 적용되는, 클래스 변수 (객체변수와 다름)
class Family:
    lastname = '김'

print('--클래스 변수')
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = '박'
print(a.lastname)
print(b.lastname)