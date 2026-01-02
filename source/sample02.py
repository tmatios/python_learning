# 簡単な機械学習プログラム
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# データセットの読み込み
iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

# モデルの訓練
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# モデルの評価
print(f"精度: {knn.score(X_test, y_test)}")
