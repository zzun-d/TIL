동기식
- 모든 일을 순서대로 하나씩 처리하는 것
- python 코드는 모두 동기식
- 요청과 응답을 동기식으로 처리시 문제가 있음

비동기식
- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리(병렬적 수행)
- 사용자 경험에서 아주 큰 차이가 있음
    - 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리시 앱이 멈춘듯한 경험
    - 비동기로 처리시 병렬처리로 데이터 불러옴과 동시에 앱 사용 가능

자바스크립트는 thread가 1개지만, 런타임 환경에서 브라우저, node에서 멀티 쓰레드가 가능하게 해줌

브라우저 환경
1. 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리
2. 오래 걸리는 작업이 **Call Stack**으로 들어오면 **Web API**로 보내 별도로 처리하도록 한다.
3. **Web API**에서 처리가 끝난 작업들은 곧바로 **Call Stack**으로 들어가지 못하고, **Task Queue**(FIFO)에 순서대로 들어간다.
4. **Event Loop**가 **Call Stack**이 비어 있는 것을 계속 체크하고 **Call Stack**이 빈다면 **Task Queue**에서 가장 오래된 작업을 **Call Stack**으로 보낸다

Axios
- JavaScript의 HTTP 웹 통신을 위한 라이브러리

- 기본 구조
```javascript
axios.get(catImageSearchURL)
      .then((response) => {
        // console.log(response.data[0].url)
        imgElem = document.createElement('img')
        imgElem.setAttribute('src', response.data[0].url)
        document.body.appendChild(imgElem)
      })
      .catch((error) => { 
        console.log('실패했다옹')
      })
      console.log('야옹야옹') 
```

**callBack 함수의 필요한 이유**
- 비동기 처리를 순차적으로 진행하기 위해