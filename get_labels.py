from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
# Load the trained model
model = load_model('FruitModel.h5')
labels = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum',
          'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant',
          'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango',
          'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato',
          'raddish', 'soy beans', 'spinach', 'sweet potato', 'sweetcorn', 'tomato', 'turnip', 'watermelon']
labels_dict = {'apple': '苹果', 'banana': '香蕉', 'beetroot': '甜菜根', 'bell pepper': '甜椒', 'cabbage': '卷心菜',
               'capsicum': '辣椒',
               'carrot': '胡萝卜', 'cauliflower': '花椰菜', 'chilli pepper': '辣椒', 'corn': '玉米', 'cucumber': '黄瓜',
               'eggplant': '茄子',
               'garlic': '大蒜', 'ginger': '生姜', 'grapes': '葡萄', 'jalepeno': '墨西哥胡椒', 'kiwi': '猕猴桃',
               'lemon': '柠檬', 'lettuce': '生菜', 'mango': '芒果',
               'onion': '洋葱', 'orange': '橙子', 'paprika': '辣椒粉', 'pear': '梨', 'peas': '豌豆',
               'pineapple': '菠萝', 'pomegranate': '石榴', 'potato': '土豆',
               'raddish': '红萝卜', 'soy beans': '大豆', 'spinach': '菠菜', 'sweet potato': '红薯',
               'sweetcorn': '甜玉米', 'tomato': '西红柿', 'turnip': '蔓菁', 'watermelon': '西瓜'}


def getClass(location):
    img = load_img(location, target_size=(224, 224, 3))
    img.show()
    img = img_to_array(img)
    img = img / 255
    img = np.expand_dims(img, [0])
    answer = model.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = labels[y]
    return labels_dict[res]

    # img = output("./images/test_cabbage.jpg")
    # print(img)

# if __name__ == '__getLabels__':
#     location = sys.argv[1]
#     img = output(location)
#     # print(img)
#     sys.exit(img)
