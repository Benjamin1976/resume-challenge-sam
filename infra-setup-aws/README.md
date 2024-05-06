sam build && sam deploy --no-confirm-changeset --no-fail-on-empty-changeset --s3-bucket benjamins-resume-challenge-testing --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --region us-east-1 --role-arn arn:aws:iam::656129116436:role/awsCloudFormationCLIRole --stack-name benjamins-resume-challenge-testing013

sam build -t create.yml && sam deploy -t create.yml --no-confirm-changeset --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --region us-east-1 --role-arn arn:aws:iam::656129116436:role/awsCloudFormationCLIRole --s3-bucket benjamins-resume-challenge-testing --stack-name benjamins-resume-challenge-testing018

sam build -t modify.yml && sam deploy -t modify.yml --no-confirm-changeset --no-fail-on-empty-changeset --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND --region us-east-1 --role-arn arn:aws:iam::656129116436:role/awsCloudFormationCLIRole --s3-bucket benjamins-resume-challenge-testing --stack-name benjamins-resume-challenge-testing018

sam build -t create.yml && sam deploy -t create.yml
sam build -t modify.yml && sam deploy -t modify.yml

Resume Challenge

1. Certification
   Your resume needs to have the AWS Cloud Practitioner certification on it. This is an introductory certification that orients you on the industry-leading AWS cloud – if you have a more advanced AWS cert, that’s fine but not expected. You can sit this exam online for $100 USD.

NEW: Pluralsight, a Cloud Resume Challenge sponsor, has a helpful Cloud Practitioner prep course. They’ve given us a special 30-day free trial of their Premium plan, which should be enough time to study for and pass the exam - use this link to get your free 30 days.

2. HTML
   Your resume needs to be written in HTML. Not a Word doc, not a PDF. Here is an example of what I mean.

3. CSS
   Your resume needs to be styled with CSS. No worries if you’re not a designer – neither am I. It doesn’t have to be fancy. But we need to see something other than raw HTML when we open the webpage.

4. Static Website
   Your HTML resume should be deployed online as an Amazon S3 static website. Services like Netlify and GitHub Pages are great and I would normally recommend them for personal static site deployments, but they make things a little too abstract for our purposes here. Use S3.

5. HTTPS
   The S3 website URL should use HTTPS for security. You will need to use Amazon CloudFront to help with this.

6. DNS
   Point a custom DNS domain name to the CloudFront distribution, so your resume can be accessed at something like my-c00l-resume-website.com. You can use Amazon Route 53 or any other DNS provider for this. A domain name usually costs about ten bucks to register.

7. Javascript
   Your resume webpage should include a visitor counter that displays how many people have accessed the site. You will need to write a bit of Javascript to make this happen. Here is a helpful tutorial to get you started in the right direction.

8. Database
   The visitor counter will need to retrieve and update its count in a database somewhere. I suggest you use Amazon’s DynamoDB for this. (Use on-demand pricing for the database and you’ll pay essentially nothing, unless you store or retrieve much more data than this project requires.) Here is a great free course on DynamoDB.

9. API
   Do not communicate directly with DynamoDB from your Javascript code. Instead, you will need to create an API that accepts requests from your web app and communicates with the database. I suggest using AWS’s API Gateway and Lambda services for this. They will be free or close to free for what we are doing.

10. Python
    You will need to write a bit of code in the Lambda function; you could use more Javascript, but it would be better for our purposes to explore Python – a common language used in back-end programs and scripts – and its boto3 library for AWS. Here is a good, free Python tutorial.

11. Tests
    You should also include some tests for your Python code. Here are some resources on writing good Python tests.

12. Infrastructure as Code
    You should not be configuring your API resources – the DynamoDB table, the API Gateway, the Lambda function – manually, by clicking around in the AWS console. Instead, define them in an AWS Serverless Application Model (SAM) template and deploy them using the AWS SAM CLI. This is called “infrastructure as code” or IaC. It saves you time in the long run.

