from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TopicForm(FlaskForm):
    """Form for Flask. Used for subscribing to topics.
    """
    name = StringField("Name", validators=[DataRequired(), Length(max=16)])
    submit = SubmitField("Subscribe")
