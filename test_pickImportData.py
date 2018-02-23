def test_pickImportData():
    from pickImportData import PickImportData
    import pandas as pd
    testClass = PickImportData()
    testClass.FilePath = "test_data1.csv"
    testClass.ImportFile()
    assert type(testClass.outPutArray) == pd.core.frame.DataFrame


def test_correctExcp():
    from pickImportData import PickImportData
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        testClass2 = PickImportData()
        testClass2.FilePath = "requirements.txt"
        testClass2.ImportFile()
