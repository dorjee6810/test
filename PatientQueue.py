from queue import Queue
patient_queue = Queue()
while True:
    print("Desk Manager - Patient Registration and Appointment Syetem")
    print("1. Register Patient")
    print("2. Remove Patient after Meeting Doctor")
    print("3. Display Patient Queue")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        patient_name = input("Enter patient's name to register:")
        patient_queue.put(patient_name)
        print(f"Patient {patient_name} registered:")

    elif choice == "2":
        if not patient_queue.empty():
            removed_patient = patient_queue.get()
            print(f"Patient {removed_patient} removed after meeting the doctor.")
        else:
            print("No patient in the queue.")

    elif choice == "3":
        if not patient_queue.empty():
            print("Current Patient Queue: ")
            for patient in list(patient_queue.Queue):
                print(patient)
            print()

        else:
            print("Patient is empty.")

    elif choice == "4":
        print("Exiting program...") 
        break   
    else:
        print("invalid choice! Please enter a valid choice.")


