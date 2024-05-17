import numpy as np
from tensorflow.keras.datasets import mnist

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # 初始化网络参数
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        exp_scores = np.exp(x)
        return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    def forward_propagation(self, X):
        layer1 = self.sigmoid(np.dot(X, self.W1) + self.b1)
        layer2 = self.softmax(np.dot(layer1, self.W2) + self.b2)
        return layer1, layer2

    def back_propagation(self, X, y, layer1, layer2, learning_rate):
        # 获取样本数量
        m = X.shape[0]
        # 计算 W2 的梯度
        dW2 = (1 / m) * np.dot(layer1.T, (layer2 - y))
        # 计算 b2 的梯度
        db2 = (1 / m) * np.sum(layer2 - y, axis=0, keepdims=True)
        # 计算隐层的梯度
        dlayer1 = np.dot(layer2 - y, self.W2.T)
        # 计算 W1 的梯度
        dW1 = (1 / m) * np.dot(X.T, dlayer1 * layer1 * (1 - layer1))
        # 计算 b1 的梯度
        db1 = (1 / m) * np.sum(dlayer1 * layer1 * (1 - layer1), axis=0, keepdims=True)

        # 更新 W1 和 b1
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        # 更新 W2 和 b2
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2

    def train(self, X_train, y_train, epochs, learning_rate):
        for epoch in range(epochs):
            layer1, layer2 = self.forward_propagation(X_train)
            self.back_propagation(X_train, y_train, layer1, layer2, learning_rate)
            if (epoch+1) % 100 == 0:
                print(f"Epoch [{epoch+1}/{epochs}], Loss: {np.mean(-(y_train * np.log(layer2))):.4f}")

    def evaluate(self, X_test, y_test):
        layer1, layer2 = self.forward_propagation(X_test)
        predictions = np.argmax(layer2, axis=1)
        accuracy = np.mean(predictions == np.argmax(y_test, axis=1))
        return accuracy

# 加载 MNIST 数据集
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 数据预处理
X_train = X_train.reshape(X_train.shape[0], -1) / 255.0
X_test = X_test.reshape(X_test.shape[0], -1) / 255.0
y_train = np.eye(10)[y_train]
y_test = np.eye(10)[y_test]

# 创建并训练模型
model = FeedForwardNN(input_size=784, hidden_size=128, output_size=10)
model.train(X_train, y_train, epochs=10000, learning_rate=0.01)

# 评估模型
accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")