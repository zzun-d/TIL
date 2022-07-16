# Cascade?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4e9ffe9-c7a1-4356-b75e-8da5d0f2285c/Untitled.png)

- cascade는 위 사진처럼 층이 나뉜 계단식의 작은 폭포를 의미한다.
- cascade rcnn은 훈련에 사용되는 IoU threshold를 단계적으로 높여 모델의 성능을 향상 시켰다.

**Close false positive?**

- object detection의 난제로 클래스는 맞췄지만 BBox를 애매하게 맞춘 데이터를 의미한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7e5520fe-739b-46b1-b7f9-607286bf245f/Untitled.png)
    
- Threshold IoU를 0.5로 주게 되면 close false positive가 많이 생성되고, 모델의 질이 낮아진다.
- Threshold IoU를 0.7로 주게 되면 output image에 BBox는 많이 줄어 깔끔하지만, 입력단에서 IoU가 높은 데이터는 그 양이 적어서 제대로 된 학습이 안되는 경우가 많다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d8fbd331-db0b-4076-abac-9e78df27359f/Untitled.png)

- (a)는 Faster R-CNN
- (b)는 같은 head를 3개를 연속적으로 거쳐서 성능을 올린 모델
    - Iterative BBox at inference의 한계
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7196bee7-599c-42f0-9cfa-993c8c18344e/Untitled.png)
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a49bf710-676f-488e-ae36-055371312260/Untitled.png)
        
- (c)는 IoU threshold가 다른 classifier를 병렬로 주었음
    - Integral Loss의 한계
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a7bf3ecf-5595-48ac-9478-b8b3adfd9221/Untitled.png)
        
- (d)가 (b), (c)의 한계점을 잘 보완한 Cascade R-CNN

**Experimental Results**

- 4-stages : 1 - RPN, + 3 - Classifier(u={0.5, 0.6, 0.7})
- horizontal image flipping외의 다른 augmentation은 사용하지 않았음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f647693b-1f9d-464b-9c59-90765a411f76/Untitled.png)

- detection performance는 stage를 거듭하면서 threshold IoU를 0.5, 0.6, 0.7로 단계적으로 높이는것이 효율이 좋음을 보여주는 그래프이다. 1st Stage에서는 IoU를 0.5로 학습했을 때가 가장 높은 성능을 보였고, 2nd Stage에서는 0.6, 3rd Stage에서는 0.6과 0.7이 거의 비슷한 성능을 나타냈다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6abda69-b237-4aa7-a853-70242ed7ce69/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e63679c-0e44-4e4d-b24d-e6f656c75e48/Untitled.png)