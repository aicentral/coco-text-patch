import numpy as np
from skimage.filters import prewitt
from skimage import io
import config
base=config.outputdir
thresh=config.thresh
def filter():
    phasenames=['train','val']
    tr=0;idx=0;cnttxt=0;cntnon=0;
    for phase in [0,1]:
        f=open('%s_unbalance.txt'%(phasenames[phase]),'r')
        f2=open('%s.txt'%(phasenames[phase]),'w')
        for s in f:
            if s.split(' ')[1][0]=='0':
                imgname='%s%s'%(base,s.split(' ')[0])
                print imgname
                im=io.imread(imgname,as_grey=True)
                e = prewitt(im)
                emax=np.amax(e)/2
                et=np.reshape(np.array([0 if e1<emax else 1 for e1 in e.flatten()]),(32,32))
                ecnt=np.sum(et)
                if ecnt>thresh:
                    f2.write(s)
                    tr=tr+(1 if (phase==0) else 0);idx=idx+1;cntnon=cntnon+1
            else:
                f2.write(s)
                tr=tr+(1 if (phase==0) else 0);idx=idx+1;cnttxt=cnttxt+1
        f.close()
        f2.close()
    print 'total=',idx,' training=',tr,' Val=',idx-tr 
    print 'Text=',cnttxt,' non-Text=',cntnon