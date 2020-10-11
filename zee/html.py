htm = """
    <!DOCTYPE html>
        <html>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title> {} </title>
        <body>
            <div align = "center">
                <body style="background-color:black;">
                    <div id = "img" align = "center">
                        <img src = '{}'/>
                    </div>
                    <div id = "text" style = "color:grey">
                        {}  ¤ {}
                            <p <b> Rating : {} | Duration : {} secs</b></br></br>
                        {} </b></p></br>
                    </div>
            <button onclick="document.location='{}'">play</button>
            </div>
        </body>
        </html>
    """
