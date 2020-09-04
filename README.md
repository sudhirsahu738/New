# Zee5
![Codacy Badge](https://api.codacy.com/project/badge/Grade/fcbc4bb229fc4c4bab285e23552cbe61)
[![CodeFactor](https://www.codefactor.io/repository/github/dedshit/zee5/badge)](https://www.codefactor.io/repository/github/dedshit/zee5)
# To grab hidden links from *ZEE5* without premium subscription

# Features

  ● Tv Shows ✅
  
  ● Movies ✅ 
  
  ● Originals ✅
# Requirements

     PYTHON >3.6
  
# Usage for Shows:
   
     python3 shows.py -h, --help
     
     For premiere Tvshows 
         
         python3 shows.py -p / --premiere <link> -q <quality>
         
         Available qualities for latest and intermediate shows:( 96,140,240,360,480,570,720,1080 )
         
         eg: python3 shows.py -p https://zee5tvshowlink -q 144
         
     For Old Tvshows
     
         python3 shows.py -s / --previous <link> -q <quality>
         
         Qualities for Old shows ( 144,240,360,480 )
         
         eg: python3 shows.py --previous https://zee5showlink -q 144
         
# Usage for movies and originals:

         python3 mov5.py -h
         
         python3 mov5.py -z, --Z movielink/originals
         
         eg : python3 mov5.py -z, --Z https://zee5.com/movies/"....."
              
              python3 mov5.py -z https://zee5.com/zee5originals/"..."(specify episode)
     
# Note

      If u need to download, use ffmpeg to download all segment(ts files) [Take long time😬]
                 Better stream it!!
# Contact

          Name : @°
     wa.me/+918428425154

| Version |           |
| ------- | ----------|
| v2.0.2  |     ✅    |
