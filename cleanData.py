def cleanData(input_data_frame):
    """"function that cleans input data. Finds string numerical data and
    converts to float. For non-numerical strings (i.e., 'bad data'),
    take average of value before and after and uses that in place of
    non-numerical string. Also finds 0 values in the time List and
    uses the same algorithm as above. Finally, finds float NaN's and uses
    the same algorithm as above to replace them in both volts and times

    :param input_data_frame: takes as input two-column pandas data frame
    :returns: cleaned float-type voltage list
    :returns: cleaned float-type time list
    :raises ImportError: raises error if pandas or math is not found
    :raises ValueError: raises error when non-numerical string is found
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="bme590hrmlogs.txt",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    try:
        import pandas as pd
        import math as mt
        logging.info("success: import pandas")
        workDF = input_data_frame
        workDF.columns = ['time', 'voltage']
        voltageListi = workDF['voltage'].tolist()
        voltageList = []
        for i in range(len(voltageListi)):
            if isinstance(voltageListi[i], float) is True:
                if mt.isnan(voltageListi[i]) is True:
                    logging.debug("found nan float in volt list")
                    preVal = float(voltageListi[i-1])
                    nextVal = float(voltageListi[i+1])
                    inputVal = float((preVal + nextVal)/2)
                    voltageList.append(inputVal)
                else:
                    voltageList.append(float(voltageListi[i]))
            else:
                try:
                    voltageList.append(float(voltageListi[i]))
                except ValueError:
                    logging.debug("found non-numerical string in volt list")
                    preVal = float(voltageListi[i-1])
                    nextVal = float(voltageListi[i+1])
                    inputVal = float((preVal + nextVal)/2)
                    voltageList.append(inputVal)
        logging.debug("success: created cleaned voltage List ")
        timeListi = workDF['time'].tolist()
        timeList = []
        for i in range(len(timeListi)):
            if isinstance(timeListi[i], float) is True:
                if mt.isnan(timeListi[i]) is True:
                    logging.debug("found nan float in time list")
                    preVal = float(timeListi[i-1])
                    nextVal = float(timeListi[i+1])
                    inputVal = float((preVal + nextVal)/2)
                    timeList.append(inputVal)
                else:
                    timeList.append(float(timeListi[i]))
            else:
                try:
                    timeList.append(float(timeListi[i]))
                except ValueError:
                    preVal = float(timeListi[i-1])
                    nextVal = float(timeListi[i+1])
                    inputVal = float((preVal + nextVal)/2)
                    timeList.append(inputVal)
        for i in range(1, len(timeList)):
            if timeList[i] == 0:
                logging.debug("output time list has 0")
                preVal = float(timeList[i-1])
                nextVal = float(timeList[i+1])
                inputVal = float((preVal + nextVal)/2)
                timeList[i] = inputVal
        logging.debug("success: created cleaned time List ")
        return(voltageList, timeList)
    except ImportError:
        print("pandas not found. Activate virtual env")
        logging.warning("pandas not found")
