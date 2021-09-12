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
Password: Enter your Secret access key from the IAM User credentials you downloaded earlier.<br>![connection-aws-credentials](https://user-images.githubusercontent.com/16669517/133000136-aa3f1169-f3ee-4402-b3af-0d6e80cba576.png)

Once you've entered these values, select Save and Add Another.<br>

![create-connection](https://user-images.githubusercontent.com/16669517/133000092-348545cc-72e5-44c6-9491-28627277b35c.png)



