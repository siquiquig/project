#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Siquiqui Gomani
# DATE CREATED:  26/10/2019                                
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep
import argparse
import os
import math
from os import listdir


# Imports print functions that check the lab
from print_functions_for_lab_checks import *   

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time()
    
    # TODO 1: Define get_input_args function within the file get_input_args.py
    def get_input_args():
        """
        Retrieves and parses the the command line arguments created and defined by argparse module.
        3 command line arguments are created:
        dir - path to the pet image files (default-'pet_images/')
        arch - CNN model architecture to use for image classiffication 
        (default - pick any of the following alexnet,vgg,resnet)
        dog file - Text file that contains all tablesassociated to dogs (default- 'dognames.txt')
        """
        # creates parse
        
        parser = argparse.ArgumentParser()
        Parser.add_argument('--dir',type = str, default = 'pet_images/',
                            help = 'path to folder of pet_images')               
        parser.add_argument('--arch', type = str, default = 'vgg' , help = 'chosen model')
        parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                            help  = 'text file that has dognames') 
        return parser.parse_args()
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    #  the collection of these command line arguments from the function call as
    # the variable in_arg
    # Acccessing values of Arguments 1 and 2 by printing them
  
    # Function that checks command line arguments using in_arg  

    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
    
def get_pet_labels():
    """
    creates a dictionary of pet labels based on the filenames of the image files. reads in pet
    filenames and extracts pet image labels from filename and returns these labels as petlabel_dic
    image_dir -The (full) path to the folder of images that are to be classified by pretraines CNN
    models (string)
    Returns:
    petlabels_dic - Dictionary storing image file name
    """
    pet_images_list = listdir('./pet_images')
    petlabels = {}
    for idx in range(len(pet_images_list)):
        pet_images_name = pet_images_list[idx].lower()
        word_list = pet_images_name.split('_')
        petlabel = " "
    for word in word_list:
        if word.isalpha():
                petlabel+= word + " "
    petlabel = petlabel.strip()
    if pet_images_name not in petlabels:
           petlabels[pet_images_name] = petlabel
    else:
           print("warning", pet_images_name, "duplicate file exists in petlabels")
    return petlabels
          
    # Once the get_pet_labels function has been defined replace 'None' 
    # in the function call with in_arg.dir  Once you have done the replacements
    # your function call should look like this: 
    #             get_pet_labels(in_arg.dir)
    # This function creates the results dictionary that contains the results, 
    # this dictionary is returned from the function call as the variable results
    

    # Function that checks Pet Images in the results Dictionary using results    
    
    # TODO 3: Define classify_images function within the file classiy_images.py
