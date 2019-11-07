# -*- coding: utf-8 -*-
import os, re
def deg_min_sec2degree(DMS_text):
    pass
def parce_gg_block_positions(GGSBlock,out_folder,NumberOfGGSs): #РАЗБОР ПО ПОЗИЦИЯМ
    pass

def parce_gg_block_keys(GGSBlock,out_folder,NumberOfGGSs): #РАЗБОР Ключевым словам
    #print('Рабочий блок'.encode('cp866'),len(GGSBlock))
    #print('Рабочий блок',len(GGSBlock))
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
    else:
        Distant='Формат??'
    #-----------------------
    SEARCH = re.search('\s*(\w\d{7}\s*\d)\s*(.*)\s*', GGSBlock[1])
    if SEARCH != None :
        Comment1=' '.join(SEARCH.groups()[0].split())
        Name_Type=' '.join(SEARCH.groups()[1].split())
        #print('Comment1:', Comment1,'.')
        #print('Name_Type:', Name_Type,'.')
    else:
        Comment1='Формат??'
        Name_Type='Формат??'
    #-----------------------
    SEARCH = GGSBlock[2].split()
    print(SEARCH)
    if SEARCH != None :
        Center_Marka=' '.join(SEARCH)
        print('Center_Marka:', Center_Marka,'.')
    else:
        Center_Marka='Формат??'
    #-----------------------
    ### projection=['СК-42','BL-42','CK-63/42','СК-95','BL-95','ПЗ-90','ПЗ-90.02','WGS-84','BL-WGS']
    #=====================ПРАСИНГ КООРДИНАТ===================================================
    line_SK42=r' A-00-000-А-а 0000000.00 0000000.00 Hn= 000.00 g00= 0.00 СК-42 ' #3
    line_BL42=r' 00°00\'00.0000\" 00°00\'00.0000\" g00= 0.00 BL-42 ' #4
    line_SK63_42=r' A-00- 00-А-А 0000000.00 P0000000.00(0000000.00 P0000000.00) CK-63/42 ' #5
    line_SK95=r' 0000000.00 0000000.00 Hg= 000.00 СК-95 ' #6
    line_BL95=r' 00°00\'00.0000\" 00°00\'00.0000\" BL-95 ' #7
    line_PZ90=r' 0000000.00 0000000.00 0000000.00 ПЗ-90 ' #8
    line_PZ9002=r' 0000000.00 0000000.00 0000000.00 ПЗ-90.02 ' #9
    line_WGS84=r' 0000000.00 0000000.00 0000000.00 WGS-84 ' #10
    line_BLWGS84=r' 00°00\'00.0000\" 00°00\'00.0000\" Hw= 000.00 Gwg= 00.00 BL-WGS ' #11
    
    for line in GGSBlock:
        if 'СК-42' in line: line_SK42=line
        if 'BL-42' in line: line_BL42=line
        if 'CK-63/42' in line: line_SK63_42=line
        if 'СК-95' in line: line_SK95=line
        if 'BL-95' in line: line_BL95=line
        if 'ПЗ-90' in line: line_PZ90=line
        if 'ПЗ-90.02' in line: line_PZ9002=line
        if 'WGS-84' in line: line_WGS84=line
        if 'BL-WGS' in line: line_BLWGS84=line
    #======================
    SEARCH = re.search('\s*(.-..-...-\w-\w)\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(Hn=\s*-{0,1}\d*\.\d*\s*\S{0,1})?\s*([gG]98=\s*-{0,1}\d*\.\d*)?\s*(\w{2}-\S*)\s*', line_SK42)
    if SEARCH != None :
        Nomenklatura1=SEARCH.groups()[0]
        SK42_X=SEARCH.groups()[1]
        SK42_Y=SEARCH.groups()[2]
        Hn=SEARCH.groups()[3]
        G98=SEARCH.groups()[4]
        Proj1=SEARCH.groups()[5]
        #print('Nomenklatura1:', Nomenklatura1, '.')
        #print('SK42_X:', SK42_X, '.')
        #print('SK42_Y:', SK42_Y, '.')
        #print('Hn:', Hn, '.')
        #print('G98:', G98, '.')
        #print('Proj1:', Proj1, '.')
    else:
        Nomenklatura1 = 'Формат??'
        SK42_X = 'Формат??'
        SK42_Y = 'Формат??'
        Hn = 'Формат??'
        G98 = 'Формат??'
        Proj1 = 'Формат??'
    # -----------------------
    SEARCH = re.search(r'\s*(\d{2}°\d{2}\'\d{2}\.\d*\")\s*(\d{2}°\d{2}\'\d{2}\.\d*\")\s*([gG]87=\s*-{0,1}\d*\.\d*)?\s*(\w{2}-\S*)\s*',line_BL42)
    if SEARCH != None:
        SK42_B = SEARCH.groups()[0]
        SK42_L = SEARCH.groups()[1]
        G87 = SEARCH.groups()[2]
        Proj2 = SEARCH.groups()[3]
        #print('SK42_B:', SK42_B, '.')
        #print('SK42_L:', SK42_L, '.')
        #print('G87:', G87, '.')
        #print('Proj2:', Proj2, '.')
    else:
        SK42_B = 'Формат??'
        SK42_L = 'Формат??'
        G87 = 'Формат??'
        Proj2 = 'Формат??'
        # print('SK42_B:', SK42_B, '.')
        # print('SK42_L:', SK42_L, '.')
        # print('G87:', G87, '.')
        # print('Proj2:', Proj2, '.')
    #-----------------------
    SEARCH = re.search('\s*(.-..-...-\w-\w)\s*(\d*\.\d*)\s*(\S{0,1}.*\d*\.\d*).*\((\d*\.\d*)\s*(\S{0,1}.*\d*\.\d*)\)\s*(\w{2}-\S*/\S*)\s*', line_SK63_42)
    if SEARCH != None :
        Nomenklatura2=SEARCH.groups()[0]
        SK63_X=SEARCH.groups()[1]
        SK63_Y=SEARCH.groups()[2]
        SK63_X2=SEARCH.groups()[3]
        SK63_Y2=SEARCH.groups()[4]
        Proj3=SEARCH.groups()[5]
        #Proj1=SEARCH.groups()[5]
        #print('Nomenklatura2:', Nomenklatura2, '.')
        #print('SK63_X:', SK63_X, '.')
        #print('SK63_Y:', SK63_Y, '.')
        #print('SK63_X2:', SK63_X2, '.')
        #print('SK63_Y2:', SK63_Y2, '.')
        #print('Proj3:', Proj3, '.')
    else:
        Nomenklatura2 = 'Формат??'
        SK63_X = 'Формат??'
        SK63_Y = 'Формат??'
        SK63_X2 = 'Формат??'
        SK63_Y2 = 'Формат??'
        Proj3 = 'Формат??'
    #-----------------------
    SEARCH = re.search('\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(Hg=\s*-{0,1}\d*\.\d*)?\s*(EGM=\s*-{0,1}\d*\.\d*)?\s*(\w{2}-\S*)\s*', line_SK95)
    if SEARCH != None :
        SK95_X=SEARCH.groups()[0]
        SK95_Y=SEARCH.groups()[1]
        Hg=SEARCH.groups()[2]
        EGM=SEARCH.groups()[3]
        Proj4=SEARCH.groups()[4]
        #print('SK95_X:', SK95_X, '.')
        #print('SK95_Y:', SK95_Y, '.')
        #print('Hg:', Hg, '.')
        #print('EGM:', EGM, '.')
        #print('Proj4:', Proj4, '.')
    else:
        SK95_X = 'Формат??'
        SK95_Y = 'Формат??'
        Hg = 'Формат??'
        EGM = 'Формат??'
        Proj4 = 'Формат??'
    # -----------------------
    SEARCH = re.search('\s*(\d{2}°\d{2}\'\d{2}\.\d*\")\s*(\d{2}°\d{2}\'\d{2}\.\d*\")\s*(\w{2}-\S*)\s*',line_BL95)
    if SEARCH != None:
        SK95_B = SEARCH.groups()[0]
        SK95_L = SEARCH.groups()[1]
        Proj5 = SEARCH.groups()[2]
        #print('SK95_B:', SK95_B, '.')
        #print('SK95_L:', SK95_L, '.')
        #print('Proj5:', Proj5, '.')
    else:
        SK95_B = 'Формат??'
        SK95_L = 'Формат??'
        Proj5 = 'Формат??'
    #-----------------------
    SEARCH = re.search('\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(\w{2}-\S*)\s*', line_PZ90)
    if SEARCH != None :
        PZ90_X=SEARCH.groups()[0]
        PZ90_Y=SEARCH.groups()[1]
        PZ90_Z=SEARCH.groups()[2]
        Proj6=SEARCH.groups()[3]
        #print('PZ90_X:', PZ90_X, '.')
        #print('PZ90_Y:', PZ90_Y, '.')
        #print('PZ90_Z:', PZ90_Z, '.')
        #print('Proj6:', Proj6, '.')
    else:
        PZ90_X = 'Формат??'
        PZ90_Y = 'Формат??'
        PZ90_Z = 'Формат??'
        Proj6 = 'Формат??'
    #-----------------------
    SEARCH = re.search('\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(\w{2}-\S*)\s*', line_PZ9002)
    if SEARCH != None :
        PZ9002_X=SEARCH.groups()[0]
        PZ9002_Y=SEARCH.groups()[1]
        PZ9002_Z=SEARCH.groups()[2]
        Proj7=SEARCH.groups()[3]
        #print('PZ90.02_X:', PZ9002_X, '.')
        #print('PZ90.02_Y:', PZ9002_Y, '.')
        #print('PZ90.02_Z:', PZ9002_Z, '.')
        #print('Proj7:', Proj7, '.')
    else:
        PZ9002_X = 'Формат??'
        PZ9002_Y = 'Формат??'
        PZ9002_Z = 'Формат??'
        Proj7 = 'Формат??'
    #-----------------------
    SEARCH = re.search('\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(\d*\.\d*)\s*(\w{3}-\S*)\s*', line_WGS84)
    if SEARCH != None :
        WGS84_X=SEARCH.groups()[0]
        WGS84_Y=SEARCH.groups()[1]
        WGS84_Z=SEARCH.groups()[2]
        Proj8=SEARCH.groups()[3]
        #print('WGS84_X:', WGS84_X, '.')
        #print('WGS84_Y:', WGS84_Y, '.')
        #print('WGS84_Z:', WGS84_Z, '.')
        #print('Proj8:', Proj8, '.')
    else:
        WGS84_X = 'Формат??'
        WGS84_Y = 'Формат??'
        WGS84_Z = 'Формат??'
        Proj8 = 'Формат??'
    #-----------------------
    SEARCH = re.search('\s*(\d{2}°\d{2}\'\d{2}\.\d*\")\s*(\d{2}°\d{2}\'\d{2}\.\d*\")\s*(Hw=\s*-{0,1}\d*\.\d*)?\s*(Gwg=\s*-{0,1}\d*\.\d*)?\s*(\w{2}-\S*)\s*', line_BLWGS84)
    if SEARCH != None :
        WGS84_B=SEARCH.groups()[0]
        WGS84_L=SEARCH.groups()[1]
        Hw=SEARCH.groups()[2]
        Gwg=SEARCH.groups()[3]
        Proj9=SEARCH.groups()[4]
        #print('WGS84_B:', WGS84_B, '.')
        #print('WGS84_L:', WGS84_L, '.')
        #print('Hw:', Hw, '.')
        #print('Gwg:', Gwg, '.')
        #print('Proj9:', Proj9, '.')
    else:
        WGS84_B = 'Формат??'
        WGS84_L = 'Формат??'
        Hw = 'Формат??'
        Gwg = 'Формат??'
        Proj9 = 'Формат??'




    out_test_file = os.path.join(out_folder, 'ggs'+str(NumberOfGGSs)+'.txt')
    with open(out_test_file, 'w') as out_f:
        for line in GGSBlock:
            out_f.write(line)
        #print(GGSBlock)
    
    return [
    Distant,Comment1,Name_Type,Center_Marka,
    Proj1,Nomenklatura1,SK42_X,SK42_Y,Hn,G98,
    Proj2,SK42_B,SK42_L,G87,
    Proj3,Nomenklatura2,SK63_X,SK63_Y,SK63_X2,SK63_Y2,
    Proj4,SK95_X,SK95_Y,Hg,EGM,
    Proj5,SK95_L,SK95_B,
    Proj6,PZ90_X,PZ90_Y,PZ90_Z,
    Proj7,PZ9002_X,PZ9002_Y,PZ9002_Z,
    Proj8,WGS84_X,WGS84_Y,WGS84_Z,
    Proj9,WGS84_B,WGS84_L,Hw,Gwg
    ]
    
    
