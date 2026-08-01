from scraper.scraper import get_attendance

student = input("Student ID: ")
password = input("Password: ")

report = get_attendance(student, password)

print("\nOverall Attendance")
print(report["overall"])

print("\nSubjects\n")

for subject in report["subjects"]:
    print(subject)