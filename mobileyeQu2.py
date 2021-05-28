def exportResultFile(flag1, f1, f2, file1Dict, file2Dict, resultFile):
    resultFile.write("First file unique details:\n\n")

    for i in file1Dict.keys():
        resultFile.write(i)

    if flag1:
        copyTheRest(f1, resultFile)

    resultFile.write("\n\nSecond file unique details:\n\n")

    for i in file2Dict.keys():
        resultFile.write(i)

    if not flag1:
        copyTheRest(f2, resultFile)


def copyTheRest(f, resultFile):
    # copy until the end
    try:
        while True:
            for i in range(1000):
                li = next(f)
                resultFile.write(li)
    except StopIteration:
        return


def readLines(f, fileDict):
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
def processData(file1Dict, file2Dict):
    valueToDel = []
    if len(file1Dict) < len(file2Dict):
        for i in file1Dict.keys():
            if i in file2Dict:
                valueToDel.append(i)
    else:
        for i in file2Dict.keys():
            if i not in file1Dict:
                valueToDel.append(i)

    for i in valueToDel:  # del the duplicate rows
        file1Dict.pop(i)
        file2Dict.pop(i)


def tryF(path1, path2, res):
    file1Dict, file2Dict = {}, {}
    f1 = open(path1)
    f2 = open(path2)
    resultFile = open(res, "w")

    f1.readline()  # ignore first lines
    f2.readline()  # ignore first lines

    flag1 = flag2 = True
    while flag1 and flag2:
        if not readLines(f1, file1Dict): flag1 = False
        if not readLines(f2, file2Dict): flag2 = False
        processData(file1Dict, file2Dict)

    exportResultFile(flag1, f1, f2, file1Dict, file2Dict, resultFile)
    f1.close()
    f2.close()
    resultFile.close()


def main():
    tryF('mobileyeHT/folder_A/file1.txt', 'mobileyeHT/folder_A/file2.txt', 'mobileyeHT/result1.txt')
    tryF('mobileyeHT/folder_B/file1.txt', 'mobileyeHT/folder_B/file2.txt', 'mobileyeHT/result2.txt')


if __name__ == "__main__":
    main()