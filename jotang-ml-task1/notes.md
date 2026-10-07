1. `scikit-learn`（简称 sklearn）是 Python 机器学习经典库，专门用来生成数据集、划分训练测试集、评估模型好坏。
2. `make_moons`:**生成月牙形（双半月）二分类数据集**，就是 MLP 例子里的月牙样本。
3. `sklearn.model_selection`:把全部数据集切分成「训练集」和「测试集」
4. `confusion_matrix`,` ConfusionMatrixDisplay`:模型训练完之后，**评估分类效果，画混淆矩阵**
5. `随机种子`：计算机里的 “随机”**不是真随机，是伪随机**。
随机种子就是给伪随机算法设定一个**起始密码**，同一个种子，每次跑出来的随机结果完全一样。
6. `scatter（）`画散点图
7. `X[:,0]`是去所有样本第0列的意思
8. `stratify=y`是按照比例分层抽样
9. `X_train = torch.FloatTensor(X_train)`是将numpy的数组转换成PyTorch的专用张量Tensor
10. `unsqueeze(1)`是给标签增加一维，适配二分类损失函数输入格式
11. `MLP`模型就是多层感知机
12. `nn.Module`是PyTorch网络的写法
13. `__init__`是构造函数的意思
14. `input_dim`是每个样本的输入特征，`hidden_dim`是每隐藏层的神经元个数，`output_dim`是输出维度
15. `super().__init__()`调用父类init构造函数，把父类该初始化的初始化
16. `nn.Sequential`把一堆层打包串在一起，数据按顺序往后走
17. 激活函数负责弯折数据，让第二层可以画出曲线分割边界
18. `forward（x）`定义前向传播，输入x，输出预测结果
20. `BCEWithLogitsLoss`是二分类专用损失函数，接受网络原始分数，内部自动算sigmoid，评估预测和真实标签差距
21. `model.parameters()`把全部参数交给优化器，学习率就是每一次改动的幅度
22. `混淆矩阵`：可以清晰直观的看出哪一类被漏掉
23. `with torch.no_grad()`：**不计算梯度，节省显存，不更新参数**，验证集只评估。
24. `if epoch % 100 == 0`每一百行打印一次，输出更加清爽
25. `model.state_dict()`只存网络的参数（偏置、权重）
26. `plt.rcParams["font.family"] = ["SimHei"]`修改了全局图像的字体
27.` plt.rcParams["axes.unicode_minus"] = False`使负号正常显示
28. 函数调用用圆括号
29. `np.arange`：按步长 0.01，生成一长串连续坐标点
30. `np.meshgrid`：生成密密麻麻的网格点。
31. `xx.ravel()` / `yy.ravel()`：把二维网格摊平成一维
32. `np.c_[...]`：把两组一维数拼接成 N 行 2 列的矩阵（每一行是一个坐标点）
33. `contourf`：画**填充等高线**。把网格区域按预测类别填充颜色，alpha=0.4 是透明度。