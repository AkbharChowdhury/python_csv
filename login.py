from custom_csv import CustomCSV


def is_authorised(username, password):
    data = CustomCSV.read_csv_file('login.txt')
    return list(filter(lambda i: i['username'] == username and i['password'] == password, data))


if __name__ == '__main__':
    username = input('username ')
    password = input('password ')
    login_info = is_authorised(username, password)

    if login_info:
        print('login success')
        print(login_info)
    else:
        print('login failed. please try again')
