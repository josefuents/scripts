import urllib2, time, os, shutil 
from time import strftime

while True:
    # defines when the operation will happen
    #if time.strftime("%a") == "Mon" and time.strftime("%H") == "13" and time.strftime("%M") == "46":

        iniCount = 369
        count = 0
        while True:
            count += 1

            # where the content is coming from
            url = "http://dts.podtrac.com/redirect.mp4/twit.cachefly.net/video/twit/twit0" + str(iniCount + count) + "/twit0" + str(iniCount + count) + "_h264m_864x480_500.mp4"
            
            # file download
            file_name = url.split('/')[-1]
            u = urllib2.urlopen(url)
            f = open(file_name, 'wb')
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            print "Downloading: %s Bytes: %s" % (file_name, file_size)

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
            print "****************************************************\n Done dowloading the Twit episode for Monday,",strftime("%b %d"),"\n \n The task finished at ",strftime("%a, %d %b %Y %H:%M:%S"), "\n****************************************************"

            # moving file
            dir_src = "/Users/jose/Desktop/aa/"
            dir_dst = "/Users/jose/Downloads/" 

            fileName = file_name

            print "Dene moving file", fileName, "to Downloads."
            src_file = os.path.join(dir_src, fileName)
            dst_file = os.path.join(dir_dst, fileName)
            shutil.move(src_file, dst_file)

             # open file
            os.system("open /Users/jose/Downloads/" + fileName)

            # time (in seconds) that the script will be paused/ sllep
            time.sleep(86400)



       
