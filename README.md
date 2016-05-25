# subscene-mass-downloader
Because it's hard to download subtitles one-by-one! A subtitles downloader for http://subscene.com

### Usage
Add subscene's links into a text file, e.g. `links.txt`
```
http://subscene.com/subtitles/the-flash-second-season-2015/indonesian/1202940
http://subscene.com/subtitles/the-flash-second-season-2015/indonesian/1207056
http://subscene.com/subtitles/the-flash-second-season-2015/indonesian/1211074
http://subscene.com/subtitles/the-flash-second-season-2015/indonesian/1215258
```

And then execute `subscene-dl.py` file with file name parameter
```
python subscene-dl.py /directory/to/links.txt
```
Output will be like
```
Downloading The-Flash-S02E01-The-Man-Who-Saved-Central-City-WEB-DL-Glasscastle ...
...The-Flash-S02E01-The-Man-Who-Saved-Central-City-WEB-DL-Glasscastle done!

Downloading The-Flash-S02E02-The-Flash-of-Two-Worlds-HDTV-Glasscastle ...
...The-Flash-S02E02-The-Flash-of-Two-Worlds-HDTV-Glasscastle done!

Downloading The-Flash-S02E03-Semua-HDTV-Indonesia-Family-of-Rogues-Glasscastle ...
...The-Flash-S02E03-Semua-HDTV-Indonesia-Family-of-Rogues-Glasscastle done!

Downloading The-Flash-S02E04-The-Fury-of-Firestorm-Semua-HDTV-Glasscastle ...
...The-Flash-S02E04-The-Fury-of-Firestorm-Semua-HDTV-Glasscastle done!
```