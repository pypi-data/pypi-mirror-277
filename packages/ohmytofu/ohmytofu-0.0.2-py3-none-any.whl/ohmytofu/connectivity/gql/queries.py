from gql import gql


list_models_query = gql("""
    query LIST_TRFT_MODELS($where: DataObjectTypeWhere) {
      dataObjectTypes (where: $where) {
        id
        name
      }
    } 
""")

model_config_query = gql("""
query TRFTMODELCFG($id: ID, $trainingID:ID){
  getTrftModelConfig(id:$id, trainingID:$trainingID) 
}
""")

batch_ingest_mutation = gql( """
  mutation BATCH_INGEST(
    $rid: String!,
    $primaryKey: String,
    $data: JSON,
    $overwrite: Boolean
  ) {
  batchIngestData(
    rid: $rid,
    primaryKey: $primaryKey,
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


create_project_from_template_mutation = gql("""
  mutation (
   $templateID: ID!,
   $projectConfig: JSONObject
  ) {  
    createProjectFromTemplate2(
      templateID: $templateID
      projectConfig: $projectConfig
  )}
""");
