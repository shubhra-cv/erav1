# 1. Question

* 99.4% validation accuracy
* Less than 20k Parameters
* Less than 20 Epochs
* Have used BN, Dropout,
* (Optional): a Fully connected layer, have used GAP. 

# 2. Solution: Please refer S6.ipynb

## Model Summary

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              72
       BatchNorm2d-2            [-1, 8, 26, 26]              16
           Dropout-3            [-1, 8, 26, 26]               0
            Conv2d-4           [-1, 16, 24, 24]           1,152
       BatchNorm2d-5           [-1, 16, 24, 24]              32
           Dropout-6           [-1, 16, 24, 24]               0
         MaxPool2d-7           [-1, 16, 12, 12]               0
            Conv2d-8           [-1, 32, 10, 10]           4,608
       BatchNorm2d-9           [-1, 32, 10, 10]              64
          Dropout-10           [-1, 32, 10, 10]               0
           Conv2d-11              [-1, 8, 8, 8]           2,304
      BatchNorm2d-12              [-1, 8, 8, 8]              16
          Dropout-13              [-1, 8, 8, 8]               0
           Conv2d-14             [-1, 16, 6, 6]           1,152
      BatchNorm2d-15             [-1, 16, 6, 6]              32
          Dropout-16             [-1, 16, 6, 6]               0
           Conv2d-17             [-1, 16, 4, 4]           2,304
      BatchNorm2d-18             [-1, 16, 4, 4]              32
          Dropout-19             [-1, 16, 4, 4]               0
           Conv2d-20             [-1, 16, 4, 4]           2,304
      BatchNorm2d-21             [-1, 16, 4, 4]              32
          Dropout-22             [-1, 16, 4, 4]               0
           Conv2d-23             [-1, 10, 4, 4]           1,440
================================================================
Total params: 15,560
Trainable params: 15,560
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.46
Params size (MB): 0.06
Estimated Total Size (MB): 0.53
----------------------------------------------------------------




* 99.4% validation accuracy
* Less than 20k Parameters
* Less than 20 Epochs
* Have used BN, Dropout,
* (Optional): a Fully connected layer, have used GAP. 