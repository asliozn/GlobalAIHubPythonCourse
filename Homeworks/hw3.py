def cal_passing_grade(midt, project, finalp):
    passing_grade = midt * 0.3 + project * 0.3 + finalp * 0.4
    return passing_grade


st_list = [None] * 5
for index in range(5):
    print("Write student's info(name-midterm grade -project grade-final project grade)")
    st = {"Name": input(), "Midterm": float(input()), "Project": float(input()), "Final Project": float(input())}
    st["Passing Grade"] = cal_passing_grade(st["Midterm"], st["Project"], st["Final Project"])
    st_list[index] = st

st_list.sort(key=lambda i: i["Passing Grade"], reverse=True)

for st in st_list:
    print(st)
