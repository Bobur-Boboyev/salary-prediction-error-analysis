from visualize import visualize_1, visualize_error_MAE, visualize_error_MSE

while True:
    print("\nMenu:")
    print("\n1 - Visualize prediction")
    print("2 - Visualize MAE")
    print("3 - Visualize MSE")
    print("0 - Exit")

    choice = input("\nInput your choice: ")

    if choice == '1':
        visualize_1()
    
    elif choice == '2':
        visualize_error_MAE()

    elif choice == '3':
        visualize_error_MSE()
    
    elif choice == '0':
        print("Goodbye...")
        break

    else:
        print("Wrong input!")