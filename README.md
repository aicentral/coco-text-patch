<h1> COCO-Text-Patch</h1>
COCO-Text-Patch is the first text verification data set created to encourage researchers to use machine learning techniques for text verification which will in turn enhance the whole end-to-end text detection and recognition process. 
<br>
The data set is derived from <a href=https://arxiv.org/abs/1601.07140v2>COCO-Text</a> and contains approximately 354 thousands images labeled as text and non-text.

<p> <H2> Using the data set </h2>
If you are going to use this data set please cite the paper
<p>@article{coco-text-patch2016,
<br> &nbsp;&nbsp;&nbsp;&nbsp; title={Text Patches Data Set for Text verification},
<br> &nbsp;&nbsp;&nbsp;&nbsp; author={Ibrahim, Ahmed and Abbott, Lynn and Hussein, Mohamed},
<br> &nbsp;&nbsp;&nbsp;&nbsp; journal={arXiv preprint arXiv:16xxxx},
<br> &nbsp;&nbsp;&nbsp;&nbsp; year={2016}
<br>}
<p>
<p> <H2> Creating the data set </h2>
<p>to create the data set you have to:-
<p>-In the COCOAPI folder, unzip the COCO_Text.json.gz file
<p>-Download the COCO 2014 training data set from <a href=http://msvocds.blob.core.windows.net/coco2014/train2014.zip>http://msvocds.blob.core.windows.net/coco2014/train2014.zip</a>
<p>-Make sure you have Python 2.7 installed with numpy, skimage, math, Image, HD5 packages
<p>-Clone the Git repository  
<p>-From Python shell run createdataset.py
<p>
<p> <H2> supplied models </h2>
<p> the folder "models" contains model description files ready to be used in caffe to train the models descibed in our paper "Text Patches Data Set for Text verification"
<p> the folder contains model desciptions as well as suggested solver files.
<p> you need to have Caffe installed from <a href=http://caffe.berkeleyvision.org/>http://caffe.berkeleyvision.org/</a>

<p>for any inquiries please contact me on nady at vt.edu
