import sys
def handler(event, context):
    return 'Hello from KodeKloud with AWS Lambda using Python' + sys.version + '!'
