from gql import gql

# Provide a GraphQL query
tofu_users_query = gql(
    """
    query tofuUsers {
        tofuUsers {
            id
            email
            name
        }

    }
"""
)

batch_ingest_mutation = gql( """
  mutation BATCH_INGEST(
    $rid: String!,
    $primaryKey: String,
    $primaryKeyVal: String,
    $data: JSON,
    $overwrite: Boolean
  ) {
  batchIngestData(
    rid: $rid,
    primaryKey: $primaryKey,
    primaryKeyVal: $primaryKeyVal,
    data: $data,
    overwrite: $overwrite,
)}""")


trigger_pipeline_mutation = gql("""
  mutation TRIGGER_PIPELINE (
    $triggerID: ID!,
    $workshopModuleID: ID,
    $settings: TriggerSettingInput
  ){
  triggerPipeline(
    triggerID: $triggerID,
    workshopModuleID: $workshopModuleID,
    settings: $settings
  )}
""")

object_view_query = gql("""
  query OBJECT_VIEW (
    $rid: String!,
    $primaryKey: String!,
    $filterSecondaryKey: String
    $value: String!
  ) {
  filterObjectViewFromCassandra (
    rid: $rid,
    primaryKey: $primaryKey,
    filterSecondaryKey: $filterSecondaryKey,
    value: $value
  )}
""")
