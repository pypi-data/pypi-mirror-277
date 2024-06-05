from ohmytofu.connectivity.gql.queries import (
    batch_ingest_mutation,
    trigger_pipeline_mutation,
    create_project_from_template_mutation, 
    object_view_query
)

async def batch_ingest(params, tofu_gql):
    res = await tofu_gql.execute_async(batch_ingest_mutation, variable_values=params)
    #await tofu_gql.transport.close()
    return res

async def trigger_pipeline(params, tofu_gql):
    res = await tofu_gql.execute_async(trigger_pipeline_mutation, variable_values=params)
    #await tofu_gql.transport.close()
    return res

async def object_view(params, tofu_gql):
    res = await tofu_gql.execute_async(object_view_query, variable_values=params)
    return res['filterObjectViewFromCassandra']


async def create_project_from_template(template_id, project_config, tofu_gql):
    variables = {
        'templateID': template_id,
        'projectConfig': project_config
    }
    res = await tofu_gql.execute_async(create_project_from_template_mutation, variable_values=variables)
    return res['createProjectFromTemplate2']

