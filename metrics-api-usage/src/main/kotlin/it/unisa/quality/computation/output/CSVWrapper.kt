package it.unisa.quality.computation.output

import com.github.doyaaaaaken.kotlincsv.dsl.csvWriter

class CSVWrapper(
        private val destinationPath: String,
        header: List<String>?
) {
    companion object {
        fun toRowsForCSV(className: String = "class", metrics: List<MetricResult>, isHeader: Boolean = false): List<String> {
            val row = mutableListOf<String>()
            row.add(className)
            metrics.forEach { metric ->
                if (isHeader) {
                    row.add(metric.metricName)
                } else {
                    row.add(metric.value.toString())
                }
            }
            return row
        }
    }

    private val writer = csvWriter()

    init {
        header?.let {
            writer.open(destinationPath) {
                writeRow(it)
            }
        }
    }

    fun writeRow(listOfMetrics: List<Any>) {
        writer.open(destinationPath, append = true) {
            writeRow(listOfMetrics)
        }
    }

}