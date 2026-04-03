import pymysql
from flask import Flask,render_template
app = Flask(__name__)

def get_au():
    conn = pymysql.connect(host='localhost', user='root', password='123456',database='test01')
    cursor = conn.cursor()
    sql = "SELECT * FROM ppa WHERE id != 0"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conn.close()


    return result

@app.route('/users')
def show_users():
    users = get_au()
    return render_template('user_1.html', users=users)
    # 先简单返回文本格式，确认数据能取到
    #return '<br>'.join([str(user) for user in users])



#print(get_au())
if __name__ == '__main__':
    app.run(debug=True)


"""安装 pymysql（pip install pymysql）http://127.0.0.1:5000/users
# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

安装 pymysql（pip install pymysql）
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
"""