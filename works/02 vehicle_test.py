import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 读取数据集
df = pd.read_csv('automobile.csv')

# 处理缺失值
df = df.fillna(method='ffill')

# 编码分类特征
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# 划分训练集和测试集
X = df.drop('Crash_severity', axis=1)
y = df['Crash_severity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 逻辑回归模型
lr = LogisticRegression()
lr.fit(X_train, y_train)

# 随机森林模型
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# 支持向量机模型
svm = SVC()
svm.fit(X_train, y_train)

# 交叉验证评估模型性能
lr_scores = cross_val_score(lr, X, y, cv=5, scoring='f1_macro')
print(f'Logistic Regression F1 Score (5-fold CV): {lr_scores.mean():.2f}')

rf_scores = cross_val_score(rf, X, y, cv=5, scoring='f1_macro')
print(f'Random Forest F1 Score (5-fold CV): {rf_scores.mean():.2f}')

svm_scores = cross_val_score(svm, X, y, cv=5, scoring='f1_macro')
print(f'SVM F1 Score (5-fold CV): {svm_scores.mean():.2f}')

# 在测试集上评估模型
y_pred_lr = lr.predict(X_test)
y_pred_rf = rf.predict(X_test)
y_pred_svm = svm.predict(X_test)

print('Test Set Performance:')
print(f'Logistic Regression: Accuracy={accuracy_score(y_test, y_pred_lr):.2f}, Precision={precision_score(y_test, y_pred_lr, average="macro"):.2f}, Recall={recall_score(y_test, y_pred_lr, average="macro"):.2f}, F1={f1_score(y_test, y_pred_lr, average="macro"):.2f}')
print(f'Random Forest: Accuracy={accuracy_score(y_test, y_pred_rf):.2f}, Precision={precision_score(y_test, y_pred_rf, average="macro"):.2f}, Recall={recall_score(y_test, y_pred_rf, average="macro"):.2f}, F1={f1_score(y_test, y_pred_rf, average="macro"):.2f}')
print(f'SVM: Accuracy={accuracy_score(y_test, y_pred_svm):.2f}, Precision={precision_score(y_test, y_pred_svm, average="macro"):.2f}, Recall={recall_score(y_test, y_pred_svm, average="macro"):.2f}, F1={f1_score(y_test, y_pred_svm, average="macro"):.2f}')

# 优化逻辑回归模型
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
print(f'Accuracy: {accuracy_score(y_test, y_pred_best_lr):.2f}')
print(f'Precision: {precision_score(y_test, y_pred_best_lr, average="macro"):.2f}')
print(f'Recall: {recall_score(y_test, y_pred_best_lr, average="macro"):.2f}')
print(f'F1 Score: {f1_score(y_test, y_pred_best_lr, average="macro"):.2f}')