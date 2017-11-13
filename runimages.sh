for file in /Users/kristen/Documents/Data-Mining-Project/Images/*
do
  python classify_image.py --image="$file" >> results.txt
  echo "???" >> results.txt


done
