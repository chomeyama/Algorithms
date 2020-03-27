""" 自作ニューラルネットワーク
    一部未完成 """

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# Affine変換を抽象化したクラス
class Affine:

    # W : 重み初期値, b : バイアス初期値
    def __init__(self, W, b):
        self.W = W
        self.b = b

    #　順伝播を行うメソッド
    def forward(self, Input):
        self.Input = Input
        Output = np.dot(Input, self.W) + self.b
        return Output

    #　逆伝播を行うメソッド
    def backward(self, gradient):
        self.dW = np.dot(self.Input.T, gradient)
        self.db = np.sum(gradient, axis = 0)
        next_gradient = np.dot(gradient, self.W.T)
        # print('Affine', next_gradient)
        return next_gradient

class BatchNormalize:

    def __init__(self, coefficient = 1.0, intercept = 0.0, EPS = 10e-7):
        self.coefficient = coefficient
        self.intercept = intercept
        self.EPS = EPS
        self.running_mean = None
        self.running_var = None

    def forward(self, Input, training = True):
        self.batch_size, d = Input.shape
        if self.running_mean is None:
            self.running_mean = np.zeros(d)
            self.running_var = np.zeros(d)

        if training:
            mu = Input.mean(axis = 0)
            var = (np.sum(Input - self.mu) ** 2) / self.batch_size
            self.std = np.sqrt(self.var + self.EPS)
            self._Input = Input - self.mu
            __Input = self._Input / self.std
            self.__Input = __Input
            self.running_mean = self.momentum * self.running_mean * (1 - self.momentum) * mu
            self.running_var = self.momentum * self.running_var + (1 - self.momentum) * var
        else:
            __Input = (Input - running_mean) / np.sqrt(self.running_var + self.EPS)

        Output = self.coefficient * __Input + self.intercept
        return Output

    def backward(self, gradient):
        self.dIntercept = np.sum(gradient, axis = 0)
        self.dCoefficient = np.sum(self._Input * gradient, axis = 0)
        d__Input = self.coefficient * gradient
        d_Input = d__Input / self.std
        dstd = -np.sum((d__Input * self._Input) / (self.std * self.std), axis=0)
        dvar = 0.5 * dstd / self.std
        d__Input += (2.0 / self.batch_size) * self._Input * dvar
        dmu = np.sum(d_Input, axis=0)
        next_gradient = d_Input - dmu / self.batch_size
        return next_gradient

# シグモイド関数を抽象化したクラス
class Sigmoid:

    # a は x の係数
    def __init__(self, a = 1):
        self.a = a
        self.Output = None

    # 順伝播を行うメソッド
    def forward(self, Input):
        Output = 1 / (1 + self.a * np.exp(-Input))
        self.Output = Output
        return Output

    # 逆伝播を行うメソッド
    def backward(self, gradient):
        next_gradient = gradient * (1.0 - self.Output) * self.Output
        # print('Sigmoid', next_gradient)
        return next_gradient

# ReLU関数を抽象化したクラス
class ReLU:

    def __init__(self):
        self.garadient = None

    #　順伝播を行うメソッド
    def forward(self, Input):
        Output = np.maximum(0, Input)
        self.gradient = np.where(Output > 0, 1, 0)
        return Output

    #　逆伝播を行うメソッド
    def backward(self, gradient):
        next_gradient = self.gradient * gradient
        return next_gradient

# Softmax関数を抽象化したクラス
class SoftmaxWithCrossentropy:

    def __init__(self):
        self.Output = None

    #　順伝播を行うメソッド
    def forward(self, Input):
        exp_Input = np.exp(Input - np.max(Input))
        Output = exp_Input / np.sum(exp_Input)
        self.Output = Output
        return Output

    #　逆伝播を行うメソッド
    def backward(self, gradient):
        next_gradient = gradient
        # print('SoftmaxWithCrossentropy', next_gradient)
        return next_gradient

# 交差エントロピー関数を抽象化したクラス
# 出力層のSoftmax関数と併用する
class CrossentropyWithSoftmax:

    def __init__(self, EPS = 10e-7):
        self.EPS = EPS

    # 損失の値
    def value(self, y, t):
        value = -np.sum(t * np.log(y + self.EPS))
        return value

    # 勾配
    def gradient(self, y, t):
        gradient = y - t
        # print('CrossentropyWithSoftmax', gradient)
        return gradient

# 平均二乗和誤差関数を抽象化したクラス
class MSE:

    def __init__(self):
        pass

    # 損失の値
    def value(self, y, t):
        value = 0.5 * np.sum((y - t) ** 2)
        return value

    # 勾配
    def gradient(self, y, t):
        gradient = y - t
        return gradient

class SGD:

    def __init__(self, lr = 0.1):
        self.lr = lr

    def update(self, params, params_num):
        for i in range(params_num):
            params[i].W -= self.lr * params[i].dW
            params[i].b -= self.lr * params[i].db

class Momentum:

    def __init__(self, momentum = 0.1, lr = 0.1):
        self.momentum = momentum
        self.lr = lr
        self.init = True
        self.v_W = {}
        self.v_b = {}

    def update(self, params, params_num):
        if self.init == True:
            for i in range(params_num):
                self.v_W[i] = np.zeros_like(params[i].W)
                self.v_b[i] = np.zeros_like(params[i].b)
            self.init = False
        for i in range(params_num):
            self.v_W[i] = self.momentum * self.v_W[i] - self.lr * params[i].dW
            self.v_b[i] = self.momentum * self.v_b[i] - self.lr * params[i].db
            params[i].W += self.v_W[i]
            params[i].b += self.v_b[i]

