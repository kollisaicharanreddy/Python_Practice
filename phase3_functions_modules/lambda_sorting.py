students = [("Raju", 75), ("Ujwal", 92), ("Charan", 88)]
answer = sorted(students, key=lambda x: x[1], reverse=True)
print(answer)