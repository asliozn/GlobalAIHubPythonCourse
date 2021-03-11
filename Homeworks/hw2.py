cv1={"Name":"Aslı","Surname":"Özen","Job Title":"Computer Engineer","Mail":"aslozn@hotmail.com","Education":"Kocaeli University "}
cv2={"Name":"Hazal","Surname":"Saç","Job Title":"Industrial Engineer","Mail":"hazlsac@gmail.com","Education":"Middle East Technical University "}
cv3={"Name":"Melek","Surname":"Coşkun","Job Title":"Dentist","Mail":"melekcskn@hotmail.com","Education":"Marmara University "}
cv4={"Name":"Beyza","Surname":"Akbaş","Job Title":"Chemical Engineer","Mail":"byzaakbas@hotmail.com","Education":"Gazi University "}
cv5={"Name":"Sema","Surname":"Gümüş","Job Title":"Chemical Engineer","Mail":"semagumus2@hotmail.com","Education":"Middle East Technical University "}
cvlist=[cv1,cv2,cv3,cv4,cv5]

for i in range(5):
 print("--------------- CV",i+1,"-----------------")
 for k,v in cvlist[i].items():
  print( k,":", v)

