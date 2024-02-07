# Python files of algorithm problems solved

---

## java 하느라 까먹은 python 재활 치료기

### 24.02.06
- `'문자열'.join(대상 문자열 or 대상 문자열 리스트)`
  - 각 대상 문자열의 문자 사이 혹은 대상 문자열 리스트의 문자열 사이에 '문자열'을 삽입한 String을 반환
- `string.capitalize()`
  - 문장의 첫 글자만 대문자로 변경, 나머지는 소문자로 바꿔 반환
- 파이썬의 사칙연산
  - 덧셈, 뺄셈, 곱셈, 나머지는 동일
  - 나눗셈시 자바는 정수간 `/` 사용시 소수부분은 모두 버리지만, 파이썬은 소수까지 살림
    - 파이썬에서 정수간의 나눗셈간 소수를 버리고 싶을 경우 `//` 사용
- 파이썬 빨리 입력 받기
  - ```python
    import sys
    input = sys.stdin.readline().rstrip # rstring()안할 경우 입력 값 끝에 개행문자 추가됨, 여러줄 입력시에는 rstrip삭제 필요
    ...    
    A = int(input()) # 정수 값 입력 받기
    A, B = map(int, input()) # 5 7 과 같은 형태로 입력 받기, 자바의 StringTokenizer 이용과 동일
    ```
- 문자열 포맷팅
  - ```python
    "I ate {0} apples. so I was sick for {1} days.".format(10, "three") # 'I ate 10 apples. so I was sick for three days.'
    "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3) # 'I ate 10 apples. so I was sick for 3 days.'
    
    ```
- 날짜 모듈 `datetime`
  - ```python
    import datetime
    print(str(datetime.datetime.now())[:10]) # YYYY-MM-DD
    print(datetime.date.today().isoformat()) # YYYY-MM-DD
    ```
    
- 파이썬의 정렬 함수 `sort()`
  - 다음과 같이 2차원 행렬의 경우 파이썬은 자동으로 처음 열부터 기준을 잡아 정렬한다. 
  ```python
    people = []
    for _ in range(n):
        name, d, m, y = input().rstrip().split()
        d, m, y = map(int, (d, m, y))
        people.append([y, m, d, name])

    people.sort() # y, m, d, name 순으로 비교하여 정렬
    print(people[-1][3])
    print(people[0][3])
  ```
  
- 파이썬의 스택 사용
  - 그냥 리스트쓰면 된다.(리스트가 `pop()` 지원)
  - ```python
    stack = []
    for _ in range(K):
        number = int(input())
        if number == 0:
            stack.pop()
        else:
            stack.append(number)
    ```
    
- `split()` 과 `split(" ")`의 차이
  - `split()`은 모든 공백을 하나로 보고 처리함.
  - `split(" ")`은 공백 1개를 각각의 공백으로 따로 처리
  - 예시
  - ```python
    string = "word1 word2  word3    word4     "
    print(string.split())
    > ['word1', 'word2', 'word3', 'word4']
    print(string.split(" "))
    > ['word1', 'word2', '', 'word3', '', '', 'word4', '', '', '', '']
    ```