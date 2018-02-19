def test_MultiPickAndImport():
    from multiPickAndImportData import MultiPickAndImportData
    testClass = MultiPickAndImportData()
    assert testClass.superList == ['test_data1.csv', 'test_data2.csv',
                                   'test_data3.csv', 'test_data4.csv',
                                   'test_data5.csv', 'test_data6.csv']


def test_correctExcp():
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
