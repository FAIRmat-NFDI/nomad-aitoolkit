# ruff: noqa: E501
from nomad.config import config
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
    Layout,
    ScaleEnum,
    WidgetTerms,
)
from pydantic import Field


class AIToolkitAppEntryPoint(AppEntryPoint):
    upload_ids: list[str] = Field(
        default_factory=list,
        description='List of upload ids make sure only curated nootbooks are available.',
    )


# TODO: apps needs to be lazy loaded
# Workaround: hardcode upolad_ids OR putting filters_locked into nomad.yaml
# config.load_plugins()
# configuration = config.get_plugin_entry_point('nomad_aitoolkit.apps:aitoolkit')
# print(configuration.upload_ids)


aitoolkit = AIToolkitAppEntryPoint(
    name='AI Toolkit notebooks',
    description='App defined using the new plugin mechanism.',
    app=App(
        label='AI Toolkit Notebooks',
        description='Search AI toolkit notebooks',
        path='ai-toolkit',
        category='Tools',
        filters=Filters(
            include=['*#nomad_aitoolkit.schema.package.AIToolkitNotebook'],
            exclude=['*#nomad.datamodel.metainfo.eln.BasicEln'],
        ),
        filters_locked={
            'section_defs.definition_qualified_name': 'nomad_aitoolkit.schema.package.AIToolkitNotebook'
        },
        columns=Columns(
            include=[
                'entry_id',
                'entry_type',
                'authors',
                # 'references',
                # 'upload_create_time',
                'data.name#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                'data.category#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                # 'data.systems#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                # 'data.methods#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                'data.platform#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                'data.date#nomad_aitoolkit.schema.package.AIToolkitNotebook',
            ],
            selected=[
                'data.name#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                'authors',
                'data.category#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                'data.date#nomad_aitoolkit.schema.package.AIToolkitNotebook',
            ],
            options={
                'entry_id': Column(),
                'entry_type': Column(label='Entry type', align=AlignEnum.LEFT),
                'authors': Column(label='Authors', align=AlignEnum.LEFT),
                # 'references': Column(label='References', align=AlignEnum.LEFT),
                # 'upload_create_time': Column(label='Upload time', align=AlignEnum.LEFT),
                'data.name#nomad_aitoolkit.schema.package.AIToolkitNotebook': Column(
                    label='Name', align=AlignEnum.LEFT
                ),
                'data.category#nomad_aitoolkit.schema.package.AIToolkitNotebook': Column(
                    label='Category'
                ),
                # 'data.systems#nomad_aitoolkit.schema.package.AIToolkitNotebook': Column(
                #     label='Systems'
                # ),
                # 'data.authors_list#nomad_aitoolkit.schema.package.AIToolkitNotebook': Column(
                #     label='Authors',
                #     align=AlignEnum.LEFT
                # ),
                'data.platform#nomad_aitoolkit.schema.package.AIToolkitNotebook': Column(
                    label='Platform', align=AlignEnum.LEFT
                ),
                'data.date#nomad_aitoolkit.schema.package.AIToolkitNotebook': Column(
                    label='Upload time', align=AlignEnum.LEFT
                ),
            },
        ),
        filter_menus=FilterMenus(
            options={
                'custom_quantities': FilterMenu(
                    label='Notebooks', size=FilterMenuSizeEnum.L
                ),
                'author': FilterMenu(
                    label='Author / Origin / Dataset', size=FilterMenuSizeEnum.M
                ),
                'metadata': FilterMenu(label='Visibility / IDs / Schema'),
                'optimade': FilterMenu(label='Optimade', size=FilterMenuSizeEnum.M),
            }
        ),
        dashboard=Dashboard(
            widgets=[
                WidgetTerms(
                    type='terms',
                    quantity='data.category#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=0, y=0),
                        BreakpointEnum.MD: Layout(h=4, w=6, x=0, y=0),
                        BreakpointEnum.SM: Layout(h=3, w=6, x=0, y=0),
                    },
                ),
                WidgetTerms(
                    type='terms',
                    quantity='data.methods.name#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                    title='Methods',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=6, y=0),
                        BreakpointEnum.MD: Layout(h=4, w=6, x=6, y=0),
                        BreakpointEnum.SM: Layout(h=3, w=6, x=6, y=0),
                    },
                ),
                WidgetTerms(
                    type='terms',
                    quantity='data.systems.name#nomad_aitoolkit.schema.package.AIToolkitNotebook',
                    title='Systems',
                    scale=ScaleEnum.POW1,
                    layout={
                        BreakpointEnum.XXL: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.XL: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.LG: Layout(h=6, w=6, x=12, y=0),
                        BreakpointEnum.MD: Layout(h=4, w=6, x=12, y=0),
                        BreakpointEnum.SM: Layout(h=3, w=6, x=12, y=0),
                    },
                ),
            ]
        ),
    ),
)
