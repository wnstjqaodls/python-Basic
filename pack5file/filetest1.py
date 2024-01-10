# file io
import os
import sys
print(os.getcwd())      #경로 나옴

try:
    print('파일 읽기 ---')
    #f1 = open(r'C:\work\psou\pypro1\pack5file\ftest.txt',mode = 'r', encoding = 'utf-8')
    #f1 = open(os.getcwd() +'r\ftest.txt',mode = 'r', encoding='utf-8')
    f1 = open('ftest', mode ='r', encoding='utf-8')
    print(f1)
    f1.close()
    
except Exception as e:
    print('파일 처리 오류: ', e)
    sys.exit(0)
    

try:
    print('파일저장 --')
    f2 = open('ftest2', mode = 'w', encoding = 'utf-8')
    f2.write('My friends\n')
    f2.write('홍길동, 신기해')
    f2.close()
    print('저장 성공')
    
    f2_1 = open('ftest2', mode='a', encoding= 'utf-8') # 파일의 내용추가
    f2_1.write('\n오공')
    f2_1.write('\n팔계')
    f2_1.write('\n아리')
    f2_1.close()
    
    f3 = open('ftest2', mode ='r', encoding='utf-8')
    print(f3.read())
    f3.close()

    print('한 줄씩 읽기')
    f4 = open('ftest2', mode='a', encoding= 'utf-8') # 파일의 내용추가
    print(f4.readline())
    print(f4.readline())
    print(f4.readline())
    f4.close()
    
except Exception as e:
    print('파일 오류 :', e)
    
    
    