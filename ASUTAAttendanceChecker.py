import xlrd
import re

attendanceLoc = input("attendance sheet filepath: ")
glistLoc = input("grading students filepath: ")

attendance = xlrd.open_workbook(attendanceLoc).sheet_by_index(0)
glist = xlrd.open_workbook(glistLoc).sheet_by_index(0)


allList = []
attendList = []
for student in range(glist.nrows):
    sname = re.sub("\(.*?\)", "", glist.cell_value(student, 0))[:-1]
    semail = re.findall("\(([^\)]+)\)", glist.cell_value(student, 0))[0]
    # only print students name if they did not attend
    allList.append(sname)

    for log in range(attendance.nrows):
        if semail.lower() in attendance.cell_value(log, 1).lower(): # or sname.lower() in attendance.cell_value(log, 2).lower() # this section checks if name is equal
            attendList.append(sname)

# print(allList)
print("These students did not attend: ", set(allList) - set(attendList))