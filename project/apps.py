from django.apps import AppConfig
from tensorflow.keras.models import load_model


class ProjectConfig(AppConfig):
    name = "project"


class DLModelConfig(AppConfig):
    name = "path_loss_predction_model"
    DLModel = load_model("./project/static/DLModel/20_20_100_v1_0510_jh1.h5")
