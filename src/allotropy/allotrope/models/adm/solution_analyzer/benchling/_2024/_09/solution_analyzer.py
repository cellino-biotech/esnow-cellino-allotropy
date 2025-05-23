# generated by datamodel-codegen:
#   filename:  solution-analyzer.schema.json
#   timestamp: 2025-03-18T15:28:39+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCell,
    TQuantityValueCountsPerMilliliter,
    TQuantityValueDegreeCelsius,
    TQuantityValueGramPerLiter,
    TQuantityValueKiloPascal,
    TQuantityValueMicrometer,
    TQuantityValueMilliAbsorbanceUnit,
    TQuantityValueMilliliter,
    TQuantityValueMilliliterPerLiter,
    TQuantityValueMillimeterOfMercury,
    TQuantityValueMillimolePerLiter,
    TQuantityValueMillionCellsPerMilliliter,
    TQuantityValueMilliOsmolesPerKilogram,
    TQuantityValueNanometer,
    TQuantityValuePercent,
    TQuantityValuePH,
    TQuantityValuePicogramPerMilliliter,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TBooleanValue,
    TClass,
    TDatacube,
    TDateTimeStampValue,
    TDateTimeValue,
    TDoubleValue,
    TIntegerValue,
    TIntValue,
    TStatisticDatumRole,
    TStringValue,
    TUnit,
)


@dataclass(kw_only=True)
class AdmCoreREC202409ManifestSchema:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: str | None = None
    field_type: str | None = None
    shapes: list[str] | None = None


@dataclass(kw_only=True)
class CustomInformationDocumentItem:
    scalar_double_datum: TDoubleValue | None = None
    unit: TUnit | None = None
    scalar_string_datum: TStringValue | None = None
    scalar_timestamp_datum: TDateTimeValue | None = None
    scalar_boolean_datum: TBooleanValue | None = None
    datum_label: TStringValue | None = None


@dataclass(kw_only=True)
class ElectronicProjectRecord:
    written_name: TStringValue
    description: Any | None = None
    start_time: TDateTimeValue | None = None


@dataclass(kw_only=True)
class ErrorDocumentItem:
    error: TStringValue
    error_feature: TStringValue | None = None


@dataclass(kw_only=True)
class ErrorAggregateDocument:
    error_document: list[ErrorDocumentItem] | None = None


@dataclass(kw_only=True)
class ImageDocumentItem:
    experimental_data_identifier: TStringValue | None = None
    index: TIntegerValue | None = None


@dataclass(kw_only=True)
class ImageAggregateDocument:
    image_document: list[ImageDocumentItem] | None = None


@dataclass(kw_only=True)
class StatisticsDocumentItem:
    statistical_feature: TClass


@dataclass(kw_only=True)
class StatisticsAggregateDocument:
    statistics_document: list[StatisticsDocumentItem] | None = None


@dataclass(kw_only=True)
class TQuantityValueModel:
    value: float
    unit: TUnit
    has_statistic_datum_role: TStatisticDatumRole | None = None
    field_type: TClass | None = None


@dataclass(kw_only=True)
class AnalysisSequenceDocument:
    written_name: TStringValue
    end_time: TDateTimeValue | None = None
    file_name: TStringValue | None = None
    identifier: TStringValue | None = None
    method_identifier: TStringValue | None = None
    method_name: TStringValue | None = None
    start_time: TDateTimeValue | None = None
    UNC_path: TStringValue | None = None
    version_number: TStringValue | None = None


@dataclass(kw_only=True)
class DataProcessingDocument:
    cell_type_processing_method: TStringValue | None = None
    cell_density_dilution_factor: TQuantityValueUnitless | None = None
    minimum_cell_diameter_setting: TQuantityValueMicrometer | None = None
    maximum_cell_diameter_setting: TQuantityValueMicrometer | None = None
    dilution_factor_setting: TQuantityValueUnitless | None = None
    data_processing_omission_setting: TBooleanValue | None = None


@dataclass(kw_only=True)
class AnalyteDocument:
    analyte_name: TStringValue
    mass_concentration: TQuantityValueGramPerLiter | None = None
    volume_concentration: TQuantityValueMilliliterPerLiter | None = None
    molar_concentration: TQuantityValueMillimolePerLiter | None = None


@dataclass(kw_only=True)
class AnalyteAggregateDocument:
    analyte_document: list[AnalyteDocument]


@dataclass(kw_only=True)
class DistributionDocumentItem:
    particle_size: TQuantityValueMicrometer
    cumulative_count: TQuantityValueUnitless
    cumulative_particle_density: TQuantityValueCountsPerMilliliter
    differential_particle_density: TQuantityValueCountsPerMilliliter
    differential_count: TQuantityValueUnitless
    distribution_identifier: TStringValue | None = None


@dataclass(kw_only=True)
class DistributionAggregateDocument:
    distribution_document: list[DistributionDocumentItem]


@dataclass(kw_only=True)
class CustomInformationAggregateDocument:
    custom_information_document: list[CustomInformationDocumentItem]


