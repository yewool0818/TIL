# 21.02.02 Homework



👩‍🦰 **학습해야 할 내용!**

> CSS Felxible Box Layout
>
> Bootstrap Grid System



## 1. CSS flex-direction

> Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오. 

- `row` : 기본 값으로 수평(좌우)를 메인 축으로 잡는 것이다.
- `row-reverse` : `row` 특성에 수평 반전을 준 것이다.
- `column` : 수직(상하)를 메인 축으로 잡는 것이다. 기본 값에서 수직 반전을 준 것이다.
- `column-reverse` : `column` 특성에 수평 반전을 준 것이다.

<br>

## 2.  Bootstrap flex-direction

> flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.

- 우선 css에서 `flex-direction:flex;`를 설정할 때처럼, `d-flex`를 클래스에 추가해주어야 한다.

| css property     | bootstrap class       |
| ---------------- | --------------------- |
| `row`            | `flex-row`            |
| `row-reverse`    | `flex-row-reverse`    |
| `column`         | `flex-column`         |
| `column-reverse` | `flex-column-reverse` |

<br>

## 3.  align-items

> align-items 속성의 4가지 값과 각각의 특징을 작성하시오.

- `center` : 교차 방향 가운데 정렬 - y축 기준으로 요소들을 중앙으로 모아줌
- `flex-start` : 교차 시작 방향으로 앞(뒤, 처음)으로 배치
- `flex-end `: 교차 끝 방향으로 뒤(끝, 마지막)으로 배치
- `baseline` : 교차 컨테이너의 기준선에 배치된다.
- `stretch` : 너비 및 높이를 여백이 없도록 꽉 채워 늘어남

<br>

## 4. flex-flow

> flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.

```
(1) flex-direction, flex-wrap
(2) flex-direction, align-items
(3) justify-content, flex-wrap
(4) justify-content, align-items
```

`(4)번`

: `flex-direction`은 flex-box의 주축을 변경할 때 사용하며, `flex-wrap`은 플렉스 요소끼리 가로세로가 겹쳐졌을 때, 겹칠지 말지 어떻게 겹칠지 설정하는 값이다. 

<br>

## 5. Bootstrap Grid System

> 하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, __(a)__, __(b)__ 각각에 입력해야 할 클래스 이름을 작성하시오.

```html
<div class="__(a)__">
    <div class="__(b)__">
        <div class="col-__(c)__-__(d)__"></div>
    </div>
</div>
```

- (a) : `container`
- (b) : `row`

<br>

## 5. Bootstrap Grid System

> Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.

- (c):  `공백`, `sm`, `md`, `lg` 등이 들어갈 수 있으며, 다양한 디바이스 별 뷰포트 크기에 맞게 조정할 수 있다.

  📚 사이즈 기준표

| Extra small |  Small  | Medium  |  Large  | X-Large  | XX-Large |
| :---------: | :-----: | :-----: | :-----: | :------: | :------: |
|   < 576px   | ≥ 576px | ≥ 768px | ≥ 992px | ≥ 1200px | ≥ 1400px |
|     `-`     |  `sm`   |  `md`   |  `lg`   |   `xl`   |  `xxl`   |

- (d): 1~12까지 들어올 수 있으며, 위 (c)에서 선택한 각 종류에 맞게 12칼럼 중 몇 개의 칼럼을 사용할 지 명시해주는 것이다.

