
from flask import Flask

app = Flask(__name__)

@app.route("/")
def blog():

    return """
    <html>
    <head>
        <title>My Personal Blog</title>

        <style>
            body {
                font-family: Arial;
                background-color: lightblue;
                margin: 20px;
            }

            h1 {
                color: darkblue;
                text-align: center;
            }

            h2 {
                color: green;
            }

            .content {
                background-color: white;
                padding: 20px;
                margin: 15px;
                border-radius: 10px;
            }

            a {
                color: blue;
            }
        </style>
    </head>

    <body>

        <h1>MY PERSONAL BLOG</h1>
        <p align="center">Welcome to My Educational Website</p>

        <hr>

        <div class="content">

            <h2>Home</h2>
            <p>Welcome to my blog website.
            This website demonstrates basic HTML tags.</p>

            <h2>1. Title Tag</h2>
            <p>The title tag displays the webpage name
            on the browser tab.</p>

            <h2>2. Anchor Tag</h2>
            <p>Anchor tags are used to create hyperlinks.</p>

            <a href="https://www.google.com"
            title="Open Google Website">
            Visit Google
            </a>

            <h2>3. Heading Tags</h2>
            <h1>Heading 1</h1>
            <h2>Heading 2</h2>
            <h3>Heading 3</h3>

            <h2>4. Paragraph Tag</h2>
            <p>This is an example of a paragraph.</p>

            <h2>5. Image Tag</h2>
            <img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"
            alt="HTML Logo" width="150">

            <h2>6. Bold and Italic Tags</h2>
            <b>This is bold text.</b>
            <br>
            <i>This is italic text.</i>

            <h2>7. List Tags</h2>
            <ul>
                <li>HTML</li>
                <li>CSS</li>
                <li>Python</li>
            </ul>

            <h2>8. Contact</h2>
            <p>Email: example@gmail.com</p>

            <a href="mailto:example@gmail.com"
            title="Send an Email">Contact Us</a>

        </div>

        <hr>

        <center>
            <p>Copyright 2026 My Personal Blog</p>
        </center>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
