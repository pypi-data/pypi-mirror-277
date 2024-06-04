"""
This snippets helps to use yt_dlp in script i.e., in embedding yt-dlp
"""

__all__ = ['Ytube']
__author__ = "Prince Kumar"
__version__ = "0.1.0-alpha"

import argparse
import re
import time
import urllib.request
from functools import partial
from json import loads as json_loads, dumps as json_dumps
from os import (
    mkdir,
    getcwd,
    chdir,
    rename,
    remove as os_remove
)
from os.path import (
    abspath,
    isdir,
    isfile,
    exists,
    dirname,
    basename,
    join as os_join,
    getsize
)
from random import randint
from shutil import rmtree as shutil_rmtree
from subprocess import run as srun

from yt_dlp import YoutubeDL

from .utils import make_filename_safe, hbs


class FileManager:
    @staticmethod
    def remove(file_or_directory):
        """To remove a file or directory"""
        if isfile(file_or_directory):
            os_remove(file_or_directory)
        elif isdir(file_or_directory):
            shutil_rmtree(file_or_directory)

    @staticmethod
    def rename(file, new_name):
        new_name = make_filename_safe(new_name)
        if dirname(file) == dirname(new_name):
            if file != new_name:
                rename(file, new_name)
        else:
            new_name = os_join(dirname(file), basename(new_name))
            if file != new_name:
                rename(file, new_name)

    @staticmethod
    def mkdir(dir_):
        """make directory and return created directory"""
        dir_ = make_filename_safe(dir_)
        if not isdir(dir_):
            mkdir(dir_)
            return dir_
        else:
            dir_ += str(time.time())
            mkdir(dir_)
            return dir_


class Progress:
    def __init__(self, pdict: dict):
        for k, v in pdict.items():
            setattr(self, k, v)


def my_hook(youtube, data: dict):
    if data['status'] == 'finished':
        youtube.stream_files['_file'] = data.get('info_dict').get('_filename')
    youtube.pdict['speed_str'] = data.get('_speed_str')
    youtube.pdict['total_size'] = data.get('_total_bytes_str')
    youtube.pdict['elapsed_str'] = data.get('_elapsed_str')
    youtube.pdict['percent_str'] = data.get('_percent_str')
    youtube.pdict['downloaded'] = hbs(data.get('downloaded_bytes'))
    youtube.progress = Progress(youtube.pdict)

class YtStream:
    def __init__(self, stream_info: dict, url: str):
        self.url = url
        self.format_id = stream_info.get('format_id')
        self.format_ = stream_info.get('format')
        self.format_note = stream_info.get('format_note')
        self.container = stream_info.get('container')
        self.abr = stream_info.get('abr')
        self.vbr = stream_info.get('vbr')
        self.tbr = stream_info.get('tbr')
        self.filesize = stream_info.get('filesize')
        self.filesize_readable = hbs(stream_info.get('filesize'))
        self.acodec = stream_info.get('acodec')
        self.vcodec = stream_info.get('vcodec')
        self.fps = stream_info.get('fps')
        self.resolution = stream_info.get('resolution')
        self.is_dash = 'dash' in stream_info.get('container')

    def __repr__(self):
        return f'[{self.format_}__{self.container}__{self.filesize_readable}]'

    @property
    def is_video_only(self):
        if self.is_dash:
            if (self.acodec == 'none' and self.vcodec != 'none') or \
               (self.vbr and not self.abr):
                return True
        return False

    @property
    def is_audio_only(self):
        if self.is_dash:
            if (self.vcodec == 'none' and self.acodec != 'none') or \
               (self.abr and not self.vbr):
                return True
        return False

class Subtitle:
    def __init__(self, name: str, subtitle_sources: list):
        self.name = name
        self.language = subtitle_sources[-1].get('name')
        self.url = subtitle_sources[-1].get('url')
        self.ext = subtitle_sources[-1].get('ext')

    def __repr__(self):
        return f'<--{self.name}:{self.language}_{self.ext}-->'


class Subtitles:
    def __init__(self, subs: dict):
        self.subtitles = [Subtitle(k, v) for k, v in subs.items()]


class YtInfo:
    def __init__(self, info: dict):
        self.id = info.get('id')
        self.title = info.get('title')
        self.thumbnail = info.get('thumbnail')
        self.duration = info.get('duration')
        self.view_count = info.get('view_count')
        self.webpage_url = info.get('webpage_url')
        self.duration_string = info.get('duration_string')
        self.formats_raw = info.get('formats')
        self.formats = None
        self.subtitles = Subtitles(info.get('subtitles')).subtitles
        self.automatic_captions_dict=info.get('automatic_captions')
        self.subtitles_dict = info.get('subtitles')
        self.has_subtitles = bool(info.get('subtitles'))

    @property
    def formats_(self):
        formats = []
        for entry in self.formats_raw:
            if entry.get('container'):
                stream = YtStream(entry, self.webpage_url)
                if not stream.format_id.startswith('sb'):
                    formats.append(stream)
        self.formats = formats
        self.formats_raw = None
        return formats


