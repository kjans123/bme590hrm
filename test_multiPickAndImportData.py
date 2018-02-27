def test_MultiPickAndImport():
    import pandas as pd
    from multiPickAndImportData import MultiPickAndImportData
    testClass = MultiPickAndImportData()
    setSuperList = set(testClass.superList)
    testSet = set(['test_data1.csv', 'test_data2.csv',
                   'test_data3.csv', 'test_data4.csv',
                   'test_data30.csv', 'test_data5.csv',
                   'test_data6.csv', 'test_data32.csv'])
    assert setSuperList == testSet
    df2 = pd.read_csv('test_data1.csv', header=None)
    dfArray = df2.values
    dfAnalyze = pd.DataFrame(dfArray, columns=list('AB'))
    print(dfAnalyze)
    df3 = testClass.dfList[0]
    df3Array = df3.values
    dfAnalyze2 = pd.DataFrame(df3Array, columns=list('AB'))
    print(dfAnalyze2)
    df1List = dfAnalyze['B'].tolist()
    df2List = dfAnalyze2['B'].tolist()
    assert df1List == df2List
    for i in range(len(testClass.superList)):
        assert type(testClass.dfList[i]) == pd.core.frame.DataFrame

<<<<<<< HEAD
def test_correctExcp():
=======
 def test_correctExcp():
>>>>>>> f3c70fc60ad4f8b4192255a1eb089c38430337d9
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
