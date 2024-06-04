"""Constants for delivery."""

from cg.constants.constants import Workflow
from cg.constants.housekeeper_tags import (
    HK_DELIVERY_REPORT_TAG,
    AlignmentFileTag,
    AnalysisTag,
    HermesFileTag,
)

ONLY_ONE_CASE_PER_TICKET: list[Workflow] = [
    Workflow.FASTQ,
    Workflow.MICROSALT,
    Workflow.MUTANT,
]

SKIP_MISSING: list[Workflow] = [
    Workflow.FASTQ,
    Workflow.MICROSALT,
    Workflow.MUTANT,
]

BALSAMIC_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {"delivery-report"},
    {"multiqc-html"},
    {"metrics"},
    {"cnv-report"},
    {"coverage"},
    {"germline"},
    {"vcf-sv"},
    {"vcf-sv-index"},
    {"vcf-sv-research"},
    {"vcf-sv-research-index"},
    {"vcf-sv-clinical"},
    {"vcf-sv-clinical-index"},
    {"vcf-snv"},
    {"vcf-snv-index"},
    {"vcf-snv-research"},
    {"vcf-snv-research-index"},
    {"vcf-snv-clinical"},
    {"vcf-snv-clinical-index"},
    {"vcf2cytosure"},
]

BALSAMIC_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {AlignmentFileTag.CRAM},
    {AlignmentFileTag.CRAM_INDEX},
]

BALSAMIC_QC_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {"delivery-report"},
    {"multiqc-html"},
]

BALSAMIC_QC_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {"qc-cram"},
    {"qc-cram-index"},
]

BALSAMIC_UMI_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {"vcf-umi-snv"},
    {"vcf-umi-snv-index"},
    {"vcf-umi-snv-research"},
    {"vcf-umi-snv-research-index"},
    {"vcf-umi-snv-clinical"},
    {"vcf-umi-snv-clinical-index"},
]

BALSAMIC_UMI_ANALYSIS_CASE_TAGS.extend(BALSAMIC_ANALYSIS_CASE_TAGS)

BALSAMIC_UMI_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {"umi-cram"},
    {"umi-cram-index"},
]

BALSAMIC_UMI_ANALYSIS_SAMPLE_TAGS.extend(BALSAMIC_ANALYSIS_SAMPLE_TAGS)


MIP_DNA_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {"delivery-report"},
    {"multiqc-html"},
    {"vcf-clinical-sv-bin"},
    {"vcf-clinical-sv-bin-index"},
    {"vcf-research-sv-bin"},
    {"vcf-research-sv-bin-index"},
    {"gbcf"},
    {"gbcf-index"},
    {"snv-gbcf"},
    {"snv-gbcf-index"},
    {"snv-bcf"},
    {"snv-bcf-index"},
    {"sv-bcf"},
    {"sv-bcf-index"},
    {"vcf-snv-clinical"},
    {"vcf-snv-clinical-index"},
    {"vcf-snv-research"},
    {"vcf-snv-research-index"},
    {"vcf-sv-clinical"},
    {"vcf-sv-clinical-index"},
    {"vcf-sv-research"},
    {"vcf-sv-research-index"},
]

MIP_DNA_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {AlignmentFileTag.BAM},
    {AlignmentFileTag.BAM_BAI},
    {AlignmentFileTag.CRAM},
    {AlignmentFileTag.CRAM_INDEX},
]

MIP_RNA_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {"fusion", "clinical", "pdf"},
    {"fusion", "research", "pdf"},
    {"fusion", "vcf"},
    {"fusion", "vcf-index"},
    {"vcf-snv-clinical"},
    {"vcf-snv-clinical-index"},
    {"vcf-snv-research"},
    {"vcf-snv-research-index"},
    {"multiqc-html"},
]

MIP_RNA_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {AnalysisTag.FUSION, AnalysisTag.STARFUSION},
    {AnalysisTag.FUSION, AnalysisTag.ARRIBA},
    {AlignmentFileTag.CRAM},
    {AlignmentFileTag.CRAM_INDEX},
    {AnalysisTag.FUSION, "vcf"},
    {AnalysisTag.FUSION, "vcf-index"},
    {"salmon-quant"},
]

