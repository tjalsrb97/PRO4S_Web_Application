import glob


def load_img(idx):
    img_input_path = "project/static/lams/" + idx + "/"
    for file in glob.glob(img_input_path + "/*.npy"):
        data.append(np.load(file))
    img_train = np.array(data)
    return img_train


def load_num(idx):
    num_input_path = "project/static/excel/" + idx + ".xlsx"