# class Adagrad:
#
#     def __init__(self):
#
#     def update(self, param):


# ニューラルネットワークを抽象化したクラス
class Neural_Network:

    # レイヤーを順に格納するリスト
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.last_size = input_size
        self.output_size = output_size
        self.layers = []
        self.parameters = {}
        self.count_param_num = 0

    #　レイヤーを追加して格納するメソッド
    def add_Affine(self, affine):
        self.layers.append(affine)
        self.parameters[self.count_param_num] = affine
        self.count_param_num += 1

    def add_activation(self, activation):
        self.layers.append(activation)

    def cmpl(self, loss, optimizer):
        self.loss = loss
        self.optimizer = optimizer
        print(self.layers)

    # 順伝播を行うメソッド
    def forward(self, Input):
        for layer in self.layers:
            next_Input = layer.forward(Input)
            Input = next_Input
        Output = next_Input
        return Output

    # 逆伝播を行うメソッド
    def backward(self, gradient):
        for layer in self.layers[::-1]:
            next_gradient = layer.backward(gradient)
            gradient = next_gradient
        # print()

    def update(self):
        self.optimizer.update(self.parameters, self.count_param_num)

    # クラスの予測を行うメソッド
    def predict(self, X):
        Output = self.forward(X)
        return np.argmax(Output, axis = 1)

    def fit(self, train_X, train_t, lr = 0.1, batch_size = 10, max_epoch = 100, show_process = False):

        # 訓練データのサイズ
        train_size = train_X.shape[0]

        for epoch in range(1, max_epoch + 1):
            perm = np.random.permutation(train_size)
            loss = 0
            for i in range(0, train_size, batch_size):
                batch_mask = perm[i : min(i + batch_size, train_size)]
                batch_X = train_X[batch_mask]
                batch_t = train_t[batch_mask]
                if batch_X.ndim == 1:
                    batch_X.reshape(1, self.input_size)
                if batch_t.ndim == 1:
                    batch_t.reshape(1, self.output_size)

                Output = self.forward(batch_X)
                loss += self.loss.value(Output, batch_t)
                gradient = self.loss.gradient(Output, batch_t)
                self.backward(gradient)
                self.update()
                # print(self.parameters[0].W)

            # 学習の様子を出力
            score = self.score(train_X, train_t)
            if show_process:
                print("エポック数 : {}\n    誤差平均 : {:.4f}\n    訓練データ正解率 : {:.2f} %"
                      .format(epoch, loss / train_size, score * 100))

    # 認識率を計算するためのメソッド
    def score(self, X, t):

        # ワンホットベクトルのラベル表現
        correct_label = np.argmax(t, axis = 1)
        Output = self.forward(X)
        pred = np.argmax(Output, axis = 1)

        # cnt は正解数
        cnt = 0
        for p, y in zip(pred, correct_label):
            cnt += (p == y)
        return cnt / len(pred)

def Initializer(initializer, node_nums):
        Ws = []
        bs = []
        pre_num = node_nums[0]
        if initializer == 'Xavier' or initializer == 'xavier':
            for node_num in node_nums[1:]:
                W = np.random.randn(pre_num, node_num) / np.sqrt(pre_num)
                b = np.random.randn(node_num) / np.sqrt(pre_num)
                pre_num = node_num
                Ws.append(W)
                bs.append(b)
        elif initializer == 'He' or initializer == 'he':
            for node_num in node_nums:
                W = np.random.randn(pre_num, node_num) / np.sqrt(pre_num / 2)
                b = np.random.randn(node_num) / np.sqrt(pre_num / 2)
                pre_num = node_num
                Ws.append(W)
                bs.append(b)
        else:
            print("Invalid Initializer")
        return Ws, bs

# ワンホットベクトルを作る関数
# y ： 変換前のベクトル, c : クラス数
def make_one_hot(y, c):
    return np.array([[0] * (i) + [1] + [0] * (c - 1 - i) for i in y])

# 必要なモジュールの読み込み
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# データの読み込み
iris = load_iris()

# データの処理
train_X, test_X, train_t, test_t = train_test_split(iris['data'], iris['target'], test_size = 0.2, random_state = 0)

# 正解データをワンホットベクトルにする
train_t = make_one_hot(train_t, 3)
test_t = make_one_hot(test_t, 3)

print(train_X.shape)
print(train_t.shape)

W, b = Initializer('Xavier', [4, 5, 3])

affine0 = Affine(W[0], b[0])
affine1 = Affine(W[1], b[1])

# ニューラルネットワーク構築
NN = Neural_Network(input_size=4, output_size=3)
NN.add_Affine(affine0)
NN.add_activation(Sigmoid())
NN.add_Affine(affine1)
# NN.add_activation(Sigmoid())
# NN.add_Affine(affine2)
# NN.add_activation(Sigmoid())
NN.add_activation(SoftmaxWithCrossentropy())

# NN.cmpl(loss = MSE(), optimizer = SGD())
# NN.cmpl(loss = CrossentropyWithSoftmax(), optimizer=SGD())
NN.cmpl(loss = CrossentropyWithSoftmax(), optimizer = Momentum(momentum=0.2, lr = 0.1))
# NN.cmpl(loss = MSE(), optimizer=Momentum(momentum = 0.1, lr = 0.1))

# 学習をする
NN.fit(train_X, train_t, batch_size = 10, max_epoch = 50, show_process = True)
