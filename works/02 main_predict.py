import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# 读取数据集
df = pd.read_csv('automobile.csv')

# 选择特征
"""
Vehicle_type: 车辆类型,可能与碰撞严重程度有关。
Engine_type: 发动机类型,可能会影响车辆性能和安全性。
Engine_displacement: 发动机排量,也可能影响车辆性能和安全性。
Transmission_type: 变速箱类型,影响车辆操控性。
Number_of_cylinders: 缸数,影响发动机性能。
Vehicle_weight: 车重,与碰撞能量直接相关。
Safety_rating: 安全评级,反映了车辆被动安全性能。
Number_of_airbags: 气囊数量,影响碰撞中的乘员保护。
ABS_presence: 是否有 ABS 系统,影响制动性能。
ESC_presence: 是否有电子稳定控制系统,影响车辆稳定性。
TCS_presence: 是否有牵引力控制系统,影响车辆抓地力。
TPMS_presence: 是否有胎压监测系统,影响行车安全。
Crash_location: 碰撞地点,可能与道路状况和环境有关。
Weather_conditions: 天气条件,可能影响车辆控制和制动。
Road_surface_conditions: 道路表面情况,影响车辆附着力。
Time_of_day: 发生事故的时间,可能与人为因素有关。
Day_of_week: 发生事故的星期几,可能与人为因素有关。
Driver_age: 驾驶员年龄,可能影响驾驶技术和判断力。
Driver_gender: 驾驶员性别,可能影响驾驶行为。
这些特征涵盖了车辆本身的性能参数、安全参数,以及外部环境因素和人为因素,应该能较好地反映影响碰撞严重程度的主要因素。
"""
features = ['Vehicle_type', 'Engine_type', 'Engine_displacement', 'Transmission_type', 'Number_of_cylinders',
           'Vehicle_weight', 'Safety_rating', 'Number_of_airbags', 'ABS_presence', 'ESC_presence', 'TCS_presence',
           'TPMS_presence', 'Crash_location', 'Weather_conditions', 'Road_surface_conditions', 'Time_of_day',
           'Day_of_week', 'Driver_age', 'Driver_gender']
X = df[features]
y = df['Crash_severity']

# One-Hot 编码
encoder = OneHotEncoder()
X = encoder.fit_transform(X).toarray()

# 填充缺失值
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 逻辑回归
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_train_score = lr.score(X_train, y_train)
lr_test_score = lr.score(X_test, y_test)
print('Logistic Regression Train Accuracy:', lr_train_score)
print('Logistic Regression Test Accuracy:', lr_test_score)

# 决策树
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt_train_score = dt.score(X_train, y_train)
dt_test_score = dt.score(X_test, y_test)
print('Decision Tree Train Accuracy:', dt_train_score)
print('Decision Tree Test Accuracy:', dt_test_score)

# 随机森林
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
rf_train_score = rf.score(X_train, y_train)
rf_test_score = rf.score(X_test, y_test)
print('Random Forest Train Accuracy:', rf_train_score)
print('Random Forest Test Accuracy:', rf_test_score)

# 比较实验结果
print('Comparison of model performance:')
print('Logistic Regression Train Accuracy:', lr_train_score)
print('Logistic Regression Test Accuracy:', lr_test_score)
print('Decision Tree Train Accuracy:', dt_train_score)
print('Decision Tree Test Accuracy:', dt_test_score)
print('Random Forest Train Accuracy:', rf_train_score)
print('Random Forest Test Accuracy:', rf_test_score)

# 交叉验证
print('\nCross-validation results:')
# 逻辑回归
lr = LogisticRegression()
lr_scores = cross_val_score(lr, X, y, cv=5, scoring='f1_macro')
print('Logistic Regression F1-score (macro average):', lr_scores.mean())

# 决策树
dt = DecisionTreeClassifier()
dt_scores = cross_val_score(dt, X, y, cv=5, scoring='f1_macro')
print('Decision Tree F1-score (macro average):', dt_scores.mean())

# 随机森林
rf = RandomForestClassifier()
rf_scores = cross_val_score(rf, X, y, cv=5, scoring='f1_macro')
print('Random Forest F1-score (macro average):', rf_scores.mean())

# 优化逻辑回归模型
"""
使用GridSearchCV 对逻辑回归模型的超参数进行了网格搜索和优化
"""
param_grid = {
    'C': [0.1, 1, 10],
    'penalty': ['l1', 'l2'],
    'max_iter': [100, 500, 1000]
}

lr_opt = LogisticRegression()
grid_search = GridSearchCV(lr_opt, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 获取最佳逻辑回归模型
best_lr = grid_search.best_estimator_

# 在测试集上评估最佳逻辑回归模型
y_pred_best_lr = best_lr.predict(X_test)
print('Optimized Logistic Regression Test Set Performance:')
print(f'F1 Score: {f1_score(y_test, y_pred_best_lr, average="macro"):.2f}')