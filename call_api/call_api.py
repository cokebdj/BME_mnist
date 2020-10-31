import os
import tempfile

import matplotlib.pyplot as plt
import requests
from sklearn.datasets import fetch_openml


def predict_image(array):
    route = os.path.join(os.getcwd(),'file.jpg')
    plt.imshow(example)
    plt.savefig(route)
    r = requests.get(f'http://localhost:7071/api/classify?img={route}')
    response_dict = r.json()
    print(f"Alvaro dice que es el número {response_dict['predictedTagName']}")
    os.remove(route)

if __name__ == '__main__':
    mnist = fetch_openml('mnist_784')
    X = mnist.data
    example = X[0].reshape((28,28))
    predict_image(example)


