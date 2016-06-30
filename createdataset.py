import math
from PIL import Image
import numpy as np
import filterdata as fd
import config
imagesbase=config.imagesbase
fullpath=config.fullpath
outputdir= config.outputdir 
outputdir1= config.outputdir if fullpath else ''
idx=0
cnttxt=0;cntnon=0;
phasenames=['train','val']
for phase in [0,1]: # 0=train , 1=val
    print 'start creating training set....' if (phase==0) else 'start creating validation set....'
    if 'ct' not in locals(): # to prevent the API from re-loading
        from COCOAPI import coco_text
        ct = coco_text.COCO_Text('COCOAPI/COCO_Text.json')
    if (phase==0):
        allimgIds = ct.getImgIds(imgIds=ct.train,catIds=[('legibility','legible')])
    else:
        allimgIds = ct.getImgIds(imgIds=ct.val,catIds=[('legibility','legible')])
    imgs = ct.loadImgs(allimgIds)
    f=open('%s_unbalance.txt'%(phasenames[phase]),'w')
    
    for x in imgs:
        annids=ct.getAnnIds(imgIds=x['id'],catIds=[('legibility','legible')])
        anns = ct.loadAnns(annids)
        image=Image.open('%s%s'%(imagesbase,x['file_name']))
        print 'processing image %d'%(x['id'])
        w=x['width']
        h=x['height']
        
        # non text areas
        xmin=int(np.floor(np.amin([z['bbox'][0] for z in anns])))
        ymin=int(np.floor(np.amin([z['bbox'][1] for z in anns])))
        if ((xmin>32) & (ymin>32)):
            for i in range(0,xmin-32,32):
                    for j in range(0,ymin-32,32):
                        box=[i,j,i+32,j+32]
                        window=image.crop(box)
                        window.save('%stxt_%d.jpg'%(outputdir,idx), "JPEG")
                        print >>f, '%stxt_%d.jpg %d'%(outputdir1,idx,0)
                        idx=idx+1
                        cntnon=cntnon+1
        xmax=int(np.floor(np.amax([z['bbox'][0] for z in anns])))
        ymax=int(np.floor(np.amax([z['bbox'][1] for z in anns])))
        if (((h-xmax)>32) & ((w-ymax)>32)):
            for i in range(xmax,h-xmax-32,32):
                    for j in range(ymax,w-ymax-32,32):
                        box=[i,j,i+32,j+32]
                        window=image.crop(box)
                        window.save('%stxt_%d.jpg'%(outputdir,idx), "JPEG")
                        print >>f, '%stxt_%d.jpg %d'%(outputdir1,idx,0)
                        idx=idx+1
                        cntnon=cntnon+1
        # text areas
        for y in anns:
            bbox=y['bbox'];
            if bbox[3]<32:
                bbox[3]=32
            if bbox[2]<32:
                bbox[2]=32
            bbox[2]=bbox[2]+bbox[0];bbox[3]=bbox[3]+bbox[1];
            bbox=[int(math.floor(xx)) for xx in bbox];
            crop = image.crop(bbox)
            if crop.size[0]<32 or crop.size[1]<32:
                crop.save('%stxt_%d.jpg'%(outputdir,idx), "JPEG")
                print >>f, '%stxt_%d.jpg %d'%(outputdir1,idx,1)
                idx=idx+1
            else:
                for i in range(0,crop.size[0]-32,32):
                    for j in range(0,crop.size[1]-32,32):
                        box=[i,j,i+32,j+32]
                        window=crop.crop(box)
                        window.save('%stxt_%d.jpg'%(outputdir,idx), "JPEG")
                        print >>f, '%stxt_%d.jpg %d'%(outputdir1,idx,1)
                        idx=idx+1
    print 'done training set....' if (phase==0)  else 'done validation set....'
    f.close()
print 'total=', idx,' non-text=', cntnon,' text=',idx-cntnon
########################
#### start filtering data
fd.filter()
print 'Data set created in' 
print outputdir
print 'unbalanced dataset images are listed in train_unbalanced.txt and val_unbalance.txt'
print 'final balanced dataset images are listed in train.txt and val.txt'