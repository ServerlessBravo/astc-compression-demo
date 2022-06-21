# ASTC Compression for images


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

### 挂载 CFS


```bash
所属网络	vpc-xxxx 
所属子网	subnet-xxx
文件系统	cfs-yyyy（用户ID: 10000 | 用户组ID：10000 | 文件系统ID：cfs-yyyy | 挂载点ID：cfs-yyyy | 本地目录：/mnt/ | 远端目录：/）
```


### 创建层

- 函数依赖的层，其中包含高版本的gcc 动态连接库依赖, 
- 见release文件: [1253970226_gcc_11_2_0_lib64_1.zip](https://github.com/ServerlessBravo/astc-compression-demo/releases/download/1.0/1253970226_gcc_11_2_0_lib64_1.zip)

![](https://user-images.githubusercontent.com/251222/174716268-4e1295d0-2ede-46c4-a065-3267c01b6572.jpg)

### 绑定层

![](https://user-images.githubusercontent.com/251222/174716300-0cfd9a06-aea6-486e-9eef-b664df349d53.jpg)

## 测试


### 输入图片

input.png

![](https://github.com/ServerlessBravo/astc-compression-demo/blob/master/input.png?raw=true)

### 输出图片

input.astc

![](https://user-images.githubusercontent.com/251222/174717520-8585f41c-8b96-4f3d-bf60-aae53f197ce2.png)

### 运行结果

```
START RequestId: 508f9889-d76c-4016-b2e5-5cb78b4ded4c

Event RequestId: 508f9889-d76c-4016-b2e5-5cb78b4ded4c

start main handler

Command to run: LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/lib64 ./astcenc/astcenc-sse2 -cl input.png /mnt/input.astc 6x6 -medium

b'Source image
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
    Performance metrics
===================
    Total time:                  0.3484 s
    Coding time:                 0.2952 s
    Coding rate:                 0.1566 MT/s
    '

success: CompletedProcess(args='LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/lib64 ./astcenc/astcenc-sse2 -cl input.png /mnt/input.astc 6x6 -medium', returncode=0, stdout=b'Source image
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
    Performance metrics
===================
    Total time:                  0.3484 s
    Coding time:                 0.2952 s
    Coding rate:                 0.1566 MT/s
    ', stderr=b'')


END RequestId: 508f9889-d76c-4016-b2e5-5cb78b4ded4c

Report RequestId: 508f9889-d76c-4016-b2e5-5cb78b4ded4c Duration:390ms Memory:512MB MemUsage:19.6758MB


```

