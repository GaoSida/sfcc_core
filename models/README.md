# 模型使用说明

#### boosting.py的使用说明

1、命令行使用
python boosting.py <train_file> <test_file> <n_estimators> <max_depth> <learning_rate> <nthread> <task_type>
决策树boosting
工作目录在当前目录(models/)
* train_file 训练集文件路径
* test_file 测试集文件路径
* n_estimators 迭代轮数，在这里是决策树数量
* max_depth 决策树深度
* learning_rate 学习率，xgboost是根据梯度调整权重的
* nthread 多线程数量
* task_type 任务类型，有'cv'和'sub'两种，其中'cv'是交叉验证（这里默认将测试集分两折进行验证），'sub'是提交模式，会在submission文件夹下创建提交文件，文件名会输出到屏幕上。

这里用了实现Scikit-Learn的API，还有一些高级选项，太多了，需要的话改代码吧。。
https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn

#### baselines.py的使用说明

1、命令行使用
本脚本可以指定使用的机器学习模型，训练和测试文件，交叉验证文件，使用的特征和模型参数等等。样例脚本为`0_direct.bash`文件。

参数说明如下（这些参数必须按顺序输入，一个都不能少）：

* alias：本次实验代号。一个任意字符串。
* train_file：完整训练集。数据文件的根目录都是`sfcc/features/`，输入时省略。
* test_file：完整测试集。
* fold_0_file：一折文件。其处理过程中不应引入另一折的分类结果信息。
* fold_1_file：另一折文件。
* feature_cols：使用的feature，用逗号隔开。其中支持注释，两条'|'之间的特征是不要的。比如`"a,b,|c,d,|e"`则只有a,b,e三个特征。
* label_col：标签列的名字。
* model_type：模型名字，需要和`name2model`字典中一致。
* model_params：模型参数。形式为`参数名:参数类型:参数值`，不同参数之间用空格分开。i为整型，f为浮点型，b为布尔型，s为字符串型。
* pred_dir：目前没有用。可以输入一个目录名用于保存交叉验证的预测结果等等。由于预测结果文件太大，我们暂时不保存。
* log_file：记录本次实验数据的文件名。实验的参数和结果都会完整记录。
* mode：为sub时会生成提交的预测结果。否则只做交叉验证。

命令行输出的信息中，比较有用的就是LogLoss，是两折交叉验证的平均值。

2、在如下情况下需要修改代码：

* 增加新模型：在`name2model`字典中增加新的项即可；
* 更改输出精度：最后一行设置这个值，当前为3位小数；

3、目前支持的模型：

* lr: Logistic Regression
* rf: Random Forest
* nb: Naive Bayes
* gb: Gradient Boosting

每个模型可以调整的参数参见sklearn官网。