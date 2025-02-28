# 项目介绍

利用树莓派、usb摄像头和称重模块组成的果蔬自动识别电子秤。

```
├──│  .gitignore
│  cart.py
│  class_dict.py
│  main.py # 主程序入口
│  README.md
│  requirements.txt # Python 第三方库
│
├─controllers # 控制器
│    main_window.py
│    pay_dialog.py
│    select_dialog.py
├─models # 逻辑
│    convertion.py
│    detection.py
│    payment_generator.py
│    train_model.py
│    weighting.py
└─view # UI 界面
        main.ui
        pay_dialog.ui
        select.ui 
```



## 如何运行

首先创建虚拟环境或 conda 环境，然后下载所需第三方库。

```bash
pip install -r requirements.txt
```

训练模型，数据在 https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition/data，也可以自行添加训练数据。
```bash
python train_model.py
```

训练完成后，会保存为本地 model.pth 文件。

```bash
python main.py
```