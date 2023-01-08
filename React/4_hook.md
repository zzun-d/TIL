### Hook에 들어가기 전에 Component 복습 !

**Function Component**

- state 사용 불가
- Lifecycle에 따른 기능 구현 불가

**Class Component**

- 생성자에서 state를 정의
- setState() 함수를 통해 state 업데이트
- Lifecycle methods 제공

> **Hook은 Function Component에서 Class Component의 기능들을 사용할 수 있게 만든 것**

---

# Hook

- 갈고리라는 뜻으로 특정 함수에 걸어서 함께 실행 시키는 의미
- 모든 Hook은 use로 시작함
- state관련, Lifecycle관련, 최적화관련하여 사용됨

### useState()

- state를 사용하기 위한 Hook

```jsx
/* 
기본적인 useState() 사용법
const [변수명, set함수명] = useState(초기값)
*/

import React, { useState } from "react";

function Counter(props) {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>총 {count}번 클릭했습니다. </p>
      <button onClick={() => setCount(count + 1)}>클릭</button>
    </div>
  );
}
```

### useEffect()

- Side Effect(효과, 영향)를 수행하기 위한 Hook
- 다른 컴포넌트에 영향을 미칠 수 있고, 렌더링 중에는 작업이 완료될 수 없는 작업들을 실행할 수 있게 해주는 Hook
- 기본적으로 useEffect 함수는 컴포넌트가 처음 렌더링된 이후와 업데이트로 인한 재렌더링 이후 실행 됨
- Effect fucntion이 mount, unmount시에 단 한 번씩만 실행되길 원하면 의존성 배열에 빈 배열을 입력
- 의존성 배열을 생략시 컴포넌트가 업데이트 될 때마다 실행
- 기본적으로는 의존성 배열속 요소가 변경되면 실행

```jsx
/* 
기본적인 useEffect() 사용법
useEffect(이펙트 함수, 의존성 배열)
*/

import React, { useState, useEffect } from "react";

function Counter(props) {
  const [count, setCount] = useState(0);

  // 의존성 배열을 안넣었기 때문에 componentDidMount, componentDidUpdate와 비슷한 동작
  useEffect(() => {
    document.title = `${count}번 클릭했음`;
    // useEffect 함수에서의 리턴은 componentWillUnmount와 동일한 시점에 동작
    return () => {
      document.title = "Unmount !";
    };
  });

  return (
    <div>
      <p>총 {count}번 클릭했습니다. </p>
      <button onClick={() => setCount(count + 1)}>클릭</button>
    </div>
  );
}
```

- 깔끔 정리
  - useEffect 실행 시점
    1. 컴포넌트가 마운트 된 이후
    2. 의존성 배열에 있는 변수 중 하나라도 값이 변경되었을 때
    3. 의존성 배열에 빈 배열을 넣으면 마운트, 언마운트시에 단 한 번씩 실행
    4. 의존성 배열 생략 시 컴포넌트가 업데이트 될 때마다 실행
    5. useEffect함수의 리턴으로 함수를 넣으면 해당 함수는 컴포넌트가 unmount되기 직전 실행 됨
