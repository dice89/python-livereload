from livereload import Server, shell
from livereload.watcher import Watcher


server = Server(watcher=Watcher(provide_filename=True))
def printfilename(filename):
    print(filename)
server.watch('*.less', printfilename)
server.serve(open_url_delay=1)
