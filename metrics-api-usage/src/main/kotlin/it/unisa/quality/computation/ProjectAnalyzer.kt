package it.unisa.quality.computation

import com.github.doyaaaaaken.kotlincsv.dsl.csvReader
import it.unisa.quality.beans.ClassBean
import it.unisa.quality.beans.PackageBean
import it.unisa.quality.computation.analysis.CKMetricsAnalyzer
import it.unisa.quality.computation.analysis.CodeSmellAnalyzer
import it.unisa.quality.computation.analysis.TestSmellAnalyzer
import it.unisa.quality.computation.output.CSVWrapper
import it.unisa.quality.computation.output.MetricResult
import it.unisa.quality.computation.output.PairDescription
import it.unisa.quality.computation.output.TestProductionPair
import it.unisa.quality.utility.ProjectConverter
import java.io.File
import java.util.*

class ProjectAnalyzer(
        sourceDirectory: String,
        testDirectory: String
) {

    val sourcePackages: Vector<PackageBean> = ProjectConverter.convert(sourceDirectory)
    private val testPackages = ProjectConverter.convert(testDirectory)

    /**
     * Parses a csv file in input and returns all the pairs of pre-processed test class and production class
     *
     * @param path the path of the csv file in input
     * @return a list of TestProductionPair
     */
    fun readInputFile(path: String): List<TestProductionPair> {
        val rows: List<Map<String, String>> = csvReader().readAllWithHeader(File(path))
        val pairDescriptions: List<PairDescription> = rows.map {
            PairDescription(
                    pathTest = it.getOrElse("path_test") { throw Exception("no path_test field") },
                    pathSource = it.getOrElse("path_src") { throw Exception("no path_src field") },
                    testName = it.getOrElse("test_name") { throw Exception("no test_name field") },
                    sourceName = it.getOrElse("class_name") { throw Exception("no class_name field") }
            )
        }
        return pairDescriptions.map {
            TestProductionPair(
                    productionClass = getClassFromSignature(it.sourceName, false),
                    testClass = getClassFromSignature(it.testName)
            )
        }
    }

    /**
     * Returns a ClassBean given the signature of a class
     *
     * @param signature
     * @param isTestClass if true, only looks in the parsed tests classes
     * @throws Exception if no match is found
     * @return a ClassBean
     */
    private fun getClassFromSignature(signature: String, isTestClass: Boolean = true): ClassBean {
        for (packageBean in if (isTestClass) testPackages else sourcePackages)
            packageBean.classes.forEach { if ("${it.belongingPackage}.${it.name}" == signature) return it }
        throw Exception("The class $signature seems to not have been parsed")
    }

    fun computeCodeSmells(pairs: List<TestProductionPair>) {
        val codeSmellAnalyzer = CodeSmellAnalyzer(sourceCodePackages = sourcePackages)
        val map: List<List<MetricResult>> = pairs.map { codeSmellAnalyzer.computeMetricForClass(it.productionClass) }
        writeOnCSV(map, "code-smells.csv")
    }

    fun computeTestSmells(pairs: List<TestProductionPair>) {
        val testSmellAnalyzer = TestSmellAnalyzer(sourceCodePackages = sourcePackages)
        val map: List<List<MetricResult>> = pairs.map { testSmellAnalyzer.computeMetricForPair(it) }
        writeOnCSV(map, "test-smells.csv")
    }

    fun computeCkMetrics(pairs: List<TestProductionPair>) {
        val ckAnalyzer = CKMetricsAnalyzer()
        val prodClasses = pairs.map { it.productionClass }
        val testClasses = pairs.map { it.testClass }
        val prodMap: List<List<MetricResult>> = prodClasses.map { ckAnalyzer.computeMetricForClass(it) }
        val testMap = testClasses.map { ckAnalyzer.computeMetricForClass(it) }
        writeOnCSV(prodMap + testMap, "ck-metrics.csv")

    }

    private fun writeOnCSV(toWrite: List<List<MetricResult>>, filename: String) {
        val csvWriter = CSVWrapper(filename,
                CSVWrapper.toRowsForCSV(metrics = toWrite[0], isHeader = true))
        toWrite.forEach { csvWriter.writeRow(CSVWrapper.toRowsForCSV(it[0].className, it)) }
    }
}