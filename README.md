Requirements
  
  Install the requirements using pip command.
  
    pip install -r requirements.txt
	
  Create the database in postgres and use the connection string to connect to the database
  
  	postgres+psycopg2://{username}:{password}@{host}:{port}/{database_name}

  Update the connection string in session.py and alembic.ini file
  
  Generate the table in the database using alembic migration script
  
  	Using the following command a new revision to generate table script will be created  -  alembic revision --autogenerate
	
	Following command create the table in the database  -  alembic upgrade head
	
	
Simple URL Shortner Application

  The application will shorten any given url to short form and it contains below three api's 

    Generate a shorten url
    POST /shorten

      Request Body
      {
          "url" = "https://www.bggc.org/"
      }

      Response
      {
          "success": true,
          "url": "https://www.bggc.org/",
          "shortUrl": "B8M",
          "id": 21
      }

    Get a url
    Get /shorten/{shortUrl}

      Response
      {
          "success": true,
          "url": "https://www.bggc.org/"
      }

    Delete a url
    DELETE /shorten/{id}

      Response
      {
          "success": true
      }
