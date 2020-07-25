package it.unisa.quality.computation.analysis

import it.unisa.quality.beans.ClassBean
import it.unisa.quality.computation.output.MetricResult
import it.unisa.quality.computation.output.TestProductionPair

interface Analyzer {
    fun computeMetricForPair(pair: TestProductionPair): List<MetricResult>
    fun computeMetricForClass(clazz: ClassBean): List<MetricResult>
}