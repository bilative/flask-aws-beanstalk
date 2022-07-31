from flask import Flask

application = Flask(__name__)

@application.route('/',methods=['GET','POST'])
def index():
    return "Example app"



if __name__=="__main__":
    application.run()



