import json


def jsFileCopy(idx, result):
    original_fp = "project/static/layers/temp_0.js"
    copied_fp = "project/static/layers/temp_" + str(idx) + ".js"

    with open(original_fp) as f:
        lines = f.readlines()
    with open(copied_fp, "w") as fw:
        for i in range(5):
            fw.write(lines[i])
    with open(original_fp) as dataFile:
        data = dataFile.read()
        obj = data[data.find("{") : data.rfind("}") + 1]
        jsonObj = json.loads(obj)
        for i in range(len(jsonObj["features"])):
            jsonObj["features"][i]["properties"]["wb1"] = result[i]
    with open(copied_fp, "a") as fww:
        for i in range(len(jsonObj["features"])):
            fww.write(str(jsonObj["features"][i]))
            if i != len(jsonObj["features"]) - 1:
                fww.write(",\n")
            else:
                fww.write("\n")
        fww.write("]\n}\n")

