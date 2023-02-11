import json,flask
import pymysql
from flask import request
from flask_sqlalchemy import SQLAlchemy

app=flask.Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:990301@Leo@localhost:3306/JOBMNGSYSDB'
#     # 协议：mysql+pymysql
#     # 用户名：root
#     # 密码：990301@Leo
#     # IP地址：localhost
#     # 端口：3306
#     # JOBMNGSYSDB #这里的数据库需要提前建好
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# db=SQLAlchemy(app)

@app.route('/')
def helloworld():
    return 'hello world'

@app.route('/testinsert', methods=['get'])
def insert():
    first_name=request.values.get('firstname')
    last_name=request.values.get('lastname')
    db=pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='990301@Leo',
                       database='JOBMNGSYSDB')
    cursor=db.cursor()
    sql="insert into `test`(user_first_name,user_last_name) values(\'%s\',\'%s\')"%(first_name,last_name)
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    cursor.close()
    db.close()
    
    return 'seccuss'
    
    


if __name__ == '__main__':
    
    app.run(debug=True,port=8000,host='127.0.0.1')    

    
    