from sys import argv, exit
from pyspark import SparkContext, SparkConf
import datetime

def print_(detail, *type_):
    if (type_ == "E"):
        type_ = "ERROR"
    else:
        type_ = "INFO"
    
    msg = ("[" + type_ + "]"+
           "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") +  "] "+
           detail)
    print(msg)

#Main
#Verifica se foram passados todos os parametros
if (len(argv[0:]) < 2):
    print_(("Informar o nome do arquivo"), 
           "E")
    exit(1)
else:
    source = "./"+argv[1]
    

#Criando o contexto do Spark - conectando a aplicacao ao cluster.
conf = SparkConf().setAppName('nasa')
sc = SparkContext(conf=conf)

# source = "./NASA"     
rdd = sc.textFile(source)

#1 Número de hosts únicos.
host_unico = rdd.map(lambda x: (x.split(' - - ')[0])).distinct().count()

#2 O total de erros 404.
rdd_erros_404 = rdd.filter(lambda x: x[-5:] == '404 -')
somar_erro_404 = rdd_erros_404.count()

#3 Os 5 URLs que mais causaram erro 404.
top_5_404 = rdd.filter(lambda x: x[-5:] == '404 -')\
    .map(lambda x: ((x.split(' - - ')[0]), 1))\
    .reduceByKey(lambda a, b: a + b)\
    .takeOrdered(5, lambda x: -x[1])

#4 Quantidade de erros 404 por dia.
qtde_dias_404 = rdd.filter(lambda x: x[-5:] == '404 -')\
    .map(lambda x: (x[x.find("[")+1:][:11], 1))\
    .reduceByKey(lambda a, b: a + b)

#5 O total de bytes retornados.
bytes_total = rdd.map(lambda x: x.split(" ")[-1])\
    .map(lambda x: int(x) if(x.isdigit()) else 0).sum()

#Results
print_("#1 Número de hosts únicos: "+str(host_unico))
print_("#2 O total de erros 404: "+str(somar_erro_404))
print_("#3 Os 5 URLs que mais causaram erro 404: "+str(top_5_404))
print_("#4 Quantidade de erros 404 por dia:  "+
    '[%s]' % ', '.join(map(str, qtde_dias_404.collect())))
print_("#5 O total de bytes retornados: "+str(bytes_total))

print_("Dados processados com sucesso!")