import numpy as np
import math
import pandas as pd
import os
import sys

x_min = 324600  # minimum x value
y_min = 4150520  # minimum y value
z_max = 288.43

# for grayscale
under_ground = 255.0
in_terrain = 200.0
in_building = 200.0
in_sky = 0.0


def load_npy():
    dim_1 = np.load("project/static/maps/Building.npy")
    dim_2 = np.load("project/static/maps/Terrain.npy")

    return dim_1, dim_2


dim_1, dim_2 = load_npy()


def discriminant(a, b, c):
    return (
        (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),
        (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),
    )


def line_equation(a, d, gradient, z):
    return (a, a * gradient + d, z)


def sol(x1, y1, z1, gradient):
    d = y1 - gradient * x1
    a = gradient ** 2 + 1
    b = -2 * x1 + 2 * gradient * d - 2 * y1 * gradient
    c = x1 ** 2 + d ** 2 - 2 * y1 * d + y1 ** 2 - 2500
    return (
        line_equation(discriminant(a, b, c)[1], d, gradient, z1),
        line_equation(discriminant(a, b, c)[0], d, gradient, z1),
    )


def gen_image(Tx_coord, Rx_coord, name, img_width, img_height, distance):
    Tx_coord[0] = Tx_coord[0] - x_min
    Tx_coord[1] = Tx_coord[1] - y_min
    Rx_coord[0] = Rx_coord[0] - x_min
    Rx_coord[1] = Rx_coord[1] - y_min
    # print(Tx_coord[2], ' -> ', end='')
    # Tx_coord[2] += dim_1[Tx_coord[0]][Tx_coord[1]]
    # print(Tx_coord[2], ' -> ', end='')
    Rx_coord[2] = dim_1[Rx_coord[0]][Rx_coord[1]]
    if distance % 10 != 0:
        alpha = (Tx_coord[0] - Rx_coord[0]) / (distance - 3)
        beta = (Tx_coord[1] - Rx_coord[1]) / (distance - 3)
        Tx_coord[0] += alpha
        Tx_coord[1] += alpha
        Rx_coord[0] -= beta
        Rx_coord[1] -= beta
    # Tx_coord[2] += dim_1[Tx_coord[0]][Tx_coord[1]]
    # Rx_coord[2] = dim_1[Rx_coord[0]][Rx_coord[1]]
    if Tx_coord[1] == Rx_coord[1]:
        XYs = [[]]
        CentreDots = np.linspace(Tx_coord, Rx_coord, distance)
        for i in range(distance):
            XYs.append(
                getDots_Of_Orthogonal_Line(CentreDots[i], None, img_width, distance)
            )
        array_to_npy(XYs, Tx_coord, Rx_coord, name, img_width, img_height, distance)
    gradient = (Tx_coord[0] - Rx_coord[0]) / (Tx_coord[1] - Rx_coord[1])
    gradient *= -1
    CentreDots = getDottedLines(Tx_coord, Rx_coord, distance)  # CentreDots,

    # Tx와 Rx를 잇는 직선위의 점들(distance로 uniform하게 나눠짐)
    # getDottedLines의 인자의 dim=2였으므로, 2차원 배열 반환
    XYs = [[]]
    for i in range(len(CentreDots)):  # 직선위의 점을 지나고, TxRx 직선을 수직하는 선분의 양 끝점들을 받아오기
        XYs.append(
            getDots_Of_Orthogonal_Line(CentreDots[i], gradient, img_width, distance)
        )

    array_to_npy(XYs, Tx_coord, Rx_coord, name, img_width, img_height, distance)


def getDottedLines(Tx, Rx, NumOfSlice):
    return np.linspace(Tx, Rx, NumOfSlice)


def getDots_Of_Orthogonal_Line(CenterPoints, gradient, img_width, distance):
    if gradient is None:
        twoDots = []
        twoDots.append(
            (CenterPoints[0], CenterPoints[1] - (img_width / 2), CenterPoints[2])
        )
        twoDots.append(
            (CenterPoints[0], CenterPoints[1] + (img_width / 2), CenterPoints[2])
        )
        return getDottedLines(twoDots[0], twoDots[1], distance)
    twoDots = sol(CenterPoints[0], CenterPoints[1], CenterPoints[2], gradient)
    return getDottedLines(twoDots[0], twoDots[1], distance)


