# Test Smells

| Metric  | Description  | 
|---|---|
| Assertion Roulette  |  This smell comes from having a number of assertions in a test method that have no explanation; thus, if an assertion fails, the identification of the assert that failed can be difficult |
| Eager Test  |  A test is affected by Eager Test when it checks more than one method of the class to be tested, making the comprehension of the actual test target difficult |
| Lazy Test  | A test is affected by this smell when several methods check the same method using the same fixture |
| Mystery Guest  | Arises when a test uses external resources (e.g., file containing test data), and thus it is not self contained  |
| Sensitive Equality  | A test is affected by a Sensitive Equality smell when an assertion contains an equality checks through the use of the toString method  |
| Resource Optimism  |  Tests affected by such smell make assumptions about the state or the existence of external resources, providing a non-deterministic result that depends on the state of the resources |

# Code Quality Metrics

| Metric  | Description  | 
|---|---|
| LOC  | Indicates the lines of code of a given class |
| HALSTEAD  | Halstead metric give a sense of how complex the individual lines of code (or statements) are |
| RFC  | Counts the number of unique method invocations in a class. As invocations are resolved via static analysis, this implementation fails when a method has overloads with same number of parameters, but different types |
| CBO | This metric indicates the dependency degree of a class by another one |
| MPC  | MPC is the total number of function and procedure calls made to external unit |
| IFC  | (Information Flow Complex Metric) It provides a measure of the information that flows between the various modules in a system|
| DAC | DAC (Data Abstraction Coupling) is defined as “the number of abstract data types (ADTs) defined in a class” |
| DAC2  | DAC2 is a variant of the classic Data Abstraction Coupling that counts the number of distinct data type defined in a class |
| LCOM1  | LCOM1counts the number of pairs of methods that do not share attributes |
| LCOM2  | LCOM2 is defined as LCOM1 minus number of pairs of methods that use common attribute. |
| LCOM3  | It is the number of connected components in graph. To compute LCOM3 each method represented as a node and the use of at least one attribute as an edge |
| LCOM4 | It is similar to LCOM3, To represent method invocation additional edges are used.  |
| CONNECTIVITY | It is a cohesion metric based on the interactions between source code methods |
| LCOM5  | LCOM5 = (a – kl) / (l – kl), where l is the number of attributes, k is the number of methods, and a is the summation of the number of distinct attributes accessed by each method in a class |
| COH  |  Is defined as COH = a / kl, where a, k and l have the same definition as above|
| TCC  | TCC is defined as the percentage of pairs of public methods of the class with common attribute usage. |
| LCC  | LCC defines the relative number of directly or indirectly connected pairs of methods  |
| ICH | Number of invocations of other methods of the same class, weighted by the number of parameters of the invoked method |
| WMC  | This is a complexity metric introduced by Chidamber and Kemerer. The WMC metric is the sum of the complexities of all class methods |
| NOA  | The Number Of Attributes metric is used to count the average number of attributes for a class in the model |
| NOPA  | NOPA (Number of Public Attributes) is the number of public attributes of a class |
| NOP  | The Number Of Packages metric counts the packages within the analyzed software system |
| McCabe  | It measures the number of linearly independent paths contained in the control flow of the program |
| BUSEWEIMER  | It is a predictive model that look at structural features, e.g. number of parenthesis in a statement, to measure the readability of a source code component |

# Code Smells

| Metric  | Description  | 
|---|---|
| CDSBP  | (Class Data Should Be Private) A class exposing its fields, violating the principle of data hiding |
| CC | CC (Complex Class) describes a class exposing its fields, violating the principle of data hiding |
| Blob | A large class implementing different responsibilities and centralizing most of the system processing |
| SC | (Spaghetti Code) a class implementing complex methods interacting between them, with no parameters, using global variables |
| MC | (Message Chain) A long chain of method invocations is performed to implement a class functionality |
| LM | (Long Method) A method that is unduly long in terms of lines of code |
| FE | (Feature Envy) A method is more interested in a class other than the one it actually is in |
| FD | (Functional Decomposition) A class where inheritance and polymorphism are poorly used, declaring many private fields and implementing few methods |

# Coverage

| Metric  | Description  | 
|---|---|
| line coverage  | Line coverage reports on the execution footprint of testing in terms of which lines of code were executed to complete the test |

# Readability

| Metric  | Description  | 
|---|---|
| readability | Expresses the probability associated to a class to be readable in the range from 0 to 1, where 1 means that the classifier is sure that the class is readable |

