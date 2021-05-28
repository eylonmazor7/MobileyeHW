class checkFiles:
    def __init__(self, f1, f2, res):
        self.file1Dict = {}
        self.file2Dict = {}
        self.f1 = open(f1)
        self.f2 = open(f2)
        self.resultFile = open(res, "w")
        # ignore first lines
        self.f1.readline()
        self.f2.readline()
        self.scanFiles()

    def scanFiles(self):
        flag1 = flag2 = True

        while flag1 and flag2:
            if not self.readLines(self.f1, self.file1Dict):
                flag1 = False
            if not self.readLines(self.f2, self.file2Dict):
                flag2 = False
            self.processData()

        self.exportResultFile(flag1, flag2)
        self.f1.close()
        self.f2.close()
        self.resultFile.close()

    def readLines(self, f, fileDict):
        try:
            for x in range(5000):
                li = next(f)
                fileDict[li] = x
        except StopIteration:
            if li in fileDict:
                fileDict.pop(li)  # ignore last row
            return False
        return True

    # run all over the smaller dict and search o(1) in the bigger dict
    def processData(self):
        valueToDel = []
        if len(self.file1Dict) < len(self.file2Dict):
            for i in self.file1Dict.keys():
                if i in self.file2Dict:
                    valueToDel.append(i)
        else:
            for i in self.file2Dict.keys():
                if i not in self.file1Dict:
                    valueToDel.append(i)

        for i in valueToDel:
            self.file1Dict.pop(i)
            self.file2Dict.pop(i)

    def exportResultFile(self, flag1, flag2):
        if len(self.file1Dict) == 0 and len(self.file2Dict) == 0:
            print("The files are identical")
            self.resultFile.write("The files are identical")
            return

        print("The files are not identical")
        self.resultFile.write("First file unique lines:\n\n")

        for i in self.file1Dict.keys():
            self.resultFile.write(i)

        if flag1 and not flag2:
            self.copyTheRest(self.f1)

        self.resultFile.write("\n\nSecond file unique lines:\n\n")

        for i in self.file2Dict.keys():
            self.resultFile.write(i)

        if flag2 and not flag1:
            self.copyTheRest(self.f2)

    def copyTheRest(self, f):
        # copy until the end
        try:
            while True:
                for i in range(1000):
                    li = next(f)
                    self.resultFile.write(li)
        except StopIteration:
            return


def main():
    checkFiles('mobileyeHW/folder_A/file1.txt', 'mobileyeHW/folder_A/file2.txt', 'mobileyeHW/result1.txt')
    checkFiles('mobileyeHW/folder_B/file1.txt', 'mobileyeHW/folder_B/file2.txt', 'mobileyeHW/result2.txt')


if __name__ == "__main__":
    main()
