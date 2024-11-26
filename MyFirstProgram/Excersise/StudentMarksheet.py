#take inputs for  4 subject, student and standard

try:
    studentName = str(input("Please enter Students name" + " "))
    standard = str(input("Please Enter Standard :" + " "))

    maths = int(input("Please Enter Maths Number:" + " "))
    science = int(input("Please enter Science number:"+" "))
    socialScience = int(input("Please Enter SS Number:"+" "))
    english = int(input("Please Enter english Number:" + " "))

    percent =  (maths+science+socialScience+english)*100/250
   # print("the percentage ",+percent)
# conditions for result mark
    if maths <50 and science<50 and socialScience<50 and english<50:

     if maths <18  or science<18 or socialScience<18 or english<18:
      print(studentName + " is failed")
     elif percent < 35:
      print (studentName +" from  ", + standard, " is Failed " )
     elif percent >= 35:

      if 35 <= percent < 60:
       print (studentName +" from  ", standard, " is Second")
      elif 60<= percent <70:
       print(studentName + " from  ", standard, " is First")
      elif percent >=70:
       print(studentName + " from  ", standard, " is Passed from Distinction")

      print("Marks are" + "\n In Maths :- ",+  maths, "\
              \n In Science", + science, "\
              \n In Science", + socialScience, "\
              \n In English", + english, "\
              \n Total Percentage are ", + percent , " %"
             )
    else :
         print("Marks should be less then 50")

except ValueError:
    print ("Enter appropriate value")
