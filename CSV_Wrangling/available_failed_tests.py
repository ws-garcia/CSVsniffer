import collections
import json
import os
import shutil

def readJSONfile(path: str)->list[dict]:
   with open(path,"r") as f:
        tmpResult=[]
        for line in f:
           obj=json.loads(line.strip())
           tmpResult.append(obj)
        f.close
   return tmpResult

def readJSONfileDICT(path: str)->dict[dict]:
   with open(path,"r") as f:
        tmpResult={}
        for line in f:
           obj=json.loads(line.strip())
           tmpResult[obj['md5']]=obj
        f.close
   return tmpResult

def getMD5_URLs(basePath: str)->dict[dict]:
  return readJSONfileDICT(os.path.join(basePath,'urls_github.json'))

def getFailedTest(basePath: str)->list[dict]:
    return readJSONfile(os.path.join(basePath,'results', 'test', 'detection', 'FAILED', 'detectionTestFailed.json'))

def MD5fromName(fName: str)->str:
    hashName=fName.split('/')[-1]
    return hashName.split('.')[0]

def getFileNameFromMD5 (strMD5: str, MD5_URLs: dict[dict]):
    tmpResult=MD5_URLs[strMD5]['urls']
    return tmpResult[0].split('/')[-1]

def main():
    basePath= os.path.dirname(__file__)
    failedTestsList=getFailedTest(basePath)
    MD5andURLlist=getMD5_URLs(basePath)
    tmpPath=os.path.join(basePath,'data', 'github', 'Curated files',)
    if os.path.exists(os.path.join(tmpPath, 'metadata')) !=True:
        os.makedirs(os.path.join(tmpPath, 'metadata'))
    jsonFile=open(os.path.join(tmpPath, 'metadata', 'TfilesJSON.json'),"w")
    csvFile=open(os.path.join(tmpPath, 'metadata', 'TfilesCSV.csv'),"w")
    csvFile.write('File_Path|MD5\n')
    dataRepo=os.path.join(basePath,'data' , 'github', 'CSV',)
    i=0
    for item in failedTestsList:
        i+=1
        vMD5=MD5fromName(item['filename'])
        cFile=getFileNameFromMD5(vMD5,MD5andURLlist)
        for filename in os.listdir(dataRepo):
            if cFile==filename:
                jsonFile.write(json.dumps(MD5andURLlist[vMD5]))
                csvFile.write('./data/github/CSV/' + cFile +'|' + vMD5)
                shutil.copy2(os.path.join(dataRepo, filename),os.path.join(tmpPath, filename))
                if i !=failedTestsList.__len__():
                    jsonFile.write('\n')
                    csvFile.write('\n')
    csvFile.close
    jsonFile.close

if __name__ == "__main__":
    main()