# Music Clients

This section explains how to use all music clients supported by musicdl, covering two main scenarios: direct use from the terminal and integration within Python code.

## Platforms in Greater China

#### BilibiliMusicClient

[Bilibili Music](https://www.bilibili.com/audio/home/?type=9) is Bilibili’s dedicated audio platform, where users can discover, stream, and enjoy a wide variety of music, podcasts, and original audio content.

We can use BilibiliMusicClient to download music from the above music platform.

BilibiliMusicClient requires no additional CLI tools such as ffmpeg or N_m3u8DL-RE. Just install musicdl via pip and it is ready to use out of the box.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m BilibiliMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m BilibiliMusicClient -i "{'BilibiliMusicClient': {'default_search_cookies': 'YOUR_COOKIES', 'default_download_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['BilibiliMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'BilibiliMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
        'default_download_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['BilibiliMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

#### FiveSingMusicClient

[5SING Music](https://5sing.kugou.com/index.html) is a KuGou-affiliated online music platform where users can upload and discover original songs, covers, instrumentals, playlists, videos, and independent musicians.

FiveSingMusicClient can be used to download music from the music platform mentioned above.

Using FiveSingMusicClient does not require installing any extra command-line tools like ffmpeg or N_m3u8DL-RE. Simply run pip install musicdl and you can start using it right away.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m FiveSingMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m FiveSingMusicClient -i "{'FiveSingMusicClient': {'default_search_cookies': 'YOUR_COOKIES', 'default_download_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://5sing.kugou.com/yeluoluo/dj/631b3fa72418b11003089b8d.html" -m FiveSingMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:
  
  `musicdl -p "https://5sing.kugou.com/yeluoluo/dj/631b3fa72418b11003089b8d.html" -m FiveSingMusicClient -i "{'FiveSingMusicClient': {'default_parse_cookies': 'YOUR_COOKIES', 'default_download_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['FiveSingMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'FiveSingMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
        'default_download_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['FiveSingMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['FiveSingMusicClient'])
  song_infos = music_client.parseplaylist("https://5sing.kugou.com/yeluoluo/dj/631b3fa72418b11003089b8d.html")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'FiveSingMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
        'default_download_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['FiveSingMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://5sing.kugou.com/yeluoluo/dj/631b3fa72418b11003089b8d.html")
  music_client.download(song_infos=song_infos)
  ```

#### KugouMusicClient (Built-in Premium Account)

[KuGou Music](http://www.kugou.com/) is a major Chinese online music platform that offers songs, charts, playlists, music videos, audiobooks, and live content.

Music from the above platform can be downloaded using KugouMusicClient.

KugouMusicClient works out of the box with no need for extra CLI dependencies such as ffmpeg or N_m3u8DL-RE — all you need is pip install musicdl.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m KugouMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  Kugou Music membership cookies copied directly from the web page can easily cause issues, so we provide the script [build_cookies_for_kugou.py](https://github.com/CharlesPikachu/musicdl/blob/master/scripts/build_cookies_for_kugou.py) in the repository to help you directly obtain valid cookies for your member account. 
  The output format is as follows:
  
  ```python
  {'KUGOU_API_GUID': 'xxx', 'KUGOU_API_MID': 'xxx', 'KUGOU_API_MAC': 'xxx', 'KUGOU_API_DEV': 'xxx', 'token': 'xxx', 'userid': 'xxx', 'dfid': 'xxx'}
  ```
  
  Then, you can use KugouMusicClient just like other music clients by passing the membership cookies as follows,
  
  `musicdl -m KugouMusicClient -i "{'KugouMusicClient': {'default_search_cookies': 'YOUR_COOKIES', 'default_download_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://www.kugou.com/yy/special/single/18170.html" -m KugouMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:

  `musicdl -p "https://www.kugou.com/yy/special/single/18170.html" -m KugouMusicClient -i "{'KugouMusicClient': {'default_parse_cookies': 'YOUR_COOKIES', 'default_download_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['KugouMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'KugouMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
        'default_download_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['KugouMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['KugouMusicClient'])
  song_infos = music_client.parseplaylist("https://www.kugou.com/yy/special/single/18170.html")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'KugouMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
        'default_download_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['KugouMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://www.kugou.com/yy/special/single/18170.html")
  music_client.download(song_infos=song_infos)
  ```

#### KuwoMusicClient (Built-in Premium Account)

[Kuwo Music](http://www.kuwo.cn/) is a major Chinese online music platform that offers high-quality music streaming, charts, playlists, radio, and downloadable songs.

We can download music from the aforementioned platform with KuwoMusicClient.

No additional command-line tools, including ffmpeg or N_m3u8DL-RE, are needed to use KuwoMusicClient. Installing musicdl with pip is enough to get started immediately.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m KuwoMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m KuwoMusicClient -i "{'KuwoMusicClient': {'default_search_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://www.kuwo.cn/playlist_detail/2648040171" -m KuwoMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:

  `musicdl -p "https://www.kuwo.cn/playlist_detail/2648040171" -m KuwoMusicClient -i "{'KuwoMusicClient': {'default_parse_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['KuwoMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'KuwoMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['KuwoMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['KuwoMusicClient'])
  song_infos = music_client.parseplaylist("https://www.kuwo.cn/playlist_detail/2648040171")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'KuwoMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['KuwoMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://www.kuwo.cn/playlist_detail/2648040171")
  music_client.download(song_infos=song_infos)
  ```

#### MiguMusicClient

[Migu Music](https://music.migu.cn/v5/#/musicLibrary) is a Chinese music streaming platform that offers a large library of songs, albums, playlists, and other digital music content.

MiguMusicClient allows us to download music from the platform above.

MiguMusicClient can be used directly without installing any extra CLI utilities like ffmpeg or N_m3u8DL-RE. Just install musicdl via pip and it is good to go.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m MiguMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m MiguMusicClient -i "{'MiguMusicClient': {'default_search_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://music.migu.cn/v5/#/playlist?playlistId=208219194&playlistType=create" -m MiguMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:

  `musicdl -p "https://music.migu.cn/v5/#/playlist?playlistId=208219194&playlistType=create" -m MiguMusicClient -i "{'MiguMusicClient': {'default_parse_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['MiguMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'MiguMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['MiguMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['MiguMusicClient'])
  song_infos = music_client.parseplaylist("https://music.migu.cn/v5/#/playlist?playlistId=208219194&playlistType=create")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'MiguMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['MiguMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://music.migu.cn/v5/#/playlist?playlistId=208219194&playlistType=create")
  music_client.download(song_infos=song_infos)
  ```

#### NeteaseMusicClient (Built-in Premium Account)

[NetEase Cloud Music](https://music.163.com/) is one of China’s most popular music streaming platforms, known for its vast song library, personalized recommendations, and active user community.

NeteaseMusicClient makes it possible to download music from the above platform.

There is no need to install extra tools such as ffmpeg or N_m3u8DL-RE to use NeteaseMusicClient. A simple pip install musicdl is all it takes.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m NeteaseMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m NeteaseMusicClient -i "{'NeteaseMusicClient': {'default_search_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://music.163.com/#/my/m/music/playlist?id=7583298906" -m NeteaseMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:

  `musicdl -p "https://music.163.com/#/my/m/music/playlist?id=7583298906" -m NeteaseMusicClient -i "{'NeteaseMusicClient': {'default_parse_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['NeteaseMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'NeteaseMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['NeteaseMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['NeteaseMusicClient'])
  song_infos = music_client.parseplaylist("https://music.163.com/#/my/m/music/playlist?id=7583298906")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'NeteaseMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['NeteaseMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://music.163.com/#/my/m/music/playlist?id=7583298906")
  music_client.download(song_infos=song_infos)
  ```

#### QianqianMusicClient

[Qianqian Music](https://music.91q.com/) is an online music platform offering a large library of songs, popular playlists, artist content, and curated videos.

We use QianqianMusicClient to download music from the above-mentioned platform.

QianqianMusicClient comes ready to use without relying on additional CLI tools like ffmpeg or N_m3u8DL-RE. Just install musicdl through pip and you are all set.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m QianqianMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m QianqianMusicClient -i "{'QianqianMusicClient': {'default_search_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://music.91q.com/songlist/309421" -m QianqianMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:

  `musicdl -p "https://music.91q.com/songlist/309421" -m QianqianMusicClient -i "{'QianqianMusicClient': {'default_parse_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['QianqianMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'QianqianMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['QianqianMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['QianqianMusicClient'])
  song_infos = music_client.parseplaylist("https://music.91q.com/songlist/309421")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'QianqianMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['QianqianMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://music.91q.com/songlist/309421")
  music_client.download(song_infos=song_infos)
  ```

#### QQMusicClient (Built-in Premium Account)

[QQ Music](https://y.qq.com/) is a high-quality music streaming platform offering a vast licensed song library, new releases, charts, playlists, MVs, and digital albums. 

QQMusicClient enables music downloads from the platform mentioned above.

To use QQMusicClient, you do not need any extra command-line tools such as ffmpeg or N_m3u8DL-RE. Once musicdl is installed with pip, it works immediately.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m QQMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

  `musicdl -m QQMusicClient -i "{'QQMusicClient': {'default_search_cookies': 'YOUR_COOKIES'}}"`

- Basic usage for playlist parsing and downloading, without login cookies:

  `musicdl -p "https://y.qq.com/n/ryqq_v2/playlist/8740590963" -m QQMusicClient`

- Simple usage for playlist parsing and downloading, with login cookies:

  `musicdl -p "https://y.qq.com/n/ryqq_v2/playlist/8740590963" -m QQMusicClient -i "{'QQMusicClient': {'default_parse_cookies': 'YOUR_COOKIES'}}"`

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['QQMusicClient'])
  music_client.startcmdui()
  ```

- Simple usage for searching and downloading songs, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'QQMusicClient': {
        'default_search_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['QQMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  music_client.startcmdui()
  ```

- Basic usage for playlist parsing and downloading, without login cookies:

  ```python
  from musicdl import musicdl

  music_client = musicdl.MusicClient(music_sources=['QQMusicClient'])
  song_infos = music_client.parseplaylist("https://y.qq.com/n/ryqq_v2/playlist/8740590963")
  music_client.download(song_infos=song_infos)
  ```

- Simple usage for playlist parsing and downloading, with login cookies:

  ```python
  from musicdl import musicdl
  
  your_vip_cookies_with_str_or_dict_format = ''
  init_music_clients_cfg = {
    'QQMusicClient': {
        'default_parse_cookies': your_vip_cookies_with_str_or_dict_format,
    }
  }
  music_client = musicdl.MusicClient(music_sources=['QQMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
  song_infos = music_client.parseplaylist("https://y.qq.com/n/ryqq_v2/playlist/8740590963")
  music_client.download(song_infos=song_infos)
  ```

#### SodaMusicClient



Music from the above-mentioned platform can be fetched using SodaMusicClient.

SodaMusicClient offers an out-of-the-box experience: no extra CLI tools like ffmpeg or N_m3u8DL-RE are required, and pip install musicdl is all you need.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

  `musicdl -m SodaMusicClient`

- Simple usage for searching and downloading songs, with login cookies:

- Basic usage for playlist parsing and downloading, without login cookies:

- Simple usage for playlist parsing and downloading, with login cookies:

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

- Simple usage for searching and downloading songs, with login cookies:

- Basic usage for playlist parsing and downloading, without login cookies:

- Simple usage for playlist parsing and downloading, with login cookies:









#### StreetVoiceMusicClient

To download music from the platform above, we can use StreetVoiceMusicClient.

(1) Command-Line Usage

- Basic usage for song search and download, without login cookies:

- Simple usage for searching and downloading songs, with login cookies:

- Basic usage for playlist parsing and downloading, without login cookies:

- Simple usage for playlist parsing and downloading, with login cookies:

(2) Invoke It in Python

- Basic usage for song search and download, without login cookies:

- Simple usage for searching and downloading songs, with login cookies:

- Basic usage for playlist parsing and downloading, without login cookies:

- Simple usage for playlist parsing and downloading, with login cookies:













## Global Streaming / Indie

#### AppleMusicClient

#### DeezerMusicClient

#### JamendoMusicClient

JamendoMusicClient requires only a pip installation of musicdl, with no additional setup for tools like ffmpeg or N_m3u8DL-RE.

#### JooxMusicClient

With JooxMusicClient, there is no extra dependency on CLI tools such as ffmpeg or N_m3u8DL-RE. Just install musicdl and you are ready to go.

#### QobuzMusicClient

#### SoundCloudMusicClient

#### SpotifyMusicClient

#### TIDALMusicClient

#### YouTubeMusicClient


## Audio / Radio

#### LizhiMusicClient

LizhiMusicClient requires nothing beyond pip install musicdl — no extra CLI tools, no complicated setup.

#### LRTSMusicClient

You can start using LRTSMusicClient right after installing musicdl via pip, without having to install tools like ffmpeg or N_m3u8DL-RE.

#### QingtingMusicClient

QingtingMusicClient keeps things easy: no additional CLI tools to install, just pip install musicdl and you’re all set.

#### XimalayaMusicClient

XimalayaMusicClient is ready to use after a simple pip install. No extra command-line tools like ffmpeg or N_m3u8DL-RE are needed.


## Aggregators / Multi-Source Gateways

#### GDStudioMusicClient

There’s no need to set up extra CLI tools such as ffmpeg or N_m3u8DL-RE. Just install musicdl via pip and start using GDStudioMusicClient right away.

#### JBSouMusicClient

Using JBSouMusicClient is simple: just pip install musicdl. No additional tools like ffmpeg or N_m3u8DL-RE are required.

#### MP3JuiceMusicClient

MP3JuiceMusicClient doesn’t rely on external CLI tools like ffmpeg or N_m3u8DL-RE. Once you install musicdl, it’s ready to use.

#### MyFreeMP3MusicClient

No extra setup is needed for MyFreeMP3MusicClient — just install musicdl with pip and it will work out of the box.

#### TuneHubMusicClient

To use TuneHubMusicClient, all you need is pip install musicdl. You don’t have to install ffmpeg, N_m3u8DL-RE, or any other CLI tools.




## Unofficial Download Sites / Scrapers

#### BuguyyMusicClient

No extra CLI tools like ffmpeg or N_m3u8DL-RE are needed. Just run pip install musicdl and start using BuguyyMusicClient right away.



#### FangpiMusicClient

FangpiMusicClient works out of the box with just pip install musicdl — no ffmpeg, no N_m3u8DL-RE, and no other CLI tools required.

#### FiveSongMusicClient

Using FiveSongMusicClient does not require the installation of any additional command-line tools, such as ffmpeg or N_m3u8DL-RE. Installing musicdl via pip is sufficient for immediate use.

#### FLMP3MusicClient

Getting started with FLMP3MusicClient is easy: no need to install ffmpeg, N_m3u8DL-RE, or any other CLI tools. Just pip install musicdl and you are good to go.

#### GequbaoMusicClient

GequbaoMusicClient saves you from dealing with extra CLI dependencies like ffmpeg or N_m3u8DL-RE — a simple pip install musicdl is all it takes.

#### GequhaiMusicClient

GequhaiMusicClient is truly plug-and-play: no external CLI tools such as ffmpeg or N_m3u8DL-RE are required. Just install musicdl and use it instantly.

#### HTQYYMusicClient

There is no need to set up external command-line tools like ffmpeg or N_m3u8DL-RE when using HTQYYMusicClient. A single pip install musicdl is enough.

#### JCPOOMusicClient

To use JCPOOMusicClient, you do not need to install any additional CLI tools such as ffmpeg or N_m3u8DL-RE. Simply install musicdl via pip and start using it immediately.

#### KKWSMusicClient

KKWSMusicClient now works without requiring extra CLI tools like ffmpeg or N_m3u8DL-RE. After installing musicdl with pip, it is ready to use straight away.

#### LivePOOMusicClient

LivePOOMusicClient operates without reliance on supplementary CLI tools, including ffmpeg and N_m3u8DL-RE. Installation of musicdl via pip alone enables out-of-the-box usage.

#### MituMusicClient

No extra setup. No external CLI tools. Just pip install musicdl and MituMusicClient is ready to use.

#### TwoT58MusicClient

TwoT58MusicClient is designed for hassle-free use: no additional CLI tools like ffmpeg or N_m3u8DL-RE are needed, and a simple pip install musicdl gets everything ready.

#### YinyuedaoMusicClient

You don’t need to install any extra tools like ffmpeg or N_m3u8DL-RE to use YinyuedaoMusicClient — just pip install musicdl and you’re good to go.

#### ZhuolinMusicClient

ZhuolinMusicClient works right out of the box. No ffmpeg, no N_m3u8DL-RE, and no other CLI tools needed — just install musicdl with pip.

























#### LizhiFM and XimalayaFM Track/Album Download

Musicdl currently also supports searching for and downloading individual audio tracks, as well as entire albums, from long-form audio platforms (*e.g.*, Ximalaya and Lizhi FM) that host podcasts and audiobooks. 
By default, both modes start simultaneously, and the top few search results for each mode are shown based on the input keyword.

A simple usage example is shown below,

```python
from musicdl import musicdl

init_music_clients_cfg = {'XimalayaMusicClient': {'search_size_per_source': 2}}
music_client = musicdl.MusicClient(music_sources=['XimalayaMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

The result of running the code above looks like this,

<div align="center">
  <div>
    <img src="https://github.com/CharlesPikachu/musicdl/raw/master/docs/screenshot/ximalayascreenshot.gif" width="600"/>
  </div>
</div>
<br />

You can also choose the search type yourself by setting `allowed_search_types`, for example:

```python
from musicdl import musicdl

# only search by track
init_music_clients_cfg = {'XimalayaMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['track']}}
# only search by album
init_music_clients_cfg = {'XimalayaMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['album']}}
# instance music_client
music_client = musicdl.MusicClient(music_sources=['XimalayaMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
# start
music_client.startcmdui()
```

Please note that the code above only supports downloading free albums and audio. 
If you need to download paid audio, please configure cookies in `init_music_clients_cfg`, just as you would with other music clients.

#### LanRenTingShu Book/Album Download

Musicdl currently supports searching and downloading books (书籍) and albums (节目) from LanRenTingShu. Example usage:

```python
from musicdl import musicdl

# only search by book
init_music_clients_cfg = {'LRTSMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['book']}}
# only search by album
init_music_clients_cfg = {'LRTSMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['album']}}
# search by album and book
init_music_clients_cfg = {'LRTSMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['album', 'book']}}
# instance music_client
music_client = musicdl.MusicClient(music_sources=['LRTSMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
# start
music_client.startcmdui()
```

By default, this example only downloads free albums and tracks. To access paid content, you must configure your user cookies in `init_music_clients_cfg`.

#### QingtingFM Track/Album Download

The usage for searching and downloading on the QingTing FM website is similar to Ximalaya and Lizhi FM. 
The only thing to watch out for is how cookies are set, it differs from typical music client objects.

Specifically, without logging in (*i.e.*, when you don’t need to download paid audio), you can invoke it by running `musicdl -m QingtingMusicClient` in the command line, or by calling it via the following code:

```python
from musicdl import musicdl

# only search by track
init_music_clients_cfg = {'QingtingMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['track']}}
# only search by album
init_music_clients_cfg = {'QingtingMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['album']}}
# search by album and track
init_music_clients_cfg = {'QingtingMusicClient': {'search_size_per_source': 2, 'allowed_search_types': ['album', 'track']}}
# instance music_client
music_client = musicdl.MusicClient(music_sources=['QingtingMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
# start
music_client.startcmdui()
```

When you need to download paid audio, you’ll have to capture the network traffic yourself on the [QingTing FM web client](https://www.qtfm.cn/).
Look for an AJAX request with the keyword `auth`, its response data will look like:

```python
{
  "errorno": 0,
  "errormsg": "",
  "data": {
    "qingting_id": "xxxx",
    "access_token": "xxx",
    "refresh_token": "xxx",
    "expires_in": 7200
  }
}
```

Or, use the script [build_cookies_for_qingtingfm.py](https://github.com/CharlesPikachu/musicdl/tree/master/scripts/build_cookies_for_qingtingfm) in this repository to retrieve it.

Once you’ve obtained this data, you can configure cookies for `QingtingMusicClient` as follows:

```python
from musicdl import musicdl

cookies = {"qingting_id": "xxxx", "access_token": "xxx", "refresh_token": "xxx"}
init_music_clients_cfg = {'QingtingMusicClient': {'default_search_cookies': cookies, 'default_download_cookies': cookies, 'search_size_per_source': 3}}
music_client = musicdl.MusicClient(music_sources=['QingtingMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

Of course, it’s worth noting that another prerequisite for downloading paid audio is that your account must already have permission to access (listen to) that audio.

#### Apple Music Download

Before using `AppleMusicClient`, please ensure that the following command-line tools are installed and available in your environment,

- [FFmpeg](https://www.ffmpeg.org/)
- [N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE)
- [Bento4](https://www.bento4.com/downloads/)
- [amdecrypt](https://github.com/CharlesPikachu/musicdl/releases/tag/clitools)

Apple Music is like TIDAL, only users with a paid Apple Music subscription can download Apple Music tracks, otherwise, you can only download an approximately 30-90 second preview clip.
Specifically, for paid Apple Music users, musicdl supports downloading music files in the following formats,

- `aac-legacy`
- `aac-he-legacy`
- `aac`
- `aac-he`
- `aac-binaural`
- `aac-downmix`
- `aac-he-binaural`
- `aac-he-downmix`
- `atmos`
- `ac3`
- `alac`

Specifically, if you only need to download tracks in the `aac-legacy` and `aac-he-legacy` quality tiers, you just need to make sure that [FFmpeg](https://www.ffmpeg.org/) and [N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE) are already installed and available in your environment variables.
Then, set the `media-user-token` argument you obtained by capturing network traffic from the Apple Music website as follows:

```python
from musicdl import musicdl
from musicdl.modules.sources.apple import SongCodec

cookies = {'media-user-token': xxx}
init_music_clients_cfg = {'AppleMusicClient': {'default_search_cookies': cookies, 'search_size_per_source': 10, 'language': 'en-US', 'codec': SongCodec.AAC_LEGACY}}
music_client = musicdl.MusicClient(music_sources=['AppleMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

However, if you need to download higher-quality audio (*e.g.*, `alac`), the setup is relatively more complex. 
First, follow the [wrapper](https://github.com/WorldObservationLog/wrapper) guide and start the wrapper server (❗ **note that Windows users need to download and install WSL first, followed by installing Ubuntu on WSL, and finally start the wrapper server within Ubuntu, otherwise, decryption will most likely fail** ❗).
Then, in addition to [FFmpeg](https://www.ffmpeg.org/) and [N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE), you also need to install [Bento4](https://www.bento4.com/downloads/) and [amdecrypt](https://github.com/CharlesPikachu/musicdl/releases/tag/clitools).
Finally, configure your musicdl as follows:

```python
from musicdl import musicdl
from musicdl.modules.sources.apple import SongCodec

init_music_clients_cfg = {'AppleMusicClient': {
    'search_size_per_source': 10, 
    'language': 'en-US', 
    'codec': SongCodec.ALAC, 
    'use_wrapper': True, 
    'wrapper_account_url': 'http://127.0.0.1:30020/',
    'wrapper_decrypt_ip': '127.0.0.1:10020',
}}
music_client = musicdl.MusicClient(music_sources=['AppleMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

Note that the `wrapper_account_url` and `wrapper_decrypt_ip` settings must match the corresponding arguments configured in your [wrapper server](https://github.com/WorldObservationLog/wrapper).

#### Deezer Music Download

musicdl now supports searching for and downloading music from the Deezer Music Client, as well as parsing playlists. Specifically, there are three possible scenarios.

The first is using musicdl directly for music search, download, or playlist parsing without configuring login cookies. 
In this case, you will most likely only be able to download song preview clips, usually around 30 seconds long (musicdl occasionally shares some shared Deezer premium accounts. Therefore, you might sometimes be able to download lossless music directly using musicdl, even without configuring any Deezer premium cookies).
A simple usage example is as follows:

```python
from musicdl import musicdl

music_client = musicdl.MusicClient(music_sources=['DeezerMusicClient'])
music_client.startcmdui()
```

The second is configuring login cookies, but the logged-in account is not a Deezer Premium subscriber. 
In this case, you will only be able to download songs at 128 kbps.
A simple example of how to use it is shown below:

```python
from musicdl import musicdl

# cookies must contain "arl"
# >>> example1: cookies = {'arl': xxx, ...}
# >>> example2: cookies = arl=xxx; key1=value1; key2=value2; ...
cookies = YOUR_COOKIES_IN_DICT_OR_STR_FORMAT
init_music_clients_cfg = {'DeezerMusicClient': {'default_search_cookies': cookies, 'search_size_per_source': 5}}
music_client = musicdl.MusicClient(music_sources=['DeezerMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

The third is configuring login cookies, with the logged-in account being a Deezer Premium subscriber. 
In this case, you can download music in Deezer’s highest-quality FLAC lossless format.
The invocation code is entirely identical to that used in the second scenario.

#### Qobuz Music Download

Qobuz is the world leader in 24-bit Hi-Res downloads, offering more than 100 million tracks for streaming in unequalled sound quality (FLAC 16 Bits / 44.1kHz).

To use musicdl to download songs from Qobuz, you must have a paid Qobuz membership account. 
Otherwise, musicdl will automatically call some third-party APIs that use shared Qobuz member accounts to try to resolve the song you need. 
Since the long-term reliability and stability of these third-party APIs cannot be guaranteed, if they become unavailable and you do not have a valid paid Qobuz membership account yourself, you will only be able to access roughly 30-second preview clips.

Specifically, if you have a valid paid Qobuz membership account, first, you need to obtain the member cookies yourself by capturing network traffic on [Qobuz’s official website](https://play.qobuz.com/discover). 
The cookies format should be as follows:

```python
{"x-user-auth-token": "xxx", ...} OR "x-user-auth-token=xxx;..."
```

Of course, you can also directly use the script [build_cookies_for_qobuz.py](https://github.com/CharlesPikachu/musicdl/blob/master/scripts/build_cookies_for_qobuz.py) provided in musicdl to build the member cookies required by musicdl.

A simple example of the download code is as follows:

```python
from musicdl import musicdl

cookies = {'x-user-auth-token': 'xxx'}
init_music_clients_cfg = {'QobuzMusicClient': {'default_search_cookies': cookies, 'search_size_per_source': 5}}
music_client = musicdl.MusicClient(music_sources=['QobuzMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

Notably, for non-member users, setting cookies can only improve the audio quality, but the downloadable content is still limited to a 30-second preview clip.

#### SoundCloud Music Download

Musicdl lets you search for and download your favorite songs from SoundCloud. Specifically, you only need to run the following command:

```
musicdl -m SoundCloudMusicClient
```

Or you can invoke it with the following code:

```python
from musicdl import musicdl

music_client = musicdl.MusicClient(music_sources=['SoundCloudMusicClient'])
music_client.startcmdui()
```

The only thing to note is that `SoundCloudMusicClient` handles login cookies for downloading subscriber-only tracks slightly differently from the other music clients. 
You need to capture packets (*i.e.*, sniff the network requests) from [SoundCloud’s official website](https://soundcloud.com/) yourself to obtain the *Authorization* field in the request headers, then fill it in as follows:

```python
from musicdl import musicdl

cookies = {'oauth_token': 'OAuth x-xxxxxx-xxxxxxxxx-xxxxxxx'}
init_music_clients_cfg = {'SoundCloudMusicClient': {'default_search_cookies': cookies, 'default_download_cookies': cookies, 'search_size_per_source': 5}}
music_client = musicdl.MusicClient(music_sources=['SoundCloudMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

#### Spotify Music Download



#### TIDAL High-Quality Music Download

Prior to using `TIDALMusicClient`, verify that the following command-line tools are correctly installed and available in your environment,

- [PyAV](https://github.com/PyAV-Org/PyAV)
- [FFmpeg](https://www.ffmpeg.org/)
- [N_m3u8DL-RE](https://github.com/nilaoda/N_m3u8DL-RE)

If you plan to use musicdl to download high-quality lossless audio from TIDAL, you must have an active TIDAL subscription. 
Otherwise, musicdl may fall back to third-party sources, and stable access to the highest-quality lossless files cannot be guaranteed.

After you have a TIDAL membership account, you need to manually capture the cookies of your account from the TIDAL website using network packet capturing. 
The format is as follows:

```python
{
  "access_token": "xxx", 
  "refresh_token": "xxx", 
  "expires": "2026-02-10T07:32:18.102233",
  "user_id": xxx, 
  "country_code": "SG", 
  "client_id": "7m7Ap0JC9j1cOM3n", 
  "client_secret": "vRAdA108tlvkJpTsGZS8rGZ7xTlbJ0qaZ2K9saEzsgY="
}
```

Of course, musicdl also provides a script [build_cookies_for_tidal.py](https://github.com/CharlesPikachu/musicdl/blob/master/scripts/build_cookies_for_tidal.py) to automatically obtain your TIDAL membership cookies. 
You can simply run the script and follow the prompts to retrieve the cookies mentioned above.

Once you have successfully obtained your membership cookies, you can use musicdl to download lossless music from TIDAL using the following method,

```python
from musicdl import musicdl

cookies = "YOUR_VIP_COOKIES"
init_music_clients_cfg = {'TIDALMusicClient': {'default_search_cookies': cookies, 'search_size_per_source': 5}}
music_client = musicdl.MusicClient(music_sources=['TIDALMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

#### YouTube Music Download

If you want to use musicdl to search for and download music from `YouTubeMusicClient`, you must have [Node.js](https://nodejs.org/en) installed, *e.g.*, on Linux, you can install Node.js using the following script:

```bash
#!/usr/bin/env bash
set -e

# Install nvm (Node Version Manager)
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# Load nvm for this script
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

# Install and use latest LTS Node.js
nvm install --lts
nvm use --lts

# Print versions
node -v
npm -v
```

On macOS, you can install Node.js using the following script:

```bash
#!/usr/bin/env bash
set -e

# Install nvm (Node Version Manager)
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# Load nvm for this script
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

# Install and use latest LTS Node.js
nvm install --lts
nvm use --lts

# Print versions
node -v
npm -v
```

On Windows (PowerShell), you can install Node.js using the following script:

```bash
# Install Node.js LTS via winget
winget install --id OpenJS.NodeJS.LTS -e --source winget

# Print hint for version check
Write-Output ""
Write-Output "Please reopen PowerShell and run:"
Write-Output "  node -v"
Write-Output "  npm -v"
```

A simple example of searching for and downloading music from `YouTubeMusicClient` is as follows,

```python
from musicdl import musicdl

music_client = musicdl.MusicClient(music_sources=['YouTubeMusicClient'])
music_client.startcmdui()
```

#### GD Studio Music Download

We’ve added `GDStudioMusicClient` to musicdl as a practical solution for users who are on a tight budget or who find it difficult to configure extra command-line tools/arguments for musicdl. 
With only the basic installation of musicdl, you can search for and download high-quality music files from the following music platforms:

| Source (EN)             | Source (CN)                        | Official Websites                     | `allowed_music_sources`      |
| -----------------       | -------------------                | -----------------------------------   | -------------------          |
| Spotify                 | Spotify                            | https://www.spotify.com               | `spotify`                    |
| Tencent (QQ Music)      | QQ音乐                             | https://y.qq.com                      | `tencent`                    |
| NetEase Cloud Music     | 网易云音乐                         | https://music.163.com                 | `netease`                    |
| Kuwo                    | 酷我音乐                           | https://www.kuwo.cn                   | `kuwo`                       |
| TIDAL                   | TIDAL                              | https://tidal.com                     | `tidal`                      |
| Qobuz                   | Qobuz                              | https://www.qobuz.com                 | `qobuz`                      |
| JOOX                    | JOOX                               | https://www.joox.com                  | `joox`                       |
| Bilibili                | 哔哩哔哩                           | https://www.bilibili.com              | `bilibili`                   |
| Apple Music             | 苹果音乐                           | https://www.apple.com/apple-music/    | `apple`                      |
| YouTube Music           | 油管音乐                           | https://music.youtube.com             | `ytmusic`                    |

Specifically, you just need to write and run a few lines of code like this 
(song retrieval from YouTube and Tencent is unstable, so musicdl disables these two sources by default. 
You can manually enable them by setting `allowed_music_sources`.):

```python
from musicdl import musicdl

music_client = musicdl.MusicClient(music_sources=['GDStudioMusicClient'])
music_client.startcmdui()
```

Or, equivalently, run the following command in the command line:

```bash
musicdl -m GDStudioMusicClient
```

By default, the above code will search for and download music from eight music platforms, excluding YouTube and Tencent Music (as using `GDStudioMusicClient` for search and download on both platforms seems to be unstable).
The screenshot of the running result is as follows:

<div align="center">
  <div>
    <img src="https://github.com/CharlesPikachu/musicdl/raw/master/docs/screenshot/gdstudioscreenshot.png" width="600"/>
  </div>
</div>
<br />

However, please note that this way of running is not very stable (*e.g.*, some sources may fail to find any valid songs) and is likely to exceed the limit on the number of requests per minute allowed for a single IP by `GDStudioMusicClient`. 
If you still wish to perform a full-platform search, we recommend modifying the default arguments as follows:

```python
from musicdl import musicdl

init_music_clients_cfg = {'GDStudioMusicClient': {'search_size_per_source': 1}}
music_client = musicdl.MusicClient(music_sources=['GDStudioMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

The equivalent command in the command line is:

```bash
musicdl -m GDStudioMusicClient -i "{'GDStudioMusicClient': {'search_size_per_source': 1}}"
```

Or, an even better option is to manually specify a few platforms where you believe your desired music files are likely to be found, for example:

```python
from musicdl import musicdl

# allowed_music_sources can be set to any subset (i.e., any combination) of ['spotify', 'tencent', 'netease', 'kuwo', 'tidal', 'qobuz', 'joox', 'bilibili', 'apple', 'ytmusic']
init_music_clients_cfg = {'GDStudioMusicClient': {'search_size_per_source': 5, 'allowed_music_sources': ['spotify', 'qobuz', 'tidal', 'apple']}}
music_client = musicdl.MusicClient(music_sources=['GDStudioMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

The way to run it from the command line is similar:

```bash
musicdl -m GDStudioMusicClient -i "{'GDStudioMusicClient': {'search_size_per_source': 5, 'allowed_music_sources': ['spotify', 'qobuz', 'tidal', 'apple']}}"
```

#### JBSou Music Download

`JBSouMusicClient`’s functionality is similar to `TuneHubMusicClient`’s. 
Both are third-party APIs that consolidate music search and download functions from multiple platforms into a single interface.
The key difference is that `JBSouMusicClient` focuses on searching and downloading 320 kbps MP3 audio files. 
The list of music platforms it currently supports is as follows:

| Source (EN)             | Source (CN)                        | Official Websites                     | `allowed_music_sources`      |
| -----------------       | -------------------                | -----------------------------------   | -------------------          |
| Tencent (QQ Music)      | QQ音乐                             | https://y.qq.com                      | `qq`                         |
| NetEase Cloud Music     | 网易云音乐                         | https://music.163.com                 | `netease`                    |
| Kuwo                    | 酷我音乐                           | https://www.kuwo.cn                   | `kuwo`                       |
| Kugou                   | 酷狗音乐                           | https://www.kugou.com/                | `kugou`                      |

More specifically, its invocation is as follows,

```python
from musicdl import musicdl

init_music_clients_cfg = {'JBSouMusicClient': {'search_size_per_source': 5, 'allowed_music_sources': ['qq', 'netease', 'kuwo', 'kugou']}}
music_client = musicdl.MusicClient(music_sources=['JBSouMusicClient'], init_music_clients_cfg=init_music_clients_cfg)
music_client.startcmdui()
```

The screenshot of the running result is as follows:

<div align="center">
  <div>
    <img src="https://github.com/CharlesPikachu/musicdl/raw/master/docs/screenshot/jbsouscreenshot.png" width="600"/>
  </div>
</div>
<br />

#### TuneHub Music Download

`TuneHubMusicClient` is actually quite similar to `GDStudioMusicClient`, as it allows music search and download from multiple music platforms. 
However, it primarily supports music platforms in Mainland China and offers fewer music sources compared to `GDStudioMusicClient`. 
Specifically, the list of platforms it currently supports is as follows:

| Source (EN)             | Source (CN)                        | Official Websites                     | `allowed_music_sources`      |
| -----------------       | -------------------                | -----------------------------------   | -------------------          |
| Tencent (QQ Music)      | QQ音乐                             | https://y.qq.com                      | `qq`                         |
| NetEase Cloud Music     | 网易云音乐                         | https://music.163.com                 | `netease`                    |
| Kuwo                    | 酷我音乐                           | https://www.kuwo.cn                   | `kuwo`                       |

Specifically, you can call it using the following code:

```python
from musicdl import musicdl

music_client = musicdl.MusicClient(music_sources=['TuneHubMusicClient'])
music_client.startcmdui()
```

Alternatively, you can directly run the following command in the terminal:

```python
musicdl -m TuneHubMusicClient
```

The screenshot of the running result is as follows:

<div align="center">
  <div>
    <img src="https://github.com/CharlesPikachu/musicdl/raw/master/docs/screenshot/tunehubscreenshot.png" width="600"/>
  </div>
</div>
<br />