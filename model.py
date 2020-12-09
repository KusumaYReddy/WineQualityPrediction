from pyspark.ml.classification import DecisionTreeClassifier, DecisionTreeClassificationModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.regression import LinearRegression

# Load training data
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.shell import spark
from pyspark.ml.linalg import Vectors

from pyspark.ml.feature import VectorAssembler
from pyspark.sql.types import DoubleType

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
accuracy = evaluator.evaluate(predictions)
pred=predictions.withColumn('""""quality"""""', predictions['""""quality"""""'].cast(DoubleType()))
LabelsPred=pred.select('prediction','""""quality"""""').rdd
lrmetrics = MulticlassMetrics(LabelsPred)
f1=lrmetrics.weightedFMeasure()
print("F1 score : " ,f1)
