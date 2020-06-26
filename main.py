from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from training import generate_image
import random
import numpy
import os


def create_seed(examples_to_generate):
    seed = []
    for i in range(examples_to_generate):
        l = []
        for j in range(100):
            num = round(random.uniform(-1, 1), 8)
            l.append(num)
        seed.append(l)
    seed = numpy.array(seed)
    return seed


def generate_random(num, examples_to_generate, model_file, seed=""):
    if model_file == "*Модель":
        return "Выберите модель!"
    if examples_to_generate == "Количество экземпляров":
        examples_to_generate = 1
    if seed != "":
        seed = seed.replace(",", " ")
        seed = seed.split()
        if len(seed) == 100:
            seed = [(float(x)-127.5)/127.5 for x in seed]
            seed = numpy.array([seed])
        else:
            return "Вектор z указан неправильно!"
    else:
        seed = create_seed(int(examples_to_generate))
    print(seed)
    generator = tf.keras.models.load_model(os.path.join("models", model_file), compile=False)
    # generator = load_model(r"model.h5", compile=False)
    return generate_image.generate_and_save_images(generator, num, seed)
