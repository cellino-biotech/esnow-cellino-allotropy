from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional
from xml.etree import ElementTree

from allotropy.exceptions import AllotropeConversionError
from allotropy.parsers.utils.values import (
    get_attrib_from_xml,
    get_element_from_xml,
    get_val_from_xml,
    get_val_from_xml_or_none,
    try_float,
    try_float_or_none,
    try_int,
)

WELLS_TAG = "Wells"
ANALYTE_NAME = "AnalyteName"
MW_ANALYTES = "MWAnalytes"
RP1_GAIN = "RP1Gain"
LABEL = "Label"
RUN_CONDITIONS = "RunConditions"
MACHINE_INFO = "MachineInfo"
DOC_LOCATION_TAG = "NativeDocumentLocation"
DESCRIPTION_TAG = "Description"
PLATE_DIMENSIONS_TAG = "PlateDimensions"
TOTAL_WELLS_ATTRIB = "TotalWells"
VERSION_ATTRIB = "BioPlexManagerVersion"
REGION_COUNT = "RegionCount"
SAMPLES = "Samples"
BEAD_MAP = "BeadMap"
MEDIAN = "Median"
MEMBER_WELLS = "MemberWells"
ROW_NUMBER = "RowNo"
COLUMN_NUMBER = "ColNo"
SERIAL_NUMBER = "SerialNumber"
WELL_NUMBER = "WellNumber"
WELL_NO = "WellNo"
REGION_NUMBER = "RegionNumber"
REGIONS_OF_INTEREST = "RegionsOfInterest"
STOP_READING_CRITERIA = "StopReadingCriteria"
READING = "Reading"
RUN_SETTINGS = "RunSettings"
SAMPLE_VOLUME = "SampleVolume"
CODE = "Code"
DILUTION = "Dilution"
BEAD_COUNT = "BeadCount"
TOTAL_EVENTS = "TotalEvents"
ACQ_TIME = "AcquisitionTime"
ROW_NAMES = "ABCDEFGH"

SAMPLE_ROLE_TYPE_MAPPING = {
    "Blank": "blank role",
    "Control": "control sample role",
    "Standard": "standard sample role",
    "Unknown": "unknown sample role",
}


@dataclass(frozen=True)
class AnalyteSample:
    analyte_name: str
    analyte_region: int
    analyte_error_code: int

    @staticmethod
    def create(analyte_xml: ElementTree.Element) -> AnalyteSample:
        return AnalyteSample(
            analyte_name=get_val_from_xml(analyte_xml, ANALYTE_NAME),
            analyte_region=try_int(analyte_xml.attrib[REGION_NUMBER], "analyte_region"),
            analyte_error_code=try_int(
                get_attrib_from_xml(analyte_xml, READING, CODE), "analyte_error_code"
            ),
        )


@dataclass(frozen=True)
class WellAnalyteMapping:
    well_name: str
    analytes: list[AnalyteSample] = field(default_factory=list)


@dataclass
class SampleDocument:
    sample_type: str
    sample_identifier: str
    description: str
    well_name: str
    sample_dilution: Optional[float]
    well_analyte_mapping: WellAnalyteMapping


@dataclass
class SampleDocumentAggregate:
    # This data class pulled from the <Samples> part of the xml.
    samples: list[SampleDocument] = field(default_factory=list)
    # Default to empty dictionary.
    analyte_region_dict: dict[int, str] = field(default_factory=dict)

    @staticmethod
    def create(samples_xml: ElementTree.Element) -> SampleDocumentAggregate:
        sample_documents = SampleDocumentAggregate()
        for sample_types in samples_xml:
            for child_sample_type in sample_types:
                sample_type = map_sample_type(child_sample_type.tag)
                sample_description = get_val_from_xml(
                    child_sample_type, DESCRIPTION_TAG
                )
                sample_identifier = get_val_from_xml(child_sample_type, LABEL)
                sample_dilution = get_val_from_xml_or_none(child_sample_type, DILUTION)
                for child in child_sample_type:
                    if child.tag == MEMBER_WELLS:
                        for member_well in child:
                            sample_document = (
                                SampleDocumentAggregate._generate_sample_document(
                                    sample_documents=sample_documents,
                                    well_xml=member_well,
                                    sample_id=sample_identifier,
                                    sample_dilution=try_float_or_none(sample_dilution),
                                    sample_type=sample_type,
                                    sample_description=sample_description,
                                )
                            )
                            sample_documents.samples.append(sample_document)

        return sample_documents

    @staticmethod
    def _generate_sample_document(
        sample_documents: SampleDocumentAggregate,
        well_xml: ElementTree.Element,
        sample_id: str,
        sample_dilution: Optional[float],
        sample_type: str,
        sample_description: str,
    ) -> SampleDocument:
        well_name = get_well_name(well_xml.attrib)
        mappings = WellAnalyteMapping(well_name=well_name, analytes=[])
        for analyte in get_element_from_xml(well_xml, MW_ANALYTES):
            # Create the analyte.
            new_analyte = AnalyteSample.create(analyte_xml=analyte)
            # Add the analyte to the well analyte mappings.
            mappings.analytes.append(new_analyte)
            # Update the analyte region dict
            sample_documents.analyte_region_dict[
                new_analyte.analyte_region
            ] = new_analyte.analyte_name
        sample_document = SampleDocument(
            sample_type=sample_type,
            sample_identifier=sample_id,
            description=sample_description,
            well_name=well_name,
            well_analyte_mapping=mappings,
            sample_dilution=sample_dilution,
        )
        return sample_document


