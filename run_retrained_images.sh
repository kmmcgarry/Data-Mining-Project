for file in /Users/gratfu/Desktop/MHI/'Fall 2017'/'SI 671'/Data-Mining-Project/images_2_test/*
do
	python 'tensorflow-for-poets-2'/scripts/label_image.py --image="$file" --graph='tensorflow-for-poets-2'/tf_files/retrained_graph.pb --labels='tensorflow-for-poets-2'/tf_files/retrained_labels.txt --input_height=299 --input_width=299 >> retrained_results.txt
	echo "???" >> retrained_results.txt

done