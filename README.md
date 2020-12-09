############ Wine Quality Predicition ##########


To build image go to that directory and use command :
Docker build -t my-app:1.0 .

To Pull docker image :
docker pull kusumayreddy/my-app

Run docker image with your dataset:
Replace c:/Kusuma/users/downloads/testdataset.csv with your local path.
Docker run -v c:/Kusuma/users/downloads/testdataset.csv:/usr/src/app/testdataset.csv kusumayreddy/my-app:1.0

The prediction with Docker is on a single EC2 instance.
Pulled docker image onto ec2 instance and predicted output.
Steps to run docker file on EC2:
Copy the TestDataset.csv into EC2 /home/ec2-user using following command:
 scp -i path/TestDataset.csv publicDNS of ec2 here:/home/ec2-user
In EC2 install docker use following command: sudo yum update -y sudo yum install docker -y sudo service docker start
Pull the image using:
Sudo docker pull kusumayreddy/my-app
Run your testdataset using:
Replace c:/Kusuma/users/downloads/testdataset.csv with your local path.
Sudo Docker run -v c:/Kusuma/users/downloads/testdataset.csv:/usr/src/app/testdataset.csv kusumayreddy/my-app:1.0

Github/Docker hub repository links:
https://github.com/KusumaYReddy/WineQualityPrediction
https://hub.docker.com/r/kusumayreddy/my-app

