#this script will download, move to 'Download' and open every day Prensa Libre at a predetermined time

import urllib2, time, os, shutil
from time import strftime

monthsOfTheYear = { "01":"enero", "02":"febrero", "03":"marzo", "04":"abril", "05":"mayo", "06":"junio", "07":"julio", "08":"agosto", "09":"septiembre", "10":"octubre", "11":"noviembre", "12":"diciembre" }  

print "\n==> This script started running on", strftime("%a %b %d"), "at", strftime("%H:%M:%S"), 

while True:
    # defines when the operation will happen (production)
    #if time.strftime("%H") == "8" and time.strftime("%M") == "00":    
       
        # where the content is coming from
        url = "http://especiales.prensalibre.com/PDFs/Ediciones/" + str(strftime("%Y")) + "/" + monthsOfTheYear[str(strftime("%m"))]+ "/" + str(strftime("%d")) + "/PDFs/PLMT" + str(strftime("%d%m%Y")) + ".pdf"

        # file download
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "\n===> Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,

        f.close()
        print "\n====> Done dowloading Prensa Libre for,",strftime("%a %b %d"),"\n=====> The task finished on ",strftime("%a, %b %d %Y"), "at", strftime("%H:%M:%S"), 
        
        # moving file
        dir_src = "/path/to/file/"
        dir_dst = "/path/to/file/" 

        fileName = file_name

        print "======> Done moving", fileName, "to Downloads."
        src_file = os.path.join(dir_src, fileName)
        dst_file = os.path.join(dir_dst, fileName)
        shutil.move(src_file, dst_file)
        
        # open file
        os.system("open /path/to/file/" + fileName)

        # time (in seconds) that the script will be paused/ sllep
        time.sleep(30)





        



            
