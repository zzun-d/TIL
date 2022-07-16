## **Point Cloud**
Lidar 센서와 RGB-D 센서 등은 물체에 빛이나 신호를 보내서 돌아오는 시간을 기록하여 센서에서부터 물체까지의 거리를 계산하고 하나의 포인트를 생성하는데 이렇게 수집된 포인트들의 집합이 바로 Point Cloud이다.

![Lidar 및 RGB-D 센서의 작동 원리](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(1).png?raw=true)

Lidar 및 RGB-D 센서의 작동 원리

Point Cloud 데이터의 성질

1. Unordered(비정형화)
    
    ![Point Cloud 데이터의 시각화 이미지(왼쪽), 실제 데이터의 저장 형태(오른쪽)](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(2).png?raw=true)
    
    Point Cloud 데이터의 시각화 이미지(왼쪽), 실제 데이터의 저장 형태(오른쪽)
    
- Point Cloud 데이터는 2D 이미지 데이터와 다르게 정형화 되어있지 않다.
2D 이미지 데이터의 경우에 정해진 N by M 크기의 격자 구조형태에 정보가 저장되지만, point cloud 데이터는 3D 공간상의 많은 점들을 순서 없이 기록하는 방식으로 데이터가 저장되기에 객체의 형상, 점들간의 상호작용 등 데이터가 가진 기하학적 특성을 파악하기 어려워 딥러닝 모델에 치명적이다.
이러한 문제점을 해결하기 위하여 Voxel 형태의 정형화된 데이터로 전처리하는 방법이 존재하지만, 그마저도 Point Cloud 데이터의 Sparse한 성질 때문에 한계가 존재한다.
1. Sparse한 성질
    
    ![20210902_3D-인공지능-데이터-Point-Cloud_그림5-2.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(3).png?raw=true)
    
- Point에 비하여 빈 공간이 훨씬 많은 Sparse한 성질이 있어서 데이터의 크기에 비하여 얻을 수 있는 유의미한 정보가 적다.

**Point based method**

- Point Cloud 데이터를 있는 그대로 해석하는 모델
    - PointNet
        
        ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(4).png?raw=true)
        
        - 모든 Point를 연산하기 때문에 연산량이 많고 모델이 무겁다.
    

**Grid based method**

- Point Cloud 데이터로부터 Feature Map을 생성하고 이를 해석하는 모델
    - VoxelNet
        
        ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(5).png?raw=true)
        
        - 주어진 Point Cloud data를 D x H x W(z, y, x축에 해당)의 Voxel로 Griding
        - 하나의 Voxel에 있는 point를 하나의 그룹으로 묶는다
        - point의 variance가 크기 때문에, voxel당 최대 point 개수를 지정하여 초과하는 voxel에서는 randomsampling을 진행하여 memory 부담을 줄인다.
        - 위 방법을 통하여 sampling bias도 줄이고, 훈련 시 variation을 주었다.
        
        ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(6).png?raw=true)
        
        - 기존 point data 인 [x, y, z, r]에다가 Voxel 내부의 점들의 local mean을 구하여 Voxel의 Centroid를 구하고 이것을 (vx, vy, vz)라 하면 새로운 Voxel에서의 새로운 데이터는 아래와 같이 구성된다.
            
            ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(7).png?raw=true)
            
        - 이 데이터로 FCN을 거쳐서 point의 feature를 뽑아내고 Element-wise Maxpool을 이용하여 Voxel 내부 대표 feature값을 붙인다.
        - point가 있는 모든 Voxel에 대하여 같은 방식으로 진행한다.
        - VFE가 진행되면서 shape 정보가 포함된 Voxel의 대표 feature를 얻을 수 있게 된다.
        
        ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(8).png?raw=true)
        
    - SECOND
        
        ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(9).png?raw=true)
        
        - Sparse Conv Layers
        
        ![img1.daumcdn.png](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(10).png?raw=true)
        
    

![Untitled](https://github.com/zzun-d/TIL/blob/master/Study%20for%20Autonomus%20Driving/assets/Untitled%20(11).png?raw=true)