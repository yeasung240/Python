[문제](https://leetcode.com/problems/prefix-and-suffix-search/)

  

  권장 시간 : 30분
  
  풀이 시간 : 30분

최종코드

```python
class WordFilter:
    def __init__(self, words):
        self.d = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix, suffix):
        return self.d.get((prefix, suffix), -1)


```

[참조](https://leetcode.com/problems/prefix-and-suffix-search/solutions/1185171/python-two-solutions-trie-and-bruteforce-explained/)

#### 공부한 내용 본인의 언어로 정리하기 ##
클래스 선정 후 완전 탐색이나 딕셔너리로 풀 수 있는 문제였다. 

#### 오늘의 회고 
컨디션 관리를 잘 못해서 피곤해서 문제를 푸는데 실수가 있었다. 





 
  

 #99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
