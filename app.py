from flask import Flask, request
app = Flask(__name__)
import docker
import os

client = docker.from_env()


@app.route('/check', methods = ['POST'])
def check():
    data = request.get_json()
    username = "demo" # comes from request
    f = open("codes/"+username+".c", "w")
    f.write(data['code'])
    f.close()
    temp=b''
    while(temp.decode('utf-8')==''):
        temp =  client.containers.run("comp:latest", "./run.sh", volumes={'/home/naoh/codeeval/codes/':{'bind':'/usr/src/','mode':'rw'}, '/home/naoh/codeeval/testcases/':{'bind':'/usr/testcases/','mode':'rw'}},detach=False, stdout=True)
    os.remove("codes/"+username+'.c')    
    return temp

if __name__ == '__main__':
   app.run(debug=True)