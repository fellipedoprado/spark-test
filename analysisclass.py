from pyspark.sql import DataFrame, functions

class Analysis():
    def __init__(self, df: DataFrame):
        self.df = df
        self.df.cache()
        self.df.count()

        self.df_404_error = self.__filter_404_errors()
        self.df_404_error.cache()
        self.df_404_error.count()

    def analyse_data(self):
        self.__get_unique_hosts()
        self.__get_total_bytes()
        self.__get_total_404_error()
        self.__get_top_links_404_error()
        self.__get_amount_day_404error()

    def __filter_404_errors(self) -> DataFrame:
        return self.df.filter(self.df.status == '404')

    def __get_unique_hosts(self) -> str:
        hosts_count = self.df.select('hosts').distinct().count()
        print('Numero de hosts unicos: ', hosts_count)

    def __get_total_bytes(self) -> str:
        bytes_sum = self.df.select(functions.sum('bytes')).collect()[0][0]
        print('O total de bytes retornados: ', bytes_sum)

    def __get_total_404_error(self) -> str:
        error_count = self.df_404_error.count()
        print('O total de erros 404: ', error_count)

    def __get_top_links_404_error(self) -> str:
        df404error = self.df_404_error.groupBy('hosts').count().sort('count', ascending=False).limit(5)
        print('Os 5 URLs que mais causaram erro 404 ')
        print(df404error.show())

    def __get_amount_day_404error(self) -> str:
        df404error = self.df_404_error.groupBy('date').count().sort('count', ascending=False)
        print('Quantidade de erros 404 por dia ')
        print(df404error.show(n=df404error.count(), truncate=False))