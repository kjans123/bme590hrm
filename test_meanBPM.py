def test_meanBPM():
    from pickImportData import PickImportData
    from meanBPM import MeanBPM
    import numpy as np
    testClass = PickImportData()
    testClass.FilePath = "test_data1.csv"
    testClass.ImportFile()
    testClassBPM = MeanBPM(testClass.outPutArray)
    testClassBPM.get_mean_bpm()
    testClassBPM.convert_beat_times_list_to_np_array()
    assert testClassBPM.meanBPM == 74.006
    x = [0.6809999999999999, 1.492,
         2.281, 3.072, 3.861,
         4.678, 5.331, 6.327999999999999, 7.169,
         7.978, 8.769, 9.542,
         10.380999999999998, 11.235999999999999,
         12.058, 12.886, 13.708,
         14.503, 15.3, 16.092, 16.914, 17.783,
         18.605999999999998, 19.392,
         20.183, 20.958000000000002, 21.744,
         22.555999999999997, 23.372, 24.2, 25.044,
         25.85, 26.625]
    assert testClassBPM.beatTimes == x
    xn = np.array(x)
    assert np.array_equal(testClassBPM.np_beat_times, xn) is True
    testClassAb = PickImportData()
    testClassAb.FilePath = "test_data1.csv"
    testClassAb.ImportFile()
    testClassBPMAb = MeanBPM(testClass.outPutArray, 20, "ms")
    testClassBPMAb.get_mean_bpm()
    testClassBPMAb.convert_beat_times_list_to_np_array()
    assert testClassBPMAb.meanBPM == 73753.407


def test_correctExcp():
    from pickImportData import PickImportData
    from meanBPM import MeanBPM
    import numpy as np
    import pandas as pd
    from cleanData import cleanData
    testClass = PickImportData()
    testClass.FilePath = "test_data1.csv"
    testClass.ImportFile()
    testClassBPM = MeanBPM(testClass.outPutArray)
    testClassBPM.get_mean_bpm()
    testClassBPM.convert_beat_times_list_to_np_array()
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(FileNotFoundError, message="Expecting \
                       FileNotFoundError"):
        standFilePath = "standardPatter.csv"
        sdf = pd.read_csv(standFilePath, header=None)
    with pytest.raises(AttributeError, message="Expecting AttributeError"):
        voltageList, timeList = cleanData(2)
    with pytest.raises(IndexError, message="Expecting IndexError"):
        testClass2 = PickImportData()
        testClass2.FilePath = "test_data1.csv"
        testClass2.ImportFile()
        testClassBPM2 = MeanBPM(testClass.outPutArray, 200)
    with pytest.raises(ValueError, message="Expecting ValueError"):
        testClass3 = PickImportData()
        testClass3.FilePath = "test_data1.csv"
        testClass3.ImportFile()
        testClassBPM3 = MeanBPM(testClass.outPutArray, -8)
    with pytest.raises(IndexError, message="Expecting IndexError. \
                       Too many heartbeats found over interval."):
        testClass4 = PickImportData()
        testClass4.FilePath = "test_data1.csv"
        testClass4.ImportFile()
        testClassBPM4 = MeanBPM(testClass4.outPutArray, 0.5)
