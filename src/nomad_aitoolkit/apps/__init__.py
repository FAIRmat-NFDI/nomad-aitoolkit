# ruff: noqa: E501
from nomad.config import _plugins
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    AlignEnum,
    App,
    BreakpointEnum,
    Column,
    Columns,
    Dashboard,
    FilterMenu,
    FilterMenus,
    FilterMenuSizeEnum,
    Filters,
    Format,
    Layout,
    ModeEnum,
    RowActions,
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
        columns=Columns(
            include=[
                'entry_id',
                'entry_type',
                'authors',
                'data.name#nomad_aitoolkit.schema.AIToolkitNotebook',
                'data.category#nomad_aitoolkit.schema.AIToolkitNotebook',
                'data.platform#nomad_aitoolkit.schema.AIToolkitNotebook',
                'data.date#nomad_aitoolkit.schema.AIToolkitNotebook',
            ],
            selected=[
                'data.name#nomad_aitoolkit.schema.AIToolkitNotebook',
                'authors',
                'data.category#nomad_aitoolkit.schema.AIToolkitNotebook',
                'data.date#nomad_aitoolkit.schema.AIToolkitNotebook',
            ],
            options={
                'entry_id': Column(),
                'entry_type': Column(label='Entry type', align=AlignEnum.LEFT),
                'authors': Column(label='Authors', align=AlignEnum.LEFT),
                'data.name#nomad_aitoolkit.schema.AIToolkitNotebook': Column(
                    label='Name', align=AlignEnum.LEFT
                ),
                'data.category#nomad_aitoolkit.schema.AIToolkitNotebook': Column(
                    label='Category'
                ),
                'data.platform#nomad_aitoolkit.schema.AIToolkitNotebook': Column(
                    label='Platform', align=AlignEnum.LEFT
                ),
                'data.date#nomad_aitoolkit.schema.AIToolkitNotebook': Column(
                    label='Last update',
                    align=AlignEnum.LEFT,
                    format=Format(mode=ModeEnum.DATE),
                ),
            },
        ),
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
                    quantity='data.systems.name#nomad_aitoolkit.schema.AIToolkitNotebook',
                    title='Systems',
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
            actions=RowActions(
                enabled=True,
                options={
                    'launch': RowActionURL(
                        type='url',
                        path="data.references[?kind=='hub'].uri",
                        description='Launch Jupyter notebook',
                    )
                },
            ),
            details=RowDetails(enabled=True),
            selection=RowSelection(enabled=True),
        ),
    ),
)
