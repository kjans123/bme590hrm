def test_MultiPickAndImport():
    import pandas as pd
    from multiPickAndImportData import MultiPickAndImportData
    testClass = MultiPickAndImportData()
    setSuperList = set(testClass.superList)
    testSet = set(['test_data1.csv', 'test_data2.csv',
                   'test_data3.csv', 'test_data4.csv',
                   'test_data30.csv', 'test_data5.csv',
                   'test_data6.csv', 'test_data32.csv',
                   'test_data7.csv', 'test_data8.csv',
                   'test_data9.csv', 'test_data10.csv',
                   'test_data11.csv', 'test_data12.csv',
                   'test_data13.csv', 'test_data14.csv',
                   'test_data15.csv', 'test_data16.csv',
                   'test_data17.csv', 'test_data18.csv',
                   'test_data19.csv', 'test_data20.csv',
                   'test_data21.csv', 'test_data22.csv',
                   'test_data23.csv', 'test_data24.csv',
                   'test_data25.csv', 'test_data26.csv',
                   'test_data27.csv', 'test_data28.csv',
                   'test_data29.csv', 'test_data31.csv'])
    assert setSuperList == testSet
    df2 = pd.read_csv('test_data27.csv', header=None)
    dfArray = df2.values
    dfAnalyze = pd.DataFrame(dfArray, columns=list('AB'))
    df3 = testClass.dfList[25]
    df3Array = df3.values
    dfAnalyze2 = pd.DataFrame(df3Array, columns=list('AB'))
    df1List = dfAnalyze['B'].tolist()
    df2List = dfAnalyze2['B'].tolist()
    assert df1List == df2List
    for i in range(len(testClass.superList)):
        assert type(testClass.dfList[i]) == pd.core.frame.DataFrame


def test_correctExcp():
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFun
