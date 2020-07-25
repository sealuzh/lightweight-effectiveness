package it.unisa.quality.computation.analysis

import it.unisa.quality.beans.ClassBean
import it.unisa.quality.beans.PackageBean
import it.unisa.quality.computation.output.MetricResult
import it.unisa.quality.computation.output.TestProductionPair
import it.unisa.quality.rules.tests.*
import java.util.*

class TestSmellAnalyzer(
        sourceCodePackages: Vector<PackageBean>
) : Analyzer {

    private val assertionRoulette = AssertionRoulette()
    private val eagerTest = EagerTest()
    private val forTestersOnly = ForTestersOnly()
    private val indirectTesting = IndirectTesting()
    private val lazyTest = LazyTest()
    private val mysteryGuest = MysteryGuest()
    private val resourceOptimism = ResourceOptimistism()
    private val sensitiveEquality = SensitiveEquality()

    private var methodsInTheProject = IndirectTesting.findInvocations(sourceCodePackages)

    override fun computeMetricForPair(pair: TestProductionPair): List<MetricResult> {
        val metrics = mutableListOf<MetricResult>()
        val clazzName = "${pair.testClass.belongingPackage}.${pair.testClass.name}"
        with(metrics) {
            add(MetricResult(assertionRoulette.name, assertionRoulette.isAssertionRoulette(pair.testClass), clazzName))
            add(MetricResult(forTestersOnly.name,
                    forTestersOnly.isForTestersOnly(pair.testClass, pair.productionClass, methodsInTheProject), clazzName))
            add(MetricResult(eagerTest.name, eagerTest.isEagerTest(pair.testClass, pair.productionClass), clazzName))
            add(MetricResult(indirectTesting.name,
                    indirectTesting.isIndirectTesting(pair.testClass, pair.productionClass, methodsInTheProject), clazzName))
            add(MetricResult(lazyTest.name, lazyTest.isLazyTest(pair.testClass, pair.productionClass), clazzName))
            add(MetricResult(mysteryGuest.name, mysteryGuest.isMysteryGuest(pair.testClass), clazzName))
            add(MetricResult(resourceOptimism.name, resourceOptimism.isResourceOptimistism(pair.testClass), clazzName))
            add(MetricResult(sensitiveEquality.name, sensitiveEquality.isSensitiveEquality(pair.testClass), clazzName))
        }
        return metrics
    }

    override fun computeMetricForClass(clazz: ClassBean): List<MetricResult> {
        TODO("Call computeMetricForPair")
    }
}