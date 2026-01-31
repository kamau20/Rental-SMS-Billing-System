import africastalking
from django.conf import settings
from .models import SMSLog

africastalking.initialize(
    settings.AFRICASTALKING_USERNAME,
    settings.AFRICASTALKING_API_KEY
)

sms = africastalking.SMS

def send_sms(tenant, message):
    try:
        response = sms.send(message, [tenant.phone])

        SMSLog.objects.create(
            tenant=tenant,
            phone=tenant.phone,
            message=message,
            status="SENT"
        )
        print(response)

    except Exception as e:
        SMSLog.objects.create(
            tenant=tenant,
            phone=tenant.phone,
            message=message,
            status="FAILED"
        )
        print(str(e))
