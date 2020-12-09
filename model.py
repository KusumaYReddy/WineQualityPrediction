from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.regression import LinearRegression

# Load training data
from pyspark.shell import spark
from pyspark.ml.linalg import Vectors

from pyspark.ml.feature import VectorAssembler

training = spark.read.csv('TrainingDataset.csv',header=True,inferSchema=True, sep=";")


assembler = VectorAssembler(inputCols=['"""""fixed acidity""""', '""""volatile acidity""""','""""citric acid""""','""""residual sugar""""','""""chlorides""""','""""free sulfur dioxide""""','""""total sulfur dioxide""""','""""density""""','""""pH""""','""""sulphates""""','""""alcohol""""','""""quality"""""'], outputCol="features")
spDF = assembler.transform(training)
fd=spDF.select("features",'""""quality"""""')

test = spark.read.csv('TestDataset.csv',header=True,inferSchema=True, sep=";")
assembler = VectorAssembler(inputCols=['"""""fixed acidity""""', '""""volatile acidity""""','""""citric acid""""','""""residual sugar""""','""""chlorides""""','""""free sulfur dioxide""""','""""total sulfur dioxide""""','""""density""""','""""pH""""','""""sulphates""""','""""alcohol""""','""""quality"""""'], outputCol="features")
spDF1 = assembler.transform(test)
fd1=spDF1.select("features",'""""quality"""""')

lr = DecisionTreeClassifier( featuresCol="features", labelCol='""""quality"""""')

# Fit the model
lrModel = lr.fit(fd)
predictions = lrModel.transform(fd1)
predictions.show(5)
# obtain evaluator.
evaluator = MulticlassClassificationEvaluator(metricName="accuracy",labelCol='""""quality"""""',predictionCol='prediction')

# compute the classification error on test data.
f1 = evaluator.evaluate(predictions)
print("F1 score : " ,f1)
