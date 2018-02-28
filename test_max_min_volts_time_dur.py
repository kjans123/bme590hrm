def test_max_min_volts_time_dur():
    from pickImportData import PickImportData
    from max_min_volts_time_dur import MaxMinVoltsTimeDur
    testClass = PickImportData()
    testClass.FilePath = "test_data1.csv"
    testClass.ImportFile()
    testClassMaxMin = MaxMinVoltsTimeDur(testClass.outPutArray)
    assert testClassMaxMin.tuple_min_max_volts == (1.05, -0.68)
    assert testClassMaxMin.max_time_strip == 27.775


def test_correctExcp():
    from pickImportData import PickImportData
    from max_min_volts_time_dur import MaxMinVoltsTimeDur
    from cleanData import cleanData
    testClass = PickImportData()
    testClass.FilePath = "test_data1.csv"
    testClass.ImportFile()
    testClassMaxMin2 = MaxMinVoltsTimeDur(testClass.outPutArray)
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(AttributeError, message="Expecting AttributeError"):
        voltageList, timeList = cleanData(2)
