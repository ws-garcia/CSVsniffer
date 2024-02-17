import collections
import json
import os

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

def getMD5_URLs()->dict[dict]:
  return readJSONfileDICT('./urls_github.json')

def getFailedTest()->list[dict]:
    return readJSONfile('./results/test/detection/FAILED/detectionTestFailed.json')

def MD5fromName(fName: str)->str:
    hashName=fName.split('/')[-1]
    return hashName.split('.')[0]

def getFileNameFromMD5 (strMD5: str, MD5_URLs: dict[dict]):
    tmpResult=MD5_URLs[strMD5]['urls']
    return tmpResult[0].split('/')[-1]

def main():
    failedTestsList=getFailedTest()
    MD5andURLlist=getMD5_URLs()
    tmpPath='data/github/AVAILABLE FILES FOR TESTING/'
    if os.path.exists(tmpPath) !=True:
        os.mkdir(tmpPath)
    jsonFile=open('./' + tmpPath +'Available files.json',"w")
    csvFile=open('./' + tmpPath +'Available files.csv',"w")
    csvFile.write('File_Path|MD5\n')
    i=0
    for item in failedTestsList:
        i+=1
        vMD5=MD5fromName(item['filename'])
        cFile=getFileNameFromMD5(vMD5,MD5andURLlist)
        for filename in os.listdir('./data/github/CSV/'):
            if cFile==filename:
                jsonFile.write(json.dumps(MD5andURLlist[vMD5]))
                csvFile.write('./data/github/CSV/' + cFile +'|' + vMD5)
                if i !=failedTestsList.__len__():
                    jsonFile.write('\n')
                    csvFile.write('\n')
        csvFile.close
        jsonFile.close

if __name__ == "__main__":
    main()