#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author: 张知临 zhzhl202@163.com
#Filename: tms_svm.py
'''此处封装了libsvm与liblinear'''
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),"dependence"))


import svm
import svmutil
import liblinear
import liblinearutil 

read_problem = lambda x:x
train =  lambda x:x
predict =  lambda x:x
save_model =  lambda x:x
load_model = lambda x:x
svm_type=""
def set_svm_type(type):
    global read_problem,train,predict,save_model,load_model,svm_type
    svm_type = type
    if svm_type=="libsvm":
        read_problem = svmutil.svm_read_problem
        train = svmutil.svm_train
        predict = svmutil.svm_predict
        save_model = svmutil.svm_save_model
        load_model = svmutil.svm_load_model
            
    if svm_type=="liblinear":
        read_problem = liblinearutil.svm_read_problem
        train = liblinearutil.train
        predict = liblinearutil.predict
        save_model = liblinearutil.save_model
        load_model = liblinearutil.load_model
        
def detect_svm_type(model):
    f= open(model,'r')
    svm_type = ""
    for line in f.readlines():
        line = line.split()
        if line[0]=="svm_type":
            svm_type="libsvm"
            break
        if line[0]=="solver_type":
            svm_type="liblinear"
            break
    return svm_type
            


     