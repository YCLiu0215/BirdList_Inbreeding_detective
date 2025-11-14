# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 20:18:09 2025

@author: Liu
"""
import pandas as pd
import numpy as np
import os

#The directory to the folder of bird list
dir_bird_list = r'C:\Users\Liu\OIST Dropbox\Liu Yung Chieh\Data\Yoko Unit\BirdList'
#Input the male and female for pairing
Male = 'O633'
Female = 'R762'

#Read the bird list
os.chdir(dir_bird_list)
files = os.listdir('.')
bl = pd.read_excel('Bird_List_new ver_2.xlsx')

#Function for the bird list search
def DadMom(seed):
    if all(bl['Bird ID'].str.contains(seed, case=False, na=False, regex=False)==False):
        matches = bl['Bird ID'][bl['Bird ID'].astype(str).apply(lambda x: x in seed)]
        if len(matches) == 0:
            print(seed+' cannot be found in bird list')
            return [np.nan,np.nan]
        elif len(matches) == 1:
            seed = matches.iloc[0]
            Parents = [bl.loc[bl['Bird ID'].str.contains(seed, case=False, na=False),'father'].iloc[0],bl.loc[bl['Bird ID'].str.contains(seed, case=False, na=False),'mother'].iloc[0]]
            if type(Parents[0])==str:
                return Parents
            else:
                return [np.nan,np.nan]
        else:
            print('Multiple targets found for ['+seed+']:')
            print(matches)
            seed = input("Which bird are you looking for:")
            Parents = [bl.loc[bl['Bird ID'].str.contains(seed, case=False, na=False),'father'].iloc[0],bl.loc[bl['Bird ID'].str.contains(seed, case=False, na=False),'mother'].iloc[0]]
            if type(Parents[0])==str:
                return Parents
            else:
                return [np.nan,np.nan]
    else:
        Parents = [bl.loc[bl['Bird ID'].str.contains(seed, case=False, na=False),'father'].iloc[0],bl.loc[bl['Bird ID'].str.contains(seed, case=False, na=False),'mother'].iloc[0]]
        if type(Parents[0])==str:
            return Parents
        else:
            return [np.nan,np.nan]


#function of getting all family information from a bird
def family_all(seeds):
    Subject = seeds[0]
    family = {'F0':[Subject]}
    family_list = [Subject]
    generation = 1
    n = [1]
    while seeds != []:
        '''
        print(n)
        '''
        n[generation-1] -= 1      
        seed = seeds[0]
        current_search = DadMom(seed)
        seeds.remove(seed)
        if current_search == [np.nan,np.nan]:
            pass
        else:
            family_list.append(current_search[0])
            family_list.append(current_search[1])
            if 'P'+str(generation) in family:
                family['P'+str(generation)].append(current_search[0])
                family['P'+str(generation)].append(current_search[1])
            else:
                family['P'+str(generation)] = current_search
            seeds.append(current_search[0])
            seeds.append(current_search[1])
            if generation == len(n):
                n.append(2)
            else:
                n[generation] +=2
        generation += (1 if n[generation-1] == 0 else 0)
    unique_elements, counts = np.unique(np.array(family_list),return_counts=True)
    if any(counts>1):
        print('INBREEDER ALERT ('+Subject+'):')
        print(unique_elements[counts > 1])
    else:
        pass
    return family, family_list
      
def SingleCheck(bird):
    FamilyTree, FamilyList = family_all([bird])
    for k, v in FamilyTree.items():
        print(f"{k}': {v}")
    
    
    
#Main code            
FT_male, family_male = family_all([Male])
FT_female, family_female = family_all([Female])

overlap = np.intersect1d(np.array(family_male), np.array(family_female))

if len(overlap) == 0:
    print('\nKin relationship not found')
else:
    print('\nInbreeding possibility detected!! \n')
    print('\nMale('+Male+'):')
    for kin in overlap:
        for P, pb in FT_male.items():
            if kin in pb:
                print('\t'+P+': '+kin+'')
    print('\nFemale('+Female+'): ')
    for kin in overlap:
        for P, pb in FT_female.items():
            if kin in pb:
                print('\t'+P+': '+kin+'')