Note: A more broadly applicable and commonly-used IaC tool in the industry is Terraform. It’s a little less straightforward to use than SAM for an AWS serverless API, but many people prefer to use it for their project anyway. If you want to use Terraform instead of SAM, follow this guide.

13. Source Control
    You do not want to be updating either your back-end API or your front-end website by making calls from your laptop, though. You want them to update automatically whenever you make a change to the code. (This is called continuous integration and deployment, or CI/CD.) Create a GitHub repository for your backend code.

14. CI/CD (Back end)
    Set up GitHub Actions such that when you push an update to your Serverless Application Model template or Python code, your Python tests get run. If the tests pass, the SAM application should get packaged and deployed to AWS.

15. CI/CD (Front end)
    Create a second GitHub repository for your website code. Create GitHub Actions such that when you push new website code, the S3 bucket automatically gets updated. (You may need to invalidate your CloudFront cache in the code as well.) Important note: DO NOT commit AWS credentials to source control! Bad hats will find them and use them against you!

16. Blog post
    Finally, in the text of your resume, you should link a short blog post describing some things you learned while working on this project. Dev.to or Hashnode are great places to publish if you don’t have your own blog.

And that’s the gist of it! For strategies, tools, and further challenges to help you get hired in cloud, check out the AWS edition of the Cloud Resume Challenge book.

1. Certification - Your resume needs to have the AWS Cloud Practitioner certification on it.
2. HTML - Your resume needs to be written in HTML
3. CSS - Your resume needs to be styled with CSS
4. Static Website - Your HTML resume should be deployed online as an Amazon S3 static website
5. HTTPS - The S3 website URL should use HTTPS for security using Amazon CloudFront.
6. DNS - Point a custom DNS domain name to the CloudFront distribution. You can use Amazon Route 53
7. Javascript- Your resume webpage should include a visitor counter
8. Database The visitor counter - Amazon’s DynamoDB
9. API - AWS’s API Gateway and Lambda services for this.
10. Python - You will need to write a bit of code in the Lambda function;
11. Tests You should also include some tests for your Python code.
12. Infrastructure as Code – the DynamoDB table, the API Gateway, the Lambda function – AWS Serverless Application Model (SAM) template and deploy them using the AWS SAM CLI.
13. Source Control - Create a GitHub repository for your backend code.
14. CI/CD (Back end) - Set up GitHub Actions such that when you push an update to your Serverless Application Model template or Python code, your Python tests get run. If the tests pass, the SAM application should get packaged and deployed to AWS.
15. CI/CD (Front end) - Create a second GitHub repository for your website code. Create GitHub Actions such that when you push new website code, the S3 bucket automatically gets updated.
16. Blog post
    Finally, in the text of your resume, you should link a short blog post describing some things you learned while working on this project.

3 actions

1. Deploy backend infra - dynamodb, api gateway, lambda
2. Deploy website infra - s3, cloudfront, route53
3. Deploy website - website code to s3

Front End
S3 Website - SAM / Cloudformation

1. S3 Bucket
2. S3 Static Website
3. Upload Website
4. CloudFront Distribution
5. Cname Entry for Route 53 (DNS) with certificate

Backend

1. DynamoDB
2. Lambda Function
3. API Gateway

curl https://k7ib9cxbs4.execute-api.us-east-1.amazonaws.com/test -d '{"operation": "create", "payload": {"Item": {"id": "5678EFGH", "number": 15}}}'

curl -X POST https://k7ib9cxbs4.execute-api.us-east-1.amazonaws.com/test/DynamoDBManager

- add s3 bucket setup for website
  - make public acl
- add certificate creation
  - request cert or use existing
  - add route53 cname entry
- add cloudfront config
  - add alternate domain with custom ssl
  - get cloudfront domain dame
- add route53 config
  - add alias record with cloudfront domain name
- change api
  - add as restapi
  - add cors config to api
    - add method response header Header mappings = 'Access-Control-Allow-Origin'
    - add integration response = method.response.header.Access-Control-Allow-Origin = '\*'
  - deploy app, create stage & get URL
