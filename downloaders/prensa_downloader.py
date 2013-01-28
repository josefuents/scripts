#this script will download, move to 'Download' and open every day Prensa Libre at a predetermined time
import urllib2, time, os, shutil, glob
from time import strftime

# script running start time
print "\n=> This script started running on", strftime("%a %b %d"), "at", strftime("%H:%M:%S") 

#months dictionary
monthsOfTheYear = { "01":"enero", "02":"febrero", "03":"marzo", "04":"abril", "05":"mayo", "06":"junio", "07":"julio", "08":"agosto", "09":"septiembre", "10":"octubre", "11":"noviembre", "12":"diciembre" }  

# moving file: origin file and destination file
dir_src = "/Users/jose/Dropbox/cs/python/downloaders/"
dir_dst = "/Users/jose/Downloads/" 

def prensaLibreDown():
    while True:
     
        # defines when the operation will happen (production)
        while time.strftime("%H") == "08" and time.strftime("%M") == "00":

        # defines when the operation will happen (testing)
        #while time.strftime("%H") == "13" and time.strftime("%M") == "07":
    
            # url where the content is coming from
            url = "http://especiales.prensalibre.com/PDFs/Ediciones/" + str(strftime("%Y")) + "/" + monthsOfTheYear[str(strftime("%m"))]+ "/" + str(strftime("%d")) + "/PDFs/PLMT" + str(strftime("%d%m%Y")) + ".pdf"

            # its the weekend
            if time.strftime("%a") in ("Sat","Sun"):
                print "\n **  It's the weekend - we'll be back on Monday - today is",strftime("%a, %b %d %Y."), "time:", strftime("%H:%M:%S"),"**\n" 
                time.sleep(60)
                continue
                            
            # the file is already downloaded
            if dir_dst + url.split('/')[-1] in glob.glob(dir_dst + 'PLMT????????.pdf'):
                print "\n >>>>> The file", url.split('/')[-1], "is already downloaded. Attempt at:", strftime("%H:%M:%S"),"<<<<<\n" 
                time.sleep(60)
                continue
            
            else:   
                # start timer
                print "\n==> The task started on ",strftime("%a, %b %d %Y"), "at", strftime("%H:%M:%S"), 

                # url where the content is coming from
                url = "http://especiales.prensalibre.com/PDFs/Ediciones/" + str(strftime("%Y")) + "/" + monthsOfTheYear[str(strftime("%m"))]+ "/" + str(strftime("%d")) + "/PDFs/PLMT" + str(strftime("%d%m%Y")) + ".pdf"

                # file download
                file_name = url.split('/')[-1]
                u = urllib2.urlopen(url)
                f = open(file_name, 'wb')
                meta = u.info()
                file_size = int(meta.getheaders("Content-Length")[0])
                print "\n===> Downloading: %s Bytes: %s" % (file_name, file_size),
    
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
                
                # file movement from 'dir_src' to 'dir_dst'
                print "\n======> Done moving", file_name, "to Downloads.\n"
                src_file = os.path.join(dir_src, file_name)
                dst_file = os.path.join(dir_dst, file_name)
                shutil.move(src_file, dst_file)
         
                # open file
                os.system("open " + dir_dst + file_name)

                # time (in seconds) that the script will be paused/ sllep
                time.sleep(60)


prensaLibreDown()









        



            
