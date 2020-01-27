from pyspark.sql import SparkSession
from fileclass import FileMainpulation
from analysisclass import Analysis

def defineSparkSession() -> SparkSession:
    spark = SparkSession.builder.appName('spark-test-semantix').master('local').getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    return spark

if __name__ == '__main__':
    spark = defineSparkSession()

    fileModule = FileMainpulation(spark)
    df = fileModule.load_format_data()

    analise = Analysis(df)
    analise.analyse_data()

    spark.stop()
    
