# S3 File Copy Lambda

This AWS Lambda function facilitates the seamless transfer of files from one S3 bucket to another, allowing for organized storage and efficient data management. The function is designed to be triggered by events, ensuring timely and automated file copying.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

- Lists objects in the source S3 bucket.
- Copies each object to the destination S3 bucket with a specified folder structure.

## Prerequisites

Ensure that you have the necessary AWS credentials set up to interact with S3.

## Setup

1. **Environment Variable Configuration:**

   - Set the following environment variables in the Lambda console or directly in the code:
     - `SourceBucketName`: Name of the source S3 bucket.
     - `DestinationBucketName`: Name of the destination S3 bucket.
     - `Folder`: The folder structure to be applied in the destination bucket.

2. **Lambda Function Deployment:**

   - Deploy the Lambda function for file copying.

## Usage

This Lambda function is triggered by S3 events. Upon triggering, it lists objects in the source bucket and copies them to the destination bucket with the specified folder structure.

## Environment Variables

- **`SourceBucketName`**: Name of the source S3 bucket.
- **`DestinationBucketName`**: Name of the destination S3 bucket.
- **`Folder`**: The folder structure to be applied in the destination bucket.

  Example:

  ```plaintext
  SourceBucketName=mySourceBucket
  DestinationBucketName=myDestinationBucket
  Folder=my/folder/structure/
  ```

## Dependencies

- `boto3`: AWS SDK for Python

## Contributing

Feel free to contribute by reporting issues or submitting pull requests.

## License

This S3 File Copy Lambda is licensed under the [MIT License](LICENSE).
