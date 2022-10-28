# Deep Residual Learning for Image Recognition
[논문 링크](https://arxiv.org/abs/1512.03385v1)

#### 이해하기 쉬운 아이디어면서 성능향상이 높았기에 좋은 모델!

 

---
### 기초적인 CNN 지식
- CNN(Convolution Neural Networks)는 filter 혹은 kerner이라는 array(tensor)를 입력 데이터에 convolution 연산을 통하여 kerner 수 만큼의 feature를 뽑아내면서 input 데이터의 특징을 학습 시키는 방법이다.

- 여기서 filter의 사이즈는 주로 3x3을 사용하며, padding을 주지 않으면 featuremap의 크기가 점점 줄어들게 되고, 반대로 채널 수는 증가시키면서 layer가 깊이 쌓일수록 featuremap의 하나의 element는 input data의 넓은 부분을 표현하게 되며, 표현 방법이 많아지게 된다.

- 일반적으로 layer의 깊이가 깊어질수록 다양한 표현이 가능해지며 모델 성능이 올라가지만,
  일정단계 이상의 깊이가 된다면 더이상 학습이 안되며, 오히려 성능이 감소하는 성향이 나타난다.

- 이러한 한계를 일정부분 해결한 모델이 Resnet

### 핵심 아이디어

#### 잔여 학습

  - layer가 깊어지면 오히려 성능이 안좋아지는 경향이 있음
  - 잔여학습을 통해서 layer가 깊어져도 성능을 향상 시키는 방법
  - 네트워크의 최적화 난이도를 낮춤
  - weight layer, activation function을 거쳐서 나온 H(x)를 곧바로 학습하는 것은 어렵기 때문에, F(x) = H(x) - x 를 학습하는 것이 핵심 원리
  - shortcut connection
  