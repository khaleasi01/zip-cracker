#!/usr/bin/python3
import zipfile

count = 1

with open('wordlist.txt','rb') as text:
    for i in text.readlines():
        password = i.strip()
        try:
            with zipfile.ZipFile('filename.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass
