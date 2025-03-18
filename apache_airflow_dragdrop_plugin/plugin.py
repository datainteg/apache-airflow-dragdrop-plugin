from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, send_from_directory, render_template
from flask_appbuilder import BaseView, expose
import os

# Get Plugin Directory
PLUGIN_DIR = os.path.dirname(__file__)

# Define Flask Blueprint
react_bp = Blueprint(
    "apache_airflow_dragdrop_plugin",
    __name__,
    static_folder=os.path.join(PLUGIN_DIR, "static"),
    template_folder=os.path.join(PLUGIN_DIR, "templates")
)

# Serve static assets (JS, CSS, images)
@react_bp.route("/drag-drop/static/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory(os.path.join(PLUGIN_DIR, "static/assets"), filename)

@react_bp.route("/drag-drop/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(os.path.join(PLUGIN_DIR, "static"), filename)


@react_bp.route("/drag-drop")
def serve_react():
    return render_template("index.html")


class ReactView(BaseView):
    default_view = "react"

    @expose("/")
    def react(self):
        return self.render_template("index.html")

# Register Plugin
class MyReactPlugin(AirflowPlugin):
    name = "apache_airflow_dragdrop_plugin"
    flask_blueprints = [react_bp]
    appbuilder_views = [
        {
            "name": "Drag and Drop",
            "category": "Custom Plugins",
            "view": ReactView(),
            "href": "/drag-drop/",
        }
    ]
