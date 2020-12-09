Building the model:
Fit the model , transform and evaluate and perform classification error on dataset.
Used DecisionTreeClassifier to train the model as it gave highest accuracy,F1 score.
Training:
The model training is done in parallel on 4 EC2 clusters 1 master and 3 slaves.
Below is the screenshot of EMR cluster configuration
 

Below is the screenshot of training the model and output in EMR.
 

Below is the screenshot of model generation myModel by parallel training.
 

The prediction with Docker is on a single EC2 instance.
Pulled docker image onto ec2 instance and predicted output.
 



To build image go to that directory and use command :
Docker build -t my-app:1.0 .
 

After build you will be able to see the image :
 

To Pull docker image :
docker pull kusumayreddy/my-app

Run docker image with your dataset:
Replace c:/Kusuma/users/downloads/testdataset.csv with your local path.
Docker run -v c:/Kusuma/users/downloads/testdataset.csv:/usr/src/app/testdataset.csv kusumayreddy/my-app:1.0

Github/Docker hub repository links:
https://github.com/KusumaYReddy/WineQualityPrediction
https://hub.docker.com/r/kusumayreddy/my-app


