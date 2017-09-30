"""SimpleApp.py"""
import time

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="PythonStreamingQueueStream")
    ssc = StreamingContext(sc, 1)

    # Create the queue through which RDDs can be pushed to
    # a QueueInputDStream
    rddQueue = []
    for i in range(5):
        rddQueue += [ssc.sparkContext.parallelize([j for j in range(1, 1001)], 10)]

    # Create the QueueInputDStream and use it do some processing
    inputStream = ssc.queueStream(rddQueue)
    mappedStream = inputStream.map(lambda x: (x % 10, 1))
    reducedStream = mappedStream.reduceByKey(lambda a, b: a + b)
    reducedStream.pprint()

    ssc.start()
    time.sleep(6)
    ssc.stop(stopSparkContext=True, stopGraceFully=True)