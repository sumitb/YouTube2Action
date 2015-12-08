# YouTube2Action
=======
Deep Learning object detectors in YouTube clips to identify action in the form of Subject-verb-Object triplets.

Dependency
------

* This code requires [Caffe](http://caffe.berkeleyvision.org) to be installed. For Installation instructions visit: 
* [Large Scale Detection through Adaptation](http://lsda.berkeleyvision.org/)
* [LRCN Activity Recognition](http://www.eecs.berkeley.edu/~lisa_anne/LRCN_video)
* Natural Language Toolkit 3.1: as a pre-requisite for [WordNet](https://wordnet.princeton.edu/) 

Dataset
-------

* Download [YouTubeClips.tar] (http://www.cs.utexas.edu/users/ml/clamp/videoDescription/YouTubeClips.tar)


Instructions
-------
* [YouTube2Action](https://github.com/sumitb/YouTube2Action) contains latest release.
* Detailed code structure
	- data: This directory act as a place to store intermediate results and final output.
	- src
		+ U2_data.py: Python script to obtain images from YouTube links using ffmpeg, youtube-dl
		+ detect_all.m: MATLAB script to run LSDA
		+ sub_obj.m: MATLAB script to obtain Subject-Objectsfrom data/subject_object.mat
		+ verb_Extractor.sh: Bash script to run LRCN
		+ svo_triplet.m: MATLAB script to combine Subject-Object and correpsonding verbs.
		+ word.py: Python script to run evaluation and obtain final_svo.txt

		+ classify_video.py, detect10k_demo.m: Libraries code which we configured for our use.		

Citing
-------

"LSDA: Large Scale Detection Through Adaptation." J. Hoffman, S. Guadarrama, E. Tzeng, R. Hu, J. Donahue, R. Girshick, T. Darrell, and K. Saenko. Neural Information Processing Systems (NIPS), 2014.
"Long-term recurrent convolutional networks for visual recognition and description." Donahue, J., Hendricks, L. A., Guadarrama, S., Rohrbach, M., Venugopalan, S., Saenko, K., & Darrell, T. (2014). 
