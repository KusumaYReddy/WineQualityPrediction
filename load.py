from pyspark.ml.classification import DecisionTreeClassifier , DecisionTreeClassificationModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.regression import LinearRegression

# Load training data
from pyspark.shell import spark
from pyspark.ml.linalg import Vectors

from pyspark.ml.feature import VectorAssembler


test = spark.read.csv('TestDataset.csv',header=True,inferSchema=True, sep=";")
assembler = VectorAssembler(inputCols=['"""""fixed acidity""""', '""""volatile acidity""""','""""citric acid""""','""""residual sugar""""','""""chlorides""""','""""free sulfur dioxide""""','""""total sulfur dioxide""""','""""density""""','""""pH""""','""""sulphates""""','""""alcohol""""','""""quality"""""'], outputCol="features")
spDF1 = assembler.transform(test)
fd1=spDF1.select("features",'""""quality"""""')


# load the model
lrModel = DecisionTreeClassificationModel.load("myModel")
predictions = lrModel.transform(fd1)
predictions.show(5)
# obtain evaluator.
evaluator = MulticlassClassificationEvaluator(metricName="accuracy",labelCol='""""quality"""""',predictionCol='prediction')

# compute the classification error on test data.
f1 = evaluator.evaluate(predictions)
print("F1 score : " ,f1)
