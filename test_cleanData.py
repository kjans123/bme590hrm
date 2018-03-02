def test_cleanData():
    import pandas as pd
    from cleanData import cleanData
    import math as mt
    from pickImportData import PickImportData
    testClass = PickImportData()
    testClass.FilePath = "test_data30.csv"
    testClass.ImportFile()
    voltage, time = cleanData(testClass.outPutArray)
    for i in range(len(voltage)):
        assert isinstance(voltage[i], float) is True
        assert isinstance(time[i], float) is True
        assert mt.isnan(voltage[i]) is False
        assert mt.isnan(time[i]) is False
    for i in range(1, len(time)):
        assert time[i] != 0
    assert len(voltage) == 10000


def test_correctExcp():
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting Value Error"):
        randStr = "aegv2"
        randFloat = float(randStr)
