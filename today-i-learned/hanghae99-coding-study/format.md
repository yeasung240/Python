문제]https://school.programmers.co.kr/learn/courses/30/lessons/12951

  최종 코드

  권장 시간 : 30m
  풀이 시간 : 1h : 36m



```python
def solution(s):

    S = s.lower()
    H = S.split(' ')
    STRING = []

    for i in H:
        print(i)
        if i:
            Z = i[0].upper() + i[1:]
        else:
            Z = i
        STRING.append(Z)
    last = ' '.join(STRING)
    
    return last

```

#### 공부한 내용 본인의 언어로 정리하기 ##
 

#### 오늘의 회고 


>##### 어떤 문제가 있었고, 나는 어떤 시도를 했는지
. 


>##### 어떻게 해결했는지
 

>##### 무엇을 새롭게 알았는지


>##### 내일 학습할 것은 무엇인지
. 



- 
  

 #99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL