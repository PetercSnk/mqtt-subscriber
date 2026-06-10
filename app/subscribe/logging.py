from apscheduler.events import (
    EVENT_JOB_ADDED,
    EVENT_JOB_REMOVED,
    EVENT_JOB_EXECUTED,
    EVENT_JOB_ERROR
)

from app.extensions import mqtt, scheduler


@mqtt.on_connect()
def connectHandler(client, userdata, flags, rc):
    mqtt.app.logger.info("Connected to: {}".format(mqtt.broker_url))


@mqtt.on_disconnect()
def disconnectHandler():
    mqtt.app.logger.warning("Disconnected from: {}".format(mqtt.broker_url))


@mqtt.on_subscribe()
def subscribeHandler(client, userdata, mid, granted_qos):
    mqtt.app.logger.warning("Subscription id: {}".format(mid))


@mqtt.on_unsubscribe()
def unsubscribeHandler(client, userdata, mid):
    mqtt.app.logger.warning("Unsubscription id: {}".format(mid))


def jobAddedHandler(event):
    scheduler.app.logger.warning("Added job: {}".format(event.job_id))


def jobRemovedHandler(event):
    scheduler.app.logger.warning("Removed job: {}".format(event.job_id))


def jobExecutedHandler(event):
    scheduler.app.logger.info("Executed job: {}".format(event.job_id))


def jobErrorHandler(event):
    scheduler.app.logger.error("Error with job: {}".format(event.job_id))


scheduler.add_listener(jobAddedHandler, EVENT_JOB_ADDED)
scheduler.add_listener(jobRemovedHandler, EVENT_JOB_REMOVED)
scheduler.add_listener(jobExecutedHandler, EVENT_JOB_EXECUTED)
scheduler.add_listener(jobErrorHandler, EVENT_JOB_ERROR)
