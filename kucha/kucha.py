# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
class yzel():
    def _private(self, value, name): # создает объект
        self._in_cucha = False
        self._depth = 0
        self._name = name
        self._value = value
        self._status_in = False
        self._status_full = False #Слой потомков заполнен
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
    def _get_status(self): #вывод статуса
        print(self._status)
    def _add_detya(self, yzelp):  #добавления ребенка элементу или ребенка ребенка (рекурсия)
        right_n = None
        left_n = None
        if self._status_full ==  False: # если есть свободный слот 
            if  self._left_det == None:
                self._left_det = yzelp._name
                yzelp._parents = self._name
            elif self._right_det == None:
                self._right_det = yzelp._name
                yzelp._parents = self._name
                self._status_full =  True
            else:
                self._status_full = True
        else:
            left_n =  self._left_det # Имя левого ребенка узла к которому добавляем 
            right_n = self._right_det# Имя правого ребенка узла к которому добавляем 

            for i in massiv: # Ищем в массиве элементы детей узла 
                if i._name == left_n:
                    left = i
                    break
            for i in massiv:
                if i._name == right_n:
                    right = i
                    break
                                   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if left_n != None and right_n != None:   

                right._update_depth() # тут скорее всего ошибка в определении направлении спуска 
                left._update_depth() # надо свапать если элименты если левый больше правого
                if right._depth <left._depth:
                    for i in massiv:
                        if i._name == self._right_det:
                            i._add_detya(yzelp)
                            break
                else:    
                    for i in massiv:
                        if i._name == self._left_det:
                            i._add_detya(yzelp)
        if self._status != 'Корень' and self._status_full == True:
            self._status = 'Узел'
    def _get_all_status(self): # вывод атрибутов узла
        print('Узел %s', self._name)
        print(self._value)
        print(self._status_in)
        print(self._status)
        print('левый ребенок  ', self._left_det)
        print('павый ребенок  ', self._right_det)
        print(self._parents)

    def _swift_up(self):
        for i in massiv:
            if i._name == self._name:
                objekt = i
        while True:
            if objekt._parents == None:
                break
                
            for i in massiv: #Ищем родителей  элемента
                if i._name  == objekt._parents:
                    parents = i
            print("значение объекта значение родителя  \n",objekt._value,parents._value )
            if objekt._value < parents._value:
                print("меняем",objekt._value,parents._value)
                kucha1._swap_element(objekt, parents) #Меняем элементы местами
                objekt._update_status()
                parents._update_status()
                kucha1._update_coren()
                # Проверяем что элементы одного слоя стоят в правильном порядке
                left_elemen = None
                right_elemen = None
                for i in massiv:
                    if i._name == objekt._left_det:
                        left_elemen = i
                    if i._name == objekt._right_det:
                        right_elemen = i
                if left_elemen != None and right_elemen != None:        
                    if left_elemen._value > right_elemen._value:
                        kucha1._swap_element(left_elemen, right_elemen)
            else:
                break
        
        
    
    def _update_status(self,):
        if self._parents == None and kucha1._coren_y == False:
            self._status = 'Корень'
        elif self._left_det == None and self._right_det == None:
            self._status = 'Лист'
        else:
            self._status = 'Узел'
            
            
        
        
