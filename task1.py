std_info = {'Rohan':87, 'Mohit':75, 'Nitin': 92, 'Arya':85, 'Nayan':68}

choice = input("Enter the name of student : ")


if choice in std_info:
     mark = std_info[choice]
     print(f"{choice} : {mark}")

else:
    print("Student not found.")