"""      
left = [
    "channel",
    "channel_follower_count",
    "uploader",
    "uploader_id",
    "uploader_url",
    "upload_date",#yyyymmdd
    "like_count"
]
"""


class Ytube:
    def __init__(self,url):
        self.url=url 
        self.id=None 
        self.title=None 
        self.duration=None 
        self.duration_string=None 
        self.thumbnail=None 
        self.has_subtitles=None 
        self.subtitles=None
        self.ytinfo=None
        self.pdict={}
        self.formats=None 
        self.audios=[]
        self.videos=[]
        self.progressive=[]
        self.stream_files={}
        self._my_hook=partial(my_hook,self)
        self.aud=[22,32,48,64,96,128,160,192,224,256,320]
        self._suitable_aud_res={
            '144p':32,
            '240p':[22,32,48],
            '360p':[32,48,64],
            '480p':[48,64,96],
            '720p':[64,96,128],
            '1080p':[96,128,160],
            '1440p':[128,160,192],
            '2160p':[160,192,224]
        }
        self._do_formats()

    def _extract_info(self):
        info=YoutubeDL().extract_info(self.url,download=False)
        self.ytinfo=YtInfo(info)

    def _do_formats(self):
        self._extract_info()
        self.formats=self.ytinfo.formats if self.ytinfo.formats else self.ytinfo.formats_
        for i in self.formats:
            if i.is_audio_only:
                self.audios.append(i)
            elif i.is_video_only:
                self.videos.append(i)
            else:
                self.progressive.append(i)
        self.id=self.ytinfo.id 
        self.title=self.ytinfo.title 
        self.duration=self.ytinfo.duration 
        self.duration_string=self.ytinfo.duration_string 
        self.thumbnail=self.ytinfo.thumbnail
        self.has_subtitles=self.ytinfo.has_subtitles 
        self.subtitles=self.ytinfo.subtitles

    def _find_a_qual(self, bit_rate):
        bit_rate = round(bit_rate)
        predefined_rates = [22, 32, 48, 64, 96, 128, 160, 192, 224, 256]
        rate_map = {}
        differences = []
        for rate in predefined_rates:
            difference = abs(bit_rate - rate)
            differences.append(difference)
            rate_map[difference] = rate
        return rate_map.get(min(differences))

    def _find_audio_by_bt_rate(self, bt_rate):
        return [audio for audio in self.audios if self._find_a_qual(audio.abr) == bt_rate]

    @property
    def best_audio(self):
        bit_rates = [audio.abr for audio in self.audios]
        bit_rate_to_audio = {audio.abr: audio for audio in self.audios}
        highest_bit_rate = max(bit_rates)
        return bit_rate_to_audio[highest_bit_rate]

    @property
    def worst_audio(self):
        bit_rates = [audio.abr for audio in self.audios]
        bit_rate_to_audio = {audio.abr: audio for audio in self.audios}
        lowest_bit_rate = min(bit_rates)
        return bit_rate_to_audio[lowest_bit_rate]

    def _find_video_by_resolution(self, resolution: str):
        all_videos = self.videos + self.progressive
        matching_videos = [
            video for video in all_videos 
            if resolution in video.format_note or resolution in video.format_
        ]
        if not matching_videos:
            raise Exception('No requested resolution found')
        return matching_videos

    def _download_stream(self,streams: list,output_folder=None):
        format_to_download = ''.join(f'{stream.format_id}+' for stream in streams).rstrip('+')
        opts = {
            'quiet':True,
            'overwrites':False, 
            'noplaylist':True,
            'format':format_to_download,
            'outtmpl':f'%(title)s_%(id)s.%(ext)s',
            'writesubtitles':True,
            'writeautomaticsub':True,
            'restrictfilenames': True,
            'subtitleslangs':['en','en-US','en-IN','en-UK'],
            'allow_multiple_audio_streams':True,
            'ignoreerrors':True,
            'progress_hooks':[self._my_hook],
            'postprocessors':[{'key':'FFmpegEmbedSubtitle'}]
        }
        if len(streams) == 1:
            if streams[0].is_audio_only:
                del opts["writeautomaticsub"]
                del opts["writesubtitles"]
                del opts["postprocessors"]
        if output_folder:
            if output_folder.endswith('/'):
                output_folder=output_folder[:-1]
                opts['outtmpl']=f'{output_folder}/%(title)s_[%(id)s].%(ext)s'
        with YoutubeDL(opts) as ydl:
            ydl.download(self.url)
        return self.stream_files.get('_file')

    def _find_suitable_aud(self,video_stream):
        if len(self.audios)!=0:
            if (video_stream.is_video_only and video_stream.is_dash):
                if video_stream.format_note=='144p':
                    return self.worst_audio
                suit_a=self._suitable_aud_res.get(video_stream.format_note)
                a2=self._find_audio_by_bt_rate(suit_a[0])
                if len(a2)!=0:
                    return a2[0]
                else:
                    a2=self._find_audio_by_bt_rate(suit_a[1])
                    if len(a2)!=0:
                        return a2[0]
                    else:
                        a2=self._find_audio_by_bt_rate(suit_a[2])
                        if len(a2)!=0:
                            return a2[0]
                        else:
                            return self.audios[0]

    @property 
    def download_thumbnail(self):
        thumbnail_file=f"thumbnail[{self.id}].jpg"
        if isfile(thumbnail_file):
            return thumbnail_file
        else:
            urllib.request.urlretrieve(self.thumbnail,thumbnail_file)
            return thumbnail_file

    def download_by_resolution(self,res: str,out_fol=None):
        """To download video and audio files together in one file by resolution e.g., 480p """
        print(f'Trying to download --> {self.title}, Requested resolution: {res}')
        try:
            vid=self._find_video_by_resolution(res)[0]
            if vid.is_dash:
                aud=self._find_suitable_aud(vid)
                return self._download_stream([vid,aud],output_folder=out_fol)
            else:
                return self._download_stream([vid],output_folder=out_fol)
        except Exception as e:
            print(e)
            return None

    def download_audio_by_bt_rate(self,bt_rate: str,out_fol=None):
        return self._download_stream([self._find_audio_by_bt_rate(bt_rate)],output_folder=out_fol)



