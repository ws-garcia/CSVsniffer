import os
import platform

from test_runner import runner

def runsingleTest(threshold: int, \
                  data_threshold: int, \
                    detector: str):
     basePath = os.path.dirname(os.path.dirname(__file__))
     out_path = []
     sys_name = platform.platform(aliased=True,terse=True)
     limit = threshold  if detector == 'CSVsniffer' else data_threshold
     fw = 'All' if limit == -1 else limit
     pw = "records" if (detector == 'CSVsniffer' or detector == 'DuckDB') else "characters"
     formated_sufix = '%r-%r %r loaded' %(detector, fw, pw)
     formated_sufix = formated_sufix.replace("'",'')
     out_path.append(os.path.join(basePath, 'tests results', sys_name, formated_sufix))
     for opath in out_path:
          if not os.path.exists(opath):
               os.makedirs(opath)
     _runner = []
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[0],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=limit,
                      sniffer=detector,
                      data_threshold=limit))
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
     """
     runsingleTest(threshold=10, # Load 10 records
                   data_threshold=-1, 
                   detector='CSVsniffer') 
     runsingleTest(threshold=-1, 
                   data_threshold=6144,   # Load 6144 characters
                    detector='CleverCSV')
     runsingleTest(threshold=-1,
                   data_threshold=6144, # Load 6144 characters
                   detector='Python sniffer')
     runsingleTest(threshold=-1, 
                   data_threshold=-1, # Load all file
                   detector='CleverCSV') 
     runsingleTest(threshold=10, # Load 10 records
                   data_threshold=-1, 
                   detector='CSVsniffer') 
    """ 
     runsingleTest(threshold=10, # Load 100 records
                   data_threshold=100, 
                   detector='DuckDB') 