import splitfolders

folder_name = "test"
parent_path = f".\\Datasets\\{folder_name}\\Dataset"
output_path = f".\\Datasets\\{folder_name}\\Splitted_Dataset"

splitfolders.ratio(parent_path, output=output_path, seed=213, ratio=(.8, .1, .1))