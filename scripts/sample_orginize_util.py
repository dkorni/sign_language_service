import os
import shutil
from pathlib import Path

def organize_train_and_test_samples(train_num_p, input_path, output_path):
    subfolders = os.listdir(input_path)
    for folder in subfolders:
        folder_path = input_path+"\\"+folder
        files = os.listdir(folder_path)
        files = [f for f in files if f.endswith(".jpg") or f.endswith(".xml")]
        files_count = len(files)/2
        # take train images
        train_num_to_take = int(files_count * train_num_p / 100)
        trainFiles = files[:train_num_to_take*2]
        testFiles = files[int(-((files_count-train_num_to_take)*2)):]

        train_path = output_path + "\\train"
        test_path = output_path + "\\test"
        if not os.path.exists(test_path):
            os.mkdir(test_path)

        if not os.path.exists(train_path):
            os.mkdir(train_path)

        for testFile in testFiles:
            test_file_path = input_path+"\\"+folder + "\\"+testFile
            shutil.copy2(test_file_path, test_path)

        for train_file in trainFiles:
            train_file_path = input_path + "\\" + folder + "\\" + train_file
            shutil.copy2(train_file_path, train_path)

train_num_p = 80
input_path = "D:\Study\Taras Shevchenko\Diplom\\abetka_daktel"
output_path = "D:\Study\Taras Shevchenko\Diplom\\samples"
organize_train_and_test_samples(train_num_p, input_path, output_path)
print("Done")