@dataclass(kw_only=True)
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass(kw_only=True)
class ElectronicSignatureDocumentItem:
    account_identifier: TStringValue
    personal_name: TStringValue
    signature_role_type: TStringValue
    time: TStringValue
    identifier: TStringValue | None = None
    measurement_identifier: TStringValue | None = None
    method_identifier: TStringValue | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class ElectronicSignatureAggregateDocument:
    electronic_signature_document: list[ElectronicSignatureDocumentItem] | None = None


@dataclass(kw_only=True)
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem]
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    electronic_project_record: ElectronicProjectRecord | None = None


@dataclass(kw_only=True)
class DataSystemDocument:
    ASM_file_identifier: TStringValue
    data_system_instance_identifier: TStringValue
    file_name: TStringValue | None = None
    UNC_path: TStringValue | None = None
    ASM_converter_name: TStringValue | None = None
    ASM_converter_version: TStringValue | None = None
    database_primary_key: TStringValue | None = None
    software_name: TStringValue | None = None
    software_version: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_type: TStringValue
    brand_name: TStringValue | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    written_name: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    asset_management_identifier: TStringValue | None = None
    brand_name: TStringValue | None = None
    description: Any | None = None
    device_document: list[DeviceDocumentItem] | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DiagnosticTraceDocumentItem:
    description: Any
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    brand_name: TStringValue | None = None
    detection_type: TStringValue | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    field_index: int | None = None
    detector_wavelength_setting: TQuantityValueNanometer | None = None
    detector_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_wavelength_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_bandwidth_setting: TQuantityValueNanometer | None = (
        None
    )
    electronic_absorbance_reference_wavelength_setting: TQuantityValueNanometer | None = (
        None
    )
    excitation_wavelength_setting: TQuantityValueNanometer | None = None
    flush_volume_setting: TQuantityValueMilliliter | None = None
    detector_view_volume: TQuantityValueMilliliter | None = None
    repetition_setting: TIntValue | None = None
    sample_volume_setting: TQuantityValueMilliliter | None = None


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    batch_identifier: TStringValue | None = None
    description: Any | None = None
    sample_role_type: TClass | None = None
    written_name: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValueModel
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass(kw_only=True)
class MeasurementDocument:
    device_control_aggregate_document: DeviceControlAggregateDocument
    measurement_identifier: TStringValue
    measurement_time: TDateTimeStampValue
    sample_document: SampleDocument
    osmolality: TQuantityValueMilliOsmolesPerKilogram | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    detection_type: TStringValue | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    error_aggregate_document: ErrorAggregateDocument | None = None
    image_aggregate_document: ImageAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    field_index: int | None = None
    absorbance: TQuantityValueMilliAbsorbanceUnit | None = None
    mass_concentration: TQuantityValuePicogramPerMilliliter | None = None
    pH: TQuantityValuePH | None = None
    temperature: TQuantityValueDegreeCelsius | None = None
    pO2: TQuantityValueKiloPascal | TQuantityValueMillimeterOfMercury | None = None
    pCO2: TQuantityValueKiloPascal | TQuantityValueMillimeterOfMercury | None = None
    carbon_dioxide_saturation: TQuantityValuePercent | None = None
    oxygen_saturation: TQuantityValuePercent | None = None
    analyte_aggregate_document: AnalyteAggregateDocument | None = None


@dataclass(kw_only=True)
class ProcessedDataDocumentItem:
    viability__cell_counter_: TQuantityValuePercent | None = None
    viable_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_processing_document: DataProcessingDocument | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None
    total_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    dead_cell_density__cell_counter_: TQuantityValueMillionCellsPerMilliliter | None = (
        None
    )
    average_total_cell_diameter: TQuantityValueMicrometer | None = None
    average_live_cell_diameter__cell_counter_: TQuantityValueMicrometer | None = None
    average_dead_cell_diameter__cell_counter_: TQuantityValueMicrometer | None = None
    total_cell_diameter_distribution: TDatacube | None = None
    total_cell_count: TQuantityValueCell | None = None
    viable_cell_count: TQuantityValueCell | None = None
    dead_cell_count: TQuantityValueCell | None = None
    average_total_cell_circularity: TQuantityValueUnitless | None = None
    average_viable_cell_circularity: TQuantityValueUnitless | None = None
    distribution_aggregate_document: DistributionAggregateDocument | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocument]
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None
    error_aggregate_document: ErrorAggregateDocument | None = None
    image_aggregate_document: ImageAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    data_processing_time: TDateTimeStampValue | None = None


@dataclass(kw_only=True)
class SolutionAnalyzerDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: TStringValue | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class SolutionAnalyzerAggregateDocument:
    solution_analyzer_document: list[SolutionAnalyzerDocumentItem]
    analysis_sequence_document: AnalysisSequenceDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_system_document: DataSystemDocument | None = None
    device_system_document: DeviceSystemDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    electronic_signature_aggregate_document: ElectronicSignatureAggregateDocument | None = (
        None
    )
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class Model:
    field_asm_manifest: AdmCoreREC202409ManifestSchema | str
    solution_analyzer_aggregate_document: SolutionAnalyzerAggregateDocument | None = (
        None
    )
