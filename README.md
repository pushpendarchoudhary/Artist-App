# Artist-App
Assignment Name - Customizing Artist API 

Description 
A customized Artist API using Django RESTFramework. The API should allow users to perform CRUD operations.

Installation 
# Clone the repository
git clone https://github.com/pushpendarchoudhary/Artist-App.git

# Change to the project directory
cd your_project

# Install dependencies
 pip install -r requirements.txt

# Set up the database
python manage.py migrate

# Start the development server
python manage.py runserver

# Usage And Features 
   * Admin panel credentials
   * username = admin
   * password = #123Admin

# Use Postman application to test the API endpoints 

# Register a user
            URL - POST- http://<your_localhost>/api/register
   * In the body tab check "raw" and select the data type to "JSON"
   * use the following JSON data format to register a user 
               {
                    "username": "sampleuser8",
                    "firstname": "John",
                    "lastname": "Doe",
                    "email": "sample8@example.com",
                    "password": "samplepassword8",
                    "confirmpassword": "samplepassword8"
                }
   * After successfully registering you will get an output in the body field with the message "success"
# Login a user
           use the URL POST- http://<your_localhost>/api/signin
 *  In the body tab check "raw" and select the data type "JSON"
 * Sample JSON data is
        {
           "username":"sampleuser8",
           "password":"samplepassword8"
         }
 * On successfully logging in you will get an output in the body tab containing a "token" value copy that token value for further use

# Create a new work
      use url POST - http://<your_localhost>/api/works
  * In headers tab assign 'key= Authorization' and 'value = token <your_generated_token>'
  * In the body tab use JSON data i.e 
         {
            "link": "http://samplelink.com",
            "work_type": "YT"     #work_type can only contain value YT, IG or Other
         }
  * After the successful creation of work you will get an output showing the work object

#
* for performing below tasks do contain  ('key= Authorization' and 'value = token <your_generated_token>)' in headers tab

  
# Retrieving a list of all works
i. use url GET - http://<your_local>/api/works
# Filtering using work_type 
i. Use URL GET - http://<your_local>/api/works?work_type=IG   # work_type can be IG , YT or Other 
# Searching using Artist's Name 
i. Use URL GET- http://<your_local>/api/works?artist=sampleuser8  # can use any username in place of sampleuser8
