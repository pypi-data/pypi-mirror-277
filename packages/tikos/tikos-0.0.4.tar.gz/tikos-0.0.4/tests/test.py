from tikos.tikos import AddExtractionFile, AddExtractionFiles, AddExtractionFileStream, AddExtractionFileStreams, ProcessExtract, GetExtract
from typing import List
import datetime
import json

def AddFile():
    requestId = 'b8d1c770-2b71-4273-a768-9cebc5b87ff2'
    authToken = '8d9f9bd7-c92f-4ce4-8f87-77180836f770'
    # files = [('README.1.md',open('README.1.md', 'rb'))]
    files = ('6 Legal agreement.pdf','6 Legal agreement.pdf')

    rtnval = AddExtractionFile(requestId=requestId, authToken=authToken, fileObj=files)
    print(rtnval)

# def AddFiles():
#     requestId = 'b8d1c770-2b71-4273-a768-9cebc5b87ff2'
#     authToken = '8d9f9bd7-c92f-4ce4-8f87-77180836f770'
#     # files = [('README.md','../README.md'), ('LICENSE','../LICENSE')]
#     files = [('README.md', open('../README.md', 'rb')), ('LICENSE', open('../LICENSE', 'rb'))]
#
#     rtnval = AddExtractionFileStreams(requestId=requestId, authToken=authToken, fileObjs=files)
#     print(rtnval)

# def checkfile(files: List[object]=None):
#
#     for fileObj in files:
#         name = fileObj[0]
#         fileLocation = fileObj[1]
#         print(name, fileLocation)

def processExtract():
    requestId = 'b8d1c770-2b71-4273-a768-9cebc5b87ff2'
    authToken = '8d9f9bd7-c92f-4ce4-8f87-77180836f770'

    rtnval = ProcessExtract(requestId=requestId, authToken=authToken)
    print(rtnval)

def getExtract():
    requestId = 'b8d1c770-2b71-4273-a768-9cebc5b87ff2'
    authToken = '8d9f9bd7-c92f-4ce4-8f87-77180836f770'

    s, r, t = GetExtract(requestId=requestId, authToken=authToken)
    # print(rtnval)
    return t


if __name__ == '__main__':
    start = datetime.datetime.now()
    # ViewVersion()
    # Description()
    # AddRequest()
    # AddText()
    # AddFile()
    # AddFiles()
    # processExtract()
    txtDocs = getExtract()

    end = datetime.datetime.now()
    print(end - start)
    print(f"start:{start}, end:{end}")

    if len(txtDocs) > 0:
        jsonfy = json.loads(txtDocs)
        for doc in jsonfy:
            print(doc)