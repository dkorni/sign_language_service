import os
from pathlib import Path
from PIL import Image
import codecs


def generate_xml_labels(path):
    subfolders = os.listdir(path)
    subfolders.sort()
    counter = 0
    for folder in subfolders:
        folderPath = path+"\\"+folder
        files = os.listdir(folderPath)

        files = [f for f in files if f.endswith(".jpg")]
        for file in files:
            file_path = path + "\\" + folder + "\\" + file
            project_root = os.path.dirname(os.path.dirname(__file__))
            im = Image.open(file_path)
            width, height = im.size
            xml_str = Path(project_root+'\\template.xml').read_text().format(folder,file,file_path,width,height,folder,width,height)
            save_path_file = path+"\\"+folder + "\\" + "{0}.xml".format(os.path.splitext(file)[0])
            with codecs.open(save_path_file, "w","utf-8") as f:
                f.write(xml_str)
            counter += 1
    print("Processed {0} images".format(counter))

generate_xml_labels("D:\Study\Taras Shevchenko\Diplom\\abetka_daktel")
print("Done")