import splitfolders
import random
import os

while True:
    folder_name = input("\nEnter the folder name: ")
    parent_path = f".\\Datasets\\{folder_name}"
    dataset_parent_path = f".\\Datasets\\{folder_name}\\Dataset"

    if not os.path.exists(parent_path):
        print(f"Error: The folder '{parent_path}' does not exist. Please enter a valid folder name.")
    elif not os.listdir(parent_path):
        print(f"Error: The folder '{parent_path}' is empty. Please enter a valid folder name.")
    elif not os.path.exists(dataset_parent_path):
        print(f"Error: The folder '{dataset_parent_path}' does not exist. Please enter a valid folder name.")
    elif not os.listdir(dataset_parent_path):
        print(f"Error: The folder '{dataset_parent_path}' is empty. Please enter a valid folder name.")
    else:
        break

output_path = f".\\Datasets\\{folder_name}\\Splitted_Dataset"
counter = 2
while os.path.exists(output_path) and os.listdir(output_path):
    output_path = f".\\Datasets\\{folder_name}\\Splitted_Dataset_{counter}"
    counter += 1

while True:
    train_percentage = int(input("Enter the percentage for training (0-100): "))
    test_percentage = int(input("Enter the percentage for testing (0-100): "))
    validation_percentage = int(input("Enter the percentage for validation (0-100): "))

    total_percentage = train_percentage + test_percentage + validation_percentage

    if total_percentage != 100:
        print("Error: The total percentage must be equal to 100. Please re-enter the percentages.\n")
    else:
        break

train_ratio = train_percentage / 100
test_ratio = test_percentage / 100
validation_ratio = validation_percentage / 100

random_seed = random.randint(1, 99999)

print()

splitfolders.ratio(dataset_parent_path, output=output_path, seed=random_seed, ratio=(train_ratio, test_ratio, validation_ratio))

print(f"\nDataset splitting completed:\nTraining = {train_percentage}%\nTesting = {test_percentage}%\nValidation = {validation_percentage}%")