class kucha(): # куча состоит из узлов
    def _private(self):
        self._coren = False #Ссылка на корень
        self._coren_y = False # Статус наличия корня
        self._count = 0
        print('Куча создана')
    def  _update_coren(self):# обнвляет статусы всех элементов
        for i in massiv:
            if i._in_cucha == True:
                i._update_status() # 
        for i in massiv:
            if i._status == 'Корень' and self._coren_y == False:
                self._coren = i._name
    def _add_yzel(self, new_yzel):# добавление нового узла
        if self._coren == False and self._coren_y == False:
            new_yzel._set_status_cor()
            self._coren = new_yzel._name
            self._count = 1
            self._coren_y = True
            print('Элемент стал корнем')
        else:
            for i in massiv:
                if i._name == self._coren:
                    i._add_detya(new_yzel) # надо пофиксить добавление
                    self._count +=1
        new_yzel._in_cucha = True  # Помечаем что элемент в куче
    def _swap_element(self, elem1, elem2): # меняет элементы местами
        # !!!!!!!!!
        # надо менять и параметры ссылающихся элементов
        time.sleep(1)
        if elem1._parents == elem2._name:# элемент 1 ребенок элемента 2
            parent_sw = elem2._parents
            left_det_sw = elem2._left_det
            right_det_sw = elem2._right_det
            # меняем ссылки на меняемые объекты
            roditel_el_2 =None
            for i in massiv: # Ищем родителя 2 элемента
                if i._name == elem2._parents:
                    roditel_el_2 = i
                    break
            #Определяем какой это ребенок левый или правый
            if roditel_el_2 != None:    
                if roditel_el_2._left_det == elem2._name:
                    roditel_el_2._left_det = elem1._name
                elif roditel_el_2._right_det == elem2._name:
                    roditel_el_2._right_det = elem1._name
                            
            elem2._parents = elem1._parents
            elem2._left_det = elem1._left_det
            elem2._right_det = elem1._right_det
            
            elem1._parents = parent_sw
            elem1._left_det = left_det_sw
            elem1._right_det = right_det_sw
            #Создается момент что элементы содержат ссылки сами на себя
            if elem2._parents == elem2._name:
                elem2._parents = elem1._name
            
            if elem1._left_det == elem1._name:
                elem1._left_det = elem2._name
            if elem1._right_det == elem1._name:
                elem1._right_det = elem2._name
            
            #Поменяем ссылки детей нижнего слоя на родителя
            for i in massiv:
                if i._name == elem1._left_det:
                    i._parents = elem1._name
            for i in massiv:
                if i._name == elem1._right_det:
                    i._parents = elem1._name  
            for i in massiv:
                if i._name == elem2._left_det:
                    i._parents = elem2._name
            for i in massiv:
                if i._name == elem2._right_det:
                    i._parents = elem2._name 
                  
            if elem2._status == "Корень":
                elem1._status = "Корень"
                elem2._status = "Узел"
            
            elem1._update_status()
            elem2._update_status()
            
        elif elem2._parents == elem1._name: #элемент 2 является ребенком элемента 2
            # меняем ребенка у родителя
            parent_sw = elem2._parents
            left_det_sw = elem2.left_det
            right_det_sw = elem2.right_det
            
            for i in massiv: # Ищем родителя 1 элемента
                if i._name == elem1._parents:
                    roditel_el_1 = i
                    break
            #Определяем какой это ребенок левый или правый
            if roditel_el_1._left_det == elem1._name:
                roditel_el_1._left_det = elem2._name
            elif roditel_el_1._right_det == elem1._name:
                roditel_el_1._right_det = elem2._name
                
            elem2._parents = elem1._parents
            elem2._left_det = elem1._left_det
            elem2._right_det = elem1._right_det
            
            elem1.parents = parent_sw
            elem1._left_det = left_det_sw
            elem1._right_det = right_det_sw
            
            
            if elem1._parents == elem1._name:
                elem1._parents = elem2._name
            
            if elem2._left_det == elem2._name:
                elem2._left_det = elem1._name
            if elem2._right_det == elem2._name:
                elem2._right_det = elem1._name
            
            #Поменяем ссылки детей нижнего слоя на родителя
            for i in massiv:
                if i._name == elem1._left_det:
                    i._parents = elem1._name
            for i in massiv:
                if i._name == elem1._right_det:
                    i._parents = elem1._name  
            for i in massiv:
                if i._name == elem2._left_det:
                    i._parents = elem2._name
            for i in massiv:
                if i._name == elem2._right_det:
                    i._parents = elem2._name
                    
            if elem1._status == "Корень":
                elem2._status = "Корень"
                elem1._status = "Узел"
                
            elem1._update_status(kucha1)
            elem2._update_status(kucha1)                    
            print('Swap happend')
        elif elem2._parents == elem1._parents: # элемент 1 и 2 имеют общего родителя
            # Меняем ссылки на эти узлы у общего родителя
            for i in massiv:
                if i._name == elem1._parents:
                    left_swap = i._left_det
                    i._left_det = i._right_det
                    i._right_det = left_swap
            parent_sw = elem2._parents
            left_det_sw = elem2._left_det
            right_det_sw = elem2._right_det
            
            elem2._parents = elem1._parents
            elem2._left_det = elem1._left_det
            elem2._right_det = elem1._right_det
            
            elem1._parents = parent_sw
            elem1._left_det = left_det_sw
            elem1._right_det = right_det_sw
            # Меняем ссылки детей на родителей
            for i in massiv:
                if i._name == elem1._left_det:
                    i._parents = elem1._name
            for i in massiv:
                if i._name == elem1._right_det:
                    i._parents = elem1._name  
            for i in massiv:
                if i._name == elem2._left_det:
                    i._parents = elem2._name
            for i in massiv:
                if i._name == elem2._right_det:
                    i._parents = elem2._name   
            elem1._update_status()
            elem2._update_status()                    
            print('Swap happend')           
        else: # в других случаях менять элементы нельзя ибо все сломается
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
# valuearr =np.arange(0,dlina)
valuearr = np.random.randint(0,15, dlina)
# valuearr =[0,3,1,2,5,7,4]
for i in range(dlina):
    value = valuearr[i]
    yzel1 = yzel()
    name = 'yzel'+str(i+1)
    yzel1._private(value, name)
    massiv.append(yzel1)


kucha1 = kucha()
kucha1._private()
j=0
for j in massiv:
    kucha1._add_yzel(j)
    # j._update_status()
    print('start element', j._value)
    j._swift_up()
    # kucha1._update_coren()
    print('element in kucha')

kucha1._update_coren()
kucha1._print_kucha()