@dataclass
class DeviceWellSettings:
    # This data class is for all metadata needed in the <Wells> section, used in measurement and device control docs.
    well_name: str
    sample_volume_setting: int
    detector_gain_setting: str
    minimum_assay_bead_count_setting: int
    well_total_events: int
    acquisition_time: str

    @staticmethod
    def create(well_xml: ElementTree.Element) -> DeviceWellSettings:
        well_name = get_well_name(well_xml.attrib)
        well_acq_time = get_val_from_xml(well_xml, ACQ_TIME)
        total_events = get_val_from_xml(well_xml, TOTAL_EVENTS)
        sample_volume = try_int(
            get_val_from_xml(well_xml, RUN_SETTINGS, SAMPLE_VOLUME), "sample_volume"
        )

        detector_gain_setting = get_val_from_xml(well_xml, RUN_CONDITIONS, RP1_GAIN)
        min_assay_bead_count_setting = get_attrib_from_xml(
            well_xml, RUN_SETTINGS, BEAD_COUNT, STOP_READING_CRITERIA
        )
        return DeviceWellSettings(
            well_name=well_name,
            sample_volume_setting=sample_volume,
            detector_gain_setting=detector_gain_setting,
            minimum_assay_bead_count_setting=try_int(
                min_assay_bead_count_setting, "minimum_assay_bead_count_settings"
            ),
            acquisition_time=well_acq_time,
            well_total_events=try_int(total_events, "well_total_events"),
        )


@dataclass
class AnalyteDocumentData:
    analyte_name: str
    assay_bead_identifier: str
    assay_bead_count: int
    fluorescence: float

    @staticmethod
    def create(
        bead_region_xml: ElementTree.Element,
        analyte_region_dict: dict[str, str],
        regions_of_interest: list[str],
    ) -> Optional[AnalyteDocumentData]:
        # Look up analyte name from sample
        assay_bead_identifier = bead_region_xml.attrib[REGION_NUMBER]
        # Look up bead region -> analyte name
        if assay_bead_identifier in regions_of_interest:
            analyte_name = analyte_region_dict[assay_bead_identifier]
            assay_bead_count = try_int(
                get_val_from_xml(bead_region_xml, REGION_COUNT), "assay_bead_count"
            )
            # Median
            fluorescence = try_float(
                get_val_from_xml(bead_region_xml, MEDIAN), "fluorescence"
            )
            return AnalyteDocumentData(
                analyte_name=analyte_name,
                assay_bead_identifier=assay_bead_identifier,
                assay_bead_count=assay_bead_count,
                fluorescence=fluorescence,
            )
        else:
            return None


@dataclass
class WellSystemLevelMetadata:
    # This class is for data that should be the same across all wells, we just need to grab the data from one well.
    serial_number: str
    controller_version: str
    user: str
    analytical_method: str
    regions_of_interest: list[int] = field(default_factory=list)

    @staticmethod
    def create(xml_well: ElementTree.Element) -> WellSystemLevelMetadata:
        serial_number = get_val_from_xml(xml_well, MACHINE_INFO, SERIAL_NUMBER)
        controller_version = get_val_from_xml(
            xml_well, MACHINE_INFO, "MicroControllerVersion"
        )
        user = get_val_from_xml(xml_well, "User")
        analytical_method = get_val_from_xml(xml_well, "RunProtocolDocumentLocation")
        regions = get_element_from_xml(xml_well, RUN_SETTINGS, REGIONS_OF_INTEREST)
        regions_of_interest = []
        for region in regions:
            int_region = try_int(region.attrib[REGION_NUMBER], "int_region")
            regions_of_interest.append(int_region)
        return WellSystemLevelMetadata(
            serial_number=serial_number,
            controller_version=controller_version,
            user=user,
            analytical_method=analytical_method,
            regions_of_interest=regions_of_interest,
        )


def validate_xml_structure(full_xml: ElementTree.Element) -> None:
    expected_tags = [
        SAMPLES,
        DOC_LOCATION_TAG,
        DESCRIPTION_TAG,
        PLATE_DIMENSIONS_TAG,
        WELLS_TAG,
    ]
    missing_tags = []
    try:
        present_tags = {child.tag for child in full_xml}
        # Check for missing tags
        for tag in expected_tags:
            if tag not in present_tags:
                missing_tags.append(tag)
    except ElementTree.ParseError as err:
        # Return all expected tags if XML parsing fails
        msg = "Error parsing xml"
        raise AllotropeConversionError(msg) from err
    if missing_tags:
        msg = f"Missing expected tags in xml: {missing_tags}"
        raise AllotropeConversionError(msg)


def get_well_name(well_attrib: dict[str, str]) -> str:
    row_name = ROW_NAMES[try_int(well_attrib[ROW_NUMBER], "row_number") - 1]
    column_name = str(well_attrib[COLUMN_NUMBER])
    well_name = row_name + column_name
    return well_name


def map_sample_type(sample_type_tag: str) -> str:
    try:
        sample_type = SAMPLE_ROLE_TYPE_MAPPING[sample_type_tag]
        return sample_type
    except KeyError as err:
        msg = f"{sample_type_tag} is not in the valid list of sample role types: {SAMPLE_ROLE_TYPE_MAPPING.keys()}"
        raise AllotropeConversionError(msg) from err