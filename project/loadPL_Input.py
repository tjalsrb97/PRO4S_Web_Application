# 원래 하던것 처럼 Deep Learning Model의 Input을 불러오는 파일
# Input은 idx으로 이는 실험 결과의 ap_idx가 인자로 받아들어옴
# return img_input(img test), num_input(numeric_test)
import glob


def load_input(idx):
    grid_path = "project/static/lams/" + idx
    data2 = []
    for file in glob.glob(grid_path + "/*.npy"):
        data2.append(np.load(file))
    img_test = np.array(data2)
    numeric_data_test = pd.read_excel(
        "project/static/excel/" + idx + ".xlsx", engine="openpyxl"
    )
    x_test = np.zeros((len(numeric_data_test), 4))
    for j in range(len(numeric_data_test)):
        x_test[j][0] = numeric_data_test["chai1"][j] / 240
        x_test[j][1] = numeric_data_test["chai2"][j] / 240
        x_test[j][2] = numeric_data_test["dist"][j] / 240
        x_test[j][3] = numeric_data_test["chaidist"][j] / 22000
    numeric_test = np.array(x_test)
    return img_test, numeric_test

