from nodestream.project import Project, ProjectPlugin


class SplunkPlugin(ProjectPlugin):
   def activate(self, project: Project) -> None:
       project.add_plugin_scope_from_pipeline_resources(
           name="splunk", package="splunk_plugin"
       )
