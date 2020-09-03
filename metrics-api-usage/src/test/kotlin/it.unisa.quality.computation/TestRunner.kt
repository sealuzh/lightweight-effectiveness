package it.unisa.quality.computation

import it.unisa.quality.computation.output.TestProductionPair
import org.junit.Ignore
import org.junit.Test

class TestRunner {
    @Test
    @Ignore
    fun `smoke test`() {
        val sourcePath = "/Users/grano/Desktop/lightweight-effectiveness/projects/commons-lang/src/main/java/"
        val testPath = "/Users/grano/Desktop/lightweight-effectiveness/projects/commons-lang/src/test/java/"
        val csvFile = "/Users/grano/Desktop/lightweight-effectiveness/metrics-api-usage/src/test/resources/csv-test.csv"
        val projectAnalyzer = ProjectAnalyzer(sourceDirectory = sourcePath, testDirectory = testPath)
        val pairs: List<TestProductionPair> = projectAnalyzer.readInputFile(csvFile)
        projectAnalyzer.computeCkMetrics(pairs)
        projectAnalyzer.computeCodeSmells(pairs)
        projectAnalyzer.computeTestSmells(pairs)
    }
}