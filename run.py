from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Функция для чтения сообщений из файла
def read_messages():
    if os.path.exists('messages.txt'):
        with open('messages.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]
    return []

# Функция для записи нового сообщения в файл
def write_message(username, message):
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"{username}: {message}\n")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/current-tech')
def current_tech():
    return render_template('current_tech.html')

@app.route('/pros-cons')
def pros_cons():
    return render_template('pros_cons.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        write_message(username, message)  # Запись сообщения в файл
        return redirect(url_for('forum'))  # Перезагрузка страницы форума

    # Чтение сообщений из файла
    messages = read_messages()
    return render_template('forum.html', messages=[{'username': msg.split(":")[0], 'message': msg.split(":")[1]} for msg in messages])

if __name__ == "__main__":
    app.run(debug=True)
