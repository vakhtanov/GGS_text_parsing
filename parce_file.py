# -*- coding: utf-8 -*-
import os, re

def parce_gg_block(GGSBlock,out_folder,NumberOfGGSs): #РАЗБОР ПО СИМВОЛАМ
    #print('Рабочий блок'.encode('cp866'),len(GGSBlock))
    print('Рабочий блок',len(GGSBlock))
    """
    ##ВАЖНО!!!! .decode('cp1251').encode('utf-8') - перекодировка в UTF8!!!! - раскоидрование из юникод символов
    i=0
    for line in GGSBlock:
        line_decode=line.decode('cp1251').encode('utf-8')
        GGSBlock[i]=line_decode
        i+=1
    """
    #=============SEARCH VARIBLES=========================
    #print(GGSBlock[0])
    #Делаем шаблон с группами
    #Distant_search0=re.compile('(\s*Удаление=\s*)(\d{1,10})')
    #Ищем и берем 2ю группу - расстояние
    #ToDO groups - надо отделить с проверкой вхождения - это защита
    #-----------------------
    SEARCH = re.search('(\s*Удаление=\s*)(\d{1,10})', GGSBlock[0])
    if SEARCH != None:
        Distant=SEARCH.groups()[1]
        #print('Distant:', Distant,'.')
    #-----------------------
    SEARCH = re.search('\s*(\w\d{7}\s*\d)\s*(.*\S)\s*', GGSBlock[1])
    if SEARCH != None :
        Comment1=SEARCH.groups()[0]
        Name_Type=SEARCH.groups()[1]
        #print('Comment1:', Comment1,'.')
        #print('Name_Type:', Name_Type,'.')
    #-----------------------
    SEARCH = re.search('\s*Центр\s*(\S*)\s*Марка №\s*(\S{1,5})\s*', GGSBlock[2])
    if SEARCH != None :
        Center=SEARCH.groups()[0]
        Marka=SEARCH.groups()[1]
        #print('Center:', Center,'.')
        #print('Marka:', Marka,'.')
    #-----------------------
    #Todo what means "G98 and rG98"
    SEARCH = re.search('\s*(.-..-...-\w-\w)\s*(\d*.\d*)\s*(\d*.\d*)\s*\S{0,1}Hn=\s*(-{0,1}\d*.\d*)\s*\S{0,1}G98=\s*(-{0,1}\d*.\d*)\s*(\w{2}-\S*)\s*', GGSBlock[3])
    print(GGSBlock[3])
    print('SEARCH',SEARCH)
    if SEARCH != None :
        Nomenklatura1=SEARCH.groups()[0]
        SK42_X=SEARCH.groups()[1]
        SK42_Y=SEARCH.groups()[2]
        Hn=SEARCH.groups()[3]
        G98=SEARCH.groups()[4]
        Proj1=SEARCH.groups()[5]
        print('Nomenklatura1:', Nomenklatura1, '.')
        print('SK42_X:', SK42_X, '.')
        print('SK42_Y:', SK42_Y, '.')
        print('Hn:', Hn, '.')
        print('G98:', G98, '.')
        print('Proj1:', Proj1, '.')





    out_test_file = os.path.join(out_folder, 'ggs'+str(NumberOfGGSs)+'.txt')
    with open(out_test_file, 'w') as out_f:
        for line in GGSBlock:
            out_f.write(line)
        #print(GGSBlock)
def parse_ggs_file(in_file,out_folder):
    StageParce=0
    StartLine=0
    NumberOfGGSs=0
    """
    Стадии парсинга для контроля 
    0 - инициализация
    1 - найдено =*78
    #2 - надена точка
    3 - найдено начало 1 го пункта стадия поиска записей пункта
        по окончанию парсинга - NumberOfGGSs +=1 и переключение на 2ю стадию
    4 - найдена вторая =*78
    """
    # Файл в виндовской кодировке!!
    with open(in_file,'r', encoding='cp1251') as in_f: 
        GGSBlock = []
        FileLine=0
        print(in_f)
        for line in in_f:
            FileLine+=1
            #print(FileLine)
            

            if '-'*60 in line and StageParce == 2:
                StageParce =3
                GGSBlockCount = 1
                GGSBlock.append(line)
                #continue
            elif  ('-'*60 in line or '=' * 78 in line) and StageParce ==3:
                #===============================================
                NumberOfGGSs += 1
                parce_gg_block(GGSBlock,out_folder,NumberOfGGSs) #обработка блока пункта
                #==============================================
                GGSBlock=[]
                GGSBlock.append(line)
                GGSBlockCount=1
                #print('Start next GGS', FileLine)
            elif StageParce ==3:
                GGSBlockCount += 1
                #print(GGSBlockCount,FileLine)
                #==================
                GGSBlock.append(line)
                #===================
            if '=' * 78 in line and StartLine==0 and StageParce == 0:
                StartLine = 1
                StageParce = 1
                print('start section',StartLine,StageParce)
            elif '=' * 78 in line and StartLine==1:
                StartLine = 2
                StageParce = 4
                #print('break')
                break
            if StageParce == 1:
                #ToDO добавить поиск точки начала
                StageParce = 2
        if StartLine == 2 and StageParce == 4:
            print('start section', StartLine, StageParce)
            print('end of file')
        else:
            print('error format of file')




if __name__=='__main__':
    in_file=u'c:\\Users\\Андрей\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\GGS_text_parsing\\sample_ggs\\Sample.txt'
    out_folder=u'c:\\Users\\Андрей\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\GGS_text_parsing\\sample_ggs\\out_folder'
    parse_ggs_file(in_file,out_folder)