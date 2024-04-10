# -*- coding: utf-8 -*-
"""python_04_list_dictionary.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AKGrAiFuLUYL_j5PDtN_V_mWU2qoNTUl

리스트
- 리스트 정의, 추가, 삭제
"""

# 리스트는 여러 개의 데이터를 하나의 변수로 묶어 정의하는 컬렉션 데이터 타입이다.

# 빈 리스트 정의
list_a = []
print(list_a)

# 단일 데이터 타입 정의
list_b = [1,2,3,4] # 숫자
print(list_b)

# 혼합 데이터 타입 정의
list_c = ['21', '푸바우', 3, 3.14, '강아지'] # 숫자, 문자
print(list_c)

# 리스트 추가 (append)
# >> 리스트의 맨 뒤에 값 추가

list_c.append(10)
print(list_c)

# 삽입 insert()
# 리스트는 순서가 있음(indexing)
# 리스트의 특정 위치에 값을 추가

print(list_b)
list_b.insert(2, 10)
print(list_b)

print(list_c)
list_c.insert(2, 3)
print(list_c)

# 리스트의 값 제거 (remove, del)

# remove
print(list_c)
list_c.remove(3)
print(list_c)
# 3이 한 개 사라짐. remove는 데이터를 하나씩 사라지게 함

list_c.remove(3)
print(list_c)

# del
# del (=delete) 데이터를 직접 지명해 주는 게 아니라, 위치로 삭제할 데이터를 알려줌

print(list_b)
del list_b[2]

print(list_b)

"""리스트의 접근
- 인덱싱: 위치(숫자)로 리스트의 값을 가져옴
- 슬라이싱: 전체 리스트를 일부 잘라서 가져옴
"""

list_f = [1,3,5,7,9]

# indexing
# 파이썬 인덱스 시작 0부터 시작
list_f[3]

# 슬라이싱(slicing)
print(list_f[1:3])
print(list_f[2:])
print(list_f[:3])
print(list_f[:-1]) ## 빈번하게 사용
print(list_f[::2]) # 건너뛰기

"""리스트의 함수"""

n_list = [2,4,6,8,10]

# len() : length 줄임. 리스트의 크기(길이) 알려줌
len(n_list)

# index : 요소가 들어가 있는 데이터 위치 반환
print(n_list.index(2))
print(n_list.index(10))

raw_data = ["황선홍", "이강인", "손흥민","조현우"]

team_korea = raw_data.copy()

# index() 해당 값의 위치 정보 알고자 함

print(team_korea.index('손흥민'))
print(team_korea.index('이강인'))

#print(team_korea.index('카리나'))
#ValueError: '카리나' is not in list

# pop : 팝팝! 튀는 것처럼 프링글스 생각해봐요
# 뒤에서부터 리스트 값을 하나씩 빼
print(team_korea.pop())

team_korea

캡틴 = team_korea.pop()

캡틴

team_korea

# sort : 정렬(default(기본값): 오름차순 )
n_list

n_list.sort()

n_list

print(raw_data)
mod_dat = raw_data.copy()
mod_dat.sort() # mod_dat 정렬 후 변경이 됨
# a,b,c, 가나다 순

raw_data

mod_dat

# sort(), sorted() 함수 비교
# sort(): 정렬된 리스트 보여줌
# sorted(): 원래 리스트를 수정하지 않음
# >> 정렬된 리스트가 필요해서 새 리스트에 넣고자 할 때
sorted_data = sorted(raw_data)
print(sorted_data)

raw_data

# 역순 정렬
n_list.reverse()

n_list

"""딕셔너리
- 딕셔너리의 정의, 추가, 삭제 접근
"""

dict_a = {}
dict_b = {"A":1, "B":"Baby", 3:3.14, 4:"four"}
# 여러 데이터 타입을 섞을 수 있음 >> 컬렉션 타입
dict_c = {'flower':['진달래','개나리','목련']}

# 추가
# >> key-value 쌍을 명시해 주어야 함
# 딕셔너리는 순서가 없음

dict_a['감탄사'] = 'wow'

print(dict_a)

# 접근 : 반드시 'key'로 접근한다.
print(dict_a['감탄사'])

# print(dict_a['wow'])
# KeyError: 'wow'

# 삭제 : key를 전달해 준다.
del dict_a['감탄사']
print(dict_a)

# 딕셔너리(dictionary) 함수

# keys: 딕셔너리의 key만 보여줌
print(dict_b)
print(dict_b.keys())

# values : 딕셔너리의 값(value)만 보여줌
dict_b.values()

# items (제일 많이 보게될거예요)
# tuple 형태로 key-value 쌍으로 짝지어 전달함

dict_b.items()

# get : key 를 전달하여 값을 가져옴

dict_b.get(3)

dict_b.get(7)
# 아무런 반응이 없네 >> 값이 없으니깐

# in 은 'key'유무를 확인한다

print(5 in dict_b)

# clear() 는 딕셔너리 모든 요소를 삭제한다.

dict_b.clear()

dict_b

