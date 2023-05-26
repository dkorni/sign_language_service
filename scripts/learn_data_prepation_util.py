import os
import shutil
import codecs
from config import *

import scripts.generate_tfrecord as gtf

# label mask
labels = [{'name':'А', 'id':1},
          {'name':'Б', 'id':2},
          {'name':'В', 'id':3},
          {'name':'Г', 'id':4},
          {'name':'Ґ', 'id':5},
          {'name':'Д', 'id':6},
          {'name':'Е', 'id':7},
          {'name':'Є', 'id':8},
          {'name':'Ж', 'id':9},
          {'name':'З', 'id':10},
          {'name':'И', 'id':11},
          {'name':'І', 'id':12},
          {'name':'Ї', 'id':13},
          {'name':'Й', 'id':14},
          {'name':'К', 'id':15},
          {'name':'Л', 'id':16},
          {'name':'М', 'id':17},
          {'name':'Н', 'id':18},
          {'name':'О', 'id':19},
          {'name':'П', 'id':20},
          {'name':'Р', 'id':21},
          {'name':'С', 'id':22},
          {'name':'Т', 'id':23},
          {'name':'У', 'id':24},
          {'name':'Ф', 'id':25},
          {'name':'Х', 'id':26},
          {'name':'Ц', 'id':27},
          {'name':'Ч', 'id':28},
          {'name':'Ш', 'id':29},
          {'name':'Щ', 'id':30},
          {'name':'Ь', 'id':31},
          {'name':'Ю', 'id':32},
          {'name':'Я', 'id':33}
          ]

with codecs.open(ANNOTATION_PATH + '/label_map.pbtxt', 'w', 'utf-8') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

gtf.main(xml_dir=IMAGE_PATH + '/train', labels_path=ANNOTATION_PATH + '/label_map.pbtxt', output_path=ANNOTATION_PATH + '/train.record')
gtf.main(xml_dir=IMAGE_PATH + '/test', labels_path=ANNOTATION_PATH + '/label_map.pbtxt', output_path=ANNOTATION_PATH + '/test.record')