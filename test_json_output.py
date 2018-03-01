def test_json_output():
    from pickImportData import PickImportData
    from max_min_volts_time_dur import MaxMinVoltsTimeDur
    from meanBPM import MeanBPM
    from json_output import Json_Output
    import os
    testClass = PickImportData()
    testClass.FilePath = "test_data1.csv"
    testClass.ImportFile()
    testClassBPM = MeanBPM(testClass.outPutArray)
    testClassBPM.get_mean_bpm()
    testClassBPM.convert_beat_times_list_to_np_array()
    testClassmm = MaxMinVoltsTimeDur(testClass.outPutArray)
    testJSONclass = Json_Output(testClass.FilePath, max(testClassBPM.timeList),
                                testClassBPM.timeUnit, testClassBPM.meanBPM,
                                testClassBPM.num_beat_times,
                                testClassBPM.beatTimes,
                                testClassmm.tuple_min_max_volts,
                                testClassmm.max_time_strip)
    test_data = {"time_range": 27.775,
                 "max_time": 27.775,
                 "times_of_beats": [0.6809999999999999, 1.492, 2.281, 3.072,
                                    3.861, 4.678, 5.331,
                                    6.327999999999999, 7.169, 7.978, 8.769,
                                    9.542, 10.380999999999998,
                                    11.235999999999999, 12.058,
                                    12.886, 13.708, 14.503,
                                    15.3, 16.092, 16.914, 17.783,
                                    18.605999999999998, 19.392,
                                    20.183, 20.958000000000002,
                                    21.744, 22.555999999999997,
                                    23.372, 24.2, 25.044, 25.85, 26.625],
                 "max_min_volt": (1.05, -0.68),
                 "mean_BPM": 74.006,
                 "time_unit": "s",
                 "number_of_beats": 33}
    assert testJSONclass.data["time_range"] == test_data["time_range"]
    assert testJSONclass.data["max_time"] == test_data["max_time"]
    assert testJSONclass.data["times_of_beats"] == test_data["times_of_beats"]
    assert testJSONclass.data["max_min_volt"] == test_data["max_min_volt"]
    assert testJSONclass.data["mean_BPM"] == test_data["mean_BPM"]
    assert testJSONclass.data["time_unit"] == test_data["time_unit"]
    string1 = "number_of_beats"
    assert testJSONclass.data["number_of_beats"] == test_data[string1]
    new_filename = str(testClass.FilePath).replace(".csv", "") + ".json"
    cf = os.path.isfile(new_filename)
    assert cf is True
