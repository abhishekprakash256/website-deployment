### The Guide for article deployment 

### Stack used 

- mongodb to store the article data
- the typesense data for the search of the data 

### IMP 

- The data is stored in the test_data.json 
- The data is divided into the section as Project, Tech and Life as per article type 
- The article data goes into section as follows -->
    - article_name, slug,article_para, section_name, id_number are for the card data and render in the section page
    - the title , image_src, article_para and markdown_data are for the blog page.
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
        - The scp of files happen from the anisble/files/blog/section/<category>
            ```bash
            #example command , the file are put into the specific location as per static media server fetching

            scp search-icon.jpg aws_machine:/home/ubuntu/static-media-server/blog/section/tech/typesense
            ```
        - The url in data set is designed based on the location of the file 

            ```bash
            #example URL
            "https://api.meabhi.me/static-media-server/v1/static/blog/section/tech/typesense/search-icon.jpg
            ```

        - Remove the old data file (Run the command)
        ```bash
            home/ubuntu/mongo-ingestion-and-testing$ rm test_data.json
        ```
        - Run the command - 
            ```bash
            #inside the dir  /Users/abhi/website-deployment/ansible/files
            scp test_data.json aws_machine:/home/ubuntu/mongo-ingestion-and-testing
            ```
        - rm the docker mongodb (Run the Command)
            ```bash
            docker rm -f mongo
            ```
        - rm the typesense conatiner (run the command)
            ```bash
            docker rm -f typesense
            ```
        - Install and run mongo db conatiner (run the command)
            ```bash
            docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest
            ```
        - Install and run typesense conatiner (run the command)
            ```bash
            docker run -d \
            --name typesense \
            --network my_network \
            -p 8108:8108 \
            -v $(pwd)/typesense-data:/data \
            typesense/typesense:29.0.rc30 \
            --data-dir /data \
            --api-key=test_key \
            --enable-cors
            ```
        - Run the command to insert the data into mongo
            ```bash
            #int the dir /home/ubuntu/mongo-ingestion-and-testing
            /home/ubuntu/.venvs/global/bin/python3 data_crud.py
            ```

        - Run the command to insert the data into typesense
            ```bash
            #int the dir /home/ubuntu/typesense-etl
            /home/ubuntu/.venvs/global/bin/python3 etl_typesense.py
            ```




