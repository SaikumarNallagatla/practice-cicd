def lambda_handler(event=None, context=None):
    return {
        'statusCode': 200,
        'body': 'Hello from DevOps Baby!'
    }

if __name__ == "__main__":
    print("Deploy to S3 test successful!")
