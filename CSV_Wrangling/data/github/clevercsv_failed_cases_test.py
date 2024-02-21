import collections
import clevercsv
import time
import os
import sys

def getCSVdata(path: str)->str:
   with open(path) as f:
        csvcontent: str = ' '.join(f.readlines())
        return csvcontent

def DetectCSVDialect(path: str):
   content= getCSVdata(path)
   # you can use verbose=True to see what CleverCSV does
   dialect = clevercsv.Sniffer().sniff(content,delimiters=[',',';','\t','|',':','.','=','<','>',' '],verbose=True)
   return dialect

def ImportExpectedResults(annotations :str)->dict:
  try:
     basePath= os.path.dirname(__file__)
     with open(os.path.join(basePath, annotations), newline='') as csvfile:
        csvFilesDict={}
        csvRowDict={}
        spamreader = clevercsv.reader(csvfile, delimiter='|', quotechar='')
        i=0
        for row in spamreader:
           if len(row)>1:
              if i>0:
                 if len(row)==6:
                  csvRowDict={
                     'encoding':row[1],
                     'fields_delimiter':row[2],
                     'quotechar':row[3],
                     'escapechar':row[4],
                     'records_delimiter':row[5]
                  }
                 elif len(row)==7:
                  csvRowDict={
                     'encoding':row[1],
                     'fields_delimiter':row[2],
                     'quotechar':row[3],
                     'escapechar':row[4],
                     'records_delimiter':row[5],
                     'normal-file': row[6]
                  }
                 csvFilesDict[row[0]]=csvRowDict
              else:
                 i+=1
        return csvFilesDict
  except Exception as err:
     print("Error was: %s" % err)

def GetDelName(aDelim:str)->str:
   if aDelim == ',':
      return 'comma'
   elif aDelim == ';':
      return 'semicolon'
   elif aDelim == '\t':
      return 'tab'
   elif aDelim == ' ':
      return 'space'
   elif aDelim == '|':
      return 'vslash'
   elif aDelim== '#':
      return 'nsign'

def GetQuoteName(aQuote:str)->str:
   if aQuote == '"' or aQuote == '':
      return 'doublequote'
   elif aQuote == '\'':
      return 'singlequote'

def main(basePath :str, outPath :str, only_messy :bool= False):
   #Get test path withing current .py file
   TestsCSVpath=os.path.join(basePath, 'Curated files')
   tmpstdofname= '[CSV Wrangling (no codec issues)-ONLY MESSY= %r]clevercsv_output.txt' % only_messy
   if only_messy:
      tSet=['Manual_Dialect_Annotation_CODEC.txt']
      stdoutArr=[ os.path.join(outPath,tmpstdofname)]
   else:
      #Testing over two datasets
      tSet=['Manual_Dialect_Annotation.txt', 'Manual_Dialect_Annotation_CODEC.txt']
      stdoutArr=[os.path.join(outPath, '[CSV Wrangling]clevercsv_output.txt'), os.path.join(outPath,tmpstdofname)]
   n=0
   for testItem in tSet:
      sys.stdout = open(stdoutArr[n], 'w')
      #Import expectect results as nested dicts
      ExpectedResults=ImportExpectedResults(tSet[n])
      passed=0
      failures=0
      totaltests=0
      t=time.time()
      #Iterate and run all test files
      for filename in os.listdir(TestsCSVpath):
         if filename in ExpectedResults:
            load_file=True
            if only_messy:
               if 'normal-file' in ExpectedResults[filename]:
                  load_file= (ExpectedResults[filename]['normal-file']=='no')
            if load_file:
               totaltests+=1
               file = os.path.join(TestsCSVpath, filename)
               #File check
               if os.path.isfile(file):
                  try:
                     dialect=DetectCSVDialect(file)
                  except Exception as err:
                     dialect=None
                     failures += 1
                     print("Error was: %s" % err)
                  if dialect !=None:
                     if GetDelName(dialect.delimiter)==ExpectedResults[filename]['fields_delimiter'] and \
                     GetQuoteName(dialect.quotechar)==ExpectedResults[filename]['quotechar']:
                        tflag ='+'
                        passed += 1
                     else:
                        tflag ='X'
                     if tflag =='+':
                        print(tflag + '[' + filename + ']: --> cleverCSV detected: delimiter = %r, quotechar = %r' 
                           % (dialect.delimiter, dialect.quotechar))
                     else:
                        print(tflag + '[' + filename + ']: --> cleverCSV detected: delimiter = %r, quotechar = %r' 
                           % (dialect.delimiter, dialect.quotechar) + \
                           '| EXPECTED:{delimiter = %r, quotechar = %r}' \
                              % (ExpectedResults[filename]['fields_delimiter'], ExpectedResults[filename]['quotechar']))
                  else:
                     print("X[" + filename + "]: --> No result from cleverCSV")
      print('[Passed test ratio]--: %r' %(round(100*passed/(totaltests-failures),4)) +'%')
      print('[Failure ratio]--: %r' %(round(100*failures/totaltests,4)) +'%')
      print('[Elapsed time]--: %r seconds' %(round(time.time()-t,2)))
      sys.stdout.close()
      n+=1
      
if __name__ == "__main__":
   basePath= os.path.dirname(__file__)
   main(basePath, basePath,True)