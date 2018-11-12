import csv
import igo

tagger = igo.tagger.Tagger()
title = [['キーワード','原形','品詞','品詞細分類']]
top_list=[]
every_row = tagger.parse(u'私はメールを送った。')
for item in every_row:
    array1=item.feature.split(",")
    top_list.append([item.surface,array1[6],array1[0],array1[1]])
with open(r'D:/igo.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(title)
    writer.writerows(top_list)
