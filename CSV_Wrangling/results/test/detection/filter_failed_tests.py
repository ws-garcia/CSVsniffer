import collections
import json
import os

def readResuls(path: str)->list:
   with open(path,"r") as f:
        tmpResult=[]
        for line in f:
           obj=json.loads(line.strip())
           tmpResult.append(obj)
        f.close
   return tmpResult

def getFailed(rObjects: list[dict]):
  fList=[]
  for obj in rObjects:
      if obj["status"]=="FAIL" or obj["status"]=="SKIP":
         fList.append(obj)
  return fList

def writeFiledTestToFile(aList: list):
    if os.path.exists('FAILED/') !=True:
        os.mkdir('FAILED/')
    with open('./FAILED/detectionTestFailed.json',"w") as f:
        i=0
        for element in aList:
            f.write(json.dumps(element))
            i+=1
            if i !=aList.__len__():
                f.write('\n')
        f.close

def main():
    path=os.path.join(os.path.dirname(__file__) ,'out_our_score_full_no_tie_github.json')
    writeFiledTestToFile(getFailed(readResuls(path)))

if __name__ == "__main__":
    main()