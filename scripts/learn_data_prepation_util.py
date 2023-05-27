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
          {'name':'Д', 'id':5},
          {'name':'Е', 'id':6},
          {'name':'Є', 'id':7},
          {'name':'Ж', 'id':8},
          {'name':'З', 'id':9},
          {'name':'И', 'id':10},
          {'name':'І', 'id':11},
          {'name':'К', 'id':12},
          {'name':'Л', 'id':13},
          {'name':'М', 'id':14},
          {'name':'Н', 'id':15},
          {'name':'О', 'id':16},
          {'name':'П', 'id':17},
          {'name':'Р', 'id':18},
          {'name':'С', 'id':19},
          {'name':'Т', 'id':20},
          {'name':'У', 'id':21},
          {'name':'Ф', 'id':22},
          {'name':'Х', 'id':23},
          {'name':'Ц', 'id':24},
          {'name':'Ч', 'id':25},
          {'name':'Ш', 'id':26},
          {'name':'Ь', 'id':27},
          {'name':'Ю', 'id':28},
          {'name':'Я', 'id':29}
          ]

with codecs.open(ANNOTATION_PATH + '/label_map.pbtxt', 'w', 'utf-8') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

gtf.main(xml_dir=IMAGE_PATH + '/train', labels_path=ANNOTATION_PATH + '/label_map.pbtxt', output_path=ANNOTATION_PATH + '/train.record')
gtf.main(xml_dir=IMAGE_PATH + '/test', labels_path=ANNOTATION_PATH + '/label_map.pbtxt', output_path=ANNOTATION_PATH + '/test.record')