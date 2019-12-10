import time, random
from src.sensors.utils import end, sendDataToTipboard, getTimeStr

NAME_OF_SENSORS = "simple_percentage"
TILE_TEMPLATE = "simple_percentage"
TILE_ID = "sp_ex"


def executeScriptToGetData():
    """ Simulate some actions for text tile exemple"""
    lv = random.randrange(1, 49)
    rl = random.randrange(1, 49)
    bv = lv + rl
    return {"title": "Sensor title",
            "subtitle": "Sensor subtitle",
            "big_value": f"{bv}%",
            "left_label": "Random label 1", "left_value": f"{lv}%",
            "right_label": "Random label 2", "right_value": f"{rl}%"}


def sonde5(isTest):
    print(f"{getTimeStr()} (+) Starting sensors 5", flush=True)
    start_time = time.time()
    data = executeScriptToGetData()
    tipboardAnswer = sendDataToTipboard(data, tile_template=TILE_TEMPLATE, tile_id=TILE_ID, isTest=isTest)
    end(title=f"sensors5 -> {TILE_ID}", start_time=start_time, tipboardAnswer=tipboardAnswer, TILE_ID=TILE_ID)