def array_to_npy(XYs, Tx, Rx, name, img_width, img_height, distance):
    cube = np.arange(img_width * img_height * distance).reshape(
        (img_width, img_height, distance)
    )
    for i in range(distance):
        for j in range(img_width):
            for k in range(img_height):
                cube[j][k][i] = 0

    for i in range(1, distance + 1):
        for j in range(img_width):
            for k in range(img_height):
                try:
                    x = int(np.rint(XYs[i][j][0]))
                    y = int(np.rint(XYs[i][j][1]))
                    z = int(np.rint(XYs[i][j][2] - (img_height / 2) + k))
                    if z < 0:
                        cube[k][j][i - 1] = under_ground
                    elif z < int(dim_1[y][x]):
                        cube[k][j][i - 1] = in_terrain
                    elif z < int(dim_2[y][x]):
                        cube[k][j][i - 1] = in_building
                    else:
                        cube[k][j][i - 1] = in_sky
                    if cube[k][j][i - 1] > 255:
                        cube[k][j][i - 1] = 255
                    # cube[k][j][i-1] /= 255

                    # print(str(x + x_min) + '\t' + str(y + y_min))
                except:
                    print(i, j, k)
                    print(cube.shape)
                    print(img_width, img_height, distance)
                    exit(1)
    cube = flip_or_not(
        cube, Tx[0] - Rx[0], Tx[1] - Rx[1], img_width, img_height, distance
    )
    np.save(name + ".npy", cube)


def flip_or_not(cube, a, b, img_width, img_height, distance):
    case = 0
    if a > 0:
        if b > 0:
            case = 1
    elif a < 0:
        if b >= 0:
            case = 1
    else:
        if b > 0:
            case = 1
    if case == 0:
        return cube
    if case == 1:
        f_cube = np.arange(img_width * img_height * distance).reshape(
            (img_width, img_height, distance)
        )
        for i in range(img_height):
            for j in range(img_width):
                for k in range(distance):
                    f_cube[i][j][k] = 0

        for i in range(img_height):
            for j in range(img_width):
                for k in range(distance):
                    try:
                        f_cube[i][j][k] = cube[i][j][img_width - k - 1]
                    except:
                        print(cube.shape, distance, img_width, img_height)
                        exit()
        return f_cube


def main(option, id):
    # img_width = 40
    # img_height = 40
    # distance = 40
    # dimension = "3d"

    if option == "lams":
        img_width = 20
        img_height = 20
        distance = 100
        try:
            os.stat("lams")
        except:
            os.mkdir("lams")
        # PATH server에서 제공
        train_path = (
            "lams/train_" + str(img_width) + "_" + str(img_height) + "_" + str(distance)
        )
        test_path = (
            "lams/test_" + str(img_width) + "_" + str(img_height) + "_" + str(distance)
        )
        try:
            os.mkdir(train_path)
            os.mkdir(test_path)
        except:
            print("덮어쓰기")
        excel_file = "pci13_dataset.csv"
        excel = pd.read_csv(excel_file)
        for i in range(len(excel)):
            Tx = [int(excel["TX"][i]), int(excel["TY"][i]), int(excel["TZ"][i])]
            Rx = [int(excel["RX"][i]), int(excel["RY"][i]), int(excel["RZ"][i])]
            gen_image(
                Tx,
                Rx,
                test_path + "/" + str(excel["idx"][i]),
                img_width,
                img_height,
                distance,
            )
            print(i + 1, " / ", len(excel), ": TEST")
        excel_file = "pci24567_dataset.csv"
        excel = pd.read_csv(excel_file)
        for i in range(len(excel)):
            Tx = [int(excel["TX"][i]), int(excel["TY"][i]), int(excel["TZ"][i])]
            Rx = [int(excel["RX"][i]), int(excel["RY"][i]), int(excel["RZ"][i])]
            gen_image(
                Tx,
                Rx,
                train_path + "/" + str(excel["idx"][i]),
                img_width,
                img_height,
                distance,
            )
            print(i + 1, " / ", len(excel), ": TRAIN")
    elif option == "grid":
        img_width = 20
        img_height = 20
        distance = 100
        try:
            os.stat("lams")
        except:
            os.mkdir("lams")
        try:
            os.stat("project/static/lams/" + id)
        except:
            os.mkdir("project/static/lams/" + id)
        grid_path = "project/static/lams/" + id
        excel_file = "project/static/excel/" + id + ".xlsx"
        excel = pd.read_excel(excel_file, engine="openpyxl")
        for i in range(len(excel)):
            Tx = [int(excel["TX"][i]), int(excel["TY"][i]), int(excel["TZ"][i])]
            Rx = [int(excel["RX"][i]), int(excel["RY"][i]), 2]
            gen_image(
                Tx,
                Rx,
                grid_path + "/" + str(excel["idx"][i]),
                img_width,
                img_height,
                distance,
            )
            print(i + 1, " / ", len(excel), ": GRID")
    else:
        print("invalid input.")
        exit(1)


if __name__ == "__main__":
    # option 변수 파라미터로 받기

    if len(sys.argv) != 3:
        print("lams_on_svr.py [option] [path]")
        print("[option] = lams or grid")
        print("[path] = 해당 파일 저장 위치")
        sys.exit()

    option = sys.argv[1]
    id = sys.argv[2]

    main(option, id)
