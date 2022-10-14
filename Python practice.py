# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 08:19:26 2021

@author: MREller
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
import sklearn
import seaborn as sns

spotify_data = pd.read_csv(r'C:\Users\MREller\PYTHON\Spotify Data\data.csv')
#spotify_data.head()

spotify_data_w_genres = pd.read_csv(r'C:\Users\MREller\PYTHON\Spotify Data\data_w_genres.csv')
#spotify_data_w_genres.head()

spotify_data_by_genres = pd.read_csv(r'C:\Users\MREller\PYTHON\Spotify Data\data_by_genres.csv')
#spotify_data_by_genres.head()

spotify_data_by_artist = pd.read_csv(r'C:\Users\MREller\PYTHON\Spotify Data\data_by_artist.csv')
#spotify_data_by_artist.head()

spotify_data_by_year = pd.read_csv(r'C:\Users\MREller\PYTHON\Spotify Data\data_by_year.csv')
#spotify_data_by_year.head()

#print('spotify_data')
#print(spotify_data.columns)
#print('\n')
#print('spotify_data_w_genres')
#print(spotify_data_w_genres.columns)
#print('\n')
#print('spotify_data_by_genres')
#print(spotify_data_by_genres.columns)
#print('\n')
#print('spotify_data_by_artist')
#print(spotify_data_by_artist.columns)
#print('\n')
#print('spotify_data_by_year')
#print(spotify_data_by_year.columns)

a = spotify_data_w_genres.columns.intersection(spotify_data.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data and spotify_data_w_genres:\n" + '\033[0m',a)
b = spotify_data_by_genres.columns.intersection(spotify_data.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data and spotify_data_by_genres:\n" + '\033[0m',b)
c = spotify_data_by_artist.columns.intersection(spotify_data.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data and spotify_data_by_artist:\n" + '\033[0m',c)
d = spotify_data_by_year.columns.intersection(spotify_data.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data and spotify_data_by_year:\n" + '\033[0m',d)
e = spotify_data_by_genres.columns.intersection(spotify_data_w_genres.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data_w_genres and spotify_data_by_genres:\n" + '\033[0m',e)
f = spotify_data_by_artist.columns.intersection(spotify_data_w_genres.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data_w_genres and spotify_data_by_artist:\n" + '\033[0m',f)
g = spotify_data_by_year.columns.intersection(spotify_data_w_genres.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data_w_genres and spotify_data_by_year:\n" + '\033[0m',g)
h = spotify_data_by_artist.columns.intersection(spotify_data_by_genres.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data_by_genres and spotify_data_by_artist:\n" + '\033[0m',h)
i = spotify_data_by_year.columns.intersection(spotify_data_by_genres.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data_by_genres and spotify_data_by_year:\n" + '\033[0m',i)
j = spotify_data_by_year.columns.intersection(spotify_data_by_artist.columns)
#print ('\033[1m' + "Common Columns betweeen spotify_data_by_artist and spotify_data_by_year:\n" + '\033[0m',j)

k = a&b&c&d&e&f&g&h&i&j

#print ('\033[1m' + "Common Columns betweeen all tables:\n" + '\033[0m',k)
#spotify_data_by_genres[k].head()

#spotify_data.corr()
#spotify_data_by_year.corr()
#spotify_data_by_genres[k].corr()

#spotify_data
#spotify_data_w_genres
#spotify_data_by_genres
#spotify_data_by_artist
#spotify_data_by_year

#spotify_data_w_genres[k].corr()
#
#spotify_data_w_genres[k].corr().unstack().sort_values().drop_duplicates()
#
#spotify_data_w_genres[k].corr().unstack().abs().sort_values().drop_duplicates()

#corr = spotify_data_w_genres[k].corr()
#kot = corr[abs(corr)<=0.99]
##plt.figure(figsize=(12,8))
#sns.heatmap(kot, cmap="viridis")

#Clustering Analysis
sdwg = spotify_data_w_genres[k].head(1000)
sdwg_labels = sdwg.columns

#create linkage matrix for clustering
z = linkage(sdwg,'ward')

#plot dendrogram of clusters
plt.figure(figsize=(20,20))
plt.title('Cluster with all shared song descriptors')
plt.ylabel('distance')
dendrogram(
        z,
        orientation = 'right',
        labels = sdwg.index,
        leaf_rotation = 0.,
        leaf_font_size = 5.,
        show_contracted = True,
)
plt.show()