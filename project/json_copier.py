import json
import pandas as pd
from pyproj import Transformer



def jsFileCopy(idx, result):
    dump_path1 = "project/static/layers/oneline_features.js"
    dump_path2 = "project/static/layers/oneline_features2.js"
    file_path1 = "project/static/data/temp_0.js"
    file_path2 = "project/static/data/ap_2.js"
    dataFrame = pd.read_excel(
        "project/static/excel/" + str(idx) + ".xlsx", engine="openpyxl"
    )

    lat=dataFrame['latitude'].tolist()
    longt=dataFrame['longitude'].tolist()
    Tx = dataFrame['TX'][0]                         #UTM52N AP 위치를 GPS좌표로 해서 visualization에 출력
    Ty = dataFrame['TY'][0]
    transformer = Transformer.from_crs(32652, 4326)
    trans_Tx = transformer.transform(Tx, Ty)[0]
    trans_Ty = transformer.transform(Tx, Ty)[1]

    with open(dump_path1) as f:                     # read file format, use first 5 lines for .js file
        temp_first_lines = f.readlines()                 # THIS IS FOR ~/data/temp_0.js

    with open(dump_path2) as f2:                    # read file format, use first 5 lines for .js file
        ap_first_lines = f2.readlines()             # THIS IS FOR ~/data/temp_0.js
    
    with open(dump_path1) as dump1:                  # get temp_0.js foramtted lines, transform to jsonObject
        data1 = dump1.read()
        obj1 = data1[data1.find("{") : data1.rfind("}") + 1]
        jsonObj1 = json.loads(obj1)                

    with open(dump_path2) as dump2:                          # get ap_2.js foramtted lines, transform to jsonObject
        data2 = dump2.read()
        obj2 = data2[data2.find("{") : data2.rfind("}") + 1]
        jsonObj2 = json.loads(obj2)                

    with open(file_path1, 'w') as temp:
        for i in range(5):
            temp.write(temp_first_lines[i])
        for i in range(len(dataFrame)):
            dumpJson = jsonObj1["features"][6]
            dumpJson["properties"]["rss"]=result[i][0]
            dumpJson["geometry"]["coordinates"]=[longt[i],lat[i]]
            temp.write(str(dumpJson))
            if i != len(dataFrame):
                temp.write(",\n")
            else:
                temp.write("\n")
        temp.write("]\n}\n")
        
    with open(file_path2, 'w') as ap:
        dumpJson = jsonObj2['features'][6]
        for i in range(5):
            ap.write(ap_first_lines[i])
        dumpJson['geometry']['coordinates']=[trans_Ty,trans_Tx]
        ap.write(str(dumpJson))
        ap.write("]\n}\n")
    


# jsFileCopy("326055_4151242",4)

