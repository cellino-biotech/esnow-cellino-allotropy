from collections.abc import Iterator

from allotropy.calcdocs.appbio_quantstudio_designandanalysis.config import (
    CalculatedDataConfigWithOptional,
)
from allotropy.calcdocs.appbio_quantstudio_designandanalysis.extractor import (
    AppbioQuantstudioDAExtractor,
)
from allotropy.calcdocs.appbio_quantstudio_designandanalysis.views import (
    SampleView,
    TargetRoleView,
    TargetView,
    UuidView,
)
from allotropy.calcdocs.config import (
    CalcDocsConfig,
    CalculatedDataConfig,
    MeasurementConfig,
)
from allotropy.calcdocs.view import ViewData
from allotropy.parsers.appbio_quantstudio_designandanalysis.structure.generic.structure import (
    WellItem,
)
from allotropy.parsers.utils.calculated_data_documents.definition import (
    CalculatedDocument,
)


def ctr() -> MeasurementConfig:
    return MeasurementConfig(
        name="cycle threshold result",
        value="cycle_threshold_result",
        required=True,
    )


def norm_reporter_result() -> MeasurementConfig:
    return MeasurementConfig(
        name="normalized reporter result",
        value="normalized_reporter_result",
    )


def amplification_score(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="amplification score",
        value="amp_score",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def cq_confidence(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="cq confidence",
        value="cq_conf",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def y_intercept(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="y intercept",
        value="y_intercept",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def slope(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="slope",
        value="slope",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def ct_mean(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="ct mean",
        value="ct_mean",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def ct_sd(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="ct sd",
        value="ct_sd",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def ct_se(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="ct se",
        value="ct_se",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def r_squared(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="r^2",
        value="r_squared",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def efficiency(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="efficiency",
        value="efficiency",
        view_data=view_data,
        source_configs=(ctr(),),
    )


def rn_mean(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="rn mean",
        value="rn_mean",
        view_data=view_data,
        source_configs=(norm_reporter_result(),),
    )


def rn_sd(view_data: ViewData) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="rn sd",
        value="rn_sd",
        view_data=view_data,
        source_configs=(norm_reporter_result(),),
    )


def quantity(
    view_data: ViewData,
    y_intercept_conf: CalculatedDataConfig | None = None,
    slope_conf: CalculatedDataConfig | None = None,
) -> CalculatedDataConfig:
    ctr_conf = ctr()
    return CalculatedDataConfig(
        name="quantity",
        value="quantity",
        view_data=view_data,
        source_configs=tuple(
            config for config in [ctr_conf, y_intercept_conf, slope_conf] if config
        ),
    )


def quantity_mean(
    view_data: ViewData,
    quantity_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="quantity mean",
        value="quantity_mean",
        view_data=view_data,
        source_configs=(quantity_conf,),
    )


def quantity_sd(
    view_data: ViewData,
    quantity_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="quantity sd",
        value="quantity_sd",
        view_data=view_data,
        source_configs=(quantity_conf,),
    )


def delta_ct_sd(
    view_data: ViewData,
    ct_sd_conf: CalculatedDataConfig,
    ref_ct_sd_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="delta equivalent ct sd",
        value="delta_ct_sd",
        view_data=view_data,
        source_configs=(ct_sd_conf, ref_ct_sd_conf),
    )


def delta_ct_se(
    view_data: ViewData,
    ct_sd_conf: CalculatedDataConfig,
    ref_ct_sd_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="delta equivalent ct se",
        value="delta_ct_se",
        view_data=view_data,
        source_configs=(ct_sd_conf, ref_ct_sd_conf),
    )


def relative_rq(
    view_data: ViewData,
    quantity_mean_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="relative rq",
        value="rq",
        view_data=view_data,
        source_configs=(quantity_mean_conf,),
    )


def relative_rq_min(
    view_data: ViewData,
    rq_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="relative rq min",
        value="rq_min",
        view_data=view_data,
        source_configs=(rq_conf,),
    )


def relative_rq_max(
    view_data: ViewData,
    rq_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="relative rq max",
        value="rq_max",
        view_data=view_data,
        source_configs=(rq_conf,),
    )


def eq_ct_mean(
    view_data: ViewData,
    ct_mean_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="equivalent ct mean",
        value="eq_ct_mean",
        view_data=view_data,
        source_configs=(ct_mean_conf,),
    )


def adj_eq_ct_mean(
    view_data: ViewData,
    eq_ct_mean_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfigWithOptional(
        name="adjusted equivalent ct mean",
        value="adj_eq_ct_mean",
        view_data=view_data,
        optional=True,
        source_configs=(eq_ct_mean_conf,),
    )


def delta_ct(
    view_data: ViewData,
    adj_eq_ct_mean_conf: CalculatedDataConfig,
    ref_adj_eq_ct_mean_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="delta equivalent ct mean",
        value="delta_ct_mean",
        view_data=view_data,
        source_configs=(adj_eq_ct_mean_conf, ref_adj_eq_ct_mean_conf),
    )


def delta_delta_ct(
    view_data: ViewData,
    delta_ct_conf: CalculatedDataConfig,
    ref_delta_ct_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="delta delta equivalent ct",
        value="delta_delta_ct",
        view_data=view_data,
        source_configs=(delta_ct_conf, ref_delta_ct_conf),
    )


def rq(
    view_data: ViewData,
    delta_delta_ct_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="rq",
        value="rq",
        view_data=view_data,
        source_configs=(delta_delta_ct_conf,),
    )


def rq_min(
    view_data: ViewData,
    rq_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="rq min",
        value="rq_min",
        view_data=view_data,
        source_configs=(rq_conf,),
    )


def rq_max(
    view_data: ViewData,
    rq_conf: CalculatedDataConfig,
) -> CalculatedDataConfig:
    return CalculatedDataConfig(
        name="rq max",
        value="rq_max",
        view_data=view_data,
        source_configs=(rq_conf,),
    )


def iter_standard_curve_calc_docs(
    well_items: list[WellItem],
) -> Iterator[CalculatedDocument]:
    # Y-intercept, Slope, Quantity, Amp score, Cq confidence,
    # Quantity Mean, Quantity SD, Ct Mean, Ct SD
    # R^2, Efficiency
    elements = AppbioQuantstudioDAExtractor.get_elements(well_items)

    sid_tdna_view_data = SampleView(sub_view=TargetView()).apply(elements)
    sid_tdna_uuid_view_data = SampleView(
        sub_view=TargetView(sub_view=UuidView())
    ).apply(elements)
    tdna_view_data = TargetRoleView().apply(elements)

    quantity_conf = quantity(
        sid_tdna_uuid_view_data,
        y_intercept(tdna_view_data),
        slope(tdna_view_data),
    )

    configs = CalcDocsConfig(
        [
            quantity_conf,
            amplification_score(sid_tdna_uuid_view_data),
            cq_confidence(sid_tdna_uuid_view_data),
            quantity_mean(sid_tdna_view_data, quantity_conf),
            quantity_sd(sid_tdna_view_data, quantity_conf),
            ct_mean(sid_tdna_view_data),
            ct_sd(sid_tdna_view_data),
            y_intercept(tdna_view_data),
            r_squared(tdna_view_data),
            slope(tdna_view_data),
            efficiency(tdna_view_data),
        ]
    )

    for calc_doc in configs.construct():
        yield from calc_doc.iter_struct()


def iter_relative_standard_curve_calc_docs(
    well_items: list[WellItem],
    r_sample: str,
    r_target: str | None,
) -> Iterator[CalculatedDocument]:
    # Y-Intercept, Slope, Quantity, Amp score, Cq confidence,
    # Ct Mean, Ct SD, Ct SE,
    # Delta Ct SD, Delta Ct SE,
    # Relative RQ min, Relative RQ max, Relative RQ, Quantity Mean,
    # RQ min, RQ max, RQ, Delta Delta Ct, Delta Ct,
    # Adjusted equivalent Ct mean, equivalent Ct mean
    elements = AppbioQuantstudioDAExtractor.get_elements(well_items)

    sid_tdna_view_data = SampleView(sub_view=TargetView()).apply(elements)
    sid_ref_tdna_view_data = SampleView(
        reference=r_sample, sub_view=TargetView()
    ).apply(elements)
    sid_tdna_ref_view_data = SampleView(
        sub_view=TargetView(is_reference=True, reference=r_target)
    ).apply(elements)
    sid_tdna_blacklist_view_data = SampleView(
        sub_view=TargetView(blacklist=[r_target] if r_target is not None else None)
    ).apply(elements)
    sid_tdna_uuid_view_data = SampleView(
        sub_view=TargetView(sub_view=UuidView())
    ).apply(elements)
    tdna_view_data = TargetRoleView().apply(elements)

    quantity_conf = quantity(
        sid_tdna_uuid_view_data,
        y_intercept(tdna_view_data),
        slope(tdna_view_data),
    )

    configs = CalcDocsConfig(
        [
            quantity_conf,
            amplification_score(sid_tdna_uuid_view_data),
            cq_confidence(sid_tdna_uuid_view_data),
            ct_mean(sid_tdna_view_data),
            ct_sd(sid_tdna_view_data),
            delta_ct_sd(
                sid_tdna_view_data,
                ct_sd(sid_tdna_view_data),
                ct_sd(sid_tdna_ref_view_data),
            ),
            delta_ct_se(
                sid_tdna_view_data,
                ct_se(sid_tdna_view_data),
                ct_se(sid_tdna_ref_view_data),
            ),
            relative_rq_min(
                sid_tdna_view_data,
                relative_rq(
                    sid_tdna_view_data,
                    quantity_mean(sid_tdna_view_data, quantity_conf),
                ),
            ),
            relative_rq_max(
                sid_tdna_view_data,
                relative_rq(
                    sid_tdna_view_data,
                    quantity_mean(sid_tdna_view_data, quantity_conf),
                ),
            ),
            rq_min(
                sid_tdna_blacklist_view_data,
                rq(
                    sid_tdna_view_data,
                    delta_delta_ct(
                        sid_tdna_view_data,
                        delta_ct(
                            sid_tdna_view_data,
                            adj_eq_ct_mean(
                                sid_tdna_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                            adj_eq_ct_mean(
                                sid_tdna_ref_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                        ),
                        delta_ct(
                            sid_ref_tdna_view_data,
                            adj_eq_ct_mean(
                                sid_tdna_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                            adj_eq_ct_mean(
                                sid_tdna_ref_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            rq_max(
                sid_tdna_blacklist_view_data,
                rq(
                    sid_tdna_view_data,
                    delta_delta_ct(
                        sid_tdna_view_data,
                        delta_ct(
                            sid_tdna_view_data,
                            adj_eq_ct_mean(
                                sid_tdna_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                            adj_eq_ct_mean(
                                sid_tdna_ref_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                        ),
                        delta_ct(
                            sid_ref_tdna_view_data,
                            adj_eq_ct_mean(
                                sid_tdna_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                            adj_eq_ct_mean(
                                sid_tdna_ref_view_data,
                                eq_ct_mean(
                                    sid_tdna_view_data,
                                    ct_mean(sid_tdna_view_data),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ]
    )

    for calc_doc in configs.construct():
        yield from calc_doc.iter_struct()


def iter_presence_absence_calc_docs(
    well_items: list[WellItem],
) -> Iterator[CalculatedDocument]:
    # Quantity, Amp score, Cq confidence, Rn Mean, Rn SD
    elements = AppbioQuantstudioDAExtractor.get_elements(well_items)

    sid_tdna_view_data = SampleView(sub_view=TargetView()).apply(elements)
    sid_tdna_uuid_view_data = SampleView(
        sub_view=TargetView(sub_view=UuidView())
    ).apply(elements)

    configs = CalcDocsConfig(
        [
            quantity(sid_tdna_uuid_view_data),
            amplification_score(sid_tdna_uuid_view_data),
            cq_confidence(sid_tdna_uuid_view_data),
            rn_mean(sid_tdna_view_data),
            rn_sd(sid_tdna_view_data),
        ]
    )

    for calc_doc in configs.construct():
        yield from calc_doc.iter_struct()


def iter_primary_analysis_calc_docs(
    well_items: list[WellItem],
) -> Iterator[CalculatedDocument]:
    # Ct Mean, Ct SD, Ct SE
    elements = AppbioQuantstudioDAExtractor.get_elements(well_items)

    sid_tdna_view_data = SampleView(sub_view=TargetView()).apply(elements)

    configs = CalcDocsConfig(
        [
            ct_mean(sid_tdna_view_data),
            ct_sd(sid_tdna_view_data),
            ct_se(sid_tdna_view_data),
        ]
    )

    for calc_doc in configs.construct():
        yield from calc_doc.iter_struct()
