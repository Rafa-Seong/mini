from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>입력 출력 웹앱</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 40px;
      }
      label,
      p {
        font-size: 1.1rem;
      }
      input[type=text] {
        width: 320px;
        padding: 8px;
        margin-right: 8px;
      }
      button {
        padding: 8px 16px;
      }
    </style>
  </head>
  <body>
    <h1>입력한 내용을 화면에 출력</h1>
    <form method="post">
      <label>텍스트 입력:
        <input type="text" name="message" placeholder="여기에 입력하세요" value="{{ message|e }}">
      </label>
      <button type="submit">전송</button>
    </form>
    {% if message %}
      <p>입력한 내용: <strong>{{ message|e }}</strong></p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = request.form.get("message", "")
    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(debug=True)
