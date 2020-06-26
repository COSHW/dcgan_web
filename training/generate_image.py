import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def calc_size(length):
    if length == 1:
        return 1
    elif 1 < length < 5:
        return 2
    elif 4 < length < 10:
        return 3
    elif 9 < length <= 16:
        return 4


def generate_and_save_images(model, number, seed):
    predictions = model(seed, training=False)

    fig = plt.figure(figsize=(4, 4))
    print(predictions.shape[3])
    if predictions.shape[3] == 1:
        for i in range(predictions.shape[0]):
            img = np.array(predictions[i, :, :, 0] * 127.5 + 127.5)
            plt.subplot(calc_size(predictions.shape[0]), calc_size(predictions.shape[0]), i + 1)
            plt.imshow(img, cmap='gray')

            plt.axis('off')
    elif predictions.shape[3] == 3:
        for i in range(predictions.shape[0]):
            img = np.array(predictions[i, :, :] * 127.5 + 127.5, np.int32)
            plt.subplot(calc_size(predictions.shape[0]), calc_size(predictions.shape[0]), i + 1)
            plt.imshow(img)

    plt.savefig(r'static/train_images/{}.png'.format(number))
    plt.close()

    return r'{}.png'.format(number)
