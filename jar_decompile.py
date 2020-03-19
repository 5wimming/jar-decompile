#python3
#aotoman
#20200318
import os
import zipfile


#参数：1、工程目录；2、编译插件路径
def decompile(filepath,toolpath):
    for root,dirs,files in os.walk(filepath):
        print('[+] '+root)
        for filename in files:
            if '.jar' in filename and '.md5' not in filename:
                if not os.path.exists(root+'_src'):#自动在jar包同级目录下创建以_src结尾的文件夹，用以存放反编译后的jar包和解压包
                    os.makedirs(root+'_src')
                try:
                    os.system('java -jar {0} {1} {2}'.format(toolpath,root+'/'+filename,root+'_src'))
                    with zipfile.ZipFile(root+'_src'+'/'+filename, 'r') as zzz:
                        zzz.extractall(root+'_src'+'/'+filename[:-4])
                except:
                    print('error:'+root+'/'+filename)


if __name__ == '__main__':
    filepath='D:/penetration/202003/JAD/' #1、需要编译的工程目录
    toolpath='D:/penetration/tools/fernflower.jar' #2、编译软件路径
    decompile(filepath,toolpath)