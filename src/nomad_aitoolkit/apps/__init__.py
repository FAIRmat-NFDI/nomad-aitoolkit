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
    RowActions,
    RowActionURL,
    Rows,
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

schema_name = 'nomad_aitoolkit.schema.AIToolkitNotebook'
if upload_ids:
    filters_locked = {
        'upload_id': upload_ids,
        'section_defs.definition_qualified_name': [
            schema_name
        ],
    }
else:
    filters_locked = {
        'section_defs.definition_qualified_name': [
            schema_name
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
            include=[f'*#{schema_name}'],
            # exclude=['*#nomad.datamodel.metainfo.eln.BasicEln'],
        ),
        filters_locked=filters_locked,
        columns=[
            Column(quantity=f'data.name#{schema_name}', selected=True),
            Column(quantity=f'data.category#{schema_name}', selected=True),
            Column(
                quantity=f'data.date#{schema_name}',
                label='Upload time',
                selected=True,
                format=Format(mode=ModeEnum.DATE),
            ),
            Column(quantity='entry_id'),
            Column(quantity='entry_type'),
            Column(quantity='authors'),
            Column(quantity=f'data.platform#{schema_name}'),
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
                    quantity=f'data.category#{schema_name}',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.MD: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.SM: Layout(h=6, w=6, x=0, y=0),
                    }
                ),
                WidgetTerms(
                    type='terms',
                    quantity=f'data.methods.name#{schema_name}',
                    title='Methods',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.MD: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.SM: Layout(h=6, w=6, x=6, y=0),
                    }
                ),
                WidgetTerms(
                    type='terms',
                    quantity=f'data.systems.name#{schema_name}',
                    title='Systems',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.MD: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.SM: Layout(h=6, w=6, x=12, y=0),
                    }
                )
            ]
        ),
        rows=Rows(
            actions=RowActions(
                items=[
                    RowActionURL(
                        path=f"data.references[?kind=='repository'].uri#{schema_name}",
                        description='Go to notebook repository',
                        icon='file_download',
                    ),
                    RowActionURL(
                        path=f"data.references[?kind=='hub'].uri#{schema_name}",
                        description='Launch Jupyter notebook',
                        icon='launch',
                    )
                ]
            )
        )
    )
)
