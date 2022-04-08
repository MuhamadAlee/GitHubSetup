
**GET FRAMES FROM VIDEO**

    !ffmpeg -i temp.mp4 -vf fps=10 res/%d.png

**GET VIDEO FROM IMAGES**

    !ffmpeg -y -framerate 10 -i images/%d.png -filter:v select="not(mod(n-1,2))" -vf "fps=25,format=yuv420p" out.mp4
