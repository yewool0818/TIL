# 21.02.02 Homework



👩‍🦰 **학습해야 할 내용!**

> HTML elements (tag + 요소)
>
> CSS Syntax



## 1. HTML 정의

> 아래의 보기 (1) ~ (4) 중에서, HTML의 본딧말을 고르시오. 

`(3)`번

```
(1) Hyperlinks and Text Markup Language
(2) Home Tool Markup Language
(3) Hyper Text Markup Language
(4) Hyper Tool Markup Language
```





## 2. HTML 개념

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

📚 

**1) 웹 표준을 만드는 곳은 Mozilla 재단이다.** 

- `F` : WHATWG 혹은 W3C이다. (HTML : The Living Standard - 계속 발전하고 있다)
  - 최근에는 WHATWG가 표준점이다.

**2) 표(table) 을 만들 때에는 반드시 `<th>` 태그를 사용해야 한다.**

- `F` : 반드시는 아니다. `<th>`

**3) 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다.**

- `T` : 그렇다. 
- 😳why? 역할을 나누어주어야 코드의 가독성이 높아지고, 유지 보수할 때 용이하기 때문이다. - 의미에 맞게 사용하는 것이 중요하다 (`semantic tag`)

**4) 리스트를 나열하기 위해서는 `<ul>` 태그만 사용 할 수 있다.**

- `F` : `<ul>` 태그 혹은 `<ol>` 태그를 사용하여, 내부에 `<li>`태그를 넣을 수 있다.
- ul : unordered list - 순서가 없는 리스트
- ol : ordered list - 순서가 있는 리스트

**5) HTML의 태그는 반드시 별도의 닫는 태그가 필요하다.**

- `F` : `<HTML>` 태그는 열린 태그이기 때문에 반드시 필요하진 않다. (`<input>`, `<button>`과 같이) 





## 3. CSS 정의

> 아래의 보기 (1) ~ (4) 중에서, CSS의 본딧말을 고르시오. 

`(2)`번

```
(1) Creative Style Sheets
(2) Cascading Style Sheets
(3) Computer Style Sheets
(4) Colorful Style Sheets
```





## 4. CSS 개념

> 각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.

📚 

**1) HTML과 CSS는 각자 문법을 갖는 별개의 언어이다.**

- `T` : 하지만 CSS는 혼자 있으면 별 의미가 없다.

**2)  브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.**

- `T` : 기존 값이 내장되어 있어 작동한다.

**3) 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다.**

- `F` : 모두는 아니다. color, font-size 등과 같은 text관련된 것들이 상속된다.

**4) 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.**

- `F` : %가 아닌 `vh`, `vw`로 설정한다.
- 사용자가 딱 눈에 보이는 화면의 크기 : `viewport` 

**5) id 값은 유일해야 하므로 중복되어서는 안된다**

- `T` : 그렇다. 대신 중복이 필요한 경우 class를 이용하면 된다.





## 5. CSS 우선 순위

> CSS는 우선 적용되는 순서가 존재 한다. 우선순위가 높은 순으로 나열 하시오.

1. !important
2. inline style - 해당 태그 내에 style=""로 지정하는 것
3. id 선택자
4. class 선택자
5. element(요소) 선택자
6. 소스(코드) 순서



