import sys, bs4, requests, argparse
def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--M", help="For Movies and Zee5 originals", action="store_true")
    args, unknown = parser.parse_known_args()
def movies():
    try:
        usage()
        if "-z" or "--Z" in sys.argv[1]:
            if "movies" in sys.argv[2]:
                try:
                    usage()
                    get_request = requests.get(sys.argv[2])
                    response_parse = bs4.BeautifulSoup(get_request.content, 'html5lib')
                    token = requests.get("http://useraction.zee5.com/tokennd/").json()
                    clt_response = response_parse.find_all("script")[9].prettify()
                    Q = []
                    for i in clt_response.split(","):
                        if "hls" in i:
                            Q.append(i)
                    pr = (str(Q[1])[11:-1].replace("drm","hls"))
                    print("https://{}".format("zee5vodnd.akamaized.net") + pr + token["video_token"])
                except IndexError:
                    print("try again..")
            elif "zee5originals" in sys.argv[2]:
                req = requests.get(sys.argv[2])
                resp = bs4.BeautifulSoup(req.content, 'html5lib')
                token = requests.get("http://useraction.zee5.com/tokennd/").content.decode()
                parse = resp.find_all("script")[9].prettify()
                A = []
                for _ in parse.split(","):
                    if "hls" in _:
                        A.append(_)
                z5 = (str(A[-1])[11:-1].replace("drm", "hls"))
                print("https://zee5vodnd.akamaized.net{}{}".format(z5, eval(token)["video_token"]))
            else:
                print("Invalid url")
        else:
            print("Invalid Tag")
    except IndexError:
        print("[*] Run Python3 mov5.py -h")
    except KeyboardInterrupt:
        print("Closing")
if __name__ == "__main__":
    movies()
