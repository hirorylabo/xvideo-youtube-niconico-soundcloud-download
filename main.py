import re, sys, os, time, subprocess
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

main_links = [
"https://www.youtube.com/",
"https://soundcloud.com/",
"https://www.nicovideo.jp/"
]

ero_links = [
"https://www.xvideos.com/"
]

# youtube soundcloud nicovideo
if any(s in sys.argv[1] for s in (main_links)):
    ans = input("type mp3 or mp4: ")
    if "https://www.youtube.com/" in sys.argv[1]:
        th_list = sys.argv[1].split("list=")[1]
    else:
        th_list = sys.argv[1]
    if ans=="mp3":
        cmd = 'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -ci --extract-audio --audio-format mp3 --add-metadata ' + th_list
    if ans=="mp4":
        cmd = 'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -i -f mp4 --add-metadata ' + th_list
    subprocess.check_call(cmd.split())
    sys.exit()

# xvideo
elif any(s in sys.argv[1] for s in (ero_links)):
    if "/tags/" in sys.argv[1] or "/c/" in sys.argv[1] or "https://www.xvideos.com/" == sys.argv[1]:
        html_page = urlopen(sys.argv[1])
        time.sleep(5)
        soup = BeautifulSoup(html_page, "lxml")
        links = soup.select("div.thumb>a")
        folder = sys.argv[1].split('/')[-1]
        for link in links:
            link = "https://www.xvideos.com" + link.get("href")
            cmd = 'youtube-dl -o ./' + folder +  '/%(title)s.%(ext)s -v ' + link
            subprocess.check_call(cmd.split())
        sys.exit()
    else:
        cmd = 'youtube-dl -v ' + sys.argv[1]
        subprocess.check_call(cmd.split())
        sys.exit()

# khinsider
else:
    html_page = urlopen(sys.argv[1])
    soup = BeautifulSoup(html_page, "lxml")

    if "https://downloads.khinsider.com/" in sys.argv[1]:
        title = soup.select("h2:nth-of-type(1)")[0].string
        th_list = soup.select('#songlist tr:nth-of-type(1) th')
        title_index = 0
        for i in th_list:
            if "Song Name" in str(i):
                break
            title_index += 1
        song_step = len(soup.select('#songlist tr:nth-of-type(2) td')) - title_index
        links = soup.select('#songlist td.clickable-row a[href$="mp3"]')[::song_step]

    print("[Start Download] " + title)
    BASE_URL = "./" + title
    if not os.path.exists(BASE_URL):
        os.mkdir(BASE_URL)

    for index, link in enumerate(links):
        time.sleep(1)
        if "https://downloads.khinsider.com/" in sys.argv[1]:
            mp3_page = urlopen("https://downloads.khinsider.com/" + link.get('href'))
            mp3_soup = BeautifulSoup(mp3_page, "lxml")
            audio = mp3_soup.select('audio')[0].get('src')
            print(str(index) + " - " + link.string)
            urlretrieve(audio, BASE_URL + "/" + str(index) + " - " + link.string + ".mp3")
