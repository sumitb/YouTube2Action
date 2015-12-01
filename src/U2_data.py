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

def image_extractor():
    import os, sys, subprocess
    
    imageformat = 'image2' # image2 sequence
    framepersec = '2'
    inputVideoDir = os.path.abspath(os.path.join('data', 'YouTubeClips'))
    outputBaseDir = os.path.abspath(os.path.join('data', 'YouTubeImgs'))

    for dirName, subdirList, videoFiles in os.walk(inputVideoDir):
        for vidFile in videoFiles:
            inputVideoFile = os.path.join(inputVideoDir, vidFile)
            outputImageDir = outputBaseDir + os.sep + vidFile[:len(vidFile)-4]
            # Create output image folder for every video
            if not os.path.exists(outputImageDir):
                os.makedirs(outputImageDir)
            outputImageFile = outputImageDir + os.sep + 'Picture%d.jpg'
            subprocess.Popen(['ffmpeg', '-i', inputVideoFile, '-r', framepersec, '-f', imageformat, outputImageFile])
    pass

if __name__ == '__main__':
    image_extractor()
    # csv_parser('data\MSR Video Description Corpus.csv')
