from evidently.metrics import ColumnDriftMetric
from evidently.metrics import ColumnSummaryMetric
from evidently.metrics import DatasetDriftMetric
from evidently.metrics import DatasetMissingValuesMetric
from evidently.report import Report
from evidently.test_preset import DataDriftTestPreset
from evidently.test_suite import TestSuite
from evidently.ui.dashboards import CounterAgg
from evidently.ui.dashboards import DashboardPanelCounter
from evidently.ui.dashboards import DashboardPanelPlot
from evidently.ui.dashboards import PanelValue
from evidently.ui.dashboards import PlotType
from evidently.ui.dashboards import ReportFilter
from evidently.ui.remote import RemoteWorkspace
from evidently.ui.workspace import Workspace
from evidently.ui.workspace import WorkspaceBase
from datetime import datetime,timedelta
import pandas as pd




def get_or_create_project(workspace: WorkspaceBase, PROJECT_NAME: str, PROJECT_DESCRIPTION: str):
    # Get name and id from all projects in workspace
    project_name_uuid_list = [{'name':project.name,'uuid':project.id} for project in workspace.list_projects()]
    
    # Loop through projects to retrieve if exists, create a new project if it does not exist
    task_project=None

    for project in project_name_uuid_list:
        if project.get('name')==PROJECT_NAME:
            task_project=workspace.get_project(project.get('uuid'))

    if task_project is None:
        task_project = create_project(workspace=workspace,YOUR_PROJECT_NAME=PROJECT_NAME,YOUR_PROJECT_DESCRIPTION=PROJECT_DESCRIPTION)
    return task_project




def create_project(workspace: WorkspaceBase,YOUR_PROJECT_NAME: str,YOUR_PROJECT_DESCRIPTION: str):
    project = workspace.create_project(YOUR_PROJECT_NAME)
    project.description = YOUR_PROJECT_DESCRIPTION
    project.dashboard.add_panel(
        DashboardPanelCounter(
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            agg=CounterAgg.NONE,
            title="Census Income Dataset (Adult)",
        )
    )
    project.dashboard.add_panel(
        DashboardPanelCounter(
            title="Model Calls",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            value=PanelValue(
                metric_id="DatasetMissingValuesMetric",
                field_path=DatasetMissingValuesMetric.fields.current.number_of_rows,
                legend="count",
            ),
            text="count",
            agg=CounterAgg.SUM,
            size=1,
        )
    )
    project.dashboard.add_panel(
        DashboardPanelCounter(
            title="Share of Drifted Features",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            value=PanelValue(
                metric_id="DatasetDriftMetric",
                field_path="share_of_drifted_columns",
                legend="share",
            ),
            text="share",
            agg=CounterAgg.LAST,
            size=1,
        )
    )
    project.dashboard.add_panel(
        DashboardPanelPlot(
            title="Dataset Quality",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            values=[
                PanelValue(metric_id="DatasetDriftMetric", field_path="share_of_drifted_columns", legend="Drift Share"),
                PanelValue(
                    metric_id="DatasetMissingValuesMetric",
                    field_path=DatasetMissingValuesMetric.fields.current.share_of_missing_values,
                    legend="Missing Values Share",
                ),
            ],
            plot_type=PlotType.LINE,
        )
    )
    project.dashboard.add_panel(
        DashboardPanelPlot(
            title="Age: Wasserstein drift distance",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            values=[
                PanelValue(
                    metric_id="ColumnDriftMetric",
                    metric_args={"column_name.name": "age"},
                    field_path=ColumnDriftMetric.fields.drift_score,
                    legend="Drift Score",
                ),
            ],
            plot_type=PlotType.BAR,
            size=1,
        )
    )
    project.dashboard.add_panel(
        DashboardPanelPlot(
            title="Education-num: Wasserstein drift distance",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            values=[
                PanelValue(
                    metric_id="ColumnDriftMetric",
                    metric_args={"column_name.name": "education-num"},
                    field_path=ColumnDriftMetric.fields.drift_score,
                    legend="Drift Score",
                ),
            ],
            plot_type=PlotType.BAR,
            size=1,
        )
    )
    project.save()
    return project


def create_report(i: int,reference_df: pd.DataFrame, current_df: pd.DataFrame ):
        data_drift_report = Report(
            metrics=[
                DatasetDriftMetric(),
                DatasetMissingValuesMetric(),
                ColumnDriftMetric(column_name="age", stattest="wasserstein"),
                ColumnSummaryMetric(column_name="age"),
                ColumnDriftMetric(column_name="education-num", stattest="wasserstein"),
                ColumnSummaryMetric(column_name="education-num"),
            ],
            timestamp=datetime.now(),
        )

        data_drift_report.run(reference_data=reference_df, current_data=current_df.iloc[100 * i : 100 * (i + 1), :])
        return data_drift_report
    

    
def create_test_suite(i: int,reference_df: pd.DataFrame, current_df: pd.DataFrame):
    data_drift_test_suite = TestSuite(
        tests=[DataDriftTestPreset()],
        timestamp=datetime.now(),
    )

    data_drift_test_suite.run(reference_data=reference_df, current_data=current_df.iloc[100 * i : 100 * (i + 1), :])
    return data_drift_test_suite