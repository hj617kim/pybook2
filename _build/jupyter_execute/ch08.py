#!/usr/bin/env python
# coding: utf-8

# # 알고리즘

# ## 알고리즘이란

# 알고리즘<font size="2">algorithm</font>이란 어떤 문제를 해결하기 위한 방법과 절차로, 주어진 문제를 해결하는 여러 종류의 알고리즘이 존재할 수 있다. 예를 들어, '두 자연수의 최대공약수 구하기'문제를 해결하는 알고리즘으로는 소인수분해를 이용하는 방법과 유클리드 호제법을 이용하는 방법등이 있다.    

# ````{prf:example}
# :label: algorithm-example01  
# 12와 20의 최대공약수를 구하여라.   
# ````

# **소인수분해를 이용하는 방법**  
# $12$와 $20$을 각각 소인수분해하면 $12 = 2^2 \times 3$, $20 = 2^2 \times 5$이다. 따라서 $12$와 $20$의 최대공약수는 $2^2 = 4$이다. 

# In[1]:


def find_prime_factors(num):
    i = 2
    p_factors = []
    while i * i <= num:
        if num % i == 0 :
            p_factors.append(i)
            num //= i
        else :
            i += 1
    
    if num > 1 :
        p_factors.append(num)
        
    return p_factors

# find_prime_factors(12)
# find_prime_factors(20)

def gcd_prime(m, n):
    m_p_factors = find_prime_factors(m)
    n_p_factors = find_prime_factors(n)
    result = 1
    
    for i in m_p_factors:
        if i in n_p_factors:
            result *= i
            n_p_factors.remove(i)
            
    return result


# In[2]:


gcd_prime(12, 20)


# **유클리드 호제법**  
# m과 n의 최대공약수를 구할 때, 
# * m을 n으로 나눌 수 있으면 n이 최대공약수이다. 
# * 그렇지 않으면, n과 m % n의 최대공약수가 원하는 최대공약수이다. 
# 
# 예를 들어, 
# * 12을 20으로 나눌 수 없다.  
# * 20과 12 % 20(= 12)의 최대공약수를 구한다. 
# * 20을 12로 나눌 수 없다. 
# * 12과 20 % 12(= 8)의 최대공약수를 구한다. 
# * 12을 8로 나눌 수 없다. 
# * 8과 12 % 8(= 4)의 최대공약수를 구한다. 
# * 8을 4로 나눌 수 있으므로, 4가 최대공약수이다. 

# In[3]:


