from flask import Flask   # type: ignore
app=Flask(__name__)

app.secret_key="key243"
DATABASE = "friends-schema"