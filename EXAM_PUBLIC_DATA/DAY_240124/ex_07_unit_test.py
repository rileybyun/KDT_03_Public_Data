"""
- 단위 테스트 : 소스 코드의 특정 모듈이 의도한 대로 정확히 작동하는지 검증하는 절차
이 소스코드는 ex_08의 단위 테스트 코드이다.
문자열 분리 : split('구분자')
"""

date_string1 = '2024 01 01'
# 공백을 기준으로 분리
print(date_string1.split())

# 구분자:'-' 기준으로 분리
date_string2 = '2023-12-31'
split_date_string = date_string2.split('-')
print(split_date_string)

year = split_date_string[0]
month = split_date_string[1]
day = split_date_string[2]

print(f'연도:{year}, 월:{month}, 일:{day}')
