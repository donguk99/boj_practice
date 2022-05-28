# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

case_num = int(input())
for i in range(case_num):
    l = list(map(int, input().split()))
    mean = sum(l[1:])/l[0]
    over_avr = 0
    for i in range(1, len(l)):
        if l[i] > mean:
            over_avr += 1
    print(format(over_avr/l[0]*100, '.3f')+'%')