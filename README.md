1.	Qual o objetivo do comando cache em Spark?

R: O objetivo do comando Cache, é criar persistência do RDD. Com esta persistência você pode acessar as informações a partir de um status específico sem a necessidade de recriar as transformações.

2.	O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

R: O mesmo código implementado em Spark é normalmente mais rápido, porque os dados são trabalhados em memória, isso evita operações de IO excessivas.

3.	Qual é a função do SparkContext ?

R: A função do SparkContext é conectar a aplicação ao cluster.

4.	Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

R: São DataSets que podem ser recriados, armazenados em memoria distribuídos pelo cluster, e podem ser criados pelo programa, ou vir de uma fonte externa.

5.	GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

R: O GroupByKey é menos eficiente que o reduceByKey, porque ele pré-agrupa os dados dentro da partição antes de enviar as tuplas para as partições. No Caso do groupByKey trafegará todas as tuplas antes do reduce ser executado isto gastará muito tempo em shuffle.

6.	Explique o que o código Scala abaixo faz.

val textFile = sc . textFile ( "hdfs://..." )

val counts = textFile . flatMap ( line => line . split ( " " ))

.map ( word => ( word , 1 ))

.reduceByKey ( _ + _ )

counts . saveAsTextFile ( "hdfs://..." )

R: Este é um programa que conta palavras. 
Cria o RDD textFile;
Separa por espaço;
Atribui o valor 1;
Cria map;
Cria o reduce;
Grava o resultado no path do hdfs;
                                                   Questões

Segue abaixo o comando para execucao do codigo:

colocar todos os arquivos no mesmo diretorio, pois o caminho do script é ./

$ sh semantix_nasa.sh NASA

Responda as seguintes questões devem ser desenvolvidas em Spark utilizando a sua linguagem de preferência.

1.	Número de hosts únicos.

R: 137979

2.	O total de erros 404.

R: 20900


3.	Os 5 URLs que mais causaram erro 404.

R: 1('hoohoo.ncsa.uiuc.edu', 251), 

   2('piweba3y.prodigy.com', 157), 

   3('jbiagioni.npt.nuwc.navy.mil', 132), 

   4('piweba1y.prodigy.com', 114), 

   5('www-d4.proxy.aol.com', 91)

4.	Quantidade de erros 404 por dia.

R: 1.('05/Aug/1995', 236),
 
  2.('11/Aug/1995', 263), 

  3.('12/Aug/1995', 196), 

  4.('26/Aug/1995', 366), 

  5.('28/Aug/1995', 410), 

  6.('30/Aug/1995', 571), 

  7.('06/Jul/1995', 640), 

  8.('18/Jul/1995', 465), 

  10.('04/Aug/1995', 346), 

  11.('14/Aug/1995', 287), 

  12.('11/Jul/1995', 471), 

  13.('13/Jul/1995', 531), 

  14.('17/Jul/1995', 406), 

  15.('09/Aug/1995', 279), 

  16.('31/Aug/1995', 526), 

  17.('22/Jul/1995', 192), 

  18.('10/Aug/1995', 315), 

  19.('17/Aug/1995', 271), 

  20.('04/Jul/1995', 359), 

  21.('19/Jul/1995', 639), 

  22.('27/Jul/1995', 336), 

  23.('03/Aug/1995', 304), 

  24.('07/Aug/1995', 537), 

  25.('16/Aug/1995', 259), 

  26.('20/Aug/1995', 312), 

  27.('08/Jul/1995', 302), 

  28.('10/Jul/1995', 398), 

  29.('12/Jul/1995', 471), 

  30.('23/Jul/1995', 233), 

  31.('24/Jul/1995', 328), 

  32.('15/Aug/1995', 327), 

  33.('19/Aug/1995', 209), 

  34.('21/Aug/1995', 305), 

  35.('25/Aug/1995', 415), 

  36.('05/Jul/1995', 497), 

  37.('18/Aug/1995', 256), 

  38.('01/Jul/1995', 316), 

  39.('15/Jul/1995', 254), 

  40.('06/Aug/1995', 373), 

  41.('29/Aug/1995', 420), 

  42.('07/Jul/1995', 570), 

  43.('21/Jul/1995', 334), 

  44.('22/Aug/1995', 288), 

  45.('23/Aug/1995', 345), 

  46.('27/Aug/1995', 370), 

  47.('09/Jul/1995', 348), 

  48.('14/Jul/1995', 413), 

  49.('25/Jul/1995', 461), 

  50.('28/Jul/1995', 94), 

  51.('13/Aug/1995', 216), 

  52.('24/Aug/1995', 420), 

  53.('02/Jul/1995', 291), 

  54.('08/Aug/1995', 391), 

  55.('20/Jul/1995', 428), 

  56.('01/Aug/1995', 243), 

  57.('03/Jul/1995', 474), 

  58.('16/Jul/1995', 257), 

  59.('26/Jul/1995', 336)

5.	O total de bytes retornados.

R: 65524314915


