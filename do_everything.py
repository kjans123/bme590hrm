def main():
    """"function that combines all of the previous classes (PickImportData,
    MultiPickAndImportData, MeanBPM, MaxMinVoltsTimeDur, Json_Output) to
    convert a csv raw ECG data file to a json file with variables
    1. Mean BPM over time range.
    2. Tuple for maximum voltage and minimum voltage in ECG strip.
    3. Number of beat events detected.
    4. List of times of each beat event (also converted to numpy array
    if needed).
    5. Maximum Time on ECG strip.
    6. User input time range for analysis.
    7. User input time units (eg. seconds or minutes).
    8. Name of the csv file.

    :param x: corresponds to time range over which the analysis is done
    :param y:  corresponds to the time unit of the ECG test
    :param z: corresponds to the type of test to run. Multi file or single
              pick
    :returns: json file with the same name as the ECG csv file
    """
    args = parse_cli()
    x = args.x
    y = args.y
    z = args.z

    if z != "m":
        from pickImportData import PickImportData
        from meanBPM import MeanBPM
        from max_min_volts_time_dur import MaxMinVoltsTimeDur
        from json_output import Json_Output
        runSingleClass = PickImportData()
        runSingleClass.PickFile()
        runSingleClass.ImportFile()
        runSingleClassBPM = MeanBPM(runSingleClass.outPutArray, x, y)
        runSingleClassBPM.get_mean_bpm()
        runSingleClassBPM.convert_beat_times_list_to_np_array()
        runSingleClassMM = MaxMinVoltsTimeDur(runSingleClass.outPutArray)
        runSingleClassJSON = Json_Output(runSingleClass.FilePath,
                                         runSingleClassBPM.timeRange, y,
                                         runSingleClassBPM.meanBPM,
                                         runSingleClassBPM.num_beat_times,
                                         runSingleClassBPM.beatTimes,
                                         runSingleClassMM.tuple_min_max_volts,
                                         runSingleClassMM.max_time_strip)
    else:
        from multiPickAndImportData import MultiPickAndImportData
        from meanBPM import MeanBPM
        from max_min_volts_time_dur import MaxMinVoltsTimeDur
        from json_output import Json_Output
        runMultiClass = MultiPickAndImportData()
        for i in range(len(runMultiClass.dfList)):
            print(runMultiClass.superList[i])
            df = runMultiClass.dfList[i]
            runMultiClassBPM = MeanBPM(df, x, y)
            runMultiClassBPM.get_mean_bpm()
            runMultiClassBPM.convert_beat_times_list_to_np_array()
            runMultClassMM = MaxMinVoltsTimeDur(df)
            runMultiClassJSON = Json_Output(runMultiClass.superList[i],
                                            runMultiClassBPM.timeRange, y,
                                            runMultiClassBPM.meanBPM,
                                            runMultiClassBPM.num_beat_times,
                                            runMultiClassBPM.beatTimes,
                                            runMultClassMM.tuple_min_max_volts,
                                            runMultClassMM.max_time_strip)


def parse_cli():
    """"function that takes in arguments from command line. Will take
    arguements for range of time, units of time and whether or not
    the user wants to analyze multiple files or pick one

    :returns: args
    """
    import argparse as ap

    par = ap.ArgumentParser(description="find data from ECG csv",
                            formatter_class=ap.ArgumentDefaultsHelpFormatter)

    par.add_argument("--x",
                     dest="x",
                     help="time range",
                     type=float,
                     default=None)

    par.add_argument("--y",
                     dest="y",
                     help="units of time",
                     type=str,
                     default="s")

    par.add_argument("--z",
                     dest="z",
                     help="single pick or multi pick",
                     type=str,
                     default="m")

    args = par.parse_args()
    return args

if __name__ == "__main__":
    main()
