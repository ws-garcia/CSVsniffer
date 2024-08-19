import os
import platform

from test_runner import runner

def main(threshold: int, data_threshold: int):
     basePath = os.path.dirname(os.path.dirname(__file__))
     out_path = []
     sys_name = platform.platform(aliased=True,terse=True)
     data_loaded = 'All' if data_threshold == -1 else data_threshold  
     out_path.append(os.path.join(basePath, 'tests results', sys_name, 'Python_sniffer' + '-%r characters loaded' %6144))
     out_path.append(os.path.join(basePath, 'tests results', sys_name, 'CSVsniffer' + '-%r records loaded' %threshold))
     out_path.append(os.path.join(basePath, 'tests results', sys_name, 'CleverCSV' + '-%r characters loaded' %data_loaded))
     for opath in out_path:
          if not os.path.exists(opath):
               os.makedirs(opath)
     _runner = []
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[0],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=threshold,
                      sniffer='Python sniffer',
                      data_threshold=6144))
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[1],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=threshold))
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[2],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=threshold,
                      sniffer='CleverCSV',
                      data_threshold=data_threshold))
     for obj in _runner:
          obj.run(base_path=basePath,
                    output_file_names=['[POLLOCK]_output.txt',
                                    '[W3C-CSVW]_output.txt',
                                    '[CSV Wrangling]_output.txt',
                                    '[CSV Wrangling (no codec issues)-ONLY MESSY= False]_output.txt', 
                                    '[CSV Wrangling (no codec issues)-ONLY MESSY= True]_output.txt'],
                    expected_results_csv_names=['POLLOCK-dialect_annotations.txt',
                                                                'W3C-CSVW-dialect_annotations.txt',
                                                                'CCSV-manual_Dialect_Annotation.txt',
                                                                'CCSV-manual_Dialect_Annotation_CODEC.txt',
                                                                'CCSV-manual_Dialect_Annotation_CODEC.txt'],
                    test_sets=['CSV', 'W3C-CSVW', 'CSV_Wrangling', 'CSV_Wrangling', 'CSV_Wrangling']
                    )

def runsingleTest(threshold: int, \
                  data_threshold: int, \
                    detector: str):
     basePath = os.path.dirname(os.path.dirname(__file__))
     out_path = []
     sys_name = platform.platform(aliased=True,terse=True)
     limit = threshold if detector == 'CSVsniffer' else data_threshold
     pw = 'records' if detector == 'CSVsniffer' else 'characters'
     out_path.append(os.path.join(basePath, 'tests results', sys_name, detector + '-%r ' + pw + 'loaded' %limit))
     for opath in out_path:
          if not os.path.exists(opath):
               os.makedirs(opath)
     _runner = []
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[0],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=10,
                      sniffer=detector,
                      data_threshold=-1))
     for obj in _runner:
          obj.run(base_path=basePath,
                    output_file_names=['[POLLOCK]_output.txt',
                                    '[W3C-CSVW]_output.txt',
                                    '[CSV Wrangling]_output.txt',
                                    '[CSV Wrangling (no codec issues)-ONLY MESSY= False]_output.txt', 
                                    '[CSV Wrangling (no codec issues)-ONLY MESSY= True]_output.txt'],
                    expected_results_csv_names=['POLLOCK-dialect_annotations.txt',
                                                                'W3C-CSVW-dialect_annotations.txt',
                                                                'CCSV-manual_Dialect_Annotation.txt',
                                                                'CCSV-manual_Dialect_Annotation_CODEC.txt',
                                                                'CCSV-manual_Dialect_Annotation_CODEC.txt'],
                    test_sets=['CSV', 'W3C-CSVW', 'CSV_Wrangling', 'CSV_Wrangling', 'CSV_Wrangling']
                    )
if __name__ == "__main__":
     #main(10,-1)
     runsingleTest(10,6144,'CleverCSV')
