def test_pickImportData():
    from pickImportData import PickImportData
    import pandas as pd
    testClass = PickImportData()
    testClass.FilePath = "/home/kj123/bme590hrm/test_data1.csv"
    testClass.ImportFile()
    assert type(testClass.outPutArray) == pd.core.frame.DataFrame


def test_correctExcp():
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
