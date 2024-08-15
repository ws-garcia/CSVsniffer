import os
from test_runner import runner

def main():
     basePath = os.path.dirname(os.path.dirname(__file__))
     out_path = os.path.join(basePath, 'tests results', 'CSVsniffer')
     if not os.path.exists(out_path):
          os.makedirs(out_path)
     _runner = runner(ground_truth_csv=None,
                      output_path=out_path,
                      delimiter_list=[',', ';', '\t','|', ':', '=', ' ', '#', '*'],
                      quotechar_list=['"', "'", '~'], 
                      expected_results=None,
                      threshold=50)
     _runner.run(base_path=basePath,
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