import os
import argparse


class VirtualHost:
    def __init__(self):
        self.getarguments()

    def getarguments(self):
        repo_parse = argparse.ArgumentParser(description='VirtualHost Generator\'s', add_help=True)

        repo_parse.add_argument('-dr', '--documentroot', dest='documentroot', action='store',
                                help='Document Root from our project')
        repo_parse.add_argument('-sn', '--servername', dest='servername', action='store',
                                help='ServerName: domain.com)')
        repo_parse.add_argument('-sa', '--serveralias', dest='serveralias', action='store', default=None,
                                help='(Optional)Server Alias: www.domain.com foo.domain.com *.somewherelse.com')

        repo_parse.add_argument('-path', '--pathsave', dest='path', action='store', default=None,
                                help='(Optional) Path to save our generated VH (by default in the same directory in '
                                     'which our script was called)')

        repo_parse.add_argument('-port', '--portserver', dest='port', action='store', default=80,
                                help='(Optional) Path to save our generated VH (by default in the same directory in '
                                     'which our script was called)')

        args = repo_parse.parse_args()
        documentroot = args.documentroot
        servername = args.servername
        serveralias = args.serveralias
        path_dir = args.path
        port = args.port
        virtual_info = self.content_vh(documentroot, servername, serveralias, path_dir, port)
        # for key, value in virtual_info.items():
        #     print(value)
        self.create_file(path_dir,virtual_info)

    def create_file(self, path, virtual_info):
        try:
            with open(path, 'w') as f:
                web_browsers = [virtual_info]
                for key, value in virtual_info.items():
                    f.writelines("%s\n" % line for line in web_browsers)


        except Exception as e:
            return print(str(e))

    def content_vh(self, documentroot, servername, serveralias, path_dir, port):
        list_content = {}
        if port is None:
            list_content['open'] = 'Listen: 80'
        else:
            list_content['open'] = 'Listen: ' + str(port)
            list_content['virtual_host'] = '<VirtualHost *:' + str(port) + '>'
            list_content['documentroot'] = 'DocumentRoot ' + str(documentroot)
            list_content['servername'] = 'ServerName ' + str(servername)
        if serveralias is None:
            list_content['serveralias'] = 'ServerAlias ' + str(servername)
        else:
            list_content['serveralias'] = 'ServerAlias ' + str(serveralias)
        list_content['close'] = '</VirtualHost> '

        if path_dir is None:
            local_path = ''
        else:
            local_path = ''
        return list_content


VirtualHost()
