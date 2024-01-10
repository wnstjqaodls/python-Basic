import MySQLdb

"""config = {
        'host':'127.0.0.1',

    'user':'root',

    'password':'123',

    'database':'test',

    'port':3307,
    'charset':'utf8',

    'use_unicode':True
}"""

import pickle
with open('mydb.dat','rb')as obj:
    config = pickle.load(obj)
    

def serchFunc():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jikwon_no = input('직원번호 입력 :')
        jikwon_name = input('직원 이름입력 :')
        
        sql="""
            select jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_jik,jikwon_gen
            from jikwon inner join buser on jikwon.buser_num = buser.buser_no
            where jikwon_no={0} and jikwon_name= "{1}"        #여기서  "{1}" 쌍따옴표 해야함. 주의! string 이기때문
            """.format(jikwon_no,jikwon_name)
        cursor.execute(sql)
        datas = cursor.fetchall()
        
        if len(datas) == 0:
            print('해당 직원은 없어요')
            return 
            
        for jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_jik,jikwon_gen in datas:
            print('해당 직원이 존재합니다')
            print(jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_jik,jikwon_gen)   
            
    except Exception as e:
        print('err :',e)
        
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    serchFunc()        