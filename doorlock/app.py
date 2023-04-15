import random
from flask import Flask,render_template,redirect,url_for,redirect, render_template, request
app = Flask(__name__)

#메인 페이지
@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'POST':
        random_list = list(range(1,11))
        randoms = random.sample(random_list, 10)
        return render_template('doorlock_one.html', numbers = randoms)
    return render_template('main.html')

#패스워드 맞을 때
@app.route('/one',methods=['GET','POST'])
def one():
    password = '1' #첫번째 패스워드 설정
    number = request.args["number"]
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    if password == number:
        return render_template('doorlock_two.html', numbers = randoms)
    else:
        return render_template('wrong_two.html', numbers = randoms)

@app.route('/two',methods=['GET','POST'])
def two():
    password = '2' #두번째 패스워드 설정
    number = request.args["number"]
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    if password == number:
        return render_template('doorlock_three.html', numbers = randoms)
    else:
        return render_template('wrong_three.html', numbers = randoms)

@app.route('/three',methods=['GET','POST'])
def three():
    password = '3' #세번쨰 패스워드 설정
    number = request.args["number"]
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    if password == number:
        return render_template('doorlock_four.html', numbers = randoms)
    else:
        return render_template('wrong_four.html', numbers = randoms)

@app.route('/four',methods=['GET','POST'])
def four():
    password = '4' #세번째 패스워드 설정
    number = request.args["number"]
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    if password == number:
        return render_template('correct.html')
    else:
        return render_template('wrong.html') #마지막에 틀리면 wrong view 리턴


#패스워드 틀렸을 때 -> wrong 경로로

@app.route('/wrong_two',methods=['GET','POST'])
def wrongTwo():
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    return render_template('wrong_three.html', numbers = randoms)

@app.route('/wrong_three',methods=['GET','POST'])
def wrongThree():
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    return render_template('wrong_four.html', numbers = randoms)

@app.route('/wrong_four',methods=['GET','POST'])
def wrongFour():
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    return render_template('wrong.html', numbers = randoms)


@app.route('/tmp', methods=['GET','POST'])
def tmp():
    random_list = list(range(1,11))
    randoms = random.sample(random_list, 10)
    return render_template('tmp.html', value = randoms, number = randoms)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port = 80, debug = True)