def classify_images(images_dir = r"pet_images/",results_dic = None, model = "resnet"):
    for key in results_dic:
            results_dic[key].append(classifier(os.path.join(images_dir,key),model).lower())
            if results_dic[key][0] in results_dic[key][1]:
                results_dic[key].append("1")
            else:
                    results_dic[key].append('0')
                    classify_images(in_arg.dir,results,in_arg.arch)
                        
    
    # Once the classify_images function has been defined replace first 'None' 
    # in the function call with in_arg.dir and replace the last 'None' in the
    # function call with in_arg.arch  Once you have done the replacements your
    # function call should look like this: 
    #             classify_images(in_arg.dir, results, in_arg.arch)
    # Creates Classifier Labels with classifier function, Compares Labels, 
    # and adds these results to the results dictionary - results
    classify_images(None, results, None)

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)    

    
    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    def adjust_results4_isadog(results_dic,dogsfile):
        
        ''' 
        Adjusts the results dictionary to determine if classifier classified images "as adog" or "not 
        dog" , especially when not a match. Demonstrate if model architecture classified dog images 
        correctly even if there is a mismatch in dog breed
        parameters:
          results_dic- Dictionary with key as image filename and value as a list
                (index)idx 0 = pet image label
                       idx 1 = classifier label
                       idx 2 = 1/0(int) where 1 = match between pet image and classifier labels and 0 = 
                               no match between labels --- where idx 3 and idx 4 are added by this 
                               function---
                       idx 3 = 1/0(int) where 1 = pet image 'is-a' dog and 0 = pet image 'is-NOT-a dog
                       idx 4 = 1/6(int) where 1 = classifier classifies image 'is-a' dog and 0 =
                               classifies image 'as-NOT-a' dog
          dogsfile- A text file that contains names of all dogs from ImageNet 1000 labels(used by
                    classifier model) and dogmanes from pet image files. This file has one dogname per
                    line . Dog names are in lower case with spaces separating them
        Returns:
                None - results_dic is mutable
        '''  
        
        dognames_dic = dict()
        # Reads in dogsnames from file, 1 name per line and closes file.
        with open(dogsfile,'r') as f:
          
             for line in f:
                 line = line.rstrip()
                 if line not in dognames_dic:
                         dognames_dic[line]=1
                 else:
                       print('duplicate dogname',line)
        # Add to whether pet labels and classifier labels are dogs by appending two items to end of value
        # in results_dic
        # List index 3 = whether(1) or not (0) pet Image Label is a dog And list 
        # List index 4 = whether (1) or not(0) classifier Label  is a dog
        # By iterating through results_dic if labels are found in dog names_dic then label 'is a dog'
        # index 3/4 = 1 otherwise index 3/4 =0 'not a dog'
        for key in results_dic:
            if results_dic[key][0] in dognames_dic:
                if results_dic[key][1] in dognames_dic:
                       results_dic[key].extend((1,1))
                # Appends (1,1) because both labels are dogs
                else:
                    results_dic[key].extend((1,0))
            else:
                if results_dic[key][1] in dognames_dic:
                    results_dic[key].extend((0,1))
                else:
                    results_dic[key].extend((0,0))
                
    # Once the adjust_results4_isadog function has been defined replace 'None' 
    # in the function call with in_arg.dogfile  Once you have done the 
    # replacements your function call should look like this: 
    #          adjust_results4_isadog(results, in_arg.dogfile)
    # Adjusts the results dictionary to determine if classifier correctly 
    # classified images as 'a dog' or 'not a dog'. This demonstrates if 
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, None)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)


    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    def calculates_results_stats(results_dic):
        ''' This calculates statistics of results of the run using classifier model archtecture on
            on classify images then puts the results statistics in a dictionary(results_stats) so that 
            is returned for printing'''
        results_stats = dict()
    # Sets all accounts to zero
        results_stats['n_dogs_img'] = 0
        results_stats['n_match'] = 0
        results_stats['n_correct_dogs'] = 0
        results_stats['n_correct_notdogs'] = 0
        results_stats['n_correct_breed'] = 0
   # Pet image label is a dog and labels match
        if results_dic[key][2] == 1:
               results_stats['n_match'] += 1
   # Counts correct breed 
        if sum(results_dic[key][2:]) == 3:
               results_stats['n_correct_breed'] += 1
   # Counts number of dog images
        if results_dic[key][3] == 1:
            results_stats['n_dog_img'] += 1
   # Counts number of NOT dog classification
        if results_dic[key][4] == 0:
            results_stats['n_correct_notdogs'] += 1
  # Calculates number of total images
            results_stats['n_images'] = len(results_dic)
  # Calculates % correct for matches
            results_stats['pct_match'] = (results_stats['n_match']/results_stats['n_images'])*100
  # calculates % correct dogs
            results_stats['pct_correct_dogs'] = (results_stats['n_correct_dogs']/results_stats['n_dogs_img ']*100)       
                          
                         
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats    
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats

    # Function that checks Results Statistics Dictionary using results_stats
 
    # TODO 6: Define print_results function within the file print_results.py
    def print_results(results_dic, results_stats, model, print_incorrect_dogs = False, 
                      print_incorrect_breed = False):
        '''
        prints summary results on the classification, prints incorrectly classified dog breeds.
        parameters:
            results_dic - Dictionary with key as image filename and value as a list(index)
                          idx 0 = pet image  label (string)
                          idx 1 = classifier label (string)
                          idx 2 = 1/0 (int) where 1= match between pet Image  and classifier labels 
                          and 0 =no match between labels
                          idx 3 = 1/0 (int) where 1 = pet image 'IS- a ' dog and 0 = pct Image 
                          'IS-NOT-a dog
            results_stats - Dictionary that contains the results statistics (either a percentage
                            or a count) where the key is the statistics' name
            model- pretrained CNN whose architecture is indicated by this parameter
            print_incorrect_dogs - True prints incorrectly classified dog images and False doesnt
                                   print anything
            print_incorrect_breed - True prints incorrectly classified dog breeds and False doesnt 
                                    print anything
        Returns:
                          None - simply printing results.
            '''                  
    # Prints summary statistics over the run                        
        print('\n\n*** Results Summary for CNN Model Architecture', model.upper(),'***')
        print('%20s: %3d' % ('N Images', results_stats ['n_images']))
        print('%20s: %3d' % ('N dog Images', results_stats['n_dogs_img']))
        print('%20s: %3d' % ('N Not-Dog Images', results_stats['n_notdogs_img']))
   # prints summary statistics (percentages) on model run
        print(' ')
        for key in results_stats:
            if key[0] == 'p':
               print('%20s: %5.1f' % (key, results_stats[key]))
    # If print_incorrect_dogs == True and there were images incorrectly classified as dogs or otherwise - 
    # print out these scenarios
        if(print_incorrect_dogs and ( ( results_stats['n_correct_dogs'] + 
                                        results_stats['n_correct_notdogs']) != results_stats['n_images'])
                                    ):
            
          print('\nINCORRECT Dog/NOT Dog Assignments:')
    # process through results_dict, printing incorrectly classified dogs
          for key in resuts_dic:
             if sum(results_dic[key][key][3:]) == 1:
                print('Real: %-26s classifier: %-30s' % (results_dic[key][0],
                      results_dic[key][1]))
    # if print_incorrect_breed == True and there were dogs whose breeds were incorrectly classified
    # - printout these scenarios
    if (print_incorrect_breed and (results_stats ['n_correct_dogs'] != 
                                       results_stats['n_correct_breed'])
            ):
             print('\nINCORRECT Dog Breed Assignment:')
             for key in results_dic:
                 if (sum(results_dic[key][3:1]) == 2 and results_dic[key][2] == 0):
                     print('Real: %-26s classifier:-30s '(results_dic[key][0],
                      results_dic[key][1]))
                      
            
    # Once the print_results function has been defined replace 'None' 
    # in the function call with in_arg.arch  Once you have done the 
    # replacements your function call should look like this: 
    #      print_results(results, results_stats, in_arg.arch, True, True)
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
   
    
    # TODO 0: Measure total program runtime by collecting end time
    end_time = time()
    
    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time#calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
