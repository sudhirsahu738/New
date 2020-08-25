import re
import sys
import argparse
import requests
import bs4

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--premiere", help="To download upcoming shows from Zee5", action="store_true")
    parser.add_argument("-s", "--previous", help="To downloads old shows", action="store_true")
    parser.add_argument("-q", help="Quality option", action="store_true")
    args, unknown = parser.parse_known_args()
def shows():
    try:
        usage()
        if sys.argv[1] == "-p" or "--premiere":
            gt_link = sys.argv[2]
            get_request = requests.get(gt_link)
            response_parse = bs4.BeautifulSoup(get_request.content, 'html5lib')
            clt_response = response_parse.find_all("script")[9].prettify()
            url = []
            for i in clt_response.split(','):
                if "hls" in i:
                    url.append(i)
            re = ((url[-1])[11:-1].replace("drm", "hls"))
            rt = (str("https://{}".format("zee5vod.akamaized.net") + re))
            return rt
        elif sys.argv[1] == "-s" or "--previous":
            get_link = sys.argv[2]
            request = requests.get(get_link)
            parse = bs4.BeautifulSoup(request.content, 'html5lib')
            parz_resp = parse.find_all("script")[9].prettify()
            urls = []
            for _ in parz_resp.split(','):
                if "hls" in _:
                    urls.append(_)
            re1 = (urls[-1][11:-1])
            re2 = (re1 + tk_m3u)
            return re2
        else:
            pass
    except IndexError:
        print("Usage : python3 shows.py -h, --help")
        
def main():
    try:
        usage()
        if "index.m3u8" in shows():
            gt_pix = sys.argv[4]
            X3 = (shows()[:-10])
            er = requests.get(shows())
            D = []
            pz = re.findall("index.*", er.text)
            D.append(pz)
            if gt_pix == "96":
                print(X3 + D[0][0])
            elif gt_pix == "144":
                print(X3 + D[0][1])
            elif gt_pix == "240":
                print(X3 + D[0][2])
            elif gt_pix == "360":
                print(X3 + D[0][3])
            elif gt_pix == "480":
                print(X3 + D[0][4])
            elif gt_pix == "570":
                print(X3 + D[0][5])
            elif gt_pix == "720":
                print(X3 + D[0][6])
            elif gt_pix == "1080":
                print(X3 + D[0][7])
            else:
                print('check your quality option')
        elif "master.m3u8" in shows():
            X2 = (shows()[29:-11])
            req_tk = requests.get("https://useraction.zee5.com/token/")
            resp_tk = req_tk.content.decode('utf-8')
            token = (eval(resp_tk)["video_token"])
            get_pix = sys.argv[4]
            X4 = (shows()[29:] + token)
            Req = requests.get(X4)
            G = []
            Re = re.findall("index.*", Req.text)
            G.append(Re)
            if get_pix == "144":
                print(X2 + G[0][0])
            elif get_pix == "240":
                print(X2 + G[0][1])
            elif get_pix == "360":
                print(X2 + G[0][2])
            elif get_pix == "480":
                print(X2 + G[0][3])
            else:
                print("check your quality ...")
    except IndexError:
        print("Usage : python3 shows.py {p}/{s} <link> -q <pixel>")
    except TypeError:
        print('\n Run help ( -h , --help) ')
        
if __name__ == "__main__":
    main()
