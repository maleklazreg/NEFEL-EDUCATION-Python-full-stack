from flask import Flask # type: ignore
DB="dojo_survey_schema"

app=Flask(__name__)
app.secret_key="cench23"
