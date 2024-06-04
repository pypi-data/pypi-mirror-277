from fairbench.reports.base import report
from fairbench.blocks import framework, reducers, expanders, metrics
from fairbench.reports.accumulate import todict as tokwargs
from fairbench.core.fork import combine, merge, role, tobackend, Fork
from fairbench.reports.surrogate import surrogate_positives
from fairbench.blocks.reducers import identical
import numpy as np
import math
from makefun import wraps

# TODO: create a differentiable report (and maybe separate metrics into subpackages of diffs vs normal)
# TODO: have to check which values are differentiable

common_adhoc_metrics = (
    metrics.accuracy,
    metrics.prule,
    metrics.dfpr,
    metrics.dfnr,
)

common_performance_metrics = (
    metrics.accuracy,
    metrics.pr,
    metrics.tpr,
    metrics.tnr,
    metrics.auc,
    metrics.avgscore,
    metrics.tophr,
    metrics.toprec,
    metrics.mae,
    metrics.rmse,
    metrics.avghr,
    metrics.avgrepr,
    metrics.r2,
)

common_reduction = (
    {"reducer": reducers.min},
    {"reducer": reducers.wmean},
    {"reducer": reducers.gini},
    {"reducer": reducers.min, "expand": expanders.ratio},
    {"reducer": reducers.max, "expand": expanders.diff},
    {"reducer": reducers.max, "expand": expanders.barea},
    {"reducer": reducers.max, "expand": expanders.rarea},
    {"reducer": reducers.max, "expand": expanders.bdcg},
    # {"reducer": reducers.max, "expand": expanders.jsdcg},
)


def accreport(*args, metrics=common_performance_metrics, **kwargs):
    return report(*args, metrics=metrics, **kwargs)


def binreport(*args, metrics=common_adhoc_metrics, **kwargs):
    return report(*args, metrics=metrics, **kwargs)


@role("report")
def multireport(
    *args,
    metrics=common_performance_metrics,
    reduction_schemes=common_reduction,
    compare_all_to=None,
    **kwargs
):
    base = report(*args, metrics=metrics, **kwargs)
    return combine(
        *[
            framework.reduce(base, **scheme, base=compare_all_to)
            for scheme in reduction_schemes
        ]
    )


@role("report")
def unireport(
    *args,
    metrics=common_performance_metrics,
    reduction_schemes=common_reduction,
    **kwargs
):
    def modify_kwargs(kwargs):
        # adds an additional branch for the whole population called Any
        if "sensitive" in kwargs and "Any" not in kwargs["sensitive"]._branches:
            length = framework.areduce(
                kwargs["sensitive"].shape[0], identical
            )  # asserts that everything has the same identical shape and returns it
            length = int(
                0 if math.isnan(length.value) else length.value
            )  # retrieve int value from the explainable
            kwargs["sensitive"]._branches["Any"] = tobackend(np.ones((length,)))
        return kwargs

    base = report(*args, metrics=metrics, modify_kwargs=modify_kwargs, **kwargs)
    # perform the reduction while accounting for the
    return combine(
        *[
            framework.reduce(
                base, **scheme, base="Any" if "expand" in scheme else None
            )  # the bas kwarg refers to the base fork branch of the base report
            for scheme in reduction_schemes
        ]
    )


@role("report")
def isecreport(*args, **kwargs):
    if len(args) == 0:
        params = tokwargs(**kwargs)
    else:
        params = dict()
        for arg in args:
            params = merge(params, arg)
        params = merge(params, kwargs)

    bayesian = framework.reduce(
        surrogate_positives(params["predictions"], params["sensitive"]),
        reducers.min,
        expanders.ratio,
        name="bayesian",
    )

    empirical = framework.reduce(
        metrics.pr(predictions=params["predictions"], sensitive=params["sensitive"]),
        reducers.min,
        expanders.ratio,
        name="empirical",
    )
    return combine(tokwargs(minprule=empirical), tokwargs(minprule=bayesian))
