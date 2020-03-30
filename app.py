from flask import Flask, request
app = Flask(__name__)
import docker
client = docker.from_env()


@app.route('/check', methods = ['POST'])
def check():
    data = request.get_json()
    f = open("codes/demo.c", "w")
    f.write(data['code'])
    f.close()
    temp=b''
    while(temp.decode('utf-8')==''):
        temp =  client.containers.run("comp:latest", "../run.sh", volumes={'/home/naoh/codeeval/codes/':{'bind':'/usr/src/','mode':'rw'}},detach=False, stdout=True)
    return temp

if __name__ == '__main__':
   app.run(debug=True)