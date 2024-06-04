# my_pkg/Hello.py
import os
import getpass

def main():
    # 获取当前用户的用户名
    username = getpass.getuser()

    # 构建文件内容
    file_content = f"Hello, {username}!"

    # 构建文件路径
    download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(download_dir, f"{username}.txt")

    # 写入文件
    with open(file_path, 'w') as file:
        file.write(file_content)

    print(f"File created at: {file_path}")

if __name__ == "__main__":
    main()
