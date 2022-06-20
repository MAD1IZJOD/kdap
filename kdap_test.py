#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:28:34 2020

@author: Main
"""

import kdap

knol = kdap.knol()

knol.download_dataset(sitename='wikipedia', article_list=['Vector', 'Derivative'], destdir='~/knolml_dataset/wikipedia_articles')

num_instances = knol.get_num_instances(dir_path='~/knolml_dataset/wikipedia_articles', granularity='yearly', start='2015-01-01')

print("Displaying the number of instances for articles")
for key,val in num_instances.items():
  print(key, val)
  
editors = knol.get_editors(dir_path='/home/descentis/knolml_dataset/wikipedia_articles', granularity='monthly')

print("Displaying the editor names")
for key,val in editors.items():
  print(key, val)
  
#edits = knol.get_author_edits(dir_path='/home/descentis/knolml_dataset/wikipedia_articles', editor_list=['212.219.142.201', 'Redvers', 'Septegram', '87.10.191.84', '72.90.235.102', 'ItsProgrammable'])

#local_gini = knol.get_local_gini_coefficient(dir_path='/home/descentis/knolml_dataset/wikipedia_articles')

#adj_list = knol.get_induced_graph_by_articles(['Vector', 'Derivative'])
