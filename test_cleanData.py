def test_cleanData():
    import pandas as pd
    from cleanData import cleanData
    from pickImportData import PickImportData
    testClass = PickImportData()
    testClass.FilePath = "test_data30.csv"
    testClass.ImportFile()
    voltage, time = cleanData(testClass.outPutArray)
    for i in range(len(voltage)):
        assert isinstance(voltage[i], float) == True
        assert isinstance(time[i], float) == True
    for i in range(1,len(time)):
        assert time[i] != 0

def test_correctExcp():
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting Value Error"):
        randStr = "aegv2"
        randFloat = float(randStr)
