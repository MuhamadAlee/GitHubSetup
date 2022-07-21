
**GET FRAMES FROM VIDEO**

    ffmpeg -i temp.mp4 -vf fps=10 res/%d.png

**GET VIDEO FROM IMAGES**

    ffmpeg -y -framerate 10 -i images/%d.png -filter:v select="not(mod(n-1,2))" -vf "fps=25,format=yuv420p" out.mp4
    
**Make gif out of video**

    ffmpeg -ss 1 -t 3 -i input.mp4 -vf "fps=10,scale=512:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
    
    ## it will ss--skip first 1 second and make the gif of total -t 3 seconds 
    
**Trim the video**

    ffmpeg -i input.mp4 -vf trim=8:13 output.mp4
    
    ## it will trim from 8 seconds to 13 seconds

**Merge audio with the video**

    ffmpeg -i input.mp4 -i audio.mp3 -map 0:v -map 1:a -c:v copy -shortest output.mp4
    
