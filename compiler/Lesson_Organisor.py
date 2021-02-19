import json

'''
{
    CS 201: {
        202002:{
            "name": Intro to comp
            "popularity":2
            "credit":3
            "faculy":FENS
            "actual":212
            "capicty":230
            "preReq":[if100]
            "coReq":[cs201R]
            "teachers":[
                {   
                tName:Ali
                tActual:30
                tCapacity:60
                tFillRate:50
                }
            ]
        }
    }   
}
'''
#functions
def termIncriment(term):
   #PreConditon:Term must be string in format = 202003
   #PostConditon:Next term returned as string
    if term[-1] == "3":
        return str(int(term) + 98) # 201703 ==> 201801
    else:
        return str(int(term) + 1)

def insertSorted(code,actual,sortList):
    #sortList = [ACC201,ACTUAL,REPEAT]
    count = len(sortList)
    sortList.append([code, actual, 1])
    loc = count

    while(loc > 0 and sortList[loc-1][1] < actual):
        sortList[loc] = sortList[loc - 1]
        loc -= 1

    sortList[loc] = [code, actual, 1]

    repeatStart = loc 
    repeat = 1
    while(loc > 0 and sortList[loc-1][1] == actual):
        repeat += 1
        loc -= 1
    repeatEnd = loc

    while(repeatStart >= loc): #first repeat wont change
        sortList[loc][2] = repeat
        loc += 1

    sortList[repeatEnd][2] = 1
    return sortList

#inputs
currentTerm = input("Enter start file (ex. 201703): ")
endTerm = input("Enter end file: ")

#main
allLessons = {}

while (int(currentTerm) <= int(endTerm)):
    json_name = "data_" + currentTerm + ".json"
    with open(json_name, 'r', encoding='utf-8') as json_file:
        termData = json.load(json_file)

        sortList = []

    for lesson in termData[currentTerm].keys():
        if lesson not in allLessons.keys():
            allLessons[lesson] = {}
    
        allLessons[lesson][currentTerm] = {}

        allLessons[lesson][currentTerm]["name"] = termData[currentTerm][lesson][1]
        allLessons[lesson][currentTerm]["credit"] = termData[currentTerm][lesson][4]
        allLessons[lesson][currentTerm]["faculy"] = termData[currentTerm][lesson][0]
        allLessons[lesson][currentTerm]["actual"] = termData[currentTerm][lesson][3]
        allLessons[lesson][currentTerm]["capicty"] = termData[currentTerm][lesson][2]
        allLessons[lesson][currentTerm]["preReqs"] = termData[currentTerm][lesson][7]
        allLessons[lesson][currentTerm]["coReqs"] = termData[currentTerm][lesson][6]
        
        teacherList = [] #list of dictinories
        for teacher in termData[currentTerm][lesson][5].keys():
            curr = {}
            curr["tName"] = teacher
            curr["tActual"] = termData[currentTerm][lesson][5][teacher][1]
            curr["tCapicty"] = termData[currentTerm][lesson][5][teacher][0]
            curr["tFillRate"] = (100* curr["tActual"])/curr["tCapicty"]
            teacherList.append(curr)
        allLessons[lesson][currentTerm]["teachers"] = teacherList

        sortList = insertSorted(lesson,allLessons[lesson][currentTerm]["actual"],sortList)


    
    #popilarity
    popi = 1
    rpopi = 1
    for lessonList in sortList:
        if lessonList[2] == 1:
            rpopi = popi
        allLessons[lessonList[0]][currentTerm]["popularity"] = rpopi
        popi += 1


    currentTerm = termIncriment(currentTerm)

#READING DONE

for lessonCode in allLessons.keys():
    dumpName = "data_" + lessonCode.replace(" ", "") + ".json"
    with open(dumpName, 'w', encoding='utf-8') as f:
        json.dump(allLessons[lessonCode], f, ensure_ascii=False, indent = 2)