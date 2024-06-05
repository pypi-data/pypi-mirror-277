The example applications in this directory provide some simple but useful visualization of the Egeria environment. They 
are built with the **Rich** python package and demonstrate the use of **pyegeria** .

The applications are invoked using the python3 command - for instance:
`python3 server_status_widget -h` would display the help information for the server_status_widget.
Running them may require that you have pyegeria installed. pyegeria can be installed using:
'pip install pyegeria'

Some of the widgets are "live" - that is running continuously until ctrl-c is issued to interrupt it.

The functions are:

* server_status_widget: provide a live view of servers running on a platform.
* gov_engine_status:    provides a live view of the specified governance engine host.
* engine_action_status: provides a live view of the engine actions - both running and completed.
* glossary_view: a paged list of terms as specified by the search string
* find_todos: find and display outstanding todos
* gov_engine_status: provide a live status view of a governance engine
* integration_daemon_status: provide a live status view of an integration daemon
* my_todos: provide a live view of my todos
* view_my_profile: view an Egeria profile
* list_asset_types: list the types of assets that have been configured in Egeria
* multi-server_status: show the status from two platforms concurrently
* coco_status.py: example showing the status of the Coco Pharmacutical platforms from the Jupyter Labs.
* get_relationship_types.py: display the different types of relationships for a given Entity type.
* get_valid_metadata_values.py: retrieve the currently defined valid metadata values for a given attribute and entity
* open_todos.py: list the open todo items
* project_list_viewer.py: List defined projects
* collection_viewer.py: Shows a collection hierarchy
* get_registered_services.py: shows the services registered on the platform
* get_tech_details.py: get the details of a technology type
* get_tech_types.py: get a list of the technology types
