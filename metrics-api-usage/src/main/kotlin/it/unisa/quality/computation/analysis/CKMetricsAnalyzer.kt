package it.unisa.quality.computation.analysis

import it.unisa.quality.beans.ClassBean
import it.unisa.quality.computation.output.MetricResult
import it.unisa.quality.computation.output.TestProductionPair
import it.unisa.quality.metrics.CKMetrics

class CKMetricsAnalyzer : Analyzer {

    override fun computeMetricForClass(clazz: ClassBean): List<MetricResult> {
        val metrics = mutableListOf<MetricResult>()
        val clazzName = "${clazz.belongingPackage}.${clazz.name}"
        with(metrics) {
            add(MetricResult("LOC", CKMetrics.getLOC(clazz), clazzName))
            add(MetricResult("HALSTEAD", CKMetrics.getHalsteadVolume(clazz), clazzName))
            add(MetricResult("RFC", CKMetrics.getRFC(clazz), clazzName))
            add(MetricResult("CBO", CKMetrics.getCBO(clazz), clazzName))
            add(MetricResult("MPC", CKMetrics.getMPC(clazz), clazzName))
            add(MetricResult("IFC", CKMetrics.getIFC(clazz), clazzName))
            add(MetricResult("DAC", CKMetrics.getDAC(clazz), clazzName))
            add(MetricResult("DAC2", CKMetrics.getDAC2(clazz), clazzName))
            add(MetricResult("LCOM1", CKMetrics.getLCOM1(clazz), clazzName))
            add(MetricResult("LCOM2", CKMetrics.getLCOM2(clazz), clazzName))
            add(MetricResult("LCOM3", CKMetrics.getLCOM3(clazz), clazzName))
            add(MetricResult("LCOM4", CKMetrics.getLCOM4(clazz), clazzName))
            add(MetricResult("CONNECTIVITY", CKMetrics.getConnectivity(clazz), clazzName))
            add(MetricResult("LCOM5", CKMetrics.getLCOM5(clazz), clazzName))
            add(MetricResult("COH", CKMetrics.getCoh(clazz), clazzName))
            add(MetricResult("TCC", CKMetrics.getTCC(clazz), clazzName))
            add(MetricResult("LCC", CKMetrics.getLCC(clazz), clazzName))
            add(MetricResult("ICH", CKMetrics.getICH(clazz), clazzName))
            add(MetricResult("WCM", CKMetrics.getWMC(clazz), clazzName))
            add(MetricResult("NOA", CKMetrics.getNOA(clazz), clazzName))
            add(MetricResult("NOPA", CKMetrics.getNOPA(clazz), clazzName))
            add(MetricResult("NOP", CKMetrics.getNOPrivateA(clazz), clazzName))
            add(MetricResult("McCABE", CKMetrics.getMcCabeMetric(clazz), clazzName))
            add(MetricResult("BUSWEIMER", CKMetrics.getBuseWeimer(clazz), clazzName))
        }
        return metrics
    }

    override fun computeMetricForPair(pair: TestProductionPair): List<MetricResult> {
        TODO("Call computeMetricForClass")
    }
}