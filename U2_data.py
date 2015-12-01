from __future__ import unicode_literals
_author_ = 'sbindal'


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def is_valid_url(url):
    """
    Determines whether current url belongs to a valid youtube video
    :param url: String
    :return: bool
    """
    pass


def download_video(url):
    """
    Download youtube urls as .avi video
    :param url: String
    :return: None
    """
    import youtube_dl
    print url
    url = 'https://www.youtube.com/v/BaW_jenozKc'
    ydl_opts = {
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    pass


def csv_parser(filename):
    with open(filename) as f:
        # data = f.readline()
        data = unicode(f.readline(), 'utf-8')
        print data, type(data)
        url = ''
        is_valid_url(url)
        download_video(url)
        while data:
            row = data.split(',')
            data = unicode(f.readline(), 'utf-8')

if __name__ == '__main__':
    csv_parser('data\MSR Video Description Corpus.csv')
