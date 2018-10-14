# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 下午9:22
# @Brief   : 

import numpy as np
import os

class LoadData(object):
    '''
        return:
        Train_data format: a dictionary, 'Y' refers to a list of y values;
                                  'X' refers to a list of feature_M demension vectors with 0 or 1 entries
        Valid_data, Test_data
    '''

    def __init(self, path, dataset, loss_type):
        self.path = path + dataset + "/"
        self.trainfile = self.path + dataset + ".train.libfm"
        self.testfile = self.path + dataset + ".test.libfm"
        self.validationfile = self.path + dataset + ".validation.libfm"
        self.features_M = self.map_features()
        self.Train_data, self.Validation_day, self.Test_data = self.construct_data(loss_type)

    def map_features(self):
        # map the feature entries in all files, kept in self.features dict
        self.features = {}
        self.read_features(self.trainfile)
        self.read_features(self.testfile)
        self.read_features(self.validationfile)
        return len(self.features)

    def read_features(self, file_path):
        f = open(file_path)
        line = f.readline()
        i = len(self.features)
        while line:
            items = line.strip().split(' ')
            for item in items[1:]:
                if item not in self.features:
                    self.features[item] = i
                    i = i + 1
            line = f.readline()
        f.close()

    def construct_data(self, loss_type):
        X_, Y_, Y_for_logloss = self.read_data(self.trainfile)
        if loss_type == 'log_loss':
            Train_data = self.construct_dataset(X_, Y_for_logloss)
        else:
            Train_data = self.construct_dataset(X_, Y_)

        X_, Y_, Y_for_logloss = self.read_data(self.validationfile)
        if loss_type == 'log_loss':
            Validation_data = self.construct_dataset(X_, Y_for_logloss)
        else:
            Validation_data = self.construct_dataset(X_, Y_)

        X_, Y_, Y_for_logloss = self.read_data(self.testfile)
        if loss_type == 'log_loss':
            Test_data = self.construct_dataset(X_, Y_for_logloss)
        else:
            Test_data = self.construct_dataset(X_, Y_)

        return Train_data, Validation_data, Test_data

    def read_data(self, file_path):
        f = open(file_path)
        X_ = []
        Y_ = []
        Y_for_logloss = []
        line = f.readline()
        while line:
            items = line.strip().split(' ')
            Y_.append(1.0 * float(items[0]))

            if float(items[0]) > 0:
                v = 1.0
            else:
                v = 0.0
            Y_for_logloss.append(v)

            X_.append([self.features[item] for item in items[1:]])
            line = f.readline()
        f.close()
        return X_, Y_, Y_for_logloss

    def construct_dataset(self, X_, Y_):
        Data_Dic = {}
        X_lens = [len(line) for line in X_]
        indexs = np.argsort(X_lens)
        Data_Dic['Y'] = [Y_[i] for i in indexs]
        Data_Dic['X'] = [X_[i] for i in indexs]
        return Data_Dic

    def truncate_features(self):
        pass







