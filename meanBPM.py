class MeanBPM:

    def __init__(self, inputDataFrame):
        self.inputDataFrame = inputDataFrame
        self.meanBPM = None
        self.getMeanBPM()


    def get_standard_pattern(self):
        import pandas as pd
        import numpy as np
        standFilePath = "standardPattern.csv"
        sdf = pd.read_csv(standFilePath, header=None)
        vals = sdf.values
        vals = vals.squeeze()
        vals = vals.tolist()
        valsUnbiased = vals - np.mean(vals)
        valsNorm = np.sum(valsUnbiased**2)
        return(valsUnbiased)

    def getMeanBPM(self):
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import signal

        sdList = self.get_standard_pattern()
        workDF = self.inputDataFrame
        workDF.columns = ['time', 'voltage']
        voltageListi = workDF['voltage'].tolist()
        print(type(voltageListi[0]))
        voltageList = []
        for i in range(len(voltageListi)):
            
            print(float(voltageListi[i]))

        print(voltageList)
        timeList = workDF['time'].tolist()
        voltageListUnbiased = voltageList-np.mean(voltageList)
        voltageNorm = np.sum(voltageListUnbiased**2)
        voltageCor = np.correlate(voltageListUnbiased, sdList)/voltageNorm
        divList = round(len(voltageCor)/2, 0)
        divList = int(divList)

        voltageCor2 = voltageCor[divList:]



        #N = 3
        #Wn = 0.01
        #B, A = signal.butter(N, Wn, output='ba')
        #smooth_data = signal.filtfilt(B,A,voltageCor)

        #print(voltageCor2[582])
        max_peaks = signal.find_peaks_cwt(voltageCor, np.arange(1,50))

        print(max_peaks)
        print(len(max_peaks))
        max_peaks = max_peaks.tolist()
        print(type(max_peaks))
        #plt.figure(1)
        #plt.plot(sdList)
        #plt.show()
        plt.figure(2)
        #plt.plot(voltageCor)
        plt.plot(voltageCor, '-bd', markevery=max_peaks)
        plt.show()

        #plt.figure(3)
        #plt.plot(smooth_data)
        #plt.show()

from pickImportData import PickImportData
testClass = PickImportData()
testClass.FilePath = "test_data30.csv"
testClass.ImportFile()
testClassBPM = MeanBPM(testClass.outPutArray)
