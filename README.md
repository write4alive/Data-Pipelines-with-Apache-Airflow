# Project: Data Pipelines with Apache Airflow

A music streaming company, Sparkify, has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

They have decided to bring you into the project and expect you to create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. They have also noted that the data quality plays a big part when analyses are executed on top the data warehouse and want to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.

The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.


<h2>Project Overview</h2>
This project will introduce you to the core concepts of Apache Airflow. To complete the project, you will need to create your own custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.

We have provided you with a project template that takes care of all the imports and provides four empty operators that need to be implemented into functional pieces of a data pipeline. The template also contains a set of tasks that need to be linked to achieve a coherent and sensible data flow within the pipeline.

You'll be provided with a helpers class that contains all the SQL transformations. Thus, you won't need to write the ETL yourselves, but you'll need to execute it with your custom operators.

<img width="977" alt="example-dag" src="https://user-images.githubusercontent.com/16669517/133000035-ec605e75-73d4-4bf5-aaf3-cfa56339237d.png">

<h2>Add Airflow Connections</h2>
Here, we'll use Airflow's UI to configure your AWS credentials and connection to Redshift.

To go to the Airflow UI:<br>
You can use the Project Workspace here and click on the blue Access Airflow button in the bottom right.
If you'd prefer to run Airflow locally, open http://localhost:8080 in Google Chrome (other browsers occasionally have issues rendering the Airflow UI).
Click on the Admin tab and select Connections.<br>

![admin-connections](https://user-images.githubusercontent.com/16669517/133000084-29260b83-16d3-4088-b677-7f1b4e5f6e24.png)

On the create connection page, enter the following values:<br>

Conn Id: Enter aws_credentials.<br>
Conn Type: Enter Amazon Web Services.<br>
Login: Enter your Access key ID from the IAM User credentials you downloaded earlier.<br>
Password: Enter your Secret access key from the IAM User credentials you downloaded earlier.<br>

Once you've entered these values, select Save and Add Another.<br>

![connection-aws-credentials](https://user-images.githubusercontent.com/16669517/133000169-c07e2dec-127a-4cfc-9fe8-80225a02697e.png)

On the next create connection page, enter the following values:<br>

Conn Id: Enter redshift.<br>
Conn Type: Enter Postgres.<br>
Host: Enter the endpoint of your Redshift cluster, excluding the port at the end. You can find this by selecting your cluster in the Clusters page of the Amazon Redshift console. See where this is located in the screenshot below. IMPORTANT: Make sure to NOT include the port at the end of the Redshift endpoint string.<br>
Schema: Enter dev. This is the Redshift database you want to connect to.<br>
Login: Enter awsuser.<br>
Password: Enter the password you created when launching your Redshift cluster.<br>
Port: Enter 5439.<br>
<br>
![cluster-details](https://user-images.githubusercontent.com/16669517/133000186-a6e3d3f8-fe90-4cd5-bf60-21c826a265b5.png)<br>
Remember to DELETE your cluster each time you are finished working to avoid large, unexpected costs.<br>


<h2>Datasets</h2>
For this project, you'll be working with two datasets. Here are the s3 links for each:<br>

Log data: s3://udacity-dend/log_data<br>
Song data: s3://udacity-dend/song_data<br>

Project Template
To get started with the project:<br>

Go to the workspace on the next page, where you'll find the project template. You can work on your project and submit your work through this workspace.<br>

Alternatively, you can download the project template package and put the contents of the package in their respective folders in your local Airflow installation.<br>

The project template package contains three major components for the project:<br>

The dag template has all the imports and task templates in place, but the task dependencies have not been set<br>
The operators folder with operator templates<br>
A helper class for the SQL transformations<br>
With these template files, you should be able see the new DAG in the Airflow UI. The graph view should look like this:<br>

<img width="851" alt="screenshot-2019-01-21-at-20 55 39" src="https://user-images.githubusercontent.com/16669517/133000249-1e32fe9e-2b61-435d-b976-eecc5725b8a3.png">


<h2>Configuring the DAG</h2>
In the DAG, add default parameters according to these guidelines<br>

The DAG does not have dependencies on past runs<br>
On failure, the task are retried 3 times<br>
Retries happen every 5 minutes<br>
Catchup is turned off<br>
Do not email on retry<br>


<h2>Building the operators</h2>
To complete the project, you need to build four different operators that will stage the data, transform the data, and run checks on data quality.<br>

You can reuse the code from Project 2, but remember to utilize Airflow's built-in functionalities as connections and hooks as much as possible and let Airflow do all the heavy-lifting when it is possible.<br>

All of the operators and task instances will run SQL statements against the Redshift database. However, using parameters wisely will allow you to build flexible, reusable, and configurable operators you can later apply to many kinds of data pipelines with Redshift and with other databases.<br>

<h3>Stage Operator</h3>
The stage operator is expected to be able to load any JSON formatted files from S3 to Amazon Redshift. The operator creates and runs a SQL COPY statement based on the parameters provided. The operator's parameters should specify where in S3 the file is loaded and what is the target table.<br>

The parameters should be used to distinguish between JSON file. Another important requirement of the stage operator is containing a templated field that allows it to load timestamped files from S3 based on the execution time and run backfills.<br>

<h3>Fact and Dimension Operators</h3>
With dimension and fact operators, you can utilize the provided SQL helper class to run data transformations. Most of the logic is within the SQL transformations and the operator is expected to take as input a SQL statement and target database on which to run the query against. You can also define a target table that will contain the results of the transformation.<br>

Dimension loads are often done with the truncate-insert pattern where the target table is emptied before the load. Thus, you could also have a parameter that allows switching between insert modes when loading dimensions. Fact tables are usually so massive that they should only allow append type functionality.<br>

<h3>Data Quality Operator</h3>
The final operator to create is the data quality operator, which is used to run checks on the data itself. The operator's main functionality is to receive one or more SQL based test cases along with the expected results and execute the tests. For each the test, the test result and expected result needs to be checked and if there is no match, the operator should raise an exception and the task should retry and fail eventually.<br>

For example one test could be a SQL statement that checks if certain column contains NULL values by counting all the rows that have NULL in the column. We do not want to have any NULLs so expected result would be 0 and the test would compare the SQL statement's outcome to the expected result.
