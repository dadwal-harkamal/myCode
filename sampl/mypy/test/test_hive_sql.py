from pyspark.sql import SparkSession
ss = SparkSession.builder.master("local").appName("Hive example").config("hive.metastore.uris", "thrift://lxdb-cd-hwxm02.np.gcp.atbcloud.com:9083").enableHiveSupport().getOrCreate()

#ss = SparkSession.builder.master("local").appName("Hive example").enableHiveSupport().getOrCreate()
ss.sql("show databases").show()
#ss.sql("create table if not exists test2 (key int,value int)")

#ss.sql("show tables").show()

#ss= SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()


#df = ss.read.format("com.databricks.spark.csv").options(header="true",inferschema="true").load("C:\WMR_Docs\SP_QUART_BONUS_PAYOUT\TBL_WMR_Connection.csv",header=True)
#df.show(5)
#df.printSchema()

#Employee = ss.createDataFrame([("1", "Joe", "70000", "1"),("2", "Henry", "80000", "2"),("3", "Sam", "60000", "2"),("4", "Max", "90000", "1")],["Id", "Name", "Sallary","DepartmentId"])
#Employee.show()                         
