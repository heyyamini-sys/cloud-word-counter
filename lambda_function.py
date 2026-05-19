import json
import os
from datetime import datetime
from pymongo import MongoClient

# Get the connection string from AWS Environment Variables
mongo_uri = os.environ.get('MONGO_URI')
client = MongoClient(mongo_uri)

db = client['WordCounterDB']
collection = db['Requests']

import json

def lambda_handler(event, context):
    body = json.loads(event['body'])
    text = body.get('text', '')
    
    word_count = len(text.split())
    char_count = len(text)
    
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",   # ← CORS fix
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "words": word_count,
            "characters": char_count
        })
    }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }