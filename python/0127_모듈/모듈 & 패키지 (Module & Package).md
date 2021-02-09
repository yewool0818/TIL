# 모듈 & 패키지 (Module & Package)



> 🙋‍♀️ **module** vs **package**
>
> - module : 파일
> - package : 폴더
>
> 로 생각하면 간단하다!



**활용 방법**

```python
import [module]
from [package] import [module]
```



> 추가 활용법

```python
from [package].[package].[package].. import [module]
from [package].[module] import [module]
from [package] import [module] as [alias(별칭)]
```





### 예제



**디렉토리 구조**

```
module_practice/
	check.py
	my_algo.py
	
	my_package/
		__init__.py
		math/
			__init__.py
			tools.py
```



👩‍🏫 **`__init__.py`** ?

> python3.3 버전부터는 `__init__.py` 파일이 없어도 패키지로 인식합니다(PEP 420). 하지만 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 `__init__.py` 파일을 생성하는 것이 권장됩니다.





module_practice/my_package/math/`tools.py`

```python
pi = 3.14159265358979323846

e = 2.71828182845904523536

result = '울라울라'

def my_max(a, b):
    if a > b:
        return a
    else:
        return b
```

<br>

module_practice/`check.py`

```python
# check.py
def odd(n):
    return bool(n % 2)

def even(n):
    return not bool(n % 2)
```

<br>



**위 코드들을 모듈, 패키지화 하여 사용해보자**

```python
# 알고리즘 공부야

import check, random
from my_package.math import tools # my_package 패키지의 math 패키지의 tools 모듈 임포트
from my_package.math.tools import pi as tools_pi #my_package의 math의 tools의 pi 변수 임포트(tools_pi이름으로)
from my_package.math.tools import my_max ## my_package 패키지의 math 패키지의 tools 모듈의 my_max 함수 임포트
# from my_package.math.tools import * # 비권장됨!


pi = '이건 내가 꼭 필요한 변수야....'

print(pi, tools_pi) 
# 이건 내가 꼭 필요한 변수야.... 3.141592653589793
# 현 모듈에서 지정한 변수가 나오고, import한 변수가 나온다.

print(dir(check)) # [..생략.. 'even', 'odd']
yewool_odd = check.odd
print(yewool_odd(10)) # False

print(dir(tools))       # [..생략.. 'e', 'my_max', 'pi', 'result']
print(tools.pi)         # 3.141592653589793
print(pi)               # 이건 내가 꼭 필요한 변수야....
print(my_max(5, 4))     # 5
```

