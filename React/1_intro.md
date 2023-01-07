# React Intro

- UI를 만들기 위한 자바스크립트 라이브러리
- 인기 1위 JS 라이브러리(Meta가 후원 !)
- Vue.js 프레임워크가 2위(중국인이 개발)

### 프레임워크 vs 라이브러리

- 프레임워크
  - 제어권한이 프레임워크에 있음
- 라이브러리
  - 제어권한이 개발자에게 있음

### 리액트의 장점

- 빠른 업데이트, 빠른 렌더링 속도
- Virtual DOM을 이용하기 때문에 빠르다
- 기존의 방식은 DOM을 직접 수정하여 업데이트 하기 때문에 변한 부분을 모두 찾아야 해서 비효율적이었다.
- Virtual DOM에서는 업데이트 해야하는 부분만 Re-render(방식은 두개의 돔을 띄워 차이나는 부분만 업데이트)
- 또 다른 장점으로는 Component-Based !
- Component-Based는 코드의 재사용성을 높여주고(개발 기간 단축), 디버깅을 용이하게 해줌(유지 보수 용이)

### 리액트의 단점

- 방대한 학습량(라이브러리이기 때문에 배워야 할 지식이 많음 Virtual DOM, JSX, Component, State, Props ...)
- 계속 업데이트 되기 때문에 꾸준한 공부가 필요
- 하지만 이것은 개발자의 숙명!
- 높은 상태관리 복잡도 또한 단점 !

# React Start

[리액트 설치를 위한 공식문서](https://reactjs-kr.firebaseapp.com/docs/installation.html)

### create-react-app

- react를 활용할 프로젝트를 생성해주는 코드
- Node.js 14.0.0 이상
- npm 6.14.0 이상
- `npx create-react-app <project-name>`
- `cd <project-name>`
- 앱 실행은 `npm start`

### JSX ?

- JavaScript의 확장 문법으로 JavaScript + XML(HTML)
- `const element = <h1>Hello, World!</h1>`
- 위 코드처럼 JavaScript 코드 + XML/HTML로 이뤄진 코드
- XML/HTML 사이에 JavaScript 코드를 삽입하고 싶으면 중괄호 이용
- JSX 코드 예시

```jsx
class Hello extends React.Component {
    render() {
        return <div>Hello {this.props.toWhat}<div/>
    }
}

ReactDPM.render(
    <Hello toWhat="World" />,
    document.getElementById('root')
)
```

- JSX 사용은 코드를 더 가독성있고 간단하게 작성 가능하게 도와줌!
- 또한 해킹방지(사용자 입력칸에 JS문법을 넣어 해킹하는 해킹방법에서 자유로움, why? -> JSX는 입력을 JS로 보지않고 우선 문자열로 바꾸어 읽기 때문에 ! )
  <br>

### React 메서드

- **React.createElement**

```jsx
React.createElement(type, [props], [...children]);
```
