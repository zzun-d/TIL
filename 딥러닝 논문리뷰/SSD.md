### 1. 개요

- **SSD(Single Shot MultiBox Detector): 한번에 여러 object를 검출할 수 있는 모델**

- **two stage-detector**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/995bf884-b81a-4891-b209-5fda0a016b65/Untitled.png)
    
    - regional proposal, classification 순차적으로 / 느리지만 정확

- **single stage-detector**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/682b79ce-3cb9-44ac-80ea-9e90669a4133/Untitled.png)
    
    - regional proposal, classification 동시에 / 빠르지만 정확성이 떨어짐

- **해상도에 따른 feature map**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3412ac2a-4178-40b5-af0c-509762898dd5/Untitled.png)
    
    (b) : SSD, (c) : FPN, (d) : PFPNEt
    

### 2.  Model

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ada987e5-1eae-417c-8739-bdc4d37fa73d/Untitled.png)

- Base network는 VGG-16을 사용(Conv5_3_layer 까지만)
- 크기가 다른 feature map 6개를 이용한 것이 특징
    - object의 크기가 작은 것은 해상도가 높은 feature map에서 검출하고 큰 것은 해상도가 낮은feature map에서 검출
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/533f1fdd-3de8-40ca-81c5-42620795cb87/Untitled.png)
        
- Classifier : Conv 3 x 3 필터를  (c+4)k 개 이용(c: class 개수, 4: cx, cy, w, h정보, k: default box 개수)
    - default box는 faster R-CNN의 앵커와 동일한 개념이지만 scale정보 추가
        
        $s_k = s_{min}+{s_{max}-s_{min} \over m-1}(k-1), \ k \in [1,m]$
        
        논문에서 $s_{min}$= 0.2, $s_{max}$= 0.9 (실제로는 $s_{min}$ = 0.1, 남은 5개에 대하여 위 식을 진행)
        
        scale이 0.1이라는 것은, input x 0.1을 의미
        
        → 0.2, 0.34, 0.48, 0.62, 0.76, 0.9 (논문ver)
        
        → 0.1, 0.2, 0.375, 0.55, 0.725, 0.9 (실제ver) 
        
        $a_r \in \{ 1,2,3,{1 \over 2}, {1 \over 3} \}$
        
        $w_k^a = s_k\sqrt a_r$
        
        $h_k^a = s_k\sqrt a_r$
        
        $a_r$이 1일 때 scale하나 추가(종횡비는 같은 1이지만 크기가 큰 box)
        
        $s'_k = \sqrt {s_ks_k+1}$
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e358d4ba-901b-41c2-8794-4c77ba822773/Untitled.png)
        
    - feature map을 Conv하여 class와 bbox를 예측한 정보를 담은 Tensor를 생성
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b5e2def3-a5b1-40ec-b111-511537dd0047/Untitled.png)
        
    
- 총 예측 bbox 수
    - feature map 1 : VGG-16의 Conv4_3 layer(38x38x512) → 38x38x4(c + 4) → 5776(c + 4)
    - feature map 2 : Conv7 layer(19x19x1024) → 19x19x6(classes + 4) → 2166(classes + 4)
    - feature map 3 : Conv8_2 layer(10x10x512) → 10x10x6(classes + 4) → 600(classes + 4)
    - feature map 4 : Conv9_2 layer(5x5x256) → 5x5x6(classes + 4) → 150(classes + 4)
    - feature map 5 : Conv10_2 layer(3x3x256) → 3x3x4(classes + 4) → 36(classes + 4)
    - feature map 6 : Conv11_2 layer(1x1x256) → 1x1x4(classes + 4) → 4(classes + 4)
    
    **total : 8732(classes + 4)**
    
    class 하나 당 8732개의 bbox를 예측
    

### 3. 훈련

- **Matching strategy**
    - default box의 IoU가 0.5보다 크고, class가 정답일 경우에는 positive, 아니면 negative
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4e44994c-7ba3-4989-8f3b-734873a5c773/Untitled.png)
    
    - default box 1, 2, 3 중에 IoU가 0.5를 넘는 것은 1과 2이므로 1, 2는 positive, 3은 negative

- **Loss function(localization, confidence)**
    - **localization loss: ground truth box와 bbox의 차이로, smooth L1 loss를 이용**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d34a03a4-fc19-42ea-9f0c-199cd6b048bb/Untitled.png)
        
    
    - **confidence loss: classification loss → cross-entropy**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1aea0bed-e5bd-4a13-9f17-59a4bc0ccf5e/Untitled.png)
        
    - **Total Loss**
        
        $L(x,c,l,g) = {1 \over N}(L_{conf}(x,c)\ +\ \alpha L_{loc}(x,l,g))$
        
        ($N$: positive 일치 수,    $\alpha$: localization loss의 가중치 )
        

- NMS 알고리즘을 이용하여 IoU가 가장 높은 bbox하나만 남김

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b9ae539f-ca64-4f12-9911-eabf784ea199/Untitled.png)

- **Hard Negative Mining**
    - bbox를 8732개를 뽑았지만 그 중 object를 잘 찾아서 bbox한 positive의 수에 비하여 일반 배경을 bbox한 negative의 수가 압도적으로 많을 것.
        
        이런 class 불균형 문제를 해결하기 위하여 도입된 방법
        
    - default box의 confidence loss가 큰 순서대로 positive의 최대 3배까지만 사용
        
        (confidence loss가 크다는 것은 실제 배경에 bbox을 했지만 그 확률을 적게 내보낸 box)
        

### 4. 결과

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6453f25e-1369-4b75-bb03-63abf8dba720/Untitled.png)

- Faster-R-CNN만큼 정확하고, 훨씬 빠르다

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/77cddfbb-a2c0-4f82-9d54-37077285a06c/Untitled.png)

- SSD의 단점은 작은 object를 잘 잡아내지 못하는 것인데, 그 이유는 작은 object를 detection하는 feature map이 정보의 압축이 덜 된 feature map이기 때문에 성능이 좋지 않다는 분석이 있음.
    
    → data augmentation으로 한계 극복
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c42f5f2f-0384-41ee-88a5-d66dd70a5957/Untitled.png)
    

Reference

[https://www.youtube.com/watch?v=ej1ISEoAK5g](https://www.youtube.com/watch?v=ej1ISEoAK5g)

[https://jonathan-hui.medium.com/ssd-object-detection-single-shot-multibox-detector-for-real-time-processing-9bd8deac0e06](https://jonathan-hui.medium.com/ssd-object-detection-single-shot-multibox-detector-for-real-time-processing-9bd8deac0e06)

[https://m.blog.naver.com/sogangori/221007697796](https://m.blog.naver.com/sogangori/221007697796)