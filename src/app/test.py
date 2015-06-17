#-*- coding: utf-8 -*-

#读取文件
def readFile(path):
    try:
        file = open(path);
        return file;
    except:
        print "读取文件出错，请检查！"
        exit();

#创建文件
def createFile(path):
    try:
        sqlFile=open(path,'w')
        return sqlFile;
    except:
        print "创建文件出错，请检查！"
        exit();

#检查字段和文件字段数量是否匹配
def check(field,line,fieldSplit,lineSplit):
    try:
        fieldLenge=len(field.split(fieldSplit))
        lineLenge=len(line.split(lineSplit))
        if fieldLenge <= lineLenge:
            return;
        else:
            print "输入字段数量和文件中的字段数量不匹配\n"+field+" 和 "+line
            exit();
    except:
        print "检查字段数量匹配异常"

#检查输入字段是否为空，模式true，为提示循环输入，模式false，直接退出程序
def raw(message):
    value="";
    while 1:
        value=raw_input(message)
        if value:
            break;
        else:
            print("输入不能为空")
    return value;

#主方法
if __name__=="__main__":
    table=raw("请输入表名：\n")
    symbol=raw("文件中的分割符：\n")
    field=raw("请输入字段列表 格式：key1,key2,key3 \n")
    #读取文件
    readPath=raw("请输入读取的文件和路径：\n")
    readFile=readFile(readPath);
    #创建文件
    createPath=raw("请输入创建的文件和路径：\n")
    sqlFile=createFile(createPath);
    while 1 :
        value="(";
        #读取一行
        line=readFile.readline().strip("\n");
        if not line:
            break
        else:
            check(field,line,",",symbol)
            temp=line.split(symbol)
            if len(temp)<=1:continue
            for str in temp:
                value=value+str+","
            value=(value[:-1])+");"
        sql="INSERT INTO "+table+" ("+field+") VALUES "+value.strip('\n') 
        sqlFile.write(sql+"\n")
        print sql;      
    
