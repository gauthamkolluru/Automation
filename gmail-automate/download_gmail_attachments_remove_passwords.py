import pdf_attachments_download as pad

import pdf_password_removal as ppr


def main():
    try:
        return pad.main() and ppr.main()
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    if main():
        print('Process Complete')
    else:
        print('Process Incomplete')
