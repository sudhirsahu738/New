import flask
import re
import sys
from g import htm
import requests
from headers import headers
import urls
import socketserver
a = flask.Flask(__name__)
@a.route('/')
def home():
    return flask.render_template("c/home.html")    
@a.route("/", methods=["GET", "POST"])
def post():
    l = flask.request.form["q"]
    if flask.request.method == "POST":
        with open("_", "wb") as a1:
            a1.write(bytes(l.encode()))
    return flask.render_template("c/home.html") and flask.redirect("/content/play")
@a.route('/about')
def about():
    return flask.render_template("x/about.html")
@a.route("/contact")
def contact():
    return flask.render_template("z/contact.html")
@a.route("/favicon.ico")
def con():
    return flask.render_template("v/ico.html")
@a.route("/content/play")
def api():   
    with open("_", 'r') as q1:
        try:
            w = q1.read()
            req1 = requests.get(urls.token_url1, headers=headers).json()
            rgx = re.findall("([0-9]?\w+)", w)[-3:]
            req2 = requests.get(urls.platform_token).json()["token"]
            headers["X-Access-Token"] = req2
            req3 = requests.get(urls.token_url2, headers=headers).json()
            if "movies" in w:
                r1 = requests.get(urls.search_api_endpoint + "-".join(rgx),
                                            headers=headers, 
                                            params={"translation":"en", "country":"IN"}).json()
                g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
                return htm.format(r1["title"], r1["image_url"], r1["title"], r1["age_rating"],
                                r1["rating"], r1["duration"], r1["description"],
                                urls.stream_baseurl + g1)
            elif "tvshows" or "originals" in w:
                r2 = requests.get(urls.search_api_endpoint + "-".join(rgx), 
                                            headers=headers, 
                                            params={"translation":"en", "country":"IN"}).json()
                g2 = (r2["hls"][0].replace("drm", "hls"))
                g3 = urls.stream_baseurl + g2 + req1["video_token"]
                s = requests.Session()
                if "netst" in g2:
                    aq1 = s.get(g2 + req3["video_token"], headers=headers)
                    c1 = re.findall("index.*", aq1.text)
                    h1 = re.findall("([a-z]\w+)", g2)[-2:]
                    h2 = g2.replace(".".join(h1), "")
                    if sys.argv[1] == "144p":
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                          r2["rating"], r2["duration"], r2["description"], h2 + c1[1])
                    elif sys.argv[1] == "240p":
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                        r2["rating"], r2["duration"], r2["description"], h2 + c1[2])
                    elif sys.argv[1] == "360p":
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                        r2["rating"], r2["duration"], r2["description"], h2 + c1[3])
                elif "Ep" in g2:
                    aq2 = s.get(urls.stream_baseurl + g2 + req1["video_token"], headers=headers)
                    c = re.findall("index.*", aq2.text)
                    d = g3.replace(re.findall("\?.*", g3)[0], "")
                    if sys.argv[1] == "96p":
                        e = d.replace("index.m3u8", c[0])
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                                    r2["rating"], r2["duration"], r2["description"], e)
                    elif sys.argv[1] == "144p":
                        e1 = d.replace("index.m3u8", c[1])
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                                    r2["rating"], r2["duration"], r2["description"], e1)
                    elif sys.argv[1] == "240p":
                        e2 = d.replace("index.m3u8", c[2])
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                                    r2["rating"], r2["duration"], r2["description"], e2)
                    elif sys.argv[1] == "360p":
                        e3 = d.replace("index.m3u8", c[3])
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                                    r2["rating"], r2["duration"], r2["description"], e3)
                    elif sys.argv[1] == "480p":
                        e4 = d.replace("index.m3u8", c[4])
                        return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"],
                                                    r2["rating"], r2["duration"], r2["description"], e4)
                    else:
                        return {"Message":"Requested Quality not Available !!"}
                else:
                    return htm.format(r2["title"], r2["image_url"], r2["title"], r2["age_rating"], 
                                    r2["rating"], r2["duration"], r2["description"], 
                                    urls.stream_baseurl + g2 + req1["video_token"])
            else:
                pass
        except IndexError:
            return flask.jsonify({ "Message" : "No Quality specified", "List of Qualities":["96, 144, 240, 360, 480"], "Sample":["run python3 zee5.py 144p"] }), 200
        except requests.exceptions.ConnectionError:
            return flask.jsonify({ "Message" : "No connection" , "Stat" : "Internet Connection is required for stream"})
        except KeyError:
            return { "Message" : "No Url Specified" }, 200
if __name__ == "__main__":
    a.run("127.0.0.1", 8080, debug=True)
