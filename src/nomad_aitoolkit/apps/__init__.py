# ruff: noqa: E501
from nomad.config import _plugins
from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    BreakpointEnum,
    Column,
    Dashboard,
    Format,
    Layout,
    Menu,
    MenuItemHistogram,
    MenuItemTerms,
    MenuItemVisibility,
    ModeEnum,
    RowActions,
    RowActionURL,
    Rows,
    ScaleEnum,
    SearchQuantities,
    WidgetTerms,
)

schema = 'nomad_aitoolkit.schema.AIToolkitNotebook'
filters_locked = {'section_defs.definition_qualified_name': [schema]}

# Workaround: read the upload_ids from plugin's raw config.
try:
    upload_ids = _plugins['entry_points']['options']['nomad_aitoolkit.apps:aitoolkit'][
        'upload_ids'
    ]
except KeyError:
    upload_ids = None

if upload_ids:
    filters_locked['upload_id'] = upload_ids


aitoolkit = AppEntryPoint(
    name='AI Toolkit notebooks',
    description='App defined using the new plugin mechanism.',
    app=App(
        label='AI Toolkit Notebooks',
        description='Search AI toolkit notebooks',
        path='ai-toolkit',
        category='Tools',
        search_quantities=SearchQuantities(
            include=[f'*#{schema}'],
        ),
        filters_locked=filters_locked,
        columns=[
            Column(quantity=f'data.name#{schema}', selected=True),
            Column(quantity=f'data.category#{schema}', selected=True),
            Column(
                quantity=f'data.date#{schema}',
                label='Upload time',
                selected=True,
                format=Format(mode=ModeEnum.DATE),
            ),
            Column(quantity='entry_id'),
            Column(quantity='entry_type'),
            Column(quantity='authors'),
            Column(quantity=f'data.platform#{schema}'),
        ],
        menu=Menu(
            title='AI Toolkit Notebook',
            items=[
                Menu(
                    title='Author',
                    items=[
                        MenuItemTerms(
                            search_quantity='authors.name',
                            options=15
                        ),
                    ]
                ),
                Menu(
                    title='Notebook',
                    items=[
                        MenuItemTerms(
                            search_quantity=f'data.category#{schema}'
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.methods.name#{schema}'
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.applications.name#{schema}'
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.platform#{schema}'
                        ),
                        MenuItemHistogram(
                            x=f'data.date#{schema}'
                        )
                    ]
                ),
                Menu(
                    title='Visibility',
                    items=[
                        MenuItemVisibility(),
                    ]
                )

            ]

        ),
        dashboard=Dashboard(
            widgets=[
                WidgetTerms(
                    type='terms',
                    quantity=f'data.category#{schema}',
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
                    quantity=f'data.methods.name#{schema}',
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
                    quantity=f'data.applications.name#{schema}',
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
            actions=RowActions(
                items=[
                    RowActionURL(
                        path=f"data.references[?kind=='repository'].uri#{schema}",
                        description='Go to notebook repository',
                        icon='file_download',
                    ),
                    RowActionURL(
                        path=f"data.references[?kind=='hub'].uri#{schema}",
                        description='Launch Jupyter notebook',
                        icon='launch',
                    ),
                ]
            )
        ),
    ),
)
