# 주민번호로 인적사항 판별하기
# 정보 뽑아내기

print("주민등록 번호 분석기 프로그램입니다!")

resident_number = input("주민번호를 입력해 주세요 :\n")

# 생년월일 탐색
birth_year = resident_number[0:2]
birth_month = resident_number[2:4]
birth_day = resident_number[4:6]
sex = resident_number[6]

# 성별 비교하기
# 조건문을 가지고 성별을 비교 합니다.
if sex == '1' or sex == '3':
    sex = '남자'
elif sex == '2' or sex == '4':
    sex = '여자'
else:
    sex = '중성'

# 주민번호로부터 정보 출력
print("\n생년월일 : {0}년 {1}월 {2}일".format(birth_year, birth_month, birth_day))
print("성별 : {0}".format(sex))
