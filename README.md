# 慧眼识蔬果蔬自助智秤系统 🍎⚖️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green)](https://opencv.org/)

## 项目概述 🌟
本项目基于树莓派 4B 打造智能电子秤系统，集成：
- **AI视觉识别**：ResNet-18 模型实现30+种果蔬识别（测试集准确率96%）
- **精准称重**：HX711 高精度传感器+动态校准算法
- **无人零售终端**：PyQt6 交互界面+支付二维码生成
- **数据中台**：MySQL 交易记录存储+销售分析

## 核心功能 🚀
### 智能识别
- 毫秒级图像处理（128x128分辨率）
- 支持多候选结果展示（Top-3预测）
- 实时视频流边缘检测优化

### 电子秤特性
- 动态去皮重功能
- 单位价格自动换算
- 重量异常检测告警

### 零售终端
- 购物车管理（增删查改）
- 交易记录云端存储
- 双模支付支持（条形码+二维码）

## 技术架构 🛠️
### 硬件配置
| 组件              | 型号              |
|-------------------|-------------------|
| 主控              | Raspberry Pi 4B  |
| 摄像头            | Logitech C920     |
| 称重传感器        | HX711+Load Cell   |
| 显示屏            | 7寸HDMI触摸屏     |

### 软件栈
```text
Python 3.8+
├── PyTorch 2.0       # 深度学习框架
├── OpenCV 4.5        # 图像处理
├── PyQt6             # 图形界面
├── HX711-Library     # 称重驱动
└── MySQL-Connector   # 数据存储
```

## 快速开始 🚦

### 环境配置

```bash
# 创建虚拟环境
conda create -n fruitscale python=3.8
conda activate fruitscale

# 安装依赖
pip install -r requirements.txt
```

### 模型训练

1. 下载Kaggle数据集：

```bash
kaggle datasets download -d kritikseth/fruit-and-vegetable-image-recognition
unzip -q fruit-and-vegetable-image-recognition.zip -d data/
```

1. 启动训练：

```bash
python models/train_model.py
```

### 运行系统

```bash
python main.py
```

## 项目结构 📂

```
fruitscale/
├── controllers/         # 业务逻辑
├── models/              # 算法模型
│   ├── detection.py     # 图像识别
│   └── weighting.py     # 称重算法
├── view/                # UI界面
├── config/              # 配置文件
└── docs/                # 文档资源
```
