tn, p = map(int, input().split())
testCase = 1
def finput(text):
    print(text, flush=True)
    return input()

def checkAnchor(firstList, secondList, rangeN, j):
    start = j
    same = []
    dif = []
    for a in range(rangeN):
        if firstList[a] == secondList[a]:
            same.append([firstList[a], start + a])
        else:
            dif.append([firstList[a], start + a])
    if len(same) == 0:
        return 'AllDif'
    elif len(dif) == 0:
        return 'AllSame'
    else:
        return [same[0], dif[0]]
def flip(i):
    if i == '0':
        return '1'
    else:
        return '0'
while tn > 0:
    Astr = ''
    if p == 10:
        for a in range(10):
            a += 1
            Astr += finput(a)
    elif p == 20:
        firstHalf = []
        reverseHalf = []
        anchors = []
        switches = []
        anchorFound = False
        CstayedSame = False
        DstayedSame = False
        for a in range(3):
            if len(firstHalf) + len(reverseHalf) == 24:
                break
            else:
                if a == 0:
                    for b in range(5):
                        firstHalf.append(finput(b + 1))
                        reverseHalf.append(finput(20 - b))
                    result = checkAnchor(firstHalf[a * 5: (a + 1) * 5], reverseHalf[a * 5:(a + 1) * 5], 5, a * 5)
                    if result == "AllDif":
                        switches.append('D')
                    elif result == "AllSame":
                        switches.append('C')
                    else:
                        anchors = result
                        anchorFound = True
                elif anchorFound == True:
                    if finput(anchors[0][1] + 1) == anchors[0][1]:
                        if finput(anchors[1][1] + 1) != anchors[1][0]:
                            bufferList = firstHalf
                            firstHalf = reverseHalf
                            reverseHalf = bufferList
                            firstHalf = map(flip, firstHalf)
                            reverseHalf = map(flip, reverseHalf)

                    else:
                        if finput(anchors[1][1] + 1) == anchors[1][0]:
                            bufferList = firstHalf
                            firstHalf = reverseHalf
                            reverseHalf = bufferList
                        else:
                            print('uo')
                            firstHalf = list(map(flip, firstHalf))
                            reverseHalf = list(map(flip, reverseHalf))
                    if len(firstHalf) == 10:
                        firstHalf[9] = finput(10)
                        reverseHalf[9] = finput(11)
                    else:
                        for b in range(4):
                            b = a * 5 + b
                            firstHalf.append(finput(b + 1))
                            reverseHalf.append(finput(20 - b))
                        firstHalf.append('K')
                        reverseHalf.append('K')

                elif anchorFound == False:
                    if 'C' in switches and 'D' in switches:
                        if finput(switches.index('C') * 5 + 1) == firstHalf[switches.index('C') * 5]:
                            CstayedSame = True
                        if finput(switches.index('D') * 5 + 1) == firstHalf[switches.index('D') * 5]:
                            DstayedSame = True
                        if CstayedSame == True:
                            if DstayedSame != True:
                                bufferList = firstHalf
                                firstHalf = reverseHalf
                                reverseHalf = bufferList
                        else:
                            if DstayedSame != True:
                                #reverse-flip
                                bufferList = firstHalf
                                firstHalf = reverseHalf
                                reverseHalf = bufferList
                                firstHalf = map(flip, firstHalf)
                                reverseHalf = map(flip, reverseHalf)
                            elif CstayedSame != True:
                                #flip
                                firstHalf = map(flip, firstHalf)
                                reverseHalf = map(flip, reverseHalf)
                    else:
                        if len(firstHalf) == 10:
                            firstHalf[9] = finput(10)
                            reverseHalf[9] = finput(11)
                        else:
                            for b in range(4):
                                b = a * 5 + b
                                firstHalf.append(finput(b + 1))
                                reverseHalf.append(finput(20 - b))
                            firstHalf.append('K')
                            reverseHalf.append('K')
                        result = checkAnchor(firstHalf[a * 5: (a + 1) * 5], reverseHalf[a * 5:(a + 1) * 5], 4, a * 5)
                        if result == "AllDif":
                            switches.append('D')
                        elif result == "AllSame":
                            switches.append('C')
                        else:
                            anchors = result
                            anchorFound = True

        Astr = ''
        reverseHalf = reverseHalf[::-1]
        Astr += ''.join(firstHalf)
        Astr += ''.join(reverseHalf)
    elif p == 100:
        firstHalf = []
        reverseHalf = []
        anchors = []
        switches = []
        anchorFound = False
        CstayedSame = False
        DstayedSame = False
        for a in range(2):
            if len(firstHalf) + len(reverseHalf) == 100:
                break
            else:
                if a == 0:
                    for b in range(5):
                        firstHalf.append(finput(b + 1))
                        reverseHalf.append(finput(100 - b))
                    result = checkAnchor(firstHalf[a * 5: (a + 1) * 5], reverseHalf[a * 5:(a + 1) * 5], 5, a * 5)
                    if result == "AllDif":
                        switches.append('D')
                    elif result == "AllSame":
                        switches.append('C')
                    else:
                        anchors = result
                        anchorFound = True
                elif anchorFound == True:
                    if finput(anchors[0][1] + 1) == anchors[0][1]:
                        if finput(anchors[1][1] + 1) != anchors[1][0]:
                            bufferList = firstHalf
                            firstHalf = reverseHalf
                            reverseHalf = bufferList
                            firstHalf = map(flip, firstHalf)
                            reverseHalf = map(flip, reverseHalf)

                    else:
                        if finput(anchors[1][1] + 1) == anchors[1][0]:
                            bufferList = firstHalf
                            firstHalf = reverseHalf
                            reverseHalf = bufferList
                        else:
                            firstHalf = list(map(flip, firstHalf))
                            reverseHalf = list(map(flip, reverseHalf))
                    for b in range(4):
                        b = a * 5 + b
                        print(firstHalf)
                        firstHalf.append(finput(b + 1))
                        reverseHalf.append(finput(100 - b))
                    firstHalf.append('K')
                    reverseHalf.append('K')

                elif anchorFound == False:
                    if 'C' in switches and 'D' in switches:
                        print('gang')
                        if finput(switches.index('C') * 5 + 1) == firstHalf[switches.index('C') * 5]:
                            CstayedSame = True
                        if finput(switches.index('D') * 5 + 1) == firstHalf[switches.index('D') * 5]:
                            DstayedSame = True
                        if CstayedSame == True:
                            if DstayedSame != True:
                                bufferList = firstHalf
                                firstHalf = reverseHalf
                                reverseHalf = bufferList
                        else:
                            if DstayedSame != True:
                                #reverse-flip
                                bufferList = firstHalf
                                firstHalf = reverseHalf
                                reverseHalf = bufferList
                                firstHalf = map(flip, firstHalf)
                                reverseHalf = map(flip, reverseHalf)
                            elif CstayedSame != True:
                                #flip
                                firstHalf = map(flip, firstHalf)
                                reverseHalf = map(flip, reverseHalf)
                    else:
                        for b in range(4):
                            b = a * 5 + b
                            firstHalf.append(finput(b + 1))
                            reverseHalf.append(finput(100 - b))
                        firstHalf.append('K')
                        reverseHalf.append('K')

                        result = checkAnchor(firstHalf[a * 5: (a + 1) * 5], reverseHalf[a * 5:(a + 1) * 5], 4, a * 5)
                        if result == "AllDif":
                            switches.append('D')
                        elif result == "AllSame":
                            switches.append('C')
                        else:
                            anchors = result
                            anchorFound = True

        Astr = ''
        firstHalf[9] = finput(10)
        reverseHalf[9] = finput(11)
        reverseHalf = reverseHalf[::-1]
        for a in range(0, 50,5):
            Astr += ''.join(firstHalf[a:a+5])
            Astr += ''.join(reverseHalf[a:a+5:])
    if finput(Astr) != 'Y':
        break
    tn -= 1
    testCase += 1