[문제](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

  

  권장 시간 : 30분

  풀이 시간 : 1시간

최종코드

```python

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

```
설명 : (https://school.programmers.co.kr/learn/courses/30/lessons/42747/solution_groups?language=python3)

#### 공부한 내용 본인의 언어로 정리하기 ##
다들 간단하게 for 문으로 풀었다. 

#### 오늘의 회고 
문제가 계속 일정한 방법으로 푸는데 런타임 오류가 나고 잘 안풀렸다. 

>##### 어떤 문제가 있었고, 나는 어떤 시도를 했는지

다른 사람의 문제를 보면서 참고했다. 

>##### 어떻게 해결했는지
 for 문으로 가볍게 풀었다. 

>##### 무엇을 새롭게 알았는지


>##### 내일 학습할 것은 무엇인지
내일 문제 올라오면 그것을 바탕으로 또 공부 할 것이다. 


 
  

 #99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL