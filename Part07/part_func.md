# 파괴적 처리(Destructive)와 비파괴적 처리(Non-destructive)
## 파괴적 처리(Destructive) 함수
- 원본 데이터 손상 > 기본 X > 새로운 데이터로 교체
- return : None, T/F, 요약정보
- 대표 함수 : .sort() .extend() .insert()

## 비파괴적 처리(Non-destructive) 함수
- 원본 데이터가 변하지 않는 연산, 대체로 연산한 결과를 return하는 것이 있음.
    - 대표 : len, sorted, str, int
- 원본 데이터가 변하지 않은 연산, 그러나 단순히 일회성 수행이라 return 없기도.
    - 대표 : print

input() : 비파괴적인 함수
list.index(v) : 비파괴적인 함수