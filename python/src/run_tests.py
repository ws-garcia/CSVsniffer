import os
from test_runner import runner

def main():
     basePath = os.path.dirname(os.path.dirname(__file__))
     out_path = []
     out_path.append(os.path.join(basePath, 'tests results', 'Python_sniffer'))
     out_path.append(os.path.join(basePath, 'tests results', 'CSVsniffer'))
     for opath in out_path:
          if not os.path.exists(opath):
               os.makedirs(opath)
     _runner = []
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[0],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=50,
                      sniffer='Python sniffer'))
     _runner.append(runner(ground_truth_csv=None,
                      output_path=out_path[1],
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=50))
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
     main()