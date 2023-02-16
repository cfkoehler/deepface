# 3rd parth dependencies
from flask import Flask
from routes import blueprint

from deepface.DeepFace import build_model


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    # TODO: Setup loading models so it does not need to happen on first call
    models = setup()
    return app


def setup():
    models = {}
    models["emotion"] = build_model("Emotion")
    models["age"] = build_model("Age")
    models["gender"] = build_model("Gender")
    models["race"] = build_model("Race")
    return models
