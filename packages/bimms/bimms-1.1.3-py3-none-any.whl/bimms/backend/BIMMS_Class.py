"""
Access and modify BIMMS Parameters
Authors: Florian Kolbl / Roland Giraud / Louis Regnacq / Thomas Couppey
(c) ETIS - University Cergy-Pontoise - CNRS
"""
from abc import ABCMeta, abstractmethod
from copy import deepcopy

# sys used in an eval
import sys
import numpy as np
from numpy import iterable

from .file_handler import json_dump, json_load


debug = False
########################################
#           check object               #
########################################


def is_BIMMS_class(x):
    return isinstance(x, BIMMS_class)


def is_BIMMS_class_list(x):
    if iterable(x):
        for xi in x:
            if not is_BIMMS_class(xi):
                return False
        return True
    return False


def is_BIMMS_class_dict(x):
    if isinstance(x, dict):
        for xi in x.values():
            if not is_BIMMS_class(xi):
                return False
        return True
    return False


##########################################
#           check dictionaries           #
##########################################


def is_BIMMS_object_dict(x):
    return is_BIMMS_dict(x) or is_BIMMS_dict_list(x) or is_BIMMS_dict_dict(x)


def is_BIMMS_dict(x):
    if isinstance(x, dict):
        if "bimms_type" in x:
            return True
    return False


def is_BIMMS_dict_list(x):
    if iterable(x):
        if len(x) > 0:
            for xi in x:
                if not (is_BIMMS_dict(xi)):
                    return False
            return True
    return False


def is_BIMMS_dict_dict(x):
    if isinstance(x, dict):
        for key in x:
            if not (is_BIMMS_dict(x[key])):
                return False
        return True
    return False


class BIMMS_class(metaclass=ABCMeta):
    """
    Instanciate a basic BIMMS class
    BIMMS Class are empty shells, defined as abstract classes of which every class in BIMMS
    should inherite. This enable automatic context backup with save and load methods
    """

    @abstractmethod
    def __init__(self,fixed_attr=True):
        """
        Init method for BIMMS class
        """
        self.__BIMMSObject__ = True
        self.verbose = True
        self.bimms_type = self.__class__.__name__
        self.__fixed_attr = fixed_attr
        if debug:
            print("DEBUG: ", self.bimms_type, " initialized")

    def __del__(self):
        """
        Destructor for BIMMS class
        """
        if debug:
            print("DEBUG: ", self.bimms_type, " deleted")

    def save(self, save=False, fname="bimms_save.json", blacklist=[], **kwargs):
        """
        Generic saving method for BIMMS class instance

        Parameters
        ----------
        save : bool, optional
            If True, save the BIMMS object in a json file
        fname : str, optional
            Name of the json file
        blacklist : dict, optional
            Dictionary containing the keys to be excluded from the save
        **kwargs : dict, optional
            Additional arguments to be passed to the save method of the BIMMS object
        """
        key_dic = {}
        for key in self.__dict__:
            if key not in blacklist:
                if is_BIMMS_class(self.__dict__[key]):
                    #print(key)
                    key_dic[key] = self.__dict__[key].save(**kwargs)
                elif is_BIMMS_class_list(self.__dict__[key]):
                    key_dic[key] = []
                    for i in range(len(self.__dict__[key])):
                        key_dic[key] += [self.__dict__[key][i].save(**kwargs)]
                elif is_BIMMS_class_dict(self.__dict__[key]):
                    key_dic[key] = {}
                    for i in self.__dict__[key]:
                        key_dic[key][i] = self.__dict__[key][i].save(**kwargs)
                else:
                    key_dic[key] = deepcopy(self.__dict__[key])
        if save:
            json_dump(key_dic, fname)
        return key_dic

    def load(self, data, blacklist={}, **kwargs):
        """
        Generic loading method for BIMMS class instance

        Parameters
        ----------
        data : dict
            Dictionary containing the BIMMS object
        blacklist : dict, optional
            Dictionary containing the keys to be excluded from the load
        **kwargs : dict, optional
            Additional arguments to be passed to the load method of the BIMMS object
        """
        if isinstance(data, str):
            key_dic = json_load(data)
        else:
            key_dic = data
        if not self.__fixed_attr:
            for key in key_dic:
                if  key not in self.__dict__ and key not in blacklist:
                    self.__dict__[key] = None
        for key in self.__dict__:
            if key in key_dic and key not in blacklist:
                if is_BIMMS_object_dict(key_dic[key]):
                    self.__dict__[key] = load_any(key_dic[key], **kwargs)
                elif isinstance(self.__dict__[key], np.ndarray):
                    self.__dict__[key] = np.array(key_dic[key])
                elif isinstance(self.__dict__[key], dict) and key_dic[key] == []:
                    self.__dict__[key] = {}
                else:
                    self.__dict__[key] = key_dic[key]


def load_any(data, **kwargs):
    """loads an object of any kind from a json file

    Args:
        data : _description_

    Returns:
        _type_: _description_
    """
    if isinstance(data, str):
        key_dic = json_load(data)
    else:
        key_dic = data
    # test if BIMMS class
    if is_BIMMS_class(key_dic) or is_BIMMS_class_list(key_dic):
        bimms_obj = key_dic
    # test if BIMMS dict
    elif is_BIMMS_dict(key_dic):
        bimms_type = key_dic["bimms_type"]
        bimms_obj = eval('sys.modules["bimms"].' + bimms_type)()
        bimms_obj.load(key_dic, **kwargs)
    elif is_BIMMS_dict_dict(key_dic):
        bimms_obj = {}
        for key in key_dic:
            bimms_obj[key] = load_any(key_dic[key], **kwargs)
    elif is_BIMMS_dict_list(key_dic):
        bimms_obj = []
        for i in key_dic:
            bimms_obj += [load_any(i, **kwargs)]
    return bimms_obj
