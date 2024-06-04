
import pyspark
spark_to_aws_hadoop = {"3.0": "2.7.4", "3.1": "3.2.0", "3.2": "3.3.1", "3.3": "3.3.2", "3.4":"3.3.4", "3.5":"3.3.4"}
spark_version = pyspark.__version__[:3]


def get_aws_version():
    return spark_to_aws_hadoop[spark_version]
