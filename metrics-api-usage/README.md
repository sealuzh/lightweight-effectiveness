# Computation of code metrics, code and test smells

This litle project uses the API of DECOR for the computation of the metrics used for this study.
Such APIs are in the `libs/it.unisa.quality-1.0.jar` jar. 
Please note I am not the developer nor the maintainer of those APIs.

## How to run
To execute such a program please modify the `pom.xml` file and add the three arguments needed to the `exec-maven-plugin`:

* absolute path of the production classes of project to examinate (e.g., `/Users/me/Desktop/project/src/main/java`)
* absolute path of the test classes of the project to examinate (e.g., `/Users/me/Desktop/project/src/test/java`)
* absolute path of the csv file that has these 4 columns: `path_test,test_name,path_src,class_name`, i.e., the absolute paths and the fully qualified names for all the pairs production/test class. The Python contains code that and the end of the mutation process gives in output such pairs (parsing either the `pom` of the `gradle` build file). 

Thus, run the following command:
```
mvn install; mvn package; mvn exec:java
```

## Readability metric
The APIs for the computation of the readability metrics have been released by the original authors at [this link](https://dibt.unimol.it/report/readability/).