# CSVsniffer in Python

## Overview

Welcome to **CSVsniffer**, a Python implementation of the **Table Uniformity Method (TUM)** for CSV Dialect Detection! TUM is an advanced, research-backed approach, designed to accurately determine the dialect of CSV files, ensuring both structural integrity and semantic correctness of your data.

## Why CSVsniffer?

- **Unmatched accuracy**: demonstrated to achieve **92.60% accuracy**, using F1 score metrics, making it the gold standard for CSV dialect detection.
- **Holistic analysis**: evaluates the entire table structure, including field count consistency, record dispersion, and data type recognition.
- **Adaptable**: works effectively across files of all sizes, from single records to large datasets.
- **Quantitative scoring**: provides a clear, numeric score, for easy comparison and decision-making in dialect selection.

## Strengths

- **Versatility**: handles both clean and messy CSV files with high accuracy.
- **Data integrity**: focuses not just on syntax but also on the semantic fit of the data.
- **Scalability**: efficient for both small and large datasets, with special handling for single-record files.
- **Research-driven**: backed by scientific research, ensuring a robust methodology.

## Key metrics

### **Table Consistency**
- Measures how uniform the number of fields is across records, ensuring a consistent table structure.

### **Records Dispersion**
- Analyzes the variability in record composition, penalizing high dispersion for better dialect fit.

### **Data Type Detection**
- Scores how well field types match expected data types, enhancing the semantic validation of the parsed data.

### **Table Score**
- Combines all metrics into a single score, offering a definitive measure of dialect accuracy. The final score is bounded (0 to 200), making the interpretation so simple and ambiguity free. The scoring reflect a balance between different aspects of CSV structure (consistency, dispersion, and data type detection). This balance is not just functional but also aesthetically pleasing in its symmetry and consideration of multiple data characteristics!

## Comparison with alternatives

- **CleverCSV**: while effective for pattern recognition, CSVsniffer along with TUM offers deeper structural analysis.
- **DuckDB Sniffer**: optimized for speed within DuckDB but less comprehensive than CSVsniffer for complex cases.

## Usage

### For researchers and developers

- **Integrate CSVsniffer** into your data processing pipelines for more reliable CSV parsing.
- **Contribute** to our ongoing research to refine and expand the TUM's capabilities.

### For data scientists and analysts

- **Ensure data quality**: use CSVsniffer to guarantee that your CSV data is parsed with the highest integrity.
- **Avoid false positives**: benefit from TUM's fine-tuned metrics to minimize errors in data interpretation.

## Get Involved

- **Star** this repository if you find CSVsniffer useful.
- **Fork** the project to contribute to its development or adapt it for your needs.
- **Open Issues** for bugs, feature requests, or to discuss potential improvements.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgements

We thank the research community for their contributions to CSV dialect detection methodologies, and we especially acknowledge the foundational work that has inspired this method.

---

Feel empowered to leverage the Table Uniformity Method for your CSV data challenges. For more information, please see our documentation or reach out to us directly!

[GitHub Repository](https://github.com/ws-garcia/CSVsniffer) | [Research paper](https://content.iospress.com/articles/data-science/ds240062) | [Contact](https://github.com/ws-garcia/CSVsniffer/discussions)
