違法に権利者の許可なくアップロードされた録音又は録画されたものを、それが許可なくアップロードされていると知りながら、ダウンロードする行為は自己責任となります。
それが「市販(ダウンロード販売含む)」されていた場合で、かつ「権利者が告訴」していた場合に、その告訴された動画や音楽をダウンロードする行為は、刑事罰の対象になります。

# install

```bash
git clone https://github.com/ryuta69/xvideo-youtube-niconico-soundcloud-download
### or download zip
brew install youtube-dl libav ffmpeg
### if you are windows, read https://teki0918.hatenablog.jp/entry/youtube-dl-windpws (japanese)
pip install beautifulsoup4
```

# how to use

```bash
python3 main.py PASTE-URL-HERE
```

just paste url.

Example:

```bash
python3 main.py https://www.youtube.com/playlist?list=PLZWB2wzAxoVAIBVUqCZ84jqOyMKzLSVUqf 
### movie url and playlist url both are available
```

Xvideos, Youtube, NicoNico, Soundcloud is available.
