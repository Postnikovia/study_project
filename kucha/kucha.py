# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:07:04 2020

@author: Иван
"""


class yzel():
    def _private(self, value, name):
        self._depth = 0
        self._name = name
        self._value = value
        self._status_in = False
        self._status_full = False
        self._status = 'Лист'
        self._left_det = None
        self._right_det = None
        self._parents = None
        print('Узел создан')
    def _update_depth(self):  #Обновляет параметр глубина
        schet = 0
        name_det = self._name
        while True:
            # ищем объект из массива
            for i in massiv:
                if i._name == name_det:
                    element = i

            # проверяем ребенка и пока есть непустое смещение вправо добавляем 1 к счетчику глубины        
            if element._right_det == None:
                break
            else:
                name_det = element._right_det
                if element._status_full == True:
                    schet += 1
        self._depth = schet
    def _set_status_cor(self):
        self._status = 'Корень'
    def _get_status(self):
        print(self._status)
    def _add_detya(self, yzelp):  #добавления ребенка элементу или ребенка ребенка (рекурсия)
        
        if self._status_full ==  False:
            if  self._left_det == None:
                self._left_det = yzelp._name
                yzelp._parents = self._name
            elif self._right_det == None:
                self._right_det = yzelp._name
                yzelp._parents = self._name
                self._status_full =  True
        else:
            left_n =  self._left_det
            right_n = self._right_det
            for i in massiv:
                if i._name == left_n:
                    left = i
                    break
            for i in massiv:
                if i._name == right_n:
                    right = i
                    break
            right._update_depth()
            left._update_depth()
            if right._depth <left._depth:
                for i in massiv:
                    if i._name == self._right_det:
                        i._add_detya(yzelp)                
            else:    
                for i in massiv:
                    if i._name == self._left_det:
                        i._add_detya(yzelp)
        if self._status != 'Корень' and self._status_full == True:
            self._status = 'Узел'
    def _get_all_status(self):
        print('Узел %s', self._name)
        print(self._value)
        print(self._status_in)
        print(self._status)
        print('левый ребенок  ', self._left_det)
        print('павый ребенок  ', self._right_det)
        print(self._parents)

    def _swift_up(self, kucha1):
        for i in massiv:
            if i._name == self._name:
                objekt = i
        while True:
            if objekt._parents == None:
                break
                
            for i in massiv:
                if i._name  == objekt._parents:
                    parents = i
            if objekt._value < parents._value:
                kucha1._swap_element(objekt, parents)
                objekt._update_status()
                parents._update_status()
                kucha1._update_coren()
            else:
                break
    
    def _update_status(self):
        if self._parents == None:
            self._status = 'Корень'
        elif self._left_det == None and self._right_det == None:
            self._status = 'Лист'
        else:
            self._status = 'Узел'
            
            
        
        
class kucha():
    def _private(self):
        self._coren = False
        self._count = 0
        print('Куча создана')
    def  _update_coren(self):
        for i in massiv:
            if i._status == 'Корень':
                self._coren = i._name
    def _add_yzel(self, new_yzel):# добавление нового узла
        if self._coren == False:
            new_yzel._set_status_cor()
            self._coren = new_yzel._name
            self._count = 1
            print('Элемент стал корнем')
        else:
            for i in massiv:
                if i._name == self._coren:
                    i._add_detya(new_yzel)
                    self._count +=1
    def _swap_element(self, elem1, elem2): # меняет родителя и ребенка местами
        if elem1._parents == elem2._name:
            # меняем ребенка у родителя
            for i in massiv:
                if i._name == elem2._parents:
                    if i._left_det == elem2._name:
                        i._left_det = elem1._name
                    else:
                        i._right_det = elem1._name
                    break
            # Замена детей и родителей
            left1 = elem1._left_det
            right1 = elem1._right_det
            parent = elem2._parents
            if elem2._left_det ==elem1._name:
                elem1._right_det = elem2._right_det
                elem1._left_det = elem2._name
            else:
                elem1._left_det = elem2._left_det
                elem1._right_det = elem2._name
            
            elem2._parents = elem1._name
            elem2._left_det = left1
            elem2._right_det = right1
            elem1._parents = parent
            print('Swap happend')
            
        elif elem2._parents == elem1._name:
            # меняем ребенка у родителя
            for i in massiv:
                if i._name == elem1._parents:
                    if i._left_det == elem1._name:
                        i._left_det = elem2._name
                    else:
                        i._right_det = elem2._name
                    break
            
            # Замена детей и родителей
            left1 = elem2._left_det
            right1 = elem2._right_det
            parent = elem1._parents
            if elem1._left_det ==elem2._name:
                elem2._right_det=elem1._right_det
                elem2._left_det = elem1._name
            else:
                elem2._left_det = elem1._left_det
                elem2._right_det = elem1._name
            
            elem1._parents = elem2._name
            elem1._left_det = left1
            elem1._right_det = right1
            elem2._parents = parent
            print('Swap happend')
        else:
            print('Swap error')
        
    def _print_kucha(self):
        obj_n = self._coren
        name=[]
        otstup = [1,2,4,8,16,32]
        schet = otstup[0]
        otstup = otstup[1:]
        j=0
        name.append(obj_n)
        while True:

            new_name = name[0]
            name = name[1:]
            for i in massiv:
                if i._name == new_name:
                    print(i._value, end =' ')
                    j+=1
                    if j == schet:
                        print(' ')
                        j=0
                        schet = otstup[0]
                        otstup = otstup[1:]
                    name.append(i._left_det)
                    name.append(i._right_det)

            if name == []:
                break
                
                        
dlina = int(input())
massiv = []
import numpy as np
valuearr =np.arange(0,dlina)
#valuearr = np.random.randint(0,15, dlina)
for i in range(dlina):
    value = valuearr[i]
    yzel1 = yzel()
    name = 'yzel'+str(i+1)
    yzel1._private(value, name)
    massiv.append(yzel1)


kucha1 = kucha()
kucha1._private()
j=0
for i in massiv:
    kucha1._add_yzel(i)
    i._update_status()
    if j>0:
        massiv[j]._swift_up(kucha1)
    j +=1
    kucha1._update_coren()

kucha1._update_coren()
kucha1._print_kucha()
    


