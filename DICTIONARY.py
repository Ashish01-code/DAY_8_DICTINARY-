#!/usr/bin/env python
# coding: utf-8

# In[7]:


d = {}

while True:
    print("\n-STUDENT MENU ")
    print("1. Add student")
    print("2. Display all students")
    print("3. Find topper")
    print("4. Average marks")
    print("5. Search student")
    print("6. Delete student")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        d[name] = marks
        print("Student added")

    elif choice == 2:
        if len(d) > 0:
            print(d)
        else:
            print("No records")

    elif choice == 3:
        if len(d) > 0:
            topper = max(d, key=d.get)
            print("Topper:", topper, "Marks:", d[topper])
        else:
            print("No records")

    elif choice == 4:
        if len(d) > 0:
            total = sum(d.values())
            print("Average:", total / len(d))
        else:
            print("No records")

    elif choice == 5:
        name = input("Enter name to search: ")
        if name in d:
            print(name, "marks:", d[name])
        else:
            print("Student not found")

    elif choice == 6:
        name = input("Enter name to delete: ")
        if name in d:
            d.pop(name)
            print("Deleted")
        else:
            print("Student not found")

    elif choice == 7:
        print("Final dictionary:", d)
        break

    else:
        print("Invalid choice")


# In[ ]:




