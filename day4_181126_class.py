## class는 노가다를 줄여준다. 엄청 좋은데?

class pre_iqs:
    salesmonth = 1
    reportmonth=salesmonth+3
    Brand = "H,K,G"

##init에는 내용을 넣어줘야 클래스가 실행된다
    def __init__(self,h_num,k_num,g_num):
        self.h_num=h_num
        self.k_num=k_num
        self.g_num=g_num

    def month(self):
            self.salesmonth=self.salesmonth+1
            self.reportmonth = self.salesmonth+3



pre_iqs1= pre_iqs(17,18,13)
print(pre_iqs1.salesmonth,pre_iqs1.reportmonth,pre_iqs1.Brand,pre_iqs1.h_num,pre_iqs1.k_num,pre_iqs1.g_num,"models")

pre_iqs1.month()
print(pre_iqs1.salesmonth,pre_iqs1.reportmonth,pre_iqs1.Brand,pre_iqs1.h_num,pre_iqs1.k_num,pre_iqs1.g_num)


##상속을 시켜볼까
class pre_vds(pre_iqs) :
    vds="Vehicle Dependability Study"
    def month(self) :
        self.reportmonth = self.salesmonth+36

prevds=pre_vds(1,2,3)
print(prevds.salesmonth, prevds.reportmonth,prevds.Brand,prevds.h_num,"models")

prevds.month()
print(prevds.salesmonth, prevds.reportmonth//12,"year",prevds.reportmonth%12,"month",prevds.Brand,prevds.h_num,"models")