MICROSALT_ANALYSIS_CASE_TAGS = [{"qc-report"}, {"typing-report"}]

MICROSALT_ANALYSIS_SAMPLE_TAGS: list[set[str]] = []

FASTQ_ANALYSIS_CASE_TAGS: list[set[str]] = []

FASTQ_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {"fastq"},
]

MUTANT_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {"pangolin"},
    {"ks-delivery"},
]

MUTANT_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {"fastq"},
    {"vcf", "vcf-report", "fohm-delivery"},
]

RNAFUSION_ANALYSIS_CASE_TAGS: list[set[str]] = [
    {AnalysisTag.FUSION, AnalysisTag.ARRIBA},
    {AnalysisTag.FUSION, AnalysisTag.STARFUSION},
    {AnalysisTag.FUSION, AnalysisTag.FUSIONCATCHER},
    {AnalysisTag.FUSIONCATCHER_SUMMARY},
    {AnalysisTag.FUSIONINSPECTOR},
    {AnalysisTag.FUSIONREPORT, AnalysisTag.RESEARCH},
    {AnalysisTag.FUSIONINSPECTOR_HTML, AnalysisTag.RESEARCH},
    {AnalysisTag.ARRIBA_VISUALIZATION, AnalysisTag.RESEARCH},
    {AnalysisTag.MULTIQC_HTML, AnalysisTag.RNA},
    {HK_DELIVERY_REPORT_TAG},
    {AnalysisTag.VCF_FUSION},
    {AnalysisTag.GENE_COUNTS},
]

RNAFUSION_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [
    {AlignmentFileTag.CRAM},
    {AlignmentFileTag.CRAM_INDEX},
]

NF_ANALYSIS_CASE_TAGS: list[set[str]] = [{HermesFileTag.CLINICAL_DELIVERY}]

NF_ANALYSIS_SAMPLE_TAGS: list[set[str]] = [{HermesFileTag.CLINICAL_DELIVERY}]

PIPELINE_ANALYSIS_TAG_MAP: dict[Workflow, dict] = {
    Workflow.BALSAMIC: {
        "case_tags": BALSAMIC_ANALYSIS_CASE_TAGS,
        "sample_tags": BALSAMIC_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.BALSAMIC_QC: {
        "case_tags": BALSAMIC_QC_ANALYSIS_CASE_TAGS,
        "sample_tags": BALSAMIC_QC_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.BALSAMIC_UMI: {
        "case_tags": BALSAMIC_UMI_ANALYSIS_CASE_TAGS,
        "sample_tags": BALSAMIC_UMI_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.MIP_DNA: {
        "case_tags": MIP_DNA_ANALYSIS_CASE_TAGS,
        "sample_tags": MIP_DNA_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.MIP_RNA: {
        "case_tags": MIP_RNA_ANALYSIS_CASE_TAGS,
        "sample_tags": MIP_RNA_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.MICROSALT: {
        "case_tags": MICROSALT_ANALYSIS_CASE_TAGS,
        "sample_tags": MICROSALT_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.FASTQ: {
        "case_tags": FASTQ_ANALYSIS_CASE_TAGS,
        "sample_tags": FASTQ_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.MUTANT: {
        "case_tags": MUTANT_ANALYSIS_CASE_TAGS,
        "sample_tags": MUTANT_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.RNAFUSION: {
        "case_tags": RNAFUSION_ANALYSIS_CASE_TAGS,
        "sample_tags": RNAFUSION_ANALYSIS_SAMPLE_TAGS,
    },
    Workflow.TAXPROFILER: {
        "case_tags": NF_ANALYSIS_CASE_TAGS,
        "sample_tags": NF_ANALYSIS_CASE_TAGS,
    },
    Workflow.TOMTE: {
        "case_tags": NF_ANALYSIS_CASE_TAGS,
        "sample_tags": NF_ANALYSIS_CASE_TAGS,
    },
}

PIPELINE_ANALYSIS_OPTIONS = PIPELINE_ANALYSIS_TAG_MAP.keys()

INBOX_NAME: str = "inbox"
OUTBOX_NAME: str = "outbox"
