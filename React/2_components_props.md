# Components

- 리액트 앱을 구성하는 가장 작은 블록들
- 하나의 컴포넌트는 또 다른 컴포넌트들로 이뤄져있음
- 리액트 컴포넌트에서의 입력은 Props, 출력은 React Element라고 할 수 있음
- 만들고자 하는 대로 Props를 컴포넌트에 입력하면 입력에 맞추어 Element로 출력
- 입력값(Props)을 변경하지 않으며, 같은 입력(props)에 대하여 항상 같은 결과(React Element)을 보여야 함
- 컴포넌트의 이름은 항상 대문자로 시작해야 함(소문자로 시작하면 DOM Component로 인식하기 때문)

# Props

- Property를 줄여 사용 함(속성이라는 뜻)
- 컴포넌트에 전달할 다양한 정보를 담고 있는 자바스크립트 객체
- React Component의 속성을 의미
- Read-Only의 특성(값 변경이 불가능 !)

## Props 사용법

```jsx
function App(props) {
  return <Profile name="이름" introduction="소개" viewCount={1000} />;
}
```

- props는 key=value 형태로 전달해 줄 수 있음
- 위 경우 Profile 컴포넌트에 {name:"이름", inroduction:"소개", viewCoount:1000}을 전달한 결과
- viewCount에서 중괄호 사용한 이유는 jsx에서 자바스크립트 문법을 사용할 경우 {}를 사용하여 나타내기 때문
- 중괄호를 사용하여 Props에 컴포넌트도 전달이 가능 함!

```jsx
function App(props) {
  return (
    <Layout
      width={1200}
      height={900}
      header={<Header title="헤드입니다." />}
      footer={<Footer />}
    />
  );
}
```

- jsx를 사용하지 않을 경우 React.Element를 이용하여 props를 전달할 수 있음

## Fucntion Component & Class Component

```jsx
// 함수 컴포넌트
function Welcome(props) {
  return <h1>안녕, {props.name}!</h1>;
}

// 클래스 컴포넌트
class Welcome extends React.Component {
  render() {
    return <h1>안녕, {this.props.name}!</h1>;
  }
}

// DOM tag로 만든 컴포넌트 인식
const element1 = <div />;

// 리액트 컴포넌트 인식
const element2 = <Welcome name="인제" />;

// 렌더링 방법
ReactDOM.render(element2, document.getElementById("root"));

// 컴포넌트 합성 방법
// App 컴포넌트 안에 3개의 Welcome 컴포넌트가 있음
function App(props) {
  return (
    <div>
      <Welcome name="이름1" />
      <Welcome name="이름2" />
      <Welcome name="이름3" />
    </div>
  );
}
```
