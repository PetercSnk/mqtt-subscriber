import os.path

from flask import render_template, request, redirect, url_for
from sqlalchemy import select

from app.models.subscribe import Topic
from app.subscribe.forms import TopicForm
from app.subscribe import subscribe
from app.extensions import db, mqtt


@subscribe.route("/", methods=["GET", "POST"])
def index():
    """Route for Flask. Displays the topic currently subscribed to and allows
    for it to be changed.
    """
    form = TopicForm()
    topic = db.session.execute(select(Topic)).scalar_one_or_none()
    if request.method == "POST" and form.validate():
        mqtt.unsubscribe_all()
        name = form.name.data
        if topic is not None:
            topic.name = name
        else:
            newTopic = Topic(name=name)
            db.session.add(newTopic)
        db.session.commit()
        mqtt.subscribe(name)
        return redirect(url_for(".index"))
    return render_template("subscribe/index.html", form=form, topic=topic)

@subscribe.route("/logs", defaults={"id": 0})
@subscribe.route("/logs/<int:id>", methods=["GET"])
def logs(id):
    """Route for Flask. Displays logging messages.
    """
    file = "./logs/app.log"
    content = ""
    maxBackups = 5
    ids = [n for n in range(maxBackups)]
    if id > 0:
        file += ("." + str(id))
    if os.path.isfile(file):
        with open(file) as f:
            content = f.read()
    return render_template("subscribe/logs.html", content=content, ids=ids)
