import sparknlp
import os
from sparknlp.base import *
from sparknlp.common import *
from sparknlp.annotator import *
from pyspark.sql import SparkSession

from pyspark.ml import Pipeline
import pandas as pd
import numpy as np
import findspark

os.environ["SPARK_HOME"] = "/Users/vitalim/Projects/courses/python_deep_dive/spark-nlp/spark-3.3.0-bin-hadoop2"

findspark.init()

spark = sparknlp.start()
MODEL_NAME = "tfhub_use"


def train_model(data=None):
    # Transforms the input text into a document usable by the SparkNLP pipeline.
    document_assembler = DocumentAssembler()
    document_assembler.setInputCol('text')
    document_assembler.setOutputCol('document')

    # # Separates the text into individual tokens (words and punctuation).
    tokenizer = Tokenizer()
    tokenizer.setInputCols(['document'])
    tokenizer.setOutputCol('token')

    # Encodes the text as a single vector representing semantic features.
    sentence_encoder = UniversalSentenceEncoder.pretrained(name=MODEL_NAME)
    sentence_encoder.setInputCols(['document', 'token'])
    sentence_encoder.setOutputCol('sentence_embeddings')

    nlp_pipeline = Pipeline(stages=[
        document_assembler,
        tokenizer,
        sentence_encoder,
    ])

    if data is None:
        data = spark.createDataFrame([['']]).toDF('text')
    # Fit the model to an empty data frame so it can be used on inputs.
    pipeline_model = nlp_pipeline.fit(data)
    light_pipeline = LightPipeline(pipeline_model)
    return light_pipeline


def get_similarity(input_list, pipeline):
    df = spark.createDataFrame(pd.DataFrame({'text': input_list}))
    result = pipeline.transform(df)
    _embeddings = []
    for r in result.collect():
        _embeddings.append(r.sentence_embeddings[0].embeddings)
    embeddings_matrix = np.array(_embeddings)
    return np.matmul(embeddings_matrix, embeddings_matrix.transpose())


print(spark.sparkContext._jsc.sc().listJars())
light_pipeline = train_model()

print(get_similarity(['Senior Platform Engineer - CI/CD (m/f/x)', 'dfdf', 'პერსონალური მწვრთნელი'], light_pipeline))