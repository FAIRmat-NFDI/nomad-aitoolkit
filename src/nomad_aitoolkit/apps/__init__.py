# ruff: noqa: E501
from nomad.config import _plugins
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    BreakpointEnum,
    Column,
    Dashboard,
    FilterMenu,
    FilterMenus,
    FilterMenuSizeEnum,
    Filters,
    Format,
    Layout,
    ModeEnum,
    RowActionURL,
    RowDetails,
    Rows,
    RowSelection,
    ScaleEnum,
    WidgetTerms,
)

# Workaround: read the upload_ids from plugin's raw config.
try:
    upload_ids = _plugins['entry_points']['options']['nomad_aitoolkit.apps:aitoolkit'][
        'upload_ids'
    ]
except KeyError:
    upload_ids = None

if upload_ids:
    filters_locked = {
        'upload_id': upload_ids,
        'section_defs.definition_qualified_name': [
            'nomad_aitoolkit.schema.AIToolkitNotebook'
        ],
    }
else:
    filters_locked = {
        'section_defs.definition_qualified_name': [
            'nomad_aitoolkit.schema.AIToolkitNotebook'
        ]
    }


aitoolkit = AppEntryPoint(
    name='AI Toolkit notebooks',
    description='App defined using the new plugin mechanism.',
    app=App(
        label='AI Toolkit Notebooks',
        description='Search AI toolkit notebooks',
        path='ai-toolkit',
        category='Tools',
        filters=Filters(
            include=['*#nomad_aitoolkit.schema.AIToolkitNotebook'],
            # exclude=['*#nomad.datamodel.metainfo.eln.BasicEln'],
        ),
        filters_locked=filters_locked,
        columns=[
            Column(
                quantity='data.name#nomad_aitoolkit.schema.AIToolkitNotebook',
                selected=True,
            ),
            Column(
                quantity='data.category#nomad_aitoolkit.schema.AIToolkitNotebook',
                selected=True,
            ),
            Column(
                quantity='data.date#nomad_aitoolkit.schema.AIToolkitNotebook',
                label='Upload time',
                selected=True,
                format=Format(mode=ModeEnum.DATE),
            ),
            Column(quantity='entry_id'),
            Column(quantity='entry_type'),
            Column(quantity='authors'),
            Column(quantity='data.platform#nomad_aitoolkit.schema.AIToolkitNotebook'),
        ],
        filter_menus=FilterMenus(
            options={
                'custom_quantities': FilterMenu(
                    label='Notebooks', size=FilterMenuSizeEnum.L
                ),
                'author': FilterMenu(label='Author', size=FilterMenuSizeEnum.M),
                'metadata': FilterMenu(label='Visibility / IDs'),
            }
        ),
        dashboard=Dashboard(
            widgets=[
                WidgetTerms(
                    type='terms',
                    quantity='data.category#nomad_aitoolkit.schema.AIToolkitNotebook',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.MD: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.SM: Layout(h=6, w=6, x=0, y=0),
                    },
                ),
                WidgetTerms(
                    type='terms',
                    quantity='data.methods.name#nomad_aitoolkit.schema.AIToolkitNotebook',
                    title='Methods',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.MD: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.SM: Layout(h=6, w=6, x=6, y=0),
                    },
                ),
                WidgetTerms(
                    type='terms',
                    quantity='data.applications.name#nomad_aitoolkit.schema.AIToolkitNotebook',
                    title='Applications',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.MD: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.SM: Layout(h=6, w=6, x=12, y=0),
                    },
                ),
            ]
        ),
        rows=Rows(
            actions=[
                RowActionURL(
                    path="data.references[?kind=='repository'].uri",
                    description='Go to the repository',
                    icon='file_download',
                ),
                RowActionURL(
                    path="data.references[?kind=='hub'].uri",
                    description='Launch Jupyter notebook',
                    icon='launch',
                ),
            ],
            details=RowDetails(enabled=True),
            selection=RowSelection(enabled=True),
        ),
    ),
)
