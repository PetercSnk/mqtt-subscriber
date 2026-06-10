import time
from threading import Event

from sqlalchemy import select

from app.extensions import mqtt, scheduler, db
from app.models.subscribe import Topic
from app.subscribe.systems import on, off

event = Event()


@mqtt.on_message()
def messageHandler(client, userdata, message):
    """MQTT message handler. Starts job if the payload is suitable and no jobs
    are already running. The job can be cancelled if the message zero is
    received.
    """
    payload = message.payload.decode()
    mqtt.app.logger.info("Message received: {}".format(payload))
    try:
        intPayload = int(payload)
    except (TypeError, ValueError) as error:
        mqtt.app.logger.error("Error with conversion: {}".format(error))
        return
    
    with mqtt.app.app_context():
        topic = db.session.execute(select(Topic)).scalar_one_or_none()
        
    if intPayload > 0 and not topic.runStatus:
        scheduler.add_job(func=process, id=topic.name, name=topic.name,
                            args=[intPayload])
    elif intPayload == 0 and topic.runStatus:
        event.set()
    else:
        mqtt.app.logger.info("Cannot execute or cancel at this time.")


def process(timeSeconds):
    """Toggles the physical system using the on and off functions. What these
    functions do can be changed freely within the systems file.
    """
    with scheduler.app.app_context():
        topic = db.session.execute(select(Topic)).scalar_one_or_none()
        topic.setRunStatus(True)
        on()
        waitSeconds(timeSeconds)
        off()
        topic.setRunStatus(False)


def waitSeconds(timeSeconds):
    for i in range(timeSeconds):
        time.sleep(1)
        if event.is_set():
            event.clear()
            return
