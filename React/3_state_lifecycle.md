# State

- 리액트에서 State는 React Component의 상태(React Component의 변경 가능한 데이터)를 나타냄
- state는 개발자가 정의하여 사용
- state 정의 시에 렌더링이나 데이터 흐름에 사용되는 값만 state에 포함시켜야 함
  - 불필요한 경우에도 컴포넌트가 다시 렌더링되어 성능저하의 원인이 될 수 있음
- state 또한 JavaScript 객체

```jsx
class LikeButton extends React.Component {
  // component 생성자
  constructor(props) {
    super(props);

    // 현재 컴포넌트의 state를 정의하는 부분
    this.state = {
      liked: false,
    };
  }
}

// state를 직접 수정(잘못된 사용)
this.state = { liked: true };

// setState 함수를 통한 수정(정상적인 사용)
this.setState({
  liked: true,
});
```

# LifeCycle

- React Component의 생명주기
- 출생 - 인생 - 사망(인간의 생명 주기)
- Mounting - Updating - Unmounting(React의 생명 주기)
- Mounting
  - **componentDidMount**
  - constructor 실행
  - state 정의
  - component mount
- Updating
  - **componentDidUpdate**
  - New props
  - setState()
  - forceUpdate()
  - 위와 같은 상황들로 component가 바뀔 때 Updating
- Unmounting
  - **componentWillUnmount**
  - 상위 컴포넌트에서 해당 컴포넌트를 더 이상 표시하지 않게 될 때
