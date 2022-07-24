# spark-studio-assignment
*this project contains HTTP API endpoints to generate and verify phone numbers using OTPs*
## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command
`python -m venv env`

After this you will activate your virtual env
You can install all the required dependencies by running

`pip install -r requirements.txt`

then from the project's root directory you will have to do migrations by running

`python manage.py migrate`

Now You are all set!
## Structure

| Endpoint                    | HTTP Method | Result                                                 |
| :---                        |    :----:   |          ---:                                          |
| authentication/generate_otp | POST        |Generates a 4 digit OTP                                 |
| authentication/verify_otp   | POST        | Verifies OTP and Create User with given Phone Number   |

## API Documentation

### Generating OTP

| Method | URL                           |
| :---   |    ---:                       |       
| POST   | authentication/generate_otp   |

> Request

| Parameter Name              | Description | Type & Length                                          |
| :---                        |    :----:   |          ---:                                          |
|                             |             |                                                        |

> Response

| HTTP Status Code      | Description                           | Response Data            | 
| ---                   |    ----                               |         --              |
|    200                |   OTP generated successfully          |            success      |  
|  400  | User attempted to generate OTP more than 10 times     |  You have exceeded the limit of verification attempts. You can try again Tommorrow |


### Verifying OTP

| Method | URL                           |
| ---   |    ---                         |       
| POST   | /authentication/verify_otp:   |

> Request

| Parameter Name             | Description              | Type & Length                                        |
| ---                        |    ----                  |          ---                                         |
|    otp                     |    OTP                   |       String                                         |
|    phone                   |    User's Phone Number   |       String                                         |

> Response

| HTTP StatusCode | Description |     Response Data     | 
| ---              |    ----  |        --                 |
|    200           |   Phone Number Verified and created <br /> User with given Phone Number    |       success   | 
|    400                 |    User Exists with given phone number            |  User Already verified |
|    400        |   User has more than 3 failed  Attempts to verify OTP      |  Maximum verification attempts exceeded |
|    400                 |    User Entered Wrong OTP           |  Invalid OTP |
|    404                |    User attempted to verify OTP without generating OTP         |  Page Not Found|
