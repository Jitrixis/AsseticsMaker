import sys
import re


class analyzer:
    def __init__(self, vendor, line):
        line = re.sub(r'\n', '', line)
        self.__line = line
        self.__isFile = False
        self.__path = ""
        self.__filename = ""
        self.__extension = ""
        self.__vendor = vendor
        self.__assetName = ""
        self.__assetInputs = ""
        self.__assetOutput = ""
        self.__parseLine()

    def __parseLine(self):
        self.__parseIsFile()
        if self.__isFile:
            self.__parseFilename()
            self.__parseExtension()
            self.__parsePath()
            self.__generateAssetName()
            self.__generateAssetInputs()
            self.__generateAssetOutput()

    def __parseIsFile(self):
        pattern = r'\.\/([^\/\n]+\/)*([^\/\n]+\.[^\/\n]+)'
        if re.search(pattern, self.__line):
            self.__isFile = True
        else:
            self.__isFile = False

    def __parseFilename(self):
        pattern = r'\.\/([^\/\n]+\/)*(([^\/\n]+)\.([^\/\n]+))'
        self.__filename = re.sub(pattern, "\g<3>", self.__line)

    def __parseExtension(self):
        pattern = r'\.\/([^\/\n]+\/)*(([^\/\n]+)\.([^\/\n]+))'
        self.__extension = re.sub(pattern, '\g<4>', self.__line)

    def __parsePath(self):
        pattern = r'\.\/(([^\/\n]+\/)*)(([^\/\n]+)\.([^\/\n]+))'
        self.__path = re.sub(pattern, '/\g<1>', self.__line)

    def __generateAssetName(self):
        text = self.__path + "-" + self.__filename + "-" + self.__extension
        pattern = r'[^a-zA-Z\-]+'
        self.__assetName = re.sub(pattern, '-', text)
        pattern = r'\-\-+'
        self.__assetName = self.__vendor + re.sub(pattern, '-', self.__assetName)
        pattern = r'(^\-)|(\-$)'
        self.__assetName = re.sub(pattern, '', self.__assetName) + ':'

    def __generateAssetInputs(self):
        self.__assetInputs = "\tinputs: \"%kernel.root_dir%/../vendor/" + self.__vendor + self.__path + self.__filename + "." + self.__extension + "\""

    def __generateAssetOutput(self):
        self.__assetOutput = "\toutput: \"lib" + self.__path + self.__filename + "." + self.__extension + "\""

    def getAssetLine(self, lineNumber):
        if lineNumber == 1:
            return self.__assetName
        elif lineNumber == 2:
            return self.__assetInputs
        elif lineNumber == 3:
            return self.__assetOutput
        else:
            return None

    def getIsFile(self):
        return self.__isFile


print("#", sys.argv[1], sep='')
for line in sys.stdin:
    a = analyzer(sys.argv[1], line)
    if a.getIsFile():
        i = 1
        while a.getAssetLine(i) is not None:
            print("", a.getAssetLine(i), sep='')
            i += 1
