# -*- coding: utf-8 -*-
import os

def parce_gg_block(GGSBlock,out_folder,NumberOfGGSs): #РАЗБОР ПО СИМВОЛАМ
    #print('Рабочий блок'.encode('cp866'),len(GGSBlock))
    print(u'Рабочий блок'.encode('cp866'),len(GGSBlock))
    ##ВАЖНО!!!! .decode('WINDOWS-1251').encode('UTF-8') - перекодировка в UTF8!!!!
    i=0
    for line in GGSBlock:
        #GGSBlock[i]=line.decode('WINDOWS-1251').encode('UTF-8')
        GGSBlock[i]=line.decode('WINDOWS-1251').encode('UTF-8')
        i+=1

    out_test_file = os.path.join(out_folder, 'ggs'+str(NumberOfGGSs)+'.txt')
    with open(out_test_file, 'w') as out_f:
        for line in GGSBlock:
            #line.decode('WINDOWS-1251').encode('UTF-8')
            out_f.write(line)
        print(GGSBlock)
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
    print ('in_file', in_file)


    with open(in_file) as in_f:
        GGSBlock = []

        FileLine=0
        for line in in_f:
            FileLine+=1
            #print(FileLine)
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

            if '-'*60 in line and StageParce == 2:
                StageParce =3
                GGSBlockCount = 1
                GGSBlock.append(line)
                #continue
            elif  '-'*60 in line and StageParce ==3:
                #===============================================
                NumberOfGGSs += 1
                parce_gg_block(GGSBlock,out_folder,NumberOfGGSs) #обработка блока пункта
                #==============================================
                GGSBlock=[]
                GGSBlock.append(line)
                GGSBlockCount=1
                print('Start next GGS', FileLine)
            elif StageParce ==3:
                GGSBlockCount += 1
                print(GGSBlockCount,FileLine)
                #==================
                GGSBlock.append(line)
                #===================


        if StartLine == 2 and StageParce == 4:
            print('start section', StartLine, StageParce)
            print('end of file')
        else:
            print('error format of file')




if __name__=='__main__':
    in_file=u'c:\\Users\\Андрей\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\GGS_text_parsing\\sample_ggs\\Sample.txt'
    out_folder=u'c:\\Users\\Андрей\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\GGS_text_parsing\\sample_ggs\\out_folder'
    parse_ggs_file(in_file,out_folder)