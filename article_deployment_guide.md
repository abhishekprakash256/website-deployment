### The Guide for article deployment 

### Stack used 

- mongodb to store the article data
- the typesense data for the search of the data 

### IMP 

- The data is stored in the test_data.json 
- The data is divided into the section as Project, Tech and Life as per article type 
- The data can be written into the file and then just pushed into the database 


### Pushing Article Step by Step Proecess

- Put the data into the test_data.json (one of the backup is in the G drive)
- Put the section and the links correctly for articles (Github link , demo link , image links as well )
- The images are put into the correct section like - blog/section and per type -> life , project , tech with subflolder as well.
- For Pushing the data -
    - Two approaches can be used -->
    - First Approach 
        -  Redeploy the whole instance 
        - Clean whipe the instance 
        - Deploy the instance again 
    - Second Approach
        - The data is put into the test_data.json
        - scp the file into the prod using the command
        - Run the command - 
            ```bash
            #inside the dir  /Users/abhi/website-deployment/ansible/files
            scp test_data.json aws_machine:/home/ubuntu/mongo-ingestion-and-testing
            ```
        - 




