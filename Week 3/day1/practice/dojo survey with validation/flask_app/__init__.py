from flask import Flask, render_template, redirect, request, session, flash
DB = "dojo_survey_schema"

app = Flask(__name__)
app.secret_key = "ssssssssssssss"