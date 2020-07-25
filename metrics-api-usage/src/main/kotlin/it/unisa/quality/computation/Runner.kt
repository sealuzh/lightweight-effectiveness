package it.unisa.quality.computation

import it.unisa.quality.computation.output.TestProductionPair

fun main(args: Array<String>) {
    val sourcePath = args[0]
    val testPath = args[1]
    val csvPath = args[2]

    val projectAnalyzer = ProjectAnalyzer(sourceDirectory = sourcePath, testDirectory = testPath)
    val pairs: List<TestProductionPair> = projectAnalyzer.readInputFile(csvPath)
    projectAnalyzer.computeCkMetrics(pairs)
    projectAnalyzer.computeCodeSmells(pairs)
    projectAnalyzer.computeTestSmells(pairs)
}