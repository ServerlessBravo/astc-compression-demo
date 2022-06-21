# ASTC Encoding for images


## 部署


### 创建函数

配置：

```bash

函数类型	Event函数
运行环境	Python 3.7
资源类型	CPU
内存	512MB
初始化超时时间	65秒
执行超时时间	10秒

```


### 创建层

- 函数依赖的层，其中包含高版本的gcc 动态连接库依赖, 
- 见release文件: [1253970226_gcc_11_2_0_lib64_1.zip]()


## 测试


### 输入图片

### 输出图片


### 运行结果

```
START RequestId: a00aee93-172a-46b9-8ae3-07aa9890e0d4

Event RequestId: a00aee93-172a-46b9-8ae3-07aa9890e0d4

start main handler

Command to run: LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/lib64 ./astcenc/astcenc-sse2 -cl input.png /mnt/input.astc 6x6 -medium

b"Source image
============
    Source:                     input.png
    Color profile:              LDR
    Dimensions:                 2D, 272x170
    Components:                 4
    Compressor settings
===================
    Color profile:              LDR linear
    Block size:                 6x6
    Bitrate:                    3.56 bpp
    RGB alpha scale weight:     0
    R component weight:         1
    G component weight:         1
    B component weight:         1
    A component weight:         1
    Partition cutoff:           4 partitions
    Partition index cutoff:     26 partition ids
    PSNR cutoff:                40.5294 dB
    3 partition cutoff:         1.2
    4 partition cutoff:         1.25
    2 plane correlation cutoff: 0.75
    Block mode centile cutoff:  76%
    Candidate cutoff:           3 candidates
    Refinement cutoff:          3 iterations
    Compressor thread count:    2
    ERROR: File open failed '/mnt/input.astc'
ERROR: Failed to store compressed image
"


END RequestId: a00aee93-172a-46b9-8ae3-07aa9890e0d4

Report RequestId: a00aee93-172a-46b9-8ae3-07aa9890e0d4 Duration:244ms Memory:512MB MemUsage:17.7889MB

```

