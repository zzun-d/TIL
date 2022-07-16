# Cascade?

![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled.png?raw=true)

- cascade는 위 사진처럼 층이 나뉜 계단식의 작은 폭포를 의미한다.
- cascade rcnn은 훈련에 사용되는 IoU threshold를 단계적으로 높여 모델의 성능을 향상 시켰다.

**Close false positive?**

- object detection의 난제로 클래스는 맞췄지만 BBox를 애매하게 맞춘 데이터를 의미한다.
    
    ![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(1).png?raw=true)
    
- Threshold IoU를 0.5로 주게 되면 close false positive가 많이 생성되고, 모델의 질이 낮아진다.
- Threshold IoU를 0.7로 주게 되면 output image에 BBox는 많이 줄어 깔끔하지만, 입력단에서 IoU가 높은 데이터는 그 양이 적어서 제대로 된 학습이 안되는 경우가 많다.

![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(2).png?raw=true)

- (a)는 Faster R-CNN
- (b)는 같은 head를 3개를 연속적으로 거쳐서 성능을 올린 모델
    - Iterative BBox at inference의 한계
        
        ![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(3).png?raw=true)
        
        ![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(4).png?raw=true)
        
- (c)는 IoU threshold가 다른 classifier를 병렬로 주었음
    - Integral Loss의 한계
        
        ![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(5).png?raw=true)
        
- (d)가 (b), (c)의 한계점을 잘 보완한 Cascade R-CNN

**Experimental Results**

- 4-stages : 1 - RPN, + 3 - Classifier(u={0.5, 0.6, 0.7})
- horizontal image flipping외의 다른 augmentation은 사용하지 않았음

![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(6).png?raw=true)

- detection performance는 stage를 거듭하면서 threshold IoU를 0.5, 0.6, 0.7로 단계적으로 높이는것이 효율이 좋음을 보여주는 그래프이다. 1st Stage에서는 IoU를 0.5로 학습했을 때가 가장 높은 성능을 보였고, 2nd Stage에서는 0.6, 3rd Stage에서는 0.6과 0.7이 거의 비슷한 성능을 나타냈다.

![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(7).png?raw=true)

![Untitled](https://github.com/zzun-d/TIL/blob/master/%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0/asset/cascade_R_CNN/Untitled%20(8).png?raw=true)