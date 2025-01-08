from core.application import Application
from bootstrap.bootstrap import Bootstrap


app = Application()
Bootstrap()


def lambda_handler(aws_event, context):
    response = app.handle(aws_event, context)
    return response


if __name__ == "__main__":
    event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/simple",
        "rawQueryString": "",
        "headers": {
            "x-amzn-tls-cipher-suite": "TLS_AES_128_GCM_SHA256",
            "content-length": "22",
            "x-amzn-tls-version": "TLSv1.3",
            "x-amzn-trace-id": "Root=1-6765b741-680ee625200e1c88417498d0",
            "x-forwarded-proto": "https",
            "host": "lsrlngbwlypzxdbniilj5xuslu0lgahf.lambda-url.ap-south-1.on.aws",
            "x-forwarded-port": "443",
            "content-type": "application/json",
            "x-forwarded-for": "49.47.157.56",
            "accept-encoding": "gzip, deflate, br",
            "accept": "*/*",
            "user-agent": "Thunder Client (https://www.thunderclient.com)"
        },
        "requestContext": {
            "accountId": "anonymous",
            "apiId": "lsrlngbwlypzxdbniilj5xuslu0lgahf",
            "domainName": "lsrlngbwlypzxdbniilj5xuslu0lgahf.lambda-url.ap-south-1.on.aws",
            "domainPrefix": "lsrlngbwlypzxdbniilj5xuslu0lgahf",
            "http": {
                "method": "POST",
                "path": "/simple",
                "protocol": "HTTP/1.1",
                "sourceIp": "49.47.157.56",
                "userAgent": "Thunder Client (https://www.thunderclient.com)"
            },
            "requestId": "91bac5af-e621-4586-8a0d-e90185a0339e",
            "routeKey": "$default",
            "stage": "$default",
            "time": "20/Dec/2024:18:28:17 +0000",
            "timeEpoch": 1734719297474
        },
        "body": "{\n  \"name\": \"Ritwik\", \"fullname\": \"Ritwik Math\"\n}",
        "isBase64Encoded": False
    }
    print(lambda_handler(event, {}))
