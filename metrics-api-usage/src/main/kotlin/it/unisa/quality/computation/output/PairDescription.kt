package it.unisa.quality.computation.output

import it.unisa.quality.beans.ClassBean

data class PairDescription(
        val pathTest: String,
        val pathSource: String,
        val testName: String,
        val sourceName: String
)

data class TestProductionPair(
        val productionClass: ClassBean,
        val testClass: ClassBean
)

data class MetricResult(
        val metricName: String,
        val value: Any,
        val className: String
)