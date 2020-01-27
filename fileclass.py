from pyspark.sql import SparkSession, DataFrame

COLUMNS_DROP = ['_c1', '_c2', '_c4']
COLUMNS_NAMES = ['hosts', 'timestamp', 'request', 'status', 'bytes']

class FileMainpulation():
    def __init__(self, sparkSession: SparkSession):
        self.sparkSession = sparkSession

    def load_format_data(self) -> DataFrame:
        dataAug = self.__load_file('access_log_Aug95')
        dataJul = self.__load_file('access_log_Jul95')
        df = self.__join_files(dataAug, dataJul)
        df = self.__adjust_data(df)
        return df

    def __load_file(self, filename: str) -> DataFrame:
        return self.sparkSession.read.load('data\\' + filename, format='csv', sep=' ', inferSchema='false')

    def __join_files(self, file_1: DataFrame, file_2: DataFrame) -> DataFrame:
        return file_1.union(file_2)

    def __adjust_data(self, df: DataFrame) -> DataFrame:
        df = df.drop(*COLUMNS_DROP).toDF(*COLUMNS_NAMES)
        return df.withColumn('date', df.timestamp.substr(2, 11))