class YtlistVid:
    def __init__(self,info:dict):
        self.id=info.get('id')
        self.url=info.get('url')
        self.title=make_filename_safe(info.get('title'))
        self.duration=info.get('duration')
        self.channel=info.get('channel')
        self.channel_id=info.get('channel_id')
        self.channel_url=info.get('channel_url') 
        self.playlist_url=info.get('playlist_url')
        self.playlist_title=info.get('playlist_title')

    def __repr__(self):
        return f'<-YtlistVid:{title[45:]}__{self.channel}->'


class Ytlist:
    def __init__(self,playlist_url):
        if ('watch?v' in playlist_url) and ('&list=' in playlist_url):
            self.url=f'https://youtube.com/playlist?list={playlist_url.split("&list=")[-1]}' 
        else:
            self.url=playlist_url
        self.entries=[]
        self.urls_of_all_videos=[]
        self.playlist_count=None
        self.id=None 
        self.title=None
        self.webpage_url=None 
        self.uploader=None 
        self.uploader_url=None 
        self.uploader_id=None
        self.channel=None 
        self.channel_url=None 
        self.channel_id=None
        self.pk_opts = {
            'skip_download':True,
            'extract_flat':True
        }

    def extract_info(self):
        with YoutubeDL(self.pk_opts) as ydl:
            e=ydl.extract_info(self.url, download=False)
        self.id=e.get('id')
        self.title=make_filename_safe(e.get('title'))
        self.webpage_url=e.get('webpage_url') 
        self.playlist_count=e.get('playlist_count') 
        self.uploader=e.get('uploader')
        self.uploader_url=e.get('uploader_url')
        self.uploader_id=e.get('uploader_id')
        self.channel=e.get('channel')
        self.channel_url=e.get('channel_url')
        self.channel_id=e.get('channel_id')
        for i in e.get('entries'):
            i['playlist_url']=self.url 
            i['playlist_title']=self.title
            self.entries.append(YtlistVid(i))
        for i in e.get('entries'):
            self.urls_of_all_videos.append(i.get('url'))

    def download_all_videos_by_resolution(self,res,out_fol=None,alt=None):
        """download all videos by resolution returns a dict containing files_list, dirrctory, no of successful and failed downloads 
        pass alt='some resolution' to download alternate resolution for videos which does not have requested resolution 
        do this to reduce no. of failed downloads"""
        downloaded_bytes=0
        if not (self.id or self.webpage_url):
            self.extract_info()
        if not out_fol:
            out_fol=self.title
            out_fol=FileManager.makdir(out_fol)
        out_fol=abspath(out_fol)
        files=[]
        downloaded,failed=0,0
        for urls in self.urls_of_all_videos:
            file=Ytube(urls).download_by_resolution(res=res,out_fol=out_fol)
        if file:
            print('Downloaded ✓',file)
            downloaded+=1
            downloaded_bytes+=getsize(file)
            files.append(file)
        else: 
            if alt: 
                file=Ytube(urls).download_by_resolution(res=alt,out_fol=out_fol)
                if file:
                    print('Downloaded ✓',file)
                    downloaded+=1
                    downloaded_bytes+=getsize(file)
                    files.append(file)
                else: 
                    failed+=1
            else: 
                failed+=1
        print(f'Downloaded {downloaded} videos of {self.playlist_count}.\nDirectory containing files: {out_fol}\n\n')
        return {'output_folder':out_fol,'files_list':files,'downloaded':downloaded,'failed':failed,'total':self.playlist_count,'size_downloaded':hbs(downloaded_bytes)}





