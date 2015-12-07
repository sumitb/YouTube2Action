for d in ./YouTubeImgs_10/*/ ; do 
  python classify_video2.py ${d:1:-1}  
done
echo 'Script started success!'