def gcd_Euclid(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


# In[4]:


gcd_Euclid(12, 20)


# ## 알고리즘 표현 방법

# 알고리즘을 표현하기 위해 자연어<font size="2">natural language</font>나 의사코드<font size="2">pseudo-code</font>를 사용할 수 있다.  
# 
# * 자연어 : 한글 또는 영어  
#     * 복잡한 알고리즘 설명과 전달이 어렵다. 
#     * 실제로 구현하기 어렵다. 
#     
# * 의사코드 : 실제 프로그래밍 언어와 유사한 언어로 작성된 코드
#     * 알고리즘을 표현하는 가장 간단한 방법이다. 
#     * 자연어 사용의 단점을 해결한다. 
#     * 직접 실행할 수 없다. 
#     
# 반면, 파이썬은 자연어와 유사할 정도로 간결하고 쉬운 문법을 가지고 있어 의사코드 수준으로 작성가능하며, 코드 작성 후 실행 가능하다.  

# 예를 들어, '자연수 n을 인자로 받아, n이 짝수면 True 아니면 False를 반환하는 함수 `is_even()`을 정의하여라'라는 문제의 알고리즘을 자연어, 의사코드, 파이썬 코드로 나타내면 다음과 같다.  
# 
# [**자연어** 예시]
# ```
# 함수명이 is_even인 함수를 정의한다. 매개변수는 n으로 둔다. 
# n을 2로 나눌 수 있는지를 확인한다. 그리고 나눌 수 있다면 True를 반환하고, 그렇지 않으면 False를 반환한다.   
# ```
#   
#     
# [**의사코드** 예시]
# ```
# 함수 is_even(n)
#     if n를 2로 나눌 수 있다면
#         result = True
#     else
#         result = False
#     return result
# ```
#   
# [**파이썬 코드** 예시]
# ```
# def is_even(n) :
#     if n % 2 == 0 :
#         result = True
#     else :
#         result = False
#     return result
# ```
# 

# ## 알고리즘 분석

# 알고리즘 분석<font size="2">analysis of algorithms</font>은 알고리즘을 실행하는 데 필요한 **컴퓨팅 자원**<font size="2">computing resources</font>의 양을 측정한다. 
# 
# **컴퓨팅 자원**  
# 컴퓨팅 자원이 의미하는 바는 크게 두 가지이다.  
# * 공간량
#     * 알고리즘이 문제를 해결하는 데 필요한 메모리, 하드 디스크 등의 공간<font size="2">space</font> 
#     * 알고리즘을 구현한 프로그램의 실행 중에 필요한 공간의 양  
#     * 입력값의 크기에 의존
#     
# * 실행시간
#     * 알고리즘이 문제를 해결하는 데 걸리는 시간
#     * 알고리즘을 구현한 프로그램이 특정 결과를 반환할 때까지 걸리는 시간
#     * 입력값의 크기에 의존 
#     
# 여기서는 알고리즘 실행에 필요한 공간량에 대해서는 거의 다루지 않고 대신 실행시간에 대한 이야기에 집중한다.  
# 
# 파이썬 프로그램의 실행시간을 측정하는 가장 간단한 방법은 `time`모듈의 `time()`함수를 이용하는 것이다. `time()`함수는 실행될 때마다 과거 특정 시간부터 측정한 초 단위의 숫자를 출력한다. 따라서 실행을 시작할 때, 종료할 때 두 번 측정 결과의 차이가 실행시간이 된다. 또 다른 방법은 `timeit` 모듈의 `Timer`클래스를 활용하는 것이다. 이를 사용하면 측정해야 할 코드 앞뒤에 `time()`함수를 추가하지 않아도 된다.  
# 
# * `Timer` 클래스
#     * 실행되어야 하는 명령문(`stmt`)과 실행환경(`setup`)을 지정하면서 객체 생성
#     * 예제 : 현재 코드가 작성되는 모듈(파일)의 `sum_of_n(100_000)`함수를 대상으로 할 때는 아래와 같이 코드를 작성한다.   
#     `Timer('sum_of_n(100_000)', 'from __main__ import sum_of_n')`
# 
# * `timeit(number=100000000)` 메서드
#     * 지정된 명령문을 (기본값으로 지정된) 1억번을 실행하는 데 걸리는 시간 측정. 단위는 초.
#     * 여기서는 `number = 1000`을 사용하여 사용된 연산자들의 실행시간 비교
#     * 알고리즘의 실행시간은 실행 순간의 컴퓨터 상태에 영향을 받기에 여러 번 실행하여 누적시간을 측정함. 동일한 이유로 평균시간 측정은 별 의미없음.

# 아래 코드는 1부터 n까지 자연수의 합을 계산하는 함수를 차례대로 더해가는 알고리즘으로 구현하여라.  

# In[5]:


from timeit import Timer


# In[6]:


def sum_of_n(n) : 
    the_sum = 0
    for i in range(1, n + 1) :
        the_sum += i
    return the_sum


# 알고리즘의 실행시간은 입력값에 의존한다. 만까지의 합은 천까지의 합보다 10배정도 더 걸리고, 10만까지의 합은 만까지의 합보다 10배정도 더 걸린다. 

# In[7]:


t1 = Timer('sum_of_n(1000)', 'from __main__ import sum_of_n')
print(t1.timeit(number = 1000))

t2 = Timer('sum_of_n(10_000)', 'from __main__ import sum_of_n')
print(t2.timeit(number = 1000))

t3 = Timer('sum_of_n(100_000)', 'from __main__ import sum_of_n')
print(t3.timeit(number = 1000))


# In[8]:


def sum_of_n_2(n) :
    the_sum = (n * (n + 1)) / 2
    return the_sum


# 반면에 `sum_of_n_2()`함수의 실행시간은 입력값에 의존하지 않는 것으로 보인다. 

# In[9]:


time1 = Timer('sum_of_n_2(1000)', 'from __main__ import sum_of_n_2')
print(time1.timeit(number = 1000))

time2 = Timer('sum_of_n_2(10_000)', 'from __main__ import sum_of_n_2')
print(time2.timeit(number = 1000))

time3 = Timer('sum_of_n_2(100_000)', 'from __main__ import sum_of_n_2')
print(time3.timeit(number = 1000))


# 또한 계산 시간이 이전 함수보다 훨씬 빠르다. 아마도 이전 함수에서 사용된 반복 알고리즘이 보다 많은 시간을 요구하며, 반복 횟수에 따라 실행시간이 비례해서 늘어나는 것으로 보인다. 즉, 실행시간이 함수의 입력값에 선형적으로 의존한다.   
# 
# 그런데 한 가지 문제가 있다. 프로그램 실행시간은 실행에 사용되는 컴퓨터, 실행환경, 컴파일러, 프로그래밍 언어 등등에 의존하기 때문에 앞서 보여진 실행시간을 절대적인 기준으로 삼을 수 없다. 따라서 이런 요소들로부터 독립적인 평가 기준을 마련해야 한다.  

# ## Big-O 표기법

# ### 기본 계산단위

# 사용하는 컴퓨터 또는 프로그램에 의존하지 않으면서 알고리즘의 효율성을 실행시간을 이용하여 측정하려면 특정 연산자 또는 특정 명령문 등과 같은 **기본 계산단위**<font size="2">basic unit of computation</font>의 실행 횟수를 확인하면 된다. 무엇을 기본 계산단위로 지정할 것인가 하는 문제는 사용되는 알고리즘에 따라 다르며, 경우에 따라 간단하지 않을 수 있다. 예를 들어, 앞에서 살펴본 `sum_of_n()` 함수의 경우에는 '변수 할당'을 기본 계산단위로 사용할 수 있다.   
# 
# ```
# def sum_of_n(n) : 
#     the_sum = 0                  # 한 번 할당
#     for i in range(1, n + 1) :
#         the_sum += i             # n 번 할당
#     return the_sum
# ```

# ### 시간복잡도와 입력 크기

# `sum_of_n()` 함수를 입력값 $n$과 함께 실행하면 총 $n + 1$번 할당이 이루어지며, 이를 아래와 같이 나타낸다.  
# 
# $$T(n) = n + 1$$
# 
# 함수 $T()$은 **'크기가 $n$인 입력값에 대해 $T(n)$의 시간이 지나면 반환값을 계산하고 종료한다'** 는 의미를 갖는 **시간복잡도**<font size="2">time complexity</font>함수이다. 또한 $n$은 **입력 크기**<font size="2">size</font>를 나타낸다.   
# 
# 따라서 `sum_of_n()` 함수의 시간복잡도 $T(n) = n + 1$이 의미하는 바는 다음과 같다.   
# 
# > $T(n)$은 입력 크기가 $n$인 문제를 해결하는 데에 필요한 시간이 $n + 1$이다. 

# :::{admonition} 주의   
# :class: caution  
# 입력 크기(예, $T(n)$의 $n$)와 입력 값 자체(예, `sum_of_n(n)`의 `n`)는 일반적으로 서로 다른다. 위의 예제에서는 우연히 같았을 뿐이다.  
# :::
# 

# ### 알고리즘과 시간복잡도

# 1부터 n까지 자연수의 합을 반복문을 이용하여 구하면 입력 크기가 클 수록 실행시간도 그에 비례하여 오래 걸린다. 즉, 실행시간이 입력 크기에 의존한다. 반면에 아래에서 사용된 알고리즘은 1번 변수 할당을 사용하였다.  
# 
# ```
# def sum_of_n_2(n) :
#     the_sum = (n * (n + 1)) / 2   #한 번 할당
#     return the_sum
# ```
# 
# 실제로 위 프로그램의 실행시간과 입력 크기 사이의 관계는 $T(n) = 1$이다. 이런 의미에서 **알고리즘을 구현한 프로그램의 실행시간이 입력 크기에 어떻게 의존하는가**를 살펴보는 일은 매우 중요하다. 

# :::{admonition} 참고    
# :class: info    
# 알고리즘의 시간복잡도는 입력 크기뿐만 아니라 알고리즘의 입력값 자체에 의존하기도 한다. 만약 시간복잡도가 입력 크기에만 의존하면, 그것을 **일정 시간복잡도**<font size="2">every-case time complexity</font>라고 부른다.  
# :::
# 

# ````{prf:example}
# :label: algorithm-example02    
# 다음 `sum_list(li)` 함수의 일정 시간복잡도를 계산해보자. 이때, `li`는 길이가 n인 리스트이고, 기본 계산단위는 변수할당으로 한다.   
# 
# def sum_list(li) :
#     ans = 0
#     for i in li :
#         ans = ans + i
#     return ans   
# ````

# 
# ```
# def sum_list(li) :
#     ans = 0            # 1번 할당
#     for i in li :   
#         ans = ans + i  #리스트li의 길이가 n이므로, n번 할당 
#     return ans   
# ```

# 
# 위의 주석으로 적은 것처럼, `sum_list()` 함수가 길이가 `n`인 리스트와 함께 호출되었을 때, 실행하는 변수 할당의 총 횟수 $T(n)$은 다음과 같다.  
# 
# $$T(n) = n + 1$$  
# 

# #### Big-O 표기법 

# 입력 크기에 의존하는 실행시간 함수 $T(n)$의 정의에 사용되는 수식을 분석할 때, 수식에 사용되는 모든 항을 다룰 필요가 없다. 예를 들어, $T(n) = n + 1$에서 $n$이 커질 수록 1은 별로 중요하지 않다. 즉, $n$이 충분히 클 때, $T(n) \approx n$이 성립한다. 이를 **Big-O 표기법**으로 나타내면 다음과 같다.   
# 
# $$T(n) \in O(n)$$

# 실행시간 함수 $T(n)$을 Big-O 표기법으로 나타내려면 앞서 설명한 것처럼 실행시간 계산에 있어서 입력 크기 $n$이 매우 커질 때 가장 중요한 역할을 수행하는 항<font size="2">term</font>을 찾아야 한다. 예를 들어, 그 항이 $f(n)$이라면 아래처럼 표기할 수 있다.  
# 
# $$T(n) \in O(f(n))$$  
# 
# 이때 상수 배수는 무시된다. 

# ````{prf:example}
# :label: algorithm-example03    
# 
# 다음과 같은 시간복잡도 함수가 있다. 이를 Big-O 표기법으로 나타내어라. 
# $T(n) = 3n^2 + 2n + 4$ 
# 
# ````

# $3n^2 + 2n + 4$에서 $n$이 커질 때 $3n^2$이 주도적 역할을 수행한다. 여기서 상수 배수를 무시하면 $T(n) \in O(n^2)$이다. 

# ````{prf:example}
# :label: algorithm-example04    
# 
# 다음과 같은 시간복잡도 함수가 있다. 이를 Big-O 표기법으로 나타내어라. 
# $T(n) = \frac{1}{1000} n log n + 3n + 205$ 
# 
# ````

# $\frac{1}{1000} n \log n + 3n + 205$에서 $n$이 커질 때 $\frac{1}{1000} n \log n$이 주도적 역할을 수행한다. 여기서 상수 배수를 무시하면 $T(n) \in O(n \log n)$이다. 

# ````{prf:example}
# :label: algorithm-example05    
# 
# 다음과 같은 시간복잡도 함수가 있다. 이를 Big-O 표기법으로 나타내어라. 
# $T(n) = c$, $c$는 상수 
# 
# ````

# 시간복잡도가 입력 크기에 전혀 의존하지 않을 때 시간복잡도는 1이라고 말한다. 시간복잡도를 따질 때 상수 배는 무시되기 때문이다. 따라서 $T(n) \in O(1)$이다. 

# #### 주요 시간복잡도  
# 
# 알고리즘 분석에 많이 사용되는 시간복잡도는 아래와 같다. 아래 표에서 위쪽에 있을 수록 더 빠르다. 
# 
# |Big-O 표기법| 의미|
# |-----------|-----|
# |O($1$)|상수 시간|
# |O($\log n$)|로그 시간|
# |O($n$)|선형 시간|
# |O($n \log n$)|로그선형 시간|
# |O($n^2$)|2차 시간|
# |O($n^3$)|3차 시간|
# |O($2^n$)|지수 시간|
# |O($n!$)|계승 시간|
