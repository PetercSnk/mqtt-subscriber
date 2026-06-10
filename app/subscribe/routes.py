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
