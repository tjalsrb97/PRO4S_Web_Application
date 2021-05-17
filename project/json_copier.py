import json
import pandas as pd


def jsFileCopy(idx, result):
    file_path = "project/static/layers/temp_0.js"
    dataFrame = pd.read_excel(
        "project/static/excel/" + str(idx) + ".xlsx", engine="openpyxl"
    )
    dump_path = "project/static/layers/oneline_features.js"
    print(dataFrame.head)
    dataFrame['wb']
    # with open(file_path) as f:
    #     first_lines = f.readlines()
    # with open(dump_path) as dump:
    #     data = dump.read()
    #     obj = data[data.find("{") : data.rfind("}") + 1]
    #     jsonObj = json.loads(obj)
    # with open("project/static/layers/test.1.js", 'w') as go:
    #     for i in range(5):
    #         go.write(first_lines[i])
    #     go.write(str(jsonObj))
    #     go.write("]\n}\n")

    # with open(copied_fp, "w") as fw:
    #     for i in range(5):
    #         fw.write(lines[i])
    # with open(file_path) as dataFile:
    #     data = dataFile.read()
    #     obj = data[data.find("{") : data.rfind("}") + 1]
    #     jsonObj = json.loads(obj)
    #     for i in range(len(jsonObj["features"])):
    #         jsonObj["features"][i]["properties"]["wb1"] = result[i]
    # with open(copied_fp, "a") as fww:
    #     for i in range(len(jsonObj["features"])):
    #         fww.write(str(jsonObj["features"][i]))
    #         if i != len(jsonObj["features"]) - 1:
    #             fww.write(",\n")
    #         else:
    #             fww.write("\n")
    #     fww.write("]\n}\n")


jsFileCopy(214, 1)

