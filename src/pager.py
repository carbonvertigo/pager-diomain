from utilities import  *
from escalationPolicy import *

class Pager:

    def _policies(self):
        policies = get_instances(EscalationPolicy)
        return policies

    def fetch_policy_svc(self):
        policy_svcs = {}
        for policy in self._policies():
            policy_svcs[policy] = policy.svc_id
        return policy_svcs

    def fetch_policy(self, alert_svc):
        for i, n in enumerate(self.fetch_policy_svc()):
            if n == alert_svc:
                return i
                break

    def _alerts(self):
        alerts = get_instances(Alert)
        return alerts

    def fetch_alert_svc(self):
        alert_svcs = {}
        for alert in self._alerts():
            alert_svcs[alert] = alert.svc_id
        return alert_svcs

    def fetch_alert(self, alert_svc):
        for i, n in enumerate(self.fetch_alert_svc()):
            if n == alert_svc:
                return i
                break

    def notify(self, alert_svc):
        timeout = (15 * 60)
        alert = self.fetch_alert(alert_svc)
        levels = self.fetch_policy(alert_svc).levels
        for targets in levels:
            for tgt in targets:
                if tgt.comm_type == 'sms':
                    send_sms(tgt.comm_link, alert)
                elif tgt.comm_type == 'email':
                    send_email(tgt.comm_link, alert)
                else:
                    raise ValueError('Input DNA sequence to communicate with this target')
            set_timeout(timeout)

            alert_status = alert.status()
            if alert_status == 1:
                break