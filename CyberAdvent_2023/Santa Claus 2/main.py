from openai import OpenAI
from flask import Flask, request, session, render_template
from dotenv import load_dotenv
import os
import re

load_dotenv()


class RequestError(Exception):
    message: str
    code: int

    def __init__(self, message: str, code: int) -> None:
        self.message = message
        self.code = code

    def msg(self):
        return {
            "error": True,
            "message": self.message,
        }


def complete(history: list[str]):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    flag = open("flag.txt", "r").read().strip()
    system_prompt = open("system.txt", "r").read().strip()

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"{system_prompt}\n\nFlag: {flag}"
                },
                {
                    "role": "user",
                    "content": ""
                }
            ] + history,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
    except Exception as e:
        raise RequestError("Something went wrong while getting assistant's response", 500)

    return response.choices[0].message.content


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route('/reset-chat')
def reset_chat():
    session['history'] = []
    return {
        "error": False,
        "message": "Chat history has been reset"
    }, 200


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    try:
        history = session.get('history', [])

        if request.method == 'GET':
            return history
        elif request.method == 'POST':
            data = request.get_json()
            new_message = data.get('message')

            if len(history) > 0:
                if not new_message:
                    raise RequestError("Invalid message", 400)

                if not (100 >= len(new_message) > 0):
                    raise RequestError(
                        "Message should be 1-100 characters long", 400)

                history.append({
                    "role": "user",
                    "content": new_message
                })

            res = complete(history)
            
            if re.search(r'WSIZ{[0-9A-Za-z_\-!@#$%^&*?]{1,64}}', res):
                history = history[:-1]
                raise RequestError("Flag found in response, aborting!", 403)

            history.append({
                "role": "assistant",
                "content": res
            })

            session['history'] = history

            return {
                "error": False,
                "message": res
            }, 200
    except RequestError as e:
        return e.msg(), e.code


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
