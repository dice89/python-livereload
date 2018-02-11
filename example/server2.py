from livereload import Server, shell
from livereload.watcher import Watcher


server = Server(watcher=Watcher(provide_filename=True))
def printfilename(filename):
    print(filename)
server.watch('style.less', printfilename)
server.serve(open_url_delay=1)
