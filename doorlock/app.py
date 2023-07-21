import random
from datetime import datetime
from flask import Flask, render_template, render_template, request
import vonage
app = Flask(__name__)

log_list = []
password = "1234"

client = vonage.Client(key="f5208b3e", secret="Z8Lwf9rOOWjuHKyx")
sms = vonage.Sms(client)

#메인화면, 첫 번째 패스워드 입력창
@app.route('/',methods=['GET','POST'])
def main():
    #number: 사용자가 입력한 패스워드
    #첫 화면일 때는(입력받지 않았을 때) default value 10으로 세팅
    number = request.args.get('number', default = '10', type = str)

    #랜덤 순서 만들기
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)

    #사용자가 입력한 경우
    if number != '10':
        #입력받은 값, 시간은 로그에 추가
        now = datetime.now()
        input_time = now.strftime("%Y-%m-%d %H:%M:%S")
        log_list.append([number, input_time])

        if password[0] == number:
            return render_template('doorlock_two.html', numbers = randoms)
        else:
            return render_template('wrong_two.html', numbers = randoms)
    return render_template('one.html', numbers = randoms)


#패스워드 맞을 때
@app.route('/two',methods=['GET','POST'])
def two():
    number = request.args["number"]

    now = datetime.now()
    input_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list.append([number, input_time])

    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)


    if password[1] == number:
        return render_template('doorlock_three.html', numbers = randoms)
    else:
        return render_template('wrong_three.html', numbers = randoms)

@app.route('/three',methods=['GET','POST'])
def three():
    number = request.args["number"]

    now = datetime.now()
    input_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list.append([number, input_time])

    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)

    if password[2] == number:
        return render_template('doorlock_four.html', numbers = randoms)
    else:
        return render_template('wrong_four.html', numbers = randoms)

@app.route('/four',methods=['GET','POST'])
def four():
    global password #전역변수 값 변경하기 위해
    number = request.args["number"]

    now = datetime.now()
    input_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list.append([number, input_time])


    if password[3] == number:
        random_list = list(range(0,10))
        password = ''.join(str(s) for s in random.sample(random_list, 4))
        print(password)
        responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "821075761460",
            "text": "Doorlock has been unlocked. New password: " + password,
        }
        )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        return render_template('correct.html')
    else:
        return render_template('wrong.html') #마지막에 틀리면 wrong view 리턴


#패스워드 틀렸을 때 -> wrong 경로로
@app.route('/wrong_two',methods=['GET','POST'])
def wrongTwo():
    number = request.args["number"]

    now = datetime.now()
    input_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list.append([number, input_time])
    
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)
    return render_template('wrong_three.html', numbers = randoms)

@app.route('/wrong_three',methods=['GET','POST'])
def wrongThree():
    number = request.args["number"]

    now = datetime.now()
    input_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list.append([number, input_time])
    
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)
    return render_template('wrong_four.html', numbers = randoms)

@app.route('/wrong_four',methods=['GET','POST'])
def wrongFour():
    number = request.args["number"]   

    now = datetime.now()
    input_time = now.strftime("%Y-%m-%d %H:%M:%S")
    log_list.append([number, input_time])
    
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)

    responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "821075761460",
        "text": "Doorlock password input detected.",
    }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    
    return render_template('wrong.html')

#wrong.html에서 다시 시작하기 버튼 눌렀을 때
@app.route('/again', methods=['GET', 'POST'])
def tmp():
    #랜덤 순서 만들기
    random_list = list(range(0,10))
    random_list.append('*')
    random_list.append('#')
    randoms = random.sample(random_list, 12)
    return render_template('one.html', numbers = randoms)

#사용자가 입력한 패스워드 전부 확인 가능한 log페이지
@app.route('/log',methods=['GET','POST'])
def log():
    return render_template('log.html', log_list = log_list)

@app.route('/init',methods=['POST'])
def init():
    password = '1234'
    return render_template('wrong.html')

if __name__ == '__main__':
   app.run(port = 5000, debug = True)
