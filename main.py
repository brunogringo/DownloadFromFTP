import ftplib

FTP_HOST = 'ftp_host'
FTP_PORT = 22
FTP_USERNAME = 'username'
FTP_PASSWORD = 'password'


def import_from_ftp():
    try:
        with ftplib.FTP(FTP_HOST) as ftp:
            try:
                print('Trying to connect in FTP')
                ftp.login(FTP_USERNAME, FTP_PASSWORD)
                print('Welcome', ftp.getwelcome())
                # for change folder inside the FTP use the next command
                # ftp.cwd('LTM')
                files = []
                ftp.retrlines('NLST', callback=files.append)
                print(files)
                for file in files:
                        if ftp.size(file) > 0:
                            print('Download the file: ' + file)
                            ftp.retrbinary('RETR ' + file, open(file, 'wb').write)
                            print('Download complete')
            except ftplib.all_errors as e:
                print('FTP error:', e)
            ftp.quit()
            print('Connection closed')
    except Exception as e:
        print('An error has occurred, at the FTP connection: ', e)


import_from_ftp()
