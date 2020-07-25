package it.unisa.quality.computation.analysis

import it.unisa.quality.beans.ClassBean
import it.unisa.quality.beans.PackageBean
import it.unisa.quality.computation.output.MetricResult
import it.unisa.quality.computation.output.TestProductionPair
import it.unisa.quality.rules.code.*
import it.unisa.quality.rules.tests.IndirectTesting
import java.util.*

class CodeSmellAnalyzer(
        sourceCodePackages: Vector<PackageBean>
) : Analyzer {

    init {
        IndirectTesting.findInvocations(sourceCodePackages)
    }

    private val classDataShouldBePrivate = ClassDataShouldBePrivate()
    private val complexClass = ComplexClass()
    private val featureEnvy = FeatureEnvy()
    private val functionalDecomposition = FunctionalDecomposition()
    private val godClass = GodClass()
    private val longMethod = LongMethod()
    private val messageChain = MessageChain()
    private val spaghettiCode = SpaghettiCode()

    override fun computeMetricForPair(pair: TestProductionPair): List<MetricResult> {
            TODO("Call computeMetricForClass")
    }

    override fun computeMetricForClass(clazz: ClassBean): List<MetricResult> {
        val metrics = mutableListOf<MetricResult>()
        val clazzName = "${clazz.belongingPackage}.${clazz.name}"
        with(metrics) {
            add(MetricResult(classDataShouldBePrivate.name,
                    classDataShouldBePrivate.isClassDataShouldBePrivate(clazz), clazzName))
            add(MetricResult(complexClass.name, complexClass.isComplexClass(clazz, SystemType.JAVA), clazzName))
            add(MetricResult(featureEnvy.name, featureEnvy.isFeatureEnvy(clazz), clazzName))
            add(MetricResult(functionalDecomposition.name,
                    functionalDecomposition.isFunctionalDecomposition(clazz), clazzName))
            add(MetricResult(godClass.name, godClass.isGodClass(clazz, SystemType.JAVA), clazzName))
            add(MetricResult(longMethod.name, longMethod.isLongMethod(clazz), clazzName))
            add(MetricResult(messageChain.name, messageChain.isMessageChain(clazz), clazzName))
            add(MetricResult(spaghettiCode.name,
                    spaghettiCode.isSpaghettiCode(clazz, SystemType.JAVA), clazzName))
        }
        return metrics
    }
}