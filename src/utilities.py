from time import sleep
import gc

def get_instances(cls):
    if not cls:
        return 0

    instances = []
    for obj in gc.get_objects():
        if isinstance(obj, cls):
            instances.append(obj)
    return instances

def send_sms(target, alert):
    return {
        'To: ': target,
        'Alert: ': alert_id,
        'Service: ': alert.svc_id,
        'Message: ': alert.message,
    }

def send_email(target, alert):
    return {
        'To: ': target,
        'Alert: ': alert_id,
        'Service: ': alert.svc_id,
        'Message: ': alert.message,
    }

def set_timeout(timeout):
    sleep(timeout)