def parse_ggs_file(in_file,out_folder):
    StageParce=0
    StartLine=0
    NumberOfGGSs=0
    columns=[
    'Distant','Comment1','Name_Type','Center_Marka',
    'Proj1','Nomenklatura1','SK42_X','SK42_Y','Hn','G98',
    'Proj2','SK42_B','SK42_L','G87',
    'Proj3','Nomenklatura2','SK63_X','SK63_Y','SK63_X2','SK63_Y2',
    'Proj4','SK95_X','SK95_Y','Hg','EGM',
    'Proj5','SK95_L','SK95_B',
    'Proj6','PZ90_X','PZ90_Y','PZ90_Z',
    'Proj7','PZ9002_X','PZ9002_Y','PZ9002_Z',
    'Proj8','WGS84_X','WGS84_Y','WGS84_Z',
    'Proj9','WGS84_B','WGS84_L','Hw','Gwg'
    ]
    out_GGS_file=os.path.splitext(in_file)[0]+'_reformat.csv'
    try:
        with open(out_GGS_file, 'w', encoding='cp1251') as out_f: out_f.write(';'.join(columns)+'\n')
    except:
        print('закрой файл')
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
        #print(in_f)
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
                parce_one_GGS=parce_gg_block_keys(GGSBlock,out_folder,NumberOfGGSs) #обработка блока пункта
                parce_one_GGS_str=[str(x) for x in parce_one_GGS]
                print(';'.join(parce_one_GGS_str))
                with open(out_GGS_file, 'a', encoding='cp1251') as out_f: out_f.write(';'.join(parce_one_GGS_str)+'\n')
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
                #print('start section',StartLine,StageParce)
            elif '=' * 78 in line and StartLine==1:
                StartLine = 2
                StageParce = 4
                #print('break')
                break
            if StageParce == 1:
                #ToDO добавить поиск точки начала
                StageParce = 2
        if StartLine == 2 and StageParce == 4:
            #print('start section', StartLine, StageParce)
            print('Найдено пунктов',NumberOfGGSs)
            #ToDO проверять количество пунктов по файлу
            print('Конец файла')
        else:
            print('error format of file')




if __name__=='__main__':
    in_file=u'c:\\Users\\Андрей\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\GGS_text_parsing\\testdata\\Sample.txt'
    out_folder=u'c:\\Users\\Андрей\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\GGS_text_parsing\\testdata\\output'
    parse_ggs_file(in_file,out